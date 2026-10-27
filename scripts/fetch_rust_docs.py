"""Fetch the Rust compiler's in-tree documentation books from rust-lang/rust into a raw folder for `p2 ingest`.

    uv run python scripts/fetch_rust_docs.py ../p2-raw/rust-docs [--sha COMMIT]

Books: src/doc/rustc-dev-guide, rustc, rustdoc and style-guide (their src/ folders, Markdown only, SUMMARY.md left out
because it is mdbook's table of contents). Every file is saved flat as <book>__<path with / as __>.md so the document
ids p2 ingest derives from file names stay unique and readable, and paths.tsv records each file's book, original path
and GitHub URL at the pinned commit. An mdbook `{{#include file}}` directive becomes a one-line note that the example is omitted. Nothing is run from the downloaded folder. Licensed MIT OR Apache-2.0 with the
Rust repository (README.md, LICENSE-MIT, LICENSE-APACHE).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = "rust-lang/rust"
BOOKS = ("rustc-dev-guide", "rustc", "rustdoc", "style-guide")
API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
INCLUDE = re.compile(r"\{\{#include\s+([^}]*)\}\}")


def get_json(url: str):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "p2-fetch"}), timeout=60) as r:
        return json.load(r)


def tree(sha: str, recursive: bool = False) -> list[dict]:
    return get_json(f"{API}/repos/{REPO}/git/trees/{sha}{'?recursive=1' if recursive else ''}")["tree"]


def child(entries: list[dict], name: str) -> str:
    for e in entries:
        if e["path"] == name and e["type"] == "tree":
            return e["sha"]
    raise SystemExit(f"no folder {name!r} in the tree")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("out", type=Path)
    ap.add_argument("--sha", default=None, help="commit of rust-lang/rust (default: the tip of main)")
    args = ap.parse_args()
    sha = args.sha or get_json(f"{API}/repos/{REPO}/commits/main")["sha"]
    print(f"rust-lang/rust at {sha}")
    doc = child(tree(child(tree(sha), "src")), "doc")
    doc_entries = tree(doc)
    jobs = []
    for book in BOOKS:
        src = child(tree(child(doc_entries, book)), "src")
        for e in tree(src, recursive=True):
            if e["type"] == "blob" and e["path"].endswith(".md") and Path(e["path"]).name != "SUMMARY.md":
                flat = f"{book}__{e['path'].replace('/', '__')}"
                jobs.append((book, e["path"], flat, e["size"]))
    args.out.mkdir(parents=True, exist_ok=True)

    def fetch(job):
        book, rel, flat, _size = job
        url = f"{RAW}/{REPO}/{sha}/src/doc/{book}/src/{rel}"
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "p2-fetch"}), timeout=60) as r:
            text = r.read().decode("utf-8")
        # mdbook's {{#include path}} splices another file in at build time; the text alone would keep the directive.
        text = INCLUDE.sub(lambda m: f"(code example omitted here: {m.group(1).strip()})", text)
        (args.out / flat).write_text(text, encoding="utf-8", newline="\n")
        return flat

    with ThreadPoolExecutor(max_workers=16) as pool:
        done = list(pool.map(fetch, jobs))
    with open(args.out / "paths.tsv", "w", encoding="utf-8", newline="\n") as f:
        f.write("file\tbook\tpath\tsource\n")
        for book, rel, flat, _ in sorted(jobs, key=lambda j: j[2]):
            f.write(f"{flat}\t{book}\t{rel}\thttps://github.com/{REPO}/blob/{sha}/src/doc/{book}/src/{rel}\n")
    (args.out / "COMMIT").write_text(sha + "\n", encoding="utf-8")
    total = sum(j[3] for j in jobs)
    print(f"saved {len(done)} files ({total / 1024 / 1024:.2f} MB) to {args.out}, paths in paths.tsv, commit in COMMIT", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
