"""Dense retrieval (stage 1): embed every chunk once, embed the query, and rank chunks by cosine similarity.

It is the embedding arm of the 12 lab's retrieve.py (load_bge, cached_doc_vectors, dense_rankings),
ported to chunks with the helpers in p2/embed.py:
- the model is [dense] model in p2.toml (default bge-small-en-v1.5), loaded with embed.load();
- embed.doc_vectors() encodes the chunks once and keeps the vectors in .cache/vectors/;
- a chunk's score is its vector times the query vector; both have length 1, so that is the cosine.

[dense] query_prefix (default "", off) is put in front of each query before it is embedded, so an
ablation can measure bge v1.5's "Represent this sentence for searching relevant passages: ".
ChunkScorer gives both search (a document scores its best chunk) and search_chunks.
"""

from __future__ import annotations

import numpy as np

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        settings = cfg.table("dense")
        self.model = str(settings.get("model", embed.BGE))
        self.query_prefix = str(settings.get("query_prefix", ""))
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> np.ndarray:
        if not self.chunks:
            return np.zeros(0, dtype=np.float32)
        query = self.embedder.encode([self.query_prefix + text])[0]
        return self.vectors @ query


def build(corpus, cfg):
    return Dense(corpus, cfg)
