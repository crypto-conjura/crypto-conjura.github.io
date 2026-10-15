#!/usr/bin/env python3
"""Preserve published Problems section URLs after Quarto generates aliases.

Runs after full and partial renders. --check validates without writing, including
the destinations, so old bookmarks remain covered even without incoming links.
"""
import argparse
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import posixpath
import re
from urllib.parse import urlsplit


DESTINATIONS = {
    "": "problems/all/index.html",
    "browse": "problems/all/index.html",
    "the-status-badge": "reviews/status-badge/index.html#status-legend",
    "latex-templates": "problems/latex-templates/index.html",
}
LEGACY_PAGES = ("problems/index.html", "open-problems/index.html")
MAP = re.compile(r"var redirects = (\{[^\n]*\});")
QUERY_LINE = "redirect = redirect + window.location.search;"
QUERY_FIX = """var target = new URL(redirect, window.location.href);
    target.search = window.location.search;
    redirect = target.href;"""


class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "name" in attrs:
            self.ids.add(attrs["name"])


def check_destinations(site):
    for destination in set(DESTINATIONS.values()):
        url = urlsplit(destination)
        target = site / url.path
        if not target.is_file():
            raise ValueError(f"missing redirect destination: {destination}")
        if url.fragment:
            anchors = Anchors()
            anchors.feed(target.read_text(encoding="utf-8"))
            if url.fragment not in anchors.ids:
                raise ValueError(f"missing redirect section: {destination}")


def update_redirects(site, check=False):
    # A single-page preview may not have rendered the other destinations yet.
    # CI checks the complete output separately after the full site render.
    if check:
        check_destinations(site)
    updated_count = 0
    for legacy in LEGACY_PAGES:
        page = site / legacy
        if not check and not page.exists():
            continue
        text = page.read_text(encoding="utf-8")
        match = MAP.search(text)
        if not match or "window.location.replace(redirect);" not in text:
            raise ValueError(f"expected a Quarto alias page: {legacy}")
        mapping = json.loads(match[1])
        expected = {
            fragment: posixpath.relpath(destination, posixpath.dirname(legacy))
            for fragment, destination in DESTINATIONS.items()
        }
        if check:
            if QUERY_FIX not in text:
                raise ValueError(f"incorrect query/fragment handling: {legacy}")
            for fragment, destination in expected.items():
                if mapping.get(fragment) != destination:
                    raise ValueError(f"incorrect legacy redirect: {legacy}#{fragment}")
        else:
            mapping.update(expected)
            replacement = "var redirects = " + json.dumps(mapping) + ";"
            updated = text[:match.start()] + replacement + text[match.end():]
            # Quarto appends search after hash; an explicit target section then
            # becomes e.g. #status-legend?utm_source=... and no longer exists.
            if QUERY_LINE in updated:
                updated = updated.replace(QUERY_LINE, QUERY_FIX)
            elif QUERY_FIX not in updated:
                raise ValueError(f"unrecognized Quarto query handling: {legacy}")
            if updated != text:
                page.write_text(updated, encoding="utf-8")
                updated_count += 1
    return updated_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path(
        os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site")))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        updated = update_redirects(args.site, check=args.check)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"problem_redirects: {exc}\n")
    print("problem_redirects: legacy Problems routes verified" if args.check else
          f"problem_redirects: updated {updated} alias page(s)")
