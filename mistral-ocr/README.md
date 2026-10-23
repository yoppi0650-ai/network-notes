# Mistral OCR PDF to Markdown

`pdf/` に置いた PDF を Mistral OCR API で読み取り、`markdown/` に Markdown として保存します。

## 使い方

1. `.env` に `MISTRAL_API_KEY=...` を設定します。
2. 変換したい PDF を `pdf/` に置きます。
3. 次を実行します。

```bash
.venv/bin/python scripts/ocr_pdfs.py
```

同名の Markdown がすでにある場合はスキップします。上書きしたい場合:

```bash
.venv/bin/python scripts/ocr_pdfs.py --overwrite
```

入出力ディレクトリを変える場合:

```bash
.venv/bin/python scripts/ocr_pdfs.py --input-dir pdf --output-dir markdown
```

## 出力

`example.pdf` は `markdown/example.md` に変換されます。

各ページの前に `<!-- Page N -->` のコメントを入れています。
