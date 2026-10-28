"""Ablation variant of dense: the same bge-small-en-v1.5 retriever with bge v1.5's recommended query prefix
switched on, "Represent this sentence for searching relevant passages: ", in front of every query before it is
embedded. The chunk vectors are unchanged (and shared through the cache); only the query side moves.
BASE names the system it varies, which `p2 score` reads for the own-ablation-queries table.
"""

from p2.retrievers import dense

BASE = "dense"
NEEDS_CLAUDE = False
PREFIX = "Represent this sentence for searching relevant passages: "


def build(corpus, cfg):
    settings = {**cfg.table("dense"), "query_prefix": PREFIX}
    return dense.Dense(corpus, cfg.replace(tables={**cfg.tables, "dense": settings}))
