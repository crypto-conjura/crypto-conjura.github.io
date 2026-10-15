#!/usr/bin/env python3
"""Use statement pagetitle in search, where Quarto otherwise copies h1 TeX.

Quarto already uses pagetitle for browser and social metadata. Its search index
instead takes the visible heading's textContent, including MathJax delimiters.
Run after rendering, including partial renders, and update only title fields of
matching statement search entries. Body text, sections and other pages stay as
generated. Authors supply a readable plain-text equivalent for arbitrary math.
"""
import json
import os
from pathlib import Path

import yaml


def update_search_titles(root, site):
    search = site / "search.json"
    if not search.is_file():
        return 0
    titles = {}
    for source in (root / "c").glob("*/index.qmd"):
        fm = yaml.safe_load(source.read_text(encoding="utf-8").split("---", 2)[1])
        if isinstance(fm.get("pagetitle"), str) and fm["pagetitle"].strip():
            titles[source.relative_to(root).with_suffix(".html").as_posix()] = fm["pagetitle"]
    entries = json.loads(search.read_text(encoding="utf-8"))
    changed = 0
    for entry in entries:
        href = entry.get("href", "").split("#", 1)[0]
        if href in titles and entry.get("title") != titles[href]:
            entry["title"] = titles[href]
            changed += 1
    if changed:
        search.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    site = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR") or root / "_site")
    if not site.is_absolute():
        site = root / site
    print(f"plain_search_titles: updated {update_search_titles(root, site)} search title(s)")
