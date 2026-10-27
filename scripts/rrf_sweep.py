"""Sweep hybrid's RRF k on the shared practice queries, from the committed bm25 and dense systems (no Claude calls).

Run from the repo root: uv run python scripts/rrf_sweep.py
It prints one line per k (scores, top-20 coverage, queries helped and hurt against k = 60, paired interval),
the per-class scores of the chosen k against 60, and whether the 12 questions' gold sections reach the top-20 chunks.
"""
from collections import defaultdict
from p2 import config, corpus as cm, metrics, paths, retrievers, stats
from p2.corpus import docid_of
from p2.runfile import order, read_qrels, read_queries, read_questions

cfg = config.load()
corpus = cm.load(cfg.root, "shared")
queries, _ = read_queries(paths.queries(cfg.root, "shared", "practice"))
qrels, _ = read_qrels(paths.qrels(cfg.root, "shared", "practice"))
judged = metrics.judged_queries(qrels, [q.qid for q in queries])
systems = {n: retrievers.build(n, corpus, cfg) for n in ("bm25", "dense")}
full = {q.qid: [s.search(q.text, len(corpus.docs)) for s in systems.values()] for q in queries}

def fuse(rankings, k, top=10):
    fused = defaultdict(float)
    for ranking in rankings:
        for rank, (d, _s) in enumerate([x for x in ranking if x[1] > 0], 1):
            fused[d] += 1.0 / (k + rank)
    return order(fused.items())[:top]

base = metrics.evaluate({qid: fuse(r, 60) for qid, r in full.items()}, qrels, judged)
print(f"{'k':>5}  recall@10  MRR@10  nDCG@10  top20 has rel  helped/hurt vs k=60   MRR diff vs k=60 [95% interval]")
for k in (0, 1, 2, 3, 5, 10, 20, 30, 60, 100):
    res = {qid: fuse(r, k) for qid, r in full.items()}
    ev = metrics.evaluate(res, qrels, judged)
    cover = sum(any(d in qrels[qid] for d, _ in fuse(r, k, 20)) for qid, r in full.items())
    up = sum(ev[q]["mrr@10"] > base[q]["mrr@10"] for q in judged)
    down = sum(ev[q]["mrr@10"] < base[q]["mrr@10"] for q in judged)
    boot = stats.paired_bootstrap([ev[q]["mrr@10"] for q in judged], [base[q]["mrr@10"] for q in judged])
    lo, hi = boot["ci95"]
    print(f"{k:>5}  {metrics.mean(ev, 'recall@10'):9.3f}  {metrics.mean(ev, 'mrr@10'):6.3f}  {metrics.mean(ev, 'ndcg@10'):7.3f}  {cover:>8} / 20  {up:>6} / {down:<10}  {boot['mean_diff']:+.3f} [{lo:+.3f}, {hi:+.3f}]")

CHOSEN = int(cfg.table("hybrid").get("rrf_k", 60))
chosen = metrics.evaluate({qid: fuse(r, CHOSEN) for qid, r in full.items()}, qrels, judged)
cls = {q.qid: q.cls for q in queries}
print()
print(f"per class, k={CHOSEN} against k=60:")
for c in dict.fromkeys(cls.values()):
    qs = [q for q in judged if cls[q] == c]
    print(f"  {c:>11} (n={len(qs)})  MRR {metrics.mean(chosen, 'mrr@10', qs):.3f} vs {metrics.mean(base, 'mrr@10', qs):.3f}   recall {metrics.mean(chosen, 'recall@10', qs):.3f} vs {metrics.mean(base, 'recall@10', qs):.3f}")
up = [q for q in judged if chosen[q]["mrr@10"] > base[q]["mrr@10"]]
down = [q for q in judged if chosen[q]["mrr@10"] < base[q]["mrr@10"]]
print(f"  helped {len(up)}: {', '.join(up)}")
print(f"  hurt {len(down)}: {', '.join(down) or 'none'}")

# The 12 questions: is a gold document's chunk inside hybrid's top-20 chunks, per k? (what rerank, then p2 answer, would see)
questions, _ = read_questions(paths.questions(cfg.root, "shared"))
n_chunks = len(corpus.chunks(cfg.chunk_words, cfg.chunk_overlap))
print()
print("in-corpus questions whose gold section has a chunk in hybrid's top-20 chunks, and in the top 5 (answer sends top 5 after rerank):")
for k in (1, 5, 10, 60):
    in20 = in5 = 0
    for q in questions:
        if q.kind != "in":
            continue
        rankings = [s.search_chunks(q.text, n_chunks) for s in systems.values()]
        top = [c for c, _ in fuse(rankings, k, 20)]
        in20 += any(docid_of(c) in q.gold for c in top)
        in5 += any(docid_of(c) in q.gold for c in top[:5])
    print(f"  k={k:<3} top-20: {in20} of 8   top-5 before rerank: {in5} of 8")
