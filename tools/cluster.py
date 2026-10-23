#!/usr/bin/env python3
"""設問本文の類似度で重複出題をクラスタリングする。"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

C = json.load(open("tools/corpus.json", encoding="utf-8"))


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"!\[img[^\]]*\]\([^)]*\)", "", s)      # 画像参照
    s = re.sub(r"[\s　，、。．\.,「」『』（）()\|\-–—:：;；]", "", s)
    return s


def shingles(s: str, n: int = 4) -> set[str]:
    return {s[i : i + n] for i in range(max(1, len(s) - n + 1))}


docs = [(x["id"], shingles(norm(x["body"]))) for x in C]

# 転置インデックスで候補を絞ってから Jaccard を計算
inv: dict[str, list[int]] = {}
for i, (_, sh) in enumerate(docs):
    for g in sh:
        inv.setdefault(g, []).append(i)

parent = list(range(len(docs)))


def find(a: int) -> int:
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a


def union(a: int, b: int) -> None:
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[max(ra, rb)] = min(ra, rb)


THRESH = 0.65
for i, (_, si) in enumerate(docs):
    cand: dict[int, int] = {}
    for g in si:
        for j in inv[g]:
            if j > i:
                cand[j] = cand.get(j, 0) + 1
    for j, overlap in cand.items():
        sj = docs[j][1]
        if overlap / (len(si) + len(sj) - overlap) >= THRESH:
            union(i, j)

groups: dict[int, list[str]] = {}
for i, (qid, _) in enumerate(docs):
    groups.setdefault(find(i), []).append(qid)

clusters = sorted(groups.values(), key=lambda g: -len(g))
Path("tools/clusters.json").write_text(
    json.dumps(clusters, ensure_ascii=False, indent=1), encoding="utf-8"
)
multi = [g for g in clusters if len(g) > 1]
print(f"総設問 {len(C)} → クラスタ {len(clusters)} 個（うち複数出題 {len(multi)} 個）")
print(f"重複として吸収される設問数: {len(C) - len(clusters)}")
print("\n--- 出題回数の多いクラスタ 上位15 ---")
byid = {x["id"]: x for x in C}
for g in clusters[:15]:
    head = byid[sorted(g)[0]]["body"].split("\n")[0][:70]
    print(f"{len(g)}回 {sorted(g)[0]}: {head}")
