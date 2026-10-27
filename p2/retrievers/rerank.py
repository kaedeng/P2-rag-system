"""Listwise reranking (stage 1): Claude reorders hybrid's top 20.

It is rerank_one() from the 13 lab's pipeline.py:
- the first stage is hybrid (p2.retrievers.build), and its top N candidates ([rerank] candidates in
  p2.toml, default 20) go to Claude as numbered passages, each document cut at [chunking] words words,
  title line included;
- the reply is forced into {"order": [N numbers]}, each between 1 and N, through p2.claude.call, one
  call per query, with saved replies in .cache/claude/;
- a reply that is not each number from 1 to N once, a reply with an error, or a call that fails keeps
  the first-stage order (only Exception is caught: ClaudeBlocked, which p2 check raises, passes through);
- the documents below the N keep their first-stage order underneath.
The prompt depends on the query and the candidates only, never on k, so a deeper search reuses the
saved reply. Scores come from the final rank (the corpus size for rank 1, one less for each rank
after), so they are whole numbers, strictly decreasing, and the same whatever k is.
search_chunks does the same over hybrid's top N chunks, for `p2 answer --system rerank`; a chunk after a
document's first is shown under the document's title line, so Claude knows which section it is from.
"""

from __future__ import annotations

import sys

from p2 import claude, retrievers
from p2.corpus import split_words

NEEDS_CLAUDE = True
CANDIDATES = 20

INSTRUCTION = (
    "Order the {n} numbered passages below by how relevant each one is to the query, most relevant first. "
    "Return every passage number from 1 to {n} exactly once."
)


def prompt(query: str, passages: list[str]) -> str:
    """What Claude sees: the instruction, the query, and the passages numbered from 1."""
    numbered = "\n\n".join(f"[{i}]\n{passage.strip()}" for i, passage in enumerate(passages, 1))
    return f"{INSTRUCTION.format(n=len(passages))}\n\nQuery: {query}\n\nPassages:\n\n{numbered}\n"


def schema(n: int) -> dict:
    """The reply's shape: n passage numbers, each from 1 to n."""
    return {
        "type": "object",
        "properties": {
            "order": {
                "type": "array",
                "items": {"type": "integer", "minimum": 1, "maximum": n},
                "minItems": n,
                "maxItems": n,
            }
        },
        "required": ["order"],
        "additionalProperties": False,
    }


def permutation(output, n: int) -> list[int] | None:
    """The reply's order as 0-based positions, or None unless it names every number from 1 to n once."""
    numbers = output.get("order") if isinstance(output, dict) else None
    if not isinstance(numbers, list) or any(type(x) is not int for x in numbers):
        return None
    if sorted(numbers) != list(range(1, n + 1)):
        return None
    return [x - 1 for x in numbers]


def warn(reason: str) -> None:
    print(f"    rerank kept the first-stage order: {reason}", file=sys.stderr, flush=True)


class Rerank:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.cfg = cfg
        self.first = retrievers.build("hybrid", corpus, cfg)
        self.n = int(cfg.table("rerank").get("candidates", CANDIDATES))
        self.model = cfg.model
        self.cache_dir = claude.cache_folder(cfg)
        # What Claude sees for a chunk: the chunk itself, or, after a document's first chunk, the
        # document's title line and then the chunk (the chunk's text is unchanged).
        self.chunk_passages: dict[str, str] = {}
        for chunk in corpus.chunks(cfg.chunk_words, cfg.chunk_overlap):
            title = corpus.docs[chunk.docid].text.split("\n", 1)[0]
            self.chunk_passages[chunk.id] = chunk.text if chunk.n == 0 else f"{title}\n\n{chunk.text}"

    def passage(self, docid: str) -> str:
        """A document cut at [chunking] words words, title line included (the whole document when words is 0)."""
        return split_words(self.corpus.docs[docid].text, self.cfg.chunk_words, 0)[0]

    def reorder(self, query: str, ids: list[str], passages: list[str]) -> list[str]:
        """The candidates in Claude's order, or in first-stage order when the reply cannot be used."""
        n = len(ids)
        if n < 2:
            return ids
        try:
            reply = claude.call(prompt(query, passages), schema(n), model=self.cfg.model, cache_dir=self.cache_dir)
        except Exception as error:  # noqa: BLE001 - any failed call keeps the first stage; ClaudeBlocked is a BaseException and passes
            warn(f"the call failed ({type(error).__name__}: {error})")
            return ids
        if reply.error:
            warn(f"the reply has an error ({reply.error})")
            return ids
        positions = permutation(reply.output, n)
        if positions is None:
            warn(f"the reply is not each number from 1 to {n} once ({reply.output})")
            return ids
        return [ids[i] for i in positions]

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        first = [docid for docid, _ in self.first.search(text, max(k, self.n))]
        top = first[: self.n]
        ranked = self.reorder(text, top, [self.passage(d) for d in top]) + first[self.n :]
        total = len(self.corpus.docs)
        return [(docid, float(total - i)) for i, docid in enumerate(ranked[:k])]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        first = [cid for cid, _ in self.first.search_chunks(text, max(k, self.n))]
        top = first[: self.n]
        ranked = self.reorder(text, top, [self.chunk_passages[c] for c in top]) + first[self.n :]
        total = len(self.chunk_passages)
        return [(cid, float(total - i)) for i, cid in enumerate(ranked[:k])]


def build(corpus, cfg):
    return Rerank(corpus, cfg)
