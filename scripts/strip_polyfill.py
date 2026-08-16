#!/usr/bin/env python3
"""
Remove the third-party polyfill script Quarto injects alongside MathJax.

Quarto 1.10.18 emits

  <script src="https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=es6"></script>

on every page carrying mathematics. It comes from Quarto's own HTML template,
not from anything in `_quarto.yml`, so `html-math-method` does not reach it and
there is no documented option that turns it off. This runs as a `post-render`
step instead, which is the supported place to touch generated output. Editing
`_site/` by hand would not survive the next build.

Why remove it rather than vendor it. MathJax's own documentation says of the
polyfill "We no longer recommend it", and separately that "We no longer test
MathJax with IE11, so you should not expect it to work with any version of
Internet Explorer" (docs.mathjax.org/en/latest/web/start.html, read 16 August
2026). A browser old enough to want an ES6 polyfill is one MathJax will not
render mathematics in anyway, so vendoring the file would ship bytes to nobody.

This is not an active security fix. The tag points at cdnjs.cloudflare.com,
which is the replacement Cloudflare stood up after the original polyfill.io
domain was sold and used to serve malware in 2024, and is not itself the
compromised host. The reason to drop it is that it is one more origin the site
depends on for no benefit, which is the same reason MathJax was vendored.

Run by `quarto render` through `project: post-render:`. Safe to run by hand,
and safe to run twice: it reports what it changed and exits 0 when there is
nothing left to change.
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Quarto sets this during a render; fall back for a manual run.
SITE = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR") or (ROOT / "_site"))
if not SITE.is_absolute():
    SITE = ROOT / SITE

# The whole tag, however Quarto spaces or quotes it, and whatever the query
# string carries. Anchored on the host so it can never match our own scripts.
TAG = re.compile(
    r"""\s*<script[^>]*\bsrc=["'][^"']*\bpolyfill[^"']*["'][^>]*>\s*</script>""",
    re.I)


def main():
    if not SITE.is_dir():
        print(f"strip_polyfill: no {SITE}, nothing to do")
        return 0
    touched = removed = 0
    for page in SITE.rglob("*.html"):
        html = page.read_text(errors="ignore")
        new, n = TAG.subn("", html)
        if n:
            page.write_text(new)
            touched += 1
            removed += n
    left = sum(1 for p in SITE.rglob("*.html")
               if "polyfill" in p.read_text(errors="ignore"))
    print(f"strip_polyfill: removed {removed} tag(s) from {touched} page(s)")
    if left:
        # Not a warning to be scrolled past: the point of the step is that no
        # page reaches a third party, and a survivor means the pattern missed.
        print(f"strip_polyfill: FAILED, {left} page(s) still mention polyfill")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
