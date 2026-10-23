#!/usr/bin/env python3
"""指定した小分類コードに属する過去問を、出題年度つきで全文表示する。"""
import json, sys, re
from pathlib import Path

code = sys.argv[1]
C = {x["id"]: x for x in json.load(open("tools/corpus.json", encoding="utf-8"))}
CL = {sorted(g)[0]: sorted(g) for g in json.load(open("tools/clusters.json", encoding="utf-8"))}

rows = []
for f in Path("tools/classify").glob("*.tsv"):
    for line in f.read_text(encoding="utf-8").splitlines():
        qid, cat, topic = line.split("\t")
        if cat == code:
            rows.append((qid, topic, CL[qid]))

def key(r):
    return (-len(r[2]), r[0])

rows.sort(key=key)
print(f"### {code}: {len(rows)}クラスタ / 延べ{sum(len(r[2]) for r in rows)}問\n")
for qid, topic, members in rows:
    q = C[qid]
    others = [m for m in members if m != qid]
    freq = f"  ★{len(members)}回出題: {', '.join(m[:-4].replace('-20',' ')+m[-4:] for m in members)}" if others else ""
    body = re.sub(r"\n{2,}", "\n", q["body"])
    print(f"[{qid} 答{q['answer']}] 〈{topic}〉{freq}\n{body}\n--")
