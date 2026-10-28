"""Why hybrid's RRF k is 60 and not 10: quality against cross-machine robustness of the fusion.

    uv run python scripts/fusion_robust.py

For each variant it scores the shared practice queries and the own gold set, then adds N(0, 4e-4) noise to every dense
cosine (the size of the differences between machines, see p2/embed.py) ten times and counts the queries whose top-10
fused scores would fail `p2 check`'s 0.001 tolerance on another machine. No Claude call. On 2026-10-27 the committed
k = 10 hybrid runs failed CI this way (own c09: 1/15 + 1/25 locally, 1/15 + 1/26 on CI)
k = 60 is the only variant
with zero fragile queries.
"""
import numpy as np
from collections import defaultdict
from p2 import config, metrics, paths, retrievers
from p2 import corpus as cm
from p2.runfile import order, read_qrels, read_queries
cfg = config.load()
rng = np.random.default_rng(0)
VARIANTS = {"k10": (10, 10), "k20": (20, 20), "k30": (30, 30), "k40": (40, 40), "k60": (60, 60), "bm25k10/dense k60": (10, 60), "bm25k10/dense k30": (10, 30)}

def fuse(b, d, kb, kd, top=10):
    f = defaultdict(float)
    for rank, (doc, _s) in enumerate([x for x in b if x[1] > 0], 1):
        f[doc] += 1.0 / (kb + rank)
    for rank, (doc, _s) in enumerate([x for x in d if x[1] > 0], 1):
        f[doc] += 1.0 / (kd + rank)
    return order(f.items())[:top]

for corpus_name, qset in (("shared", "practice"), ("own", "own")):

    corpus = cm.load(cfg.root, corpus_name)
    queries = read_queries(paths.queries(cfg.root, corpus_name, qset))[0]
    qrels, _ = read_qrels(paths.qrels(cfg.root, corpus_name, qset))
    judged = metrics.judged_queries(qrels, [q.qid for q in queries])
    bm25 = retrievers.build("bm25", corpus, cfg)
    dense = retrievers.build("dense", corpus, cfg)
    n = len(corpus.docs)
    B = {q.qid: bm25.search(q.text, n) for q in queries}
    D = {q.qid: dense.search(q.text, n) for q in queries}
    print(f"\n== {corpus_name} ({len(judged)} queries)   recall@10  MRR@10  nDCG@10   fragile queries (of {len(judged)}, 10 noise trials)")
    for name, (kb, kd) in VARIANTS.items():
        res = {q: fuse(B[q], D[q], kb, kd) for q in B}
        ev = metrics.evaluate(res, qrels, judged)
        fragile = 0
        for q in judged:
            base = dict(res[q])
            bad = False
            for _ in range(10):
                noisy = order([(doc, s + rng.normal(0, 4e-4)) for doc, s in D[q]])
                new = dict(fuse(B[q], noisy, kb, kd))
                for doc, s in base.items():
                    if doc in new:
                        if abs(new[doc] - s) >= 1e-3:
                            bad = True
                    else:
                        cut = min(new.values())
                        if abs(s - cut) >= 1e-3:
                            bad = True
                if bad:
                    break
            fragile += bad
        print(f"  {name:>18}  {metrics.mean(ev,'recall@10'):9.3f}  {metrics.mean(ev,'mrr@10'):6.3f}  {metrics.mean(ev,'ndcg@10'):7.3f}   {fragile}")

# Variant: k = 10 but dense ranks taken on cosines rounded to 2 or 3 decimals (ties by docid), to blunt the noise.
print("\n== rounding variants (k = 10 both arms)")
for corpus_name, qset in (("shared", "practice"), ("own", "own")):
    corpus = cm.load(cfg.root, corpus_name)
    queries = read_queries(paths.queries(cfg.root, corpus_name, qset))[0]
    qrels, _ = read_qrels(paths.qrels(cfg.root, corpus_name, qset))
    judged = metrics.judged_queries(qrels, [q.qid for q in queries])
    bm25 = retrievers.build("bm25", corpus, cfg)
    dense = retrievers.build("dense", corpus, cfg)
    n = len(corpus.docs)
    B = {q.qid: bm25.search(q.text, n) for q in queries}
    D = {q.qid: dense.search(q.text, n) for q in queries}
    for decimals in (3, 2):
        def rd(lst, decimals=decimals):
            return order([(doc, round(s, decimals)) for doc, s in lst])
        res = {q: fuse(B[q], rd(D[q]), 10, 10) for q in B}
        ev = metrics.evaluate(res, qrels, judged)
        fragile = 0
        for q in judged:
            base = dict(res[q])
            bad = False
            for _ in range(10):
                noisy = rd([(doc, s + rng.normal(0, 4e-4)) for doc, s in D[q]])
                new = dict(fuse(B[q], noisy, 10, 10))
                for doc, s in base.items():
                    if doc in new:
                        if abs(new[doc] - s) >= 1e-3:
                            bad = True
                    elif abs(s - min(new.values())) >= 1e-3:
                        bad = True
                if bad:
                    break
            fragile += bad
        print(f"  {corpus_name:>6} round{decimals}  recall {metrics.mean(ev,'recall@10'):.3f}  MRR {metrics.mean(ev,'mrr@10'):.3f}  nDCG {metrics.mean(ev,'ndcg@10'):.3f}   fragile {fragile} of {len(judged)}")
