#!/usr/bin/env python3
"""クラスタ代表問題を分類作業用テキストに書き出す。"""
import json, re, sys
from pathlib import Path

C = {x["id"]: x for x in json.load(open("tools/corpus.json", encoding="utf-8"))}
CL = json.load(open("tools/clusters.json", encoding="utf-8"))

# 代表は最古の出題、cid は代表ID
items = []
for g in CL:
    g = sorted(g)
    rep = C[g[0]]
    items.append({"cid": g[0], "n": len(g), "members": g, "sec": rep["section"], "rep": rep})

items.sort(key=lambda x: (x["sec"], x["cid"]))
Path("tools/clusters_meta.json").write_text(
    json.dumps([{k: v for k, v in i.items() if k != "rep"} for i in items],
               ensure_ascii=False, indent=1), encoding="utf-8")

out = Path("tools/dump"); out.mkdir(exist_ok=True)
for sec in ("AM1", "AM2"):
    sub = [i for i in items if i["sec"] == sec]
    CH = 120
    for k in range(0, len(sub), CH):
        chunk = sub[k:k+CH]
        lines = [f"## {sec} クラスタ {k+1}-{k+len(chunk)} / 全{len(sub)}\n"]
        for i in chunk:
            freq = f" ★{i['n']}回" if i["n"] > 1 else ""
            body = re.sub(r"\n{2,}", "\n", i["rep"]["body"])
            lines.append(f"[{i['cid']} 答{i['rep']['answer']}{freq}]\n{body}\n--")
        (out / f"{sec}-{k//CH+1:02d}.txt").write_text("\n".join(lines), encoding="utf-8")
for f in sorted(out.iterdir()):
    print(f"{f.name}: {f.stat().st_size//1024}KB")
