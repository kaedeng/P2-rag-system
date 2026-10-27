"""Point each own-corpus manifest row at the real GitHub path of its document, after a flattened ingest.

    uv run python scripts/fix_rust_sources.py ../p2-raw/rust-docs

p2 ingest fills `source` from a template with {name}, the flat file name; paths.tsv (written by
scripts/fetch_rust_docs.py) has the nested path and URL at the pinned commit, and this script matches
each manifest docid to its row by the same slug rule ingest used.
"""

from __future__ import annotations

import sys
from pathlib import Path

from p2.ingest import slugify

MANIFEST = Path("corpora/own/manifest.tsv")


def main() -> int:
    raw = Path(sys.argv[1])
    rows = [line.rstrip("\n").split("\t") for line in (raw / "paths.tsv").read_text(encoding="utf-8").splitlines()[1:]]
    by_slug = {slugify(Path(file).stem): source for file, _book, _path, source in rows}
    lines = MANIFEST.read_text(encoding="utf-8").splitlines()
    out, fixed, missing = [lines[0]], 0, []
    for line in lines[1:]:
        cells = line.split("\t")
        docid = cells[0]
        base = docid.split("__p")[0] if "__p" in docid else docid  # a part keeps its file's source
        if base in by_slug:
            cells[2] = by_slug[base]
            fixed += 1
        else:
            missing.append(docid)
        out.append("\t".join(cells))
    MANIFEST.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(f"sources fixed for {fixed} rows; {len(missing)} without a match" + (f": {missing[:5]}" if missing else ""))
    return 0 if not missing else 1


if __name__ == "__main__":
    sys.exit(main())
