#!/usr/bin/env python3
"""Validate summary math markup and its passage through Quarto listing templates.

Source errors are blocking; likely unmarked notation is advisory. The rendered
check compares inline TeX with the source, not mathematical correctness or
MathJax's browser output. Run browser checks after changes to the rendering path.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


# Deliberately advisory: these can also be ordinary words or identifiers.
SUSPECT = re.compile(
    r"[\^_]|\\[A-Za-z]+|[α-ωΑ-Ω]|>=|<=|"
    r"\b(?:alpha|beta|gamma|delta|eps|epsilon|eta|theta|kappa|lambda|mu|"
    r"pi|rho|sigma|tau|Omega|Theta|Otilde|sqrt|log|ln)\b|"
    r"\b(?:O|o|poly)\s*\("
)


def escaped(text, pos):
    start = pos
    while start and text[start - 1] == "\\":
        start -= 1
    return (pos - start) % 2 == 1


def parse_summary(text):
    """Return (inline TeX expressions, prose, definite markup errors)."""
    if not isinstance(text, str) or not text.strip():
        return [], "", ["status_summary must be a non-empty string"]
    errors, maths, prose = [], [], []
    if re.search(r"[\x00-\x1f\x7f-\x9f\u2028\u2029]", text):
        errors.append("line break or control character in summary; use YAML >- to preserve TeX backslashes")
    start = None
    i = 0
    while i < len(text):
        # Inline code is prose, not TeX. Avoid flagging literal examples.
        if start is None and text[i] == "`" and not escaped(text, i):
            end_run = i + 1
            while end_run < len(text) and text[end_run] == "`":
                end_run += 1
            end = text.find(text[i:end_run], end_run)
            if end != -1:
                i = end + end_run - i
                prose.append(" ")
                continue
        if text[i] == "$" and not escaped(text, i):
            if i + 1 < len(text) and text[i + 1] == "$":
                errors.append("display math ($$) is not supported in summaries; use inline $...$")
                i += 2
                continue
            if start is None:
                start = i + 1
                prose.append(" ")
            else:
                expr = text[start:i]
                if not expr or expr != expr.strip():
                    errors.append("inline math must be non-empty with no whitespace next to $ delimiters")
                if i + 1 < len(text) and text[i + 1].isdigit():
                    errors.append("closing math delimiter cannot be followed immediately by a digit")
                balance = 0
                for j, char in enumerate(expr):
                    if escaped(expr, j):
                        continue
                    if char == "{":
                        balance += 1
                    elif char == "}":
                        balance -= 1
                        if balance < 0:
                            break
                if balance != 0:
                    errors.append("unbalanced braces in inline math")
                maths.append(expr)
                start = None
        elif start is None:
            prose.append(text[i])
        i += 1
    if start is not None:
        errors.append("unclosed $ delimiter in summary")
    return maths, "".join(prose), list(dict.fromkeys(errors))


def check_summary(text):
    _, prose, errors = parse_summary(text)
    tokens = sorted(set(m.group() for m in SUSPECT.finditer(prose)))
    warnings = ["possible unmarked math outside $...$: " + ", ".join(tokens)] if tokens else []
    return errors, warnings


class SummaryHTML(HTMLParser):
    """Collect each statement-table row, even if its summary has disappeared."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows = []
        self.table_depth = 0
        self.row = None
        self.title_cell = False
        self.title_link_seen = False
        self.summary_depth = 0
        self.math_depth = 0
        self.math_text = ""
        self.maths = []
        self.has_mathjax = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "script" and "mathjax" in attrs.get("src", "").lower():
            self.has_mathjax = True
        if tag == "table":
            if self.table_depth:
                self.table_depth += 1
            elif "cj-statement-table" in classes:
                self.table_depth = 1
        if not self.table_depth:
            return
        if tag == "tr":
            self.row = {"leaf": None, "summaries": [], "data": False}
            self.title_link_seen = False
        if self.row is None:
            return
        if tag == "td":
            self.row["data"] = True
            self.title_cell = "listing-title" in classes
        # Only the title cell's first link identifies the row. A cross-link
        # in its summary, or any other column, must not replace that identity.
        if tag == "a" and self.title_cell and not self.summary_depth and not self.title_link_seen:
            self.title_link_seen = True
            match = re.search(r"(?:^|/)c/(\d{4})/(?:index\.html)?(?:[?#].*)?$", attrs.get("href", ""))
            if match:
                self.row["leaf"] = match[1]
        if tag != "span":
            return
        if "cj-status-summary" in classes:
            self.summary_depth = 1
            self.maths = []
        elif self.summary_depth:
            self.summary_depth += 1
        if self.summary_depth and "math" in classes:
            self.math_depth = self.summary_depth
            self.math_text = ""

    def handle_data(self, data):
        if self.math_depth:
            self.math_text += data

    def handle_endtag(self, tag):
        if tag == "span" and self.summary_depth:
            if self.math_depth == self.summary_depth:
                self.maths.append(self.math_text)
                self.math_depth = 0
            self.summary_depth -= 1
            if self.summary_depth == 0 and self.row is not None:
                self.row["summaries"].append(self.maths)
        elif tag == "td":
            self.title_cell = False
        elif tag == "tr" and self.row is not None:
            if self.row["data"]:
                self.rows.append(self.row)
            self.row = None
            self.title_cell = False
            self.summary_depth = self.math_depth = 0
        elif tag == "table" and self.table_depth:
            self.table_depth -= 1


def rendered_errors(html, summaries, expected_ids=None):
    page = SummaryHTML()
    page.feed(html)
    errors = []
    if expected_ids is not None:
        expected_rows = Counter(expected_ids)
        actual_rows = Counter(row["leaf"] for row in page.rows)
        missing = list((expected_rows - actual_rows).elements())
        extra = list((actual_rows - expected_rows).elements())
        if missing or extra:
            errors.append(f"listing membership differs from generated index (missing {missing!r}, extra {extra!r})")
    for row in page.rows:
        leaf = row["leaf"]
        if leaf not in summaries:
            errors.append(f"row has no matching source statement title: {leaf}")
            continue
        if len(row["summaries"]) != 1:
            errors.append(f"c/{leaf}: expected exactly one summary, found {len(row['summaries'])}")
            continue
        actual = row["summaries"][0]
        maths, _, source_errors = parse_summary(summaries[leaf])
        errors.extend(f"c/{leaf}: {error}" for error in source_errors)
        expected = [r"\(" + expr + r"\)" for expr in maths]
        if actual != expected:
            errors.append(f"c/{leaf}: rendered math differs from source (expected {expected!r}, got {actual!r})")
        if expected and not page.has_mathjax:
            errors.append(f"c/{leaf}: page has math but no MathJax script")
    return errors, len(page.rows)


def audit_site(root, site):
    """Check every configured statement listing against its generated membership."""
    import yaml

    def frontmatter(path):
        return yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])

    summaries, browsable = {}, set()
    errors, warnings = [], []
    for path in sorted((root / "c").glob("*/index.qmd")):
        fm = frontmatter(path)
        summary = fm.get("status_summary")
        leaf = path.parent.name
        summaries[leaf] = summary
        if fm.get("category") != "withdrawn":
            browsable.add(leaf)
        source_errors, source_warnings = check_summary(summary)
        errors.extend(f"{path.relative_to(root)}: {e}" for e in source_errors)
        warnings.extend(f"{path.relative_to(root)}: {w}" for w in source_warnings)
    total = pages = 0
    found_catalogue = False
    for source in sorted((root / "problems").rglob("*.qmd")):
        listing = frontmatter(source).get("listing", {})
        if not isinstance(listing, dict) or Path(listing.get("template", "")).name != "statement-table.ejs.md":
            continue
        output = site / source.relative_to(root).with_suffix(".html")
        contents = source.parent / listing["contents"]
        if not contents.is_file():
            errors.append(f"{source}: generated listing index missing: {contents}; run build_index.py")
            continue
        items = yaml.safe_load(contents.read_text(encoding="utf-8"))
        expected_ids = [str(item["id"]) for item in items]
        if source.relative_to(root).as_posix() == "problems/all/index.qmd":
            found_catalogue = True
            if Counter(expected_ids) != Counter(browsable):
                errors.append("all-statements generated index does not match browsable source statements")
        if not output.is_file():
            errors.append(f"{output}: rendered listing missing; render the site first")
            continue
        found, count = rendered_errors(output.read_text(encoding="utf-8"), summaries, expected_ids)
        errors.extend(f"{output}: {e}" for e in found)
        total += count
        pages += 1
    if not found_catalogue:
        errors.append("all-statements catalogue configuration or generated index missing")
    if not total:
        errors.append("no rendered catalogue summaries found; render the site first")
    return errors, warnings, total, pages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True, help="rendered site directory")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors, warnings, total, pages = audit_site(root, args.site)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"Checked {total} summary rows across {pages} listing pages; {len(errors)} error(s)")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
