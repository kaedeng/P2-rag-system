"""Stretch option 3 variant of rerank: Claude reorders hybrid's top 10 instead of its top 20.

Same prompt, schema and fallback as rerank.py; only the number of candidates differs, so each call
sends about half the passages. Its practice run and trace sit next to rerank's for the stretch-cost
table, which pairs the two on the same queries: MRR@10 difference with its interval against the
input tokens and seconds saved per query.
"""

from p2.retrievers import rerank

BASE = "rerank"
NEEDS_CLAUDE = True
CANDIDATES = 10


def build(corpus, cfg):
    system = rerank.Rerank(corpus, cfg)  # hybrid underneath comes from p2.retrievers.build, so it is shared
    system.n = CANDIDATES
    return system
