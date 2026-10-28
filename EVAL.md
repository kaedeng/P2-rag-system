# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

chunking (for all parts): each section is cut into 300 word windows, neighbors share 50 words. Most sections are shorter than 300
words so one chunk. Each run is document level. Documents scores its best chunk.

`dense`: Using `bge-small-en-v1.5`, loaded from `fastembed`, uses `384-dim` vectors, and the dot product is equal to the cosine. What's kept from the lab is that query prefixes were kept off.

`hybrid`: Combines `bm25` plus `dense` using reciprocal rank fusion with `k=10` (changed after benchmarking different values) over the entirety of both rankings. One change from the code is that we dropped bm25's zero score padding before running fusion.

`reranker`: Chooses the top 20 from hybrid each query gets a `claude -p` call using sonnet, each passage is cut at 300 words, and reply is forced to a permutation of 1-20. bad reply keeps it's hybrid order, and docs below 20 stay underneath.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.617 | 0.471 | 0.456 |
| rerank | 0.700 | 0.750 | 0.705 |
| rerank_c10 | 0.617 | 0.705 | 0.618 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.571 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.152 | 0.792 |
| hybrid | nDCG@10 | 0.435 | 0.202 | 0.779 |
| rerank | Recall@10 | 0.643 | 0.500 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.571 | 1.000 |
| rerank | nDCG@10 | 0.641 | 0.516 | 1.000 |
| rerank_c10 | Recall@10 | 0.571 | 0.405 | 0.917 |
| rerank_c10 | MRR@10 | 0.586 | 0.571 | 1.000 |
| rerank_c10 | nDCG@10 | 0.524 | 0.440 | 0.936 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.008 | [-0.225, +0.208] | 0.317 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.037 | [-0.178, +0.083] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.062 | [-0.218, +0.082] | 0.218 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.058 | [-0.117, +0.242] | 0.261 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.092 | [-0.306, +0.109] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.023 | [-0.193, +0.137] | 0.240 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.075 | [-0.150, +0.300] | 0.341 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.243 | [+0.010, +0.476] | 0.339 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.187 | [-0.040, +0.412] | 0.328 | not distinguishable |
| rerank minus dense | Recall@10 | +0.142 | [-0.050, +0.325] | 0.267 | not distinguishable |
| rerank minus dense | MRR@10 | +0.188 | [-0.017, +0.392] | 0.294 | not distinguishable |
| rerank minus dense | nDCG@10 | +0.226 | [+0.041, +0.402] | 0.263 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.083 | [+0.000, +0.175] | 0.129 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.279 | [+0.128, +0.443] | 0.230 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.249 | [+0.135, +0.372] | 0.174 | rerank higher |
| rerank_c10 minus bm25 | Recall@10 | -0.008 | [-0.225, +0.208] | 0.317 | not distinguishable |
| rerank_c10 minus bm25 | MRR@10 | +0.198 | [-0.068, +0.452] | 0.374 | not distinguishable |
| rerank_c10 minus bm25 | nDCG@10 | +0.100 | [-0.137, +0.325] | 0.335 | not distinguishable |
| rerank_c10 minus dense | Recall@10 | +0.058 | [-0.117, +0.242] | 0.261 | not distinguishable |
| rerank_c10 minus dense | MRR@10 | +0.142 | [-0.086, +0.371] | 0.331 | not distinguishable |
| rerank_c10 minus dense | nDCG@10 | +0.139 | [-0.052, +0.324] | 0.275 | not distinguishable |
| rerank_c10 minus hybrid | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| rerank_c10 minus hybrid | MRR@10 | +0.234 | [+0.037, +0.424] | 0.281 | rerank_c10 higher |
| rerank_c10 minus hybrid | nDCG@10 | +0.162 | [+0.044, +0.281] | 0.172 | rerank_c10 higher |
| rerank_c10 minus rerank | Recall@10 | -0.083 | [-0.175, +0.000] | 0.129 | not distinguishable |
| rerank_c10 minus rerank | MRR@10 | -0.045 | [-0.135, +0.000] | 0.126 | not distinguishable |
| rerank_c10 minus rerank | nDCG@10 | -0.087 | [-0.172, -0.019] | 0.113 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

MRR@10 is distinguishable from zero, with rerank minus hybrid +0.313 [+0.160, +0.478]; rerank minus bm25 +0.393 [+0.200, +0.595];  rerank minus dense +0.338 [+0.150, +0.533]).
Not distinguishable is hybrid minus bm25 +0.080 [-0.099, +0.267].
The minimum detectable difference is roughly 0.19-0.41.
Lecture 12's claim about how no retriever wins is supported by my numbers, ex. bm25 identifier recall 1.000, paraphrase 0.000; dense 0.214 and 0.595. One thing left open was whether hybrid beats either input, since those intervals include zero.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 13 of 13 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

The system answered was rerank because its the only one with a visible win over its firsts stage. the prompts/answer.txt was unchanged. the verified/declined share stayed the same.

a01: 'Within how many minutes must a mine operator call MSHA after an accident that kills a miner?' \\
Source: 'The operator shall immediately contact MSHA at once without delay and within 15 minutes at the toll-free number, 1-800-746-1553, once the operator knows or should know that an accident has occurred involving:' \\
This supports the claim

a02: 'What minimum incombustible content must the combined dust in an underground coal mine keep where no methane is present?'
Source: 'Where rock dust is required to be applied, it shall be distributed upon the top, floor, and sides of all underground areas of a coal mine and maintained in such quantities that the incombustible content of the combined coal dust, rock dust, and other dust shall be not less than 80 percent. Where methane is present in any ventilating current, the percent of incombustible content of such combined dust shall be increased 0.4 percent for each 0.1 percent of methane.'
This supports the claim

a05: 'How many hours of training must a new underground miner receive before being assigned to work duties?'
Source: '(a) Each new miner shall receive no less than 40 hours of training as prescribed in this section before such miner is assigned to work duties. Such training shall be conducted in conditions which as closely as practicable duplicate actual underground conditions, and approximately 8 hours of training shall be given at the minesite.'
This supports the claim

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

Corpus is from the rust compiler documentation (rustc-dev-guide, rustc book, rustdoc book, style guide, from rust-lang/rust) from commit 41089d07a0a2afc16adfe28a760d94d73d7298a4 fetched with `scripts/fetch_rust_docs.py`. It is a 424 document corpus which is roughly 2.6 MB. The set has a median of 520 words, which is 69% larger than one chunk. The license and repo licence is MIT/Apache 2.0. We removed some licensing that was unknown.  

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

The set is 30 queries, 10 hand picked and 20 claude picked. there is 10 identifiers, 11 paraphrases, and 9 mixed. The rule was that the document must have either examples of the requested item, or the document's behavior is related to the requested item's behavior. We excluded files that were 0 lines long. The candidates wer echosen from a union of bm25, dense, and hybrid top 10 using `scripts/candidates.py`, keyword grep, and the page each draft was written from. three draft source pages (c11-13) were in no system's top 10.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.780 | 0.762 | 0.716 |
| dense | 0.682 | 0.776 | 0.636 |
| hybrid | 0.778 | 0.827 | 0.745 |
| rerank | 0.763 | 0.887 | 0.747 |

50 judged queries; nDCG uses binary labels; a random ranking of the 424 documents would get recall@10 near 0.024.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | identifier (n=17) | paraphrase (n=18) | mixed (n=15) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 0.992 | 0.479 | 0.900 |
| bm25 | MRR@10 | 0.953 | 0.420 | 0.956 |
| bm25 | nDCG@10 | 0.953 | 0.349 | 0.889 |
| dense | Recall@10 | 0.838 | 0.458 | 0.775 |
| dense | MRR@10 | 0.894 | 0.505 | 0.967 |
| dense | nDCG@10 | 0.788 | 0.394 | 0.753 |
| hybrid | Recall@10 | 0.954 | 0.516 | 0.894 |
| hybrid | MRR@10 | 0.971 | 0.576 | 0.967 |
| hybrid | nDCG@10 | 0.928 | 0.463 | 0.875 |
| rerank | Recall@10 | 0.924 | 0.546 | 0.841 |
| rerank | MRR@10 | 0.947 | 0.736 | 1.000 |
| rerank | nDCG@10 | 0.864 | 0.555 | 0.843 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=40) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.930 | 0.742 | +0.188 | [+0.039, +0.326] | hand higher |
| bm25 | MRR@10 | 0.787 | 0.756 | +0.031 | [-0.219, +0.256] | not distinguishable |
| bm25 | nDCG@10 | 0.791 | 0.698 | +0.093 | [-0.106, +0.280] | not distinguishable |
| dense | Recall@10 | 0.848 | 0.641 | +0.207 | [+0.058, +0.352] | hand higher |
| dense | MRR@10 | 0.900 | 0.745 | +0.155 | [-0.024, +0.324] | not distinguishable |
| dense | nDCG@10 | 0.787 | 0.598 | +0.189 | [+0.064, +0.317] | hand higher |
| hybrid | Recall@10 | 0.983 | 0.727 | +0.256 | [+0.149, +0.364] | hand higher |
| hybrid | MRR@10 | 0.900 | 0.809 | +0.091 | [-0.081, +0.251] | not distinguishable |
| hybrid | nDCG@10 | 0.903 | 0.705 | +0.198 | [+0.060, +0.330] | hand higher |
| rerank | Recall@10 | 0.938 | 0.720 | +0.219 | [+0.090, +0.344] | hand higher |
| rerank | MRR@10 | 0.910 | 0.881 | +0.029 | [-0.191, +0.194] | not distinguishable |
| rerank | nDCG@10 | 0.818 | 0.729 | +0.089 | [-0.083, +0.246] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.101 | +0.082 | +0.019 | [-0.122, +0.149] | not distinguishable |
| MRR@10 | +0.011 | -0.113 | +0.124 | [-0.090, +0.344] | not distinguishable |
| nDCG@10 | +0.100 | +0.003 | +0.097 | [-0.062, +0.251] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.92 (10 queries), claude 0.82 (40 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 40 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.097 | [-0.163, -0.031] | 0.095 | bm25 higher |
| dense minus bm25 | MRR@10 | +0.014 | [-0.058, +0.086] | 0.103 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.081 | [-0.144, -0.015] | 0.092 | bm25 higher |
| hybrid minus bm25 | Recall@10 | -0.001 | [-0.050, +0.042] | 0.065 | not distinguishable |
| hybrid minus bm25 | MRR@10 | +0.065 | [+0.018, +0.124] | 0.078 | hybrid higher |
| hybrid minus bm25 | nDCG@10 | +0.028 | [-0.019, +0.079] | 0.070 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.096 | [+0.046, +0.148] | 0.074 | hybrid higher |
| hybrid minus dense | MRR@10 | +0.052 | [+0.002, +0.108] | 0.077 | hybrid higher |
| hybrid minus dense | nDCG@10 | +0.109 | [+0.069, +0.151] | 0.059 | hybrid higher |
| rerank minus bm25 | Recall@10 | -0.016 | [-0.074, +0.039] | 0.081 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.125 | [+0.050, +0.212] | 0.118 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.030 | [-0.036, +0.098] | 0.096 | not distinguishable |
| rerank minus dense | Recall@10 | +0.081 | [+0.030, +0.134] | 0.074 | rerank higher |
| rerank minus dense | MRR@10 | +0.111 | [+0.037, +0.195] | 0.114 | rerank higher |
| rerank minus dense | nDCG@10 | +0.111 | [+0.058, +0.166] | 0.077 | rerank higher |
| rerank minus hybrid | Recall@10 | -0.015 | [-0.058, +0.026] | 0.061 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.060 | [+0.000, +0.130] | 0.094 | not distinguishable |
| rerank minus hybrid | nDCG@10 | +0.002 | [-0.046, +0.052] | 0.070 | not distinguishable |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

Whats distinguishable is hybrid minus bm25 +0.101 [+0.026, +0.196] and rerank minus bm25 +0.132 [+0.039, +0.243].
Whats not distinguishable is rerank minus hybrid +0.032 [-0.026, +0.106], MDD 0.098; rerank minus dense +0.078 [-0.002, +0.172].
Hand queries were ranked higher on every system, while claude queries performed lower, there was a recall cap of +0.18 to +0.22. My prediction was that rerank would perform the worse, but it was indistinguishable in performance to hybrid (one of the best systems).

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

<!-- p2:begin own-ablation -->
_No ablation runs yet: `uv run p2 run --corpus own --system NAME --ablation` writes one to runs/own/ablation/, then `uv run p2 score` fills this table._
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
_No ablation runs yet: `uv run p2 run --corpus own --system NAME --ablation` writes one to runs/own/ablation/, then `uv run p2 score` fills this table._
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

I expect that dense_prefix will have no change in dense's MRR@10 since the 40 drafts are full sentences and my chunks are 300 word passages, the prefix was designed for short queries, so the effect would be too small for the 50 queries to see. MDD for a dense vs dense pair will be small.

After running it, the result was +0.007 k=10 - k=60, so based on this, the k value on this corpus does not matter. In the shared corpus that was split by class, the systems had some disagreeances, but in this corpus, the two systems mostly agree (28/30 queries identical).

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|
|c12|rustc_jobserver|rank 41, RR0|idk|idk|
|c11|rustc_remap-source-paths|rank below 50|idk|idk|
|c08|two-phase-borrows|rank below 50 despite example|idk|idk|
|c09|pr_lifecycle|missing tests_crater|idk|idk|
|h03|rustdoc_unstable-features|hybrid 2, rerank 10, 5280 words|idk|idk|

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

The winner by MRR was rerank on both, but the gap between the two is different, on the shared corpus its +0.313, on my corpus its +0.032. The difference is likely the page length being so different, with the shared corpus having a median length of 62 while my corpus has 520.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
rider
2. What you did, and the files that hold it.
files: 
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.
For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 2 | 192,395 | 4,375 | 101.0 | 16,033 | 365 | 8.4 |
| traces/answers-rerank.r1.jsonl | rerank | 12 | 24 | 0 | 192,297 | 4,062 | 86.6 | 16,025 | 338 | 7.2 |
| traces/answers-rerank.r2.jsonl | rerank | 12 | 24 | 0 | 205,912 | 4,487 | 92.0 | 17,159 | 374 | 7.7 |
| traces/answers-rerank.r3.jsonl | rerank | 12 | 24 | 0 | 191,641 | 4,407 | 94.0 | 15,970 | 367 | 7.8 |
| traces/own-own-rerank.jsonl | rerank | 50 | 50 | 2 | 841,528 | 4,985 | 199.6 | 16,831 | 100 | 4.0 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 20 | 258,859 | 2,122 | 113.5 | 12,943 | 106 | 5.7 |
| traces/shared-practice-rerank.r1.jsonl | rerank | 20 | 20 | 0 | 279,754 | 2,206 | 87.6 | 13,988 | 110 | 4.4 |
| traces/shared-practice-rerank.r2.jsonl | rerank | 20 | 20 | 0 | 257,310 | 2,183 | 73.4 | 12,866 | 109 | 3.7 |
| traces/shared-practice-rerank.r3.jsonl | rerank | 20 | 20 | 0 | 245,042 | 1,820 | 70.3 | 12,252 | 91 | 3.5 |
| traces/shared-practice-rerank_c10.jsonl | rerank_c10 | 20 | 20 | 0 | 157,135 | 1,560 | 63.4 | 7,857 | 78 | 3.2 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 40 | 532,625 | 4,456 | 200.2 | 13,316 | 111 | 5.0 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.243 | [-0.476, -0.010] | 12,943 | 5.7 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.188 | [-0.392, +0.017] | 12,943 | 5.7 | not distinguishable |
| shared practice: hybrid minus rerank | 20 | -0.279 | [-0.443, -0.128] | 12,943 | 5.7 | rerank higher |
| shared practice: bm25 minus rerank_c10 | 20 | -0.198 | [-0.452, +0.068] | 7,857 | 3.2 | not distinguishable |
| shared practice: dense minus rerank_c10 | 20 | -0.142 | [-0.371, +0.086] | 7,857 | 3.2 | not distinguishable |
| shared practice: hybrid minus rerank_c10 | 20 | -0.234 | [-0.424, -0.037] | 7,857 | 3.2 | rerank_c10 higher |
| shared practice: rerank_c10 minus rerank | 20 | -0.045 | [-0.135, +0.000] | 5,086 | 2.5 | not distinguishable |
| own: bm25 minus rerank | 50 | -0.125 | [-0.212, -0.050] | 16,831 | 4.0 | rerank higher |
| own: dense minus rerank | 50 | -0.111 | [-0.195, -0.037] | 16,831 | 4.0 | rerank higher |
| own: hybrid minus rerank | 50 | -0.060 | [-0.130, +0.000] | 16,831 | 4.0 | not distinguishable |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-hybrid_k60.jsonl | hybrid_k60 | 50 | 0.22 | 4.3 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 50 | 0.03 | 0.6 |
| traces/retrieval/own-own-dense.jsonl | dense | 50 | 0.18 | 3.5 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 50 | 0.22 | 4.4 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.02 | 1.1 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.09 | 4.7 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.12 | 6.2 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.05 | 1.2 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.16 | 4.0 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.25 | 6.3 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
Repeated runs of rerank on shared/practice:

| Run | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank.r1 | 0.700 | 0.750 | 0.705 |
| rerank.r2 | 0.700 | 0.750 | 0.707 |
| rerank.r3 | 0.700 | 0.750 | 0.703 |
| range (max minus min) | 0.000 | 0.000 | 0.004 |

| Comparison | Metric | Mean difference | 95% interval | Reading |
| --- | --- | ---: | ---: | --- |
| rerank.r1 minus hybrid | Recall@10 | +0.083 | [+0.000, +0.175] | not distinguishable |
| rerank.r2 minus hybrid | Recall@10 | +0.083 | [+0.000, +0.175] | not distinguishable |
| rerank.r3 minus hybrid | Recall@10 | +0.083 | [+0.000, +0.175] | not distinguishable |
| rerank.r1 minus hybrid | MRR@10 | +0.279 | [+0.128, +0.443] | rerank.r1 higher |
| rerank.r2 minus hybrid | MRR@10 | +0.279 | [+0.128, +0.443] | rerank.r2 higher |
| rerank.r3 minus hybrid | MRR@10 | +0.279 | [+0.128, +0.443] | rerank.r3 higher |
| rerank.r1 minus hybrid | nDCG@10 | +0.249 | [+0.135, +0.372] | rerank.r1 higher |
| rerank.r2 minus hybrid | nDCG@10 | +0.251 | [+0.137, +0.375] | rerank.r2 higher |
| rerank.r3 minus hybrid | nDCG@10 | +0.247 | [+0.131, +0.373] | rerank.r3 higher |

Repeated answers shared/rerank:

| File | Verified (in) | 95% interval | Declined (out) | 95% interval |
| --- | ---: | ---: | ---: | ---: |
| rerank.r1 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r2 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r3 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| range (max minus min) | 0.000 |  | 0.000 |  |

Each repeat answers the same questions, so the repeats are not independent trials and their counts are not pooled into one interval.
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
