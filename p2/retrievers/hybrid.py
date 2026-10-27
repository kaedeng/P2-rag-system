"""Hybrid retrieval (stage 1): reciprocal rank fusion of bm25 and dense.

It is rrf() from the 13 lab's pipeline.py: each document scores the sum of 1 / (k + rank) over the
rankings it appears in, rank counted from 1. k is [hybrid] rrf_k in p2.toml (the lab's 60 when unset);
a smaller k lets one system's top rank win, a larger one rewards agreement between the two.
- Both systems come from p2.retrievers.build, so each index is built once per run.
- It fuses full rankings (every document, or every chunk), not top-10 lists, because a document
  that is 11th in both lists can belong in the fused top 10.
- Entries that score 0 or less are dropped before fusing: bm25 gives every document that shares no
  word with the query a 0, in document id order, which is padding, not a match, and should not earn
  a rank. Dropping them leaves the ranks of the real matches as they were.
- The fused list is ordered with p2.runfile.order(), so equal scores fall in id order, and cut at k.
search_chunks does the same fusion over the two systems' chunk rankings, for `p2 answer`.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Sequence

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False
RRF_K = 60
SYSTEMS = ("bm25", "dense")


def rrf(rankings: Iterable[Sequence[tuple[str, float]]], k: int = RRF_K) -> list[tuple[str, float]]:
    """Reciprocal rank fusion of rankings of (id, score), best first; entries scoring 0 or less are left out."""
    fused: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        kept = [item for item, score in ranking if score > 0]
        for rank, item in enumerate(kept, 1):
            fused[item] += 1.0 / (k + rank)
    return order(fused.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.cfg = cfg
        self.systems = [retrievers.build(name, corpus, cfg) for name in SYSTEMS]
        self.k = int(cfg.table("hybrid").get("rrf_k", RRF_K))
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(corpus.chunks(cfg.chunk_words, cfg.chunk_overlap))

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        return rrf((system.search(text, self.n_docs) for system in self.systems), self.k)[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        return rrf((system.search_chunks(text, self.n_chunks) for system in self.systems), self.k)[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
