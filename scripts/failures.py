"""Evidence for the failure analysis (EVAL.md section 6): for one system on the own corpus, every query whose first
relevant document is not at rank 1, with what the system returned and where the relevant documents landed.

    uv run python scripts/failures.py [--system rerank] [--deep 50]

Reads the committed run file for the top 10 and asks the system again for a deeper ranking (no Claude call for
the systems that do not call Claude; rerank reuses its saved replies) to find relevant documents below the top 10.
The causes and the prose are the student's.
"""

from __future__ import annotations

import argparse
import sys

from p2 import config, metrics, paths, retrievers
from p2 import corpus as cm
from p2.runfile import read_qrels, read_queries, read_run


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--system", default="rerank")
    ap.add_argument("--deep", type=int, default=50)
    args = ap.parse_args()
    cfg = config.load()
    corpus = cm.load(cfg.root, "own")
    queries = {q.qid: q for q in read_queries(paths.queries(cfg.root, "own", "own"))[0]}
    qrels, _ = read_qrels(paths.qrels(cfg.root, "own", "own"))
    run = read_run(paths.run_file(cfg.root, "own", "own", args.system))
    per_query = metrics.evaluate(run, qrels, list(queries))
    system = retrievers.build(args.system, corpus, cfg)
    title = lambda d: corpus.docs[d].title[:60]  # noqa: E731
    shown = 0
    for qid in sorted(queries, key=lambda q: (per_query[q]["mrr@10"], q)):
        rr = per_query[qid]["mrr@10"]
        if rr >= 1.0:
            continue
        shown += 1
        q = queries[qid]
        rel = {d for d, r in qrels[qid].items() if r > 0}
        deep = [d for d, _ in system.search(q.text, args.deep)]
        print(f"\n=== {qid} [{q.cls}, {q.origin}] RR {rr:.3f}  recall@10 {per_query[qid]['recall@10']:.2f}   {q.text[:110]}")
        print("  returned (top 5):")
        for i, (d, _s) in enumerate(run[qid][:5], 1):
            print(f"    {i}. {d}  {title(d)}{'   <- relevant' if d in rel else ''}")
        print("  relevant, with rank in the deeper list:")
        for d in sorted(rel, key=lambda d: deep.index(d) if d in deep else 999):
            where = f"rank {deep.index(d) + 1}" if d in deep else f"below {args.deep}"
            print(f"    {d}  {title(d)}  ({where}, {len(corpus.docs[d].text.split())} words)")
    print(f"\n{shown} of {len(queries)} queries have their first relevant document below rank 1 for {args.system}.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
