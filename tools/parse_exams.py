#!/usr/bin/env python3
"""OCR済み過去問を構造化JSONに変換する。"""
from __future__ import annotations

import json
import re
from pathlib import Path

SRC = Path("mistral-ocr/markdown")
OUT = Path("tools/corpus.json")

# ページ区切り・ノンブル・著作権表記などの除去対象
NOISE = re.compile(
    r"^(?:<!-- Page \d+ -->|<!-- Source: .*-->|[-–—]\s*\d+\s*[-–—]|©.*|注意事項.*|"
    r"問題冊子.*|この問題冊子.*|次の.*に従って解答.*)$"
)
QHEAD = re.compile(r"^問\s*(\d{1,2})[　 ．.]?\s*(.*)$")
# 最終問題の後ろに続く巻末の注意事項・奥付（ここ以降は本文ではない）
TAIL = re.compile(
    r"問題に関する質問にはお答えできません|〔メモ用紙〕|試験問題に記載されている会社名|"
    r"^\s*#+\s*お知らせ|答案用紙は，?、?いかなる場合でも提出"
)
ANS = re.compile(r"^\|\s*問\s*(\d{1,2})\s*\|\s*([アイウエ])\s*\|")


def clean(lines: list[str]) -> list[str]:
    return [l for l in lines if not NOISE.match(l.strip())]


def parse_problems(path: Path) -> dict[int, str]:
    lines = clean(path.read_text(encoding="utf-8").splitlines())
    out: dict[int, list[str]] = {}
    cur: int | None = None
    expected = 1
    for line in lines:
        m = QHEAD.match(line.strip())
        # 誤検出防止: 問番号は 1 から連番で現れるものだけを見出しとみなす
        if m and int(m.group(1)) == expected:
            cur = expected
            expected += 1
            out[cur] = [m.group(2).strip()]
        elif TAIL.search(line):
            cur = None
        elif cur is not None:
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def parse_answers(path: Path) -> dict[int, str]:
    out: dict[int, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ANS.match(line.strip())
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def main() -> None:
    corpus = []
    for prob in sorted(SRC.glob("*-problems.md")):
        key = prob.name.replace("-problems.md", "")
        sol = SRC / f"{key}-solutions.md"
        year, section = key.rsplit("-", 1)
        questions = parse_problems(prob)
        answers = parse_answers(sol)
        for num in sorted(questions):
            corpus.append(
                {
                    "id": f"{year}-{section}-Q{num:02d}",
                    "year": year,
                    "section": section,
                    "num": num,
                    "answer": answers.get(num),
                    "body": questions[num],
                }
            )
    OUT.write_text(json.dumps(corpus, ensure_ascii=False, indent=1), encoding="utf-8")

    # 検算
    from collections import Counter
    per = Counter((c["year"], c["section"]) for c in corpus)
    bad = [f"{y}-{s}:{n}" for (y, s), n in sorted(per.items()) if n != (30 if s == "AM1" else 25)]
    noans = [c["id"] for c in corpus if not c["answer"]]
    print(f"total={len(corpus)} files={len(per)}")
    print(f"問数が想定外: {bad or 'なし'}")
    print(f"正解未取得: {len(noans)}件 {noans[:10]}")


if __name__ == "__main__":
    main()
