#!/usr/bin/env python3
"""Convert PDFs in ./pdf to Markdown files in ./markdown using Mistral OCR."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_BASE_URL = "https://api.mistral.ai/v1"
DEFAULT_MODEL = "mistral-ocr-latest"


class MistralApiError(RuntimeError):
    pass


def load_env(path: Path) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def request_json(
    method: str,
    url: str,
    api_key: str,
    *,
    body: bytes | None = None,
    content_type: str | None = None,
    timeout: int = 300,
) -> dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
    }
    if content_type:
        headers["Content-Type"] = content_type

    request = Request(url, data=body, headers=headers, method=method)
    try:
        with urlopen(request, timeout=timeout) as response:
            response_body = response.read()
    except HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise MistralApiError(f"{method} {url} failed: HTTP {exc.code}\n{error_body}") from exc
    except URLError as exc:
        raise MistralApiError(f"{method} {url} failed: {exc.reason}") from exc

    if not response_body:
        return {}

    try:
        return json.loads(response_body.decode("utf-8"))
    except json.JSONDecodeError as exc:
        snippet = response_body[:500].decode("utf-8", errors="replace")
        raise MistralApiError(f"{method} {url} returned invalid JSON:\n{snippet}") from exc


def multipart_form(fields: dict[str, str], file_field: str, file_path: Path) -> tuple[bytes, str]:
    boundary = f"----mistral-ocr-{uuid.uuid4().hex}"
    chunks: list[bytes] = []

    for name, value in fields.items():
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode("utf-8"),
                b"\r\n",
            ]
        )

    content_type = mimetypes.guess_type(file_path.name)[0] or "application/pdf"
    chunks.extend(
        [
            f"--{boundary}\r\n".encode(),
            (
                f'Content-Disposition: form-data; name="{file_field}"; '
                f'filename="{file_path.name}"\r\n'
            ).encode(),
            f"Content-Type: {content_type}\r\n\r\n".encode(),
            file_path.read_bytes(),
            b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ]
    )

    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def upload_pdf(pdf_path: Path, api_key: str) -> str:
    body, content_type = multipart_form({"purpose": "ocr"}, "file", pdf_path)
    response = request_json(
        "POST",
        f"{API_BASE_URL}/files",
        api_key,
        body=body,
        content_type=content_type,
    )

    file_id = response.get("id")
    if not isinstance(file_id, str) or not file_id:
        raise MistralApiError(f"Upload response did not include a file id: {response}")

    return file_id


def get_signed_url(file_id: str, api_key: str, expiry_hours: int) -> str:
    query = urlencode({"expiry": expiry_hours})
    response = request_json("GET", f"{API_BASE_URL}/files/{file_id}/url?{query}", api_key)

    signed_url = response.get("url")
    if not isinstance(signed_url, str) or not signed_url:
        raise MistralApiError(f"Signed URL response did not include a url: {response}")

    return signed_url


def run_ocr(document_url: str, api_key: str, model: str, include_images: bool) -> dict[str, Any]:
    payload = {
        "model": model,
        "document": {
            "type": "document_url",
            "document_url": document_url,
        },
        "include_image_base64": include_images,
    }
    return request_json(
        "POST",
        f"{API_BASE_URL}/ocr",
        api_key,
        body=json.dumps(payload).encode("utf-8"),
        content_type="application/json",
    )


def markdown_from_ocr(response: dict[str, Any], source_name: str) -> str:
    pages = response.get("pages")
    if not isinstance(pages, list):
        raise MistralApiError(f"OCR response did not include pages: {response}")

    parts = [f"<!-- Source: {source_name} -->"]
    for page_number, page in enumerate(pages, start=1):
        if not isinstance(page, dict):
            continue

        markdown = page.get("markdown")
        if not isinstance(markdown, str):
            markdown = ""

        parts.append(f"\n\n<!-- Page {page_number} -->\n\n{markdown.strip()}")

    return "".join(parts).strip() + "\n"


def convert_pdf(
    pdf_path: Path,
    output_path: Path,
    api_key: str,
    model: str,
    include_images: bool,
    overwrite: bool,
) -> None:
    if output_path.exists() and not overwrite:
        print(f"skip: {pdf_path.name} -> {output_path} already exists", file=sys.stderr)
        return

    started = time.monotonic()
    print(f"upload: {pdf_path.name}", file=sys.stderr)
    file_id = upload_pdf(pdf_path, api_key)

    print(f"ocr: {pdf_path.name}", file=sys.stderr)
    signed_url = get_signed_url(file_id, api_key, expiry_hours=24)
    response = run_ocr(signed_url, api_key, model, include_images)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_from_ocr(response, pdf_path.name), encoding="utf-8")

    elapsed = time.monotonic() - started
    print(f"done: {pdf_path.name} -> {output_path} ({elapsed:.1f}s)", file=sys.stderr)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert PDFs in a directory to Markdown using Mistral OCR."
    )
    parser.add_argument("--input-dir", default="pdf", type=Path)
    parser.add_argument("--output-dir", default="markdown", type=Path)
    parser.add_argument("--env-file", default=".env", type=Path)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--include-images", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_env(args.env_file)

    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("error: MISTRAL_API_KEY is not set in the environment or .env", file=sys.stderr)
        return 2

    input_dir = args.input_dir
    output_dir = args.output_dir
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(input_dir.glob("*.pdf"))
    if not pdfs:
        print(f"No PDF files found in {input_dir}/")
        return 0

    for pdf_path in pdfs:
        output_path = output_dir / f"{pdf_path.stem}.md"
        try:
            convert_pdf(
                pdf_path=pdf_path,
                output_path=output_path,
                api_key=api_key,
                model=args.model,
                include_images=args.include_images,
                overwrite=args.overwrite,
            )
        except MistralApiError as exc:
            print(f"error: {pdf_path.name}: {exc}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
