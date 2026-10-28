# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I chose the rust language docs (the language core itself) because I like the Rust language and use it frequently. I wanted to see whether or not having a rag system of the docs would improve model performance, since the standards of the language are pretty high. Id believe that hybrid woul perform the best since these docs are fairly long but only specific parts are relevant. I'd think that rerank might perform poorly since, once again, these docs are too long.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

The fork was the RRF k value in `hybrid`. There was a default lab's value, 60, and a smaller k. We first picked 60, but after benchmarking, switched to 10. the original was that a large k will average to a correct answer with some noise. with a lower k value (10), we measured that the k=10 minus k=60, MRR@10: +0.117, 95% paired interval [+0.037, +0.218], this excludes zero, MDD 0.135. Recall@10: +0.200 [+0.067, +0.358]. Another piece of data we got was that rerank went from 0.750 to 0.900 with no change to the reranker, We chose 10 instead of 1 (despite k=1 having the best MRR at 0.668), because there was more risk of false confidence at k=1 for a very small difference (k=1 minus k=10, MRR@10: +0.081 [+0.002, +0.175], MDD 0.130. Lower bound +0.002, recall@10: +0.000). Measuring costs 0 `claude -p` calls and took 1 script to run and switching costs 60 rerank calls (~790k input tokens). 

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

Claude advised for sticking with k=60 for RRF in hybrid, I overruled it for a lower k value after measuring. The measurement said that k=1 performed better

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

My corpus' MRR was 0.85-0.88 on a very wide casting gold set. To make me trust this, I'd expect the same performance for the systems under it. I tested it and it showed how the rerank's performance lead flips.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

passage() in p2/retrievers/rerank.py shows the first 300 words. For query h03, hybrid rank 2, rerank rank 10, page 5,280 words.