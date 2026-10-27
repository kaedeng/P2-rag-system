"""Sensitivity of the own-corpus scores to the width of the relevance rule.

    uv run python scripts/narrow_labels.py

Keeps one label per query, the labeled page with the most lines containing one of the query's content words,
drops the rest, and scores the committed runs against that narrow set next to the full one. The narrow set is
a mechanical subset of the student's labels, a check on how much the wide rule drives the result, not a gold set.
No Claude call.
"""

from __future__ import annotations

import re
import sys

from p2 import config, metrics, paths, stats
from p2 import corpus as cm
from p2.runfile import read_qrels, read_queries, read_run

SYSTEMS = ("bm25", "dense", "hybrid", "rerank")
PAIRS = (("hybrid", "bm25"), ("hybrid", "dense"), ("rerank", "hybrid"), ("rerank", "bm25"), ("rerank", "dense"), ("dense", "bm25"))


def main() -> int:
    cfg = config.load()
    corpus = cm.load(cfg.root, "own")
    queries = {q.qid: q for q in read_queries(paths.queries(cfg.root, "own", "own"))[0]}
    qrels, _ = read_qrels(paths.qrels(cfg.root, "own", "own"))

    def strength(qid: str, docid: str) -> int:
        words = [w for w in re.findall(r"[a-z0-9_-]+", queries[qid].text.lower()) if len(w) > 3]
        return sum(1 for line in corpus.docs[docid].text.lower().splitlines() if any(w in line for w in words))

    narrow = {q: {max(ds, key=lambda d: strength(q, d)): 1} for q, ds in qrels.items()}
    print("narrow set, one page per query:")
    for q in queries:
        print(f"  {q}: {next(iter(narrow[q]))}  (of {len(qrels[q])} labeled)")
    runs = {n: read_run(paths.run_file(cfg.root, "own", "own", n)) for n in SYSTEMS}
    wide = {n: metrics.evaluate(r, qrels, list(queries)) for n, r in runs.items()}
    nar = {n: metrics.evaluate(r, narrow, list(queries)) for n, r in runs.items()}
    print(f"\n{'system':>7}  {'MRR wide':>9}  {'MRR narrow':>10}  {'recall wide':>11}  {'recall narrow':>13}")
    for n in SYSTEMS:
        print(f"{n:>7}  {metrics.mean(wide[n], 'mrr@10'):9.3f}  {metrics.mean(nar[n], 'mrr@10'):10.3f}  {metrics.mean(wide[n], 'recall@10'):11.3f}  {metrics.mean(nar[n], 'recall@10'):13.3f}")
    for label, ev in (("full labels", wide), ("narrow labels", nar)):
        print(f"\npairs on MRR@10, {label}:")
        for a, b in PAIRS:
            boot = stats.paired_bootstrap([ev[a][q]["mrr@10"] for q in queries], [ev[b][q]["mrr@10"] for q in queries])
            lo, hi = boot["ci95"]
            print(f"  {a} minus {b}: {boot['mean_diff']:+.3f} [{lo:+.3f}, {hi:+.3f}]  MDD {stats.mdd(boot['sd_diff'], boot['n']):.3f}  {stats.reading(boot['ci95'], a, b)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
