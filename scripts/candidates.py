"""A candidate sheet for judging relevance on the own corpus: for each query, the union of the top 10 of bm25, dense
and hybrid, plus optional keyword hits, with each document's title and its best-scoring chunk's opening.

    uv run python scripts/candidates.py QUERIES.tsv [--grep WORD ...] [--top 10] [--only q01,q02]

QUERIES.tsv has the queries file's columns (qid, class, text, origin; lines starting with # are skipped). Makes no
Claude call. The student reads the documents and judges; this only gathers candidates from several places, as the
brief asks, so the gold set is not built from one system's output.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from p2 import config, retrievers
from p2 import corpus as cm
from p2.corpus import docid_of
from p2.runfile import read_queries

SYSTEMS = ("bm25", "dense", "hybrid")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("queries", type=Path)
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--only", default="")
    ap.add_argument("--snippet", type=int, default=240, help="characters of the best chunk to show")
    args = ap.parse_args()
    cfg = config.load()
    corpus = cm.load(cfg.root, "own")
    queries, problems = read_queries(args.queries)
    if problems:
        print("\n".join(problems), file=sys.stderr)
    only = {q.strip() for q in args.only.split(",") if q.strip()}
    systems = {n: retrievers.build(n, corpus, cfg) for n in SYSTEMS}
    texts = corpus.chunk_texts(cfg.chunk_words, cfg.chunk_overlap)
    for q in queries:
        if only and q.qid not in only:
            continue
        ranks: dict[str, dict[str, int]] = {}
        best_chunk: dict[str, str] = {}
        for name, system in systems.items():
            for rank, (docid, _s) in enumerate(system.search(q.text, args.top), 1):
                ranks.setdefault(docid, {})[name] = rank
            for cid, _s in system.search_chunks(q.text, args.top * 3):
                best_chunk.setdefault(docid_of(cid), cid)
        words = [w for w in re.findall(r"[a-z0-9_]+", q.text.lower()) if len(w) > 3]
        print(f"\n=== {q.qid} [{q.cls}, {q.origin}] {q.text}")
        order = sorted(ranks, key=lambda d: min(ranks[d].values()))
        for docid in order:
            where = " ".join(f"{n}:{ranks[docid][n]}" if n in ranks[docid] else f"{n}:-" for n in SYSTEMS)
            cid = best_chunk.get(docid, f"{docid}#0")
            body = texts.get(cid, corpus.docs[docid].text)
            start = body.find("\n\n") + 2 if cid.endswith("#0") and "\n\n" in body else 0
            snippet = " ".join(body[start:].split())[: args.snippet]
            hits = sum(1 for w in words if w in corpus.docs[docid].text.lower())
            print(f"  {docid}  ({where}; {hits}/{len(words)} query words)  {corpus.docs[docid].title}")
            print(f"      [{cid}] {snippet}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
