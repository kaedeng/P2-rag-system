"""Ablation variant of hybrid: the same reciprocal rank fusion of bm25 and dense with the lab's k = 60
instead of the k = 10 in p2.toml. Everything else is hybrid's own code.

On the shared practice queries k = 10 beat k = 60 (MRR@10 +0.117 [+0.037, +0.218], scripts/rrf_sweep.py);
this variant asks whether that holds on the own corpus. BASE names the system it varies, which
`p2 score` reads for the own-ablation-queries table.
"""

from p2.retrievers import hybrid

BASE = "hybrid"
NEEDS_CLAUDE = False
RRF_K = 60


def build(corpus, cfg):
    system = hybrid.Hybrid(corpus, cfg)  # its bm25 and dense come from p2.retrievers.build, so the indexes are shared
    system.k = RRF_K
    return system
