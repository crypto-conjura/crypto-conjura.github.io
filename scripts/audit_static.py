#!/usr/bin/env python3
"""Audit rendered HTML. Use --check-links to fail on broken internal links.

Other findings remain advisory and need browser confirmation.
Usage: python3 scripts/audit_static.py [_site] [report.json] [--check-links]
"""
import argparse, collections, html, json, pathlib, re, sys, urllib.parse
from html.parser import HTMLParser

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("site", nargs="?", default="_site")
parser.add_argument("report", nargs="?", default="/tmp/audit.json")
parser.add_argument("--check-links", action="store_true")
args = parser.parse_args()
# Link targets and the ID index must use the same absolute path convention.
ROOT = pathlib.Path(args.site).resolve()
SITE_URL = "https://aicr.info"
pages = sorted(ROOT.rglob("*.html"))
if not pages:
    parser.error(f"no HTML pages found in {ROOT}; render the site first")
text = {}
for p in pages:
    try:
        text[p] = p.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        parser.error(f"cannot read {p}: {exc}")

F = collections.defaultdict(list)          # id -> [detail, ...]
def add(cid, detail):
    F[cid].append(detail)

def rel(p):
    return str(p.relative_to(ROOT))

TAG = re.compile(r"<(\w+)([^>]*)>", re.S)
def attrs(s):
    d = dict(re.findall(r'(\w[\w:-]*)\s*=\s*"([^"]*)"', s))
    d.update(re.findall(r"(\w[\w:-]*)\s*=\s*'([^']*)'", s))
    return d

# Parse navigation with the HTML parser so quoting, character references,
# legacy named anchors and anchor-like text inside scripts are handled correctly.
class Navigation(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.named_anchors = set()
        self.links = []
        self.scripts = []
        self.script = None

    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if tag == "script":
            self.script = []
        if a.get("id") is not None:
            self.ids.add(a["id"])
        if tag == "a":
            if a.get("name") is not None:
                self.named_anchors.add(a["name"])
            if a.get("href") is not None:
                self.links.append(a["href"])

    handle_startendtag = handle_starttag

    def handle_data(self, data):
        if self.script is not None:
            self.script.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.script is not None:
            self.scripts.append("".join(self.script))
            self.script = None


def quarto_redirect(scripts):
    """Read the JSON map in Quarto's known alias stub; never execute scripts."""
    for script in scripts:
        if ('window.location.replace(redirect);' not in script or
                'redirects[hash] || redirects[""] || "/"' not in script):
            continue
        match = re.search(r'var redirects = (\{[^\n]*\});', script)
        if match:
            try:
                mapping = json.loads(match[1])
            except ValueError:
                continue
            if isinstance(mapping, dict) and all(isinstance(v, str) for v in mapping.values()):
                return mapping
    return None

ids = {}
fragment_targets = {}
links = {}
redirects = {}
for p, h in text.items():
    navigation = Navigation()
    navigation.feed(h)
    ids[p] = navigation.ids
    fragment_targets[p] = navigation.ids | navigation.named_anchors
    links[p] = navigation.links
    redirect = quarto_redirect(navigation.scripts)
    if redirect is not None:
        redirects[p] = redirect

# ---------------------------------------------------------------- LNK ----
def decode_dot_segments(path):
    segments = []
    for segment in path.split("/"):
        dots = re.sub("%2e", ".", segment, flags=re.I)
        segments.append(dots if dots in (".", "..") else segment)
    return "/".join(segments)


def normalize_url_path(path):
    """Remove literal/percent-encoded dot segments, retaining a final slash."""
    segments = decode_dot_segments(path).split("/")[1:]
    normalized = []
    for i, segment in enumerate(segments):
        if segment in (".", ".."):
            if segment == ".." and normalized:
                normalized.pop()
            if i == len(segments) - 1:
                normalized.append("")
        else:
            normalized.append(segment)
    return "/" + "/".join(normalized)


def resolve(src, href):
    """Return (path, frag) inside ROOT, or None if external/unresolvable."""
    # Resolve ordinary relative/root-relative URLs, then handle encoded dot
    # segments before percent-decoding into filesystem paths.
    base = SITE_URL + "/" + urllib.parse.quote(src.relative_to(ROOT).as_posix())
    reference = urllib.parse.urlsplit(href)
    # Decode dot segments before urljoin processes literal '..', so mixed
    # paths such as a/%2e%2e/../index.html are shortened in the right order.
    reference = reference._replace(path=decode_dot_segments(reference.path))
    u = urllib.parse.urlsplit(urllib.parse.urljoin(base, urllib.parse.urlunsplit(reference)))
    default_port = {"http": 80, "https": 443}.get(u.scheme)
    if (default_port is None or u.hostname != urllib.parse.urlsplit(SITE_URL).hostname
            or u.port not in (None, default_port)):
        return None
    path = normalize_url_path(u.path)
    q = (ROOT / urllib.parse.unquote(path).lstrip("/")).resolve()
    # A slash denotes a directory even if the slash-free path is a file.
    if path.endswith("/") or q.is_dir():
        q = q / "index.html"
    return (q, u.fragment)


def resolve_navigation(src, href):
    """Follow at most 20 recognized Quarto redirects, preserving their hashes."""
    target = resolve(src, href)
    seen = set()
    for hops in range(21):
        if target is None or target[0] not in redirects:
            return target
        if target in seen:
            raise ValueError("redirect cycle")
        if hops == 20:
            raise ValueError("redirect limit exceeded (20 hops)")
        seen.add(target)
        page, fragment = target
        mapping = redirects[page]
        destination = mapping.get(fragment) or mapping.get("") or "/"
        # Quarto replaces explicitly mapped hashes, and carries other hashes
        # onto the default destination. Queries do not affect static targets.
        if not mapping.get(fragment) and fragment:
            destination += "#" + fragment
        target = resolve(page, destination)


# These are the deterministic checks used by CI. Fragments on PDFs and other
# non-HTML assets have their own semantics, so only check their file exists.
for p, hrefs in links.items():
    for href in hrefs:
        if href in ("", "#"):
            continue  # Quarto UI controls, reported separately as advisory.
        try:
            r = resolve_navigation(p, href)
        except ValueError as exc:
            add("LNK-01", f"{rel(p)}: -> {href} ({exc})")
            continue
        if r is None:
            continue
        q, frag = r
        if not q.is_relative_to(ROOT) or not q.is_file():
            add("LNK-01", f"{rel(p)}: -> {href} (no such file)")
            if q.suffix in (".pdf", ".lean", ".tex", ".json", ".bib"):
                add("LNK-10", f"{rel(p)}: missing asset {href}")
            continue
        fr = urllib.parse.unquote(frag.split(":~:", 1)[0])
        if fr and fr.lower() != "top" and q in fragment_targets and fr not in fragment_targets[q]:
            add("LNK-02", f"{rel(p)}: -> {href} (no such anchor)")

ext_urls = collections.Counter()
for p, h in text.items():
    for m in re.finditer(r'<a\b([^>]*?)>(.*?)</a>', h, re.S):
        a = attrs(m.group(1))
        href = html.unescape(a.get("href", ""))
        label = re.sub(r"<[^>]+>", " ", m.group(2))
        label = " ".join(html.unescape(label).split())

        if href.startswith(("http://", "https://")):
            ext_urls[href] += 1
            host = urllib.parse.urlparse(href).netloc
            if href.startswith(f"{SITE_URL}"):
                add("LNK-05", f"{rel(p)}: absolute self-link {href}")
            if href.startswith("http://"):
                add("LNK-07", f"{rel(p)}: http:// link {href}")
            if a.get("target") == "_blank" and "noopener" not in a.get("rel", ""):
                add("SEC-01", f"{rel(p)}: target=_blank without rel=noopener -> {href}")
            continue

        if href in ("", "#"):
            if "quarto" not in a.get("class", ""):
                add("LNK-09", f"{rel(p)}: empty/# href, text={label[:40]!r}")
            continue

        if label.lower() in ("here", "this", "link", "click here", "read more"):
            add("A11Y-08", f"{rel(p)}: non-descriptive link text {label!r}")

# ---------------------------------------------------------------- SEM ----
for p, h in text.items():
    allids = re.findall(r'\bid="([^"]+)"', h)
    dup = [k for k, v in collections.Counter(allids).items() if v > 1]
    for d in dup:
        add("SEM-01", f"{rel(p)}: duplicate id {d!r}")

    heads = [(int(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2)).strip()[:40])
             for m in re.finditer(r"<h([1-6])\b[^>]*>(.*?)</h\1>", h, re.S)]
    h1 = [t for lvl, t in heads if lvl == 1]
    if len(h1) == 0:
        add("SEM-03", f"{rel(p)}: no <h1>")
    elif len(h1) > 1:
        add("SEM-03", f"{rel(p)}: {len(h1)} <h1> elements")
    prev = None
    for lvl, t in heads:
        if prev is not None and lvl > prev + 1:
            add("SEM-02", f"{rel(p)}: h{prev} -> h{lvl} at {t!r}")
        prev = lvl

    if not re.search(r"<html[^>]*\blang=", h):
        add("SEM-07", f"{rel(p)}: <html> without lang")
    if not re.search(r'<meta[^>]*charset', h, re.I):
        add("SEM-08", f"{rel(p)}: no meta charset")

    for m in re.finditer(r"<table\b(.*?)</table>", h, re.S):
        if "<th" not in m.group(1):
            add("SEM-06", f"{rel(p)}: table without <th>")
            break

# ---------------------------------------------------------------- MET ----
titles = collections.Counter()
descs = collections.Counter()
for p, h in text.items():
    m = re.search(r"<title>(.*?)</title>", h, re.S)
    t = html.unescape(re.sub(r"\s+", " ", m.group(1)).strip()) if m else ""
    if not t:
        add("MET-01", f"{rel(p)}: empty or missing <title>")
    else:
        titles[t] += 1
    d = re.search(r'<meta name="description" content="([^"]*)"', h)
    if not d or not d.group(1).strip():
        add("MET-02", f"{rel(p)}: no meta description")
    else:
        descs[d.group(1).strip()] += 1
    if not re.search(r'<link[^>]*rel="canonical"', h):
        add("MET-03", f"{rel(p)}: no canonical link")
    if not re.search(r'<meta property="og:title"', h):
        add("MET-04", f"{rel(p)}: no og:title")
    if not re.search(r'<meta property="og:image"', h):
        add("MET-05", f"{rel(p)}: no og:image")
    if re.search(r'<meta[^>]*name="robots"[^>]*noindex', h, re.I):
        add("MET-08", f"{rel(p)}: noindex present")
    # raw TeX leaking into metadata (MTH-07)
    for mm in re.finditer(r'<meta (?:name|property)="(og:[a-z]+|description|twitter:[a-z]+)" content="([^"]*)"', h):
        if re.search(r"\\[a-zA-Z]{2,}|\$\$|\\\(", html.unescape(mm.group(2))):
            add("MTH-07", f"{rel(p)}: raw TeX in {mm.group(1)}: {mm.group(2)[:60]!r}")

for t, n in titles.items():
    if n > 1:
        add("MET-01", f"duplicate <title> on {n} pages: {t!r}")
for d, n in descs.items():
    if n > 3:
        add("MET-02", f"same description reused on {n} pages: {d[:60]!r}")

# ---------------------------------------------------------------- A11Y ---
for p, h in text.items():
    for m in re.finditer(r"<img\b([^>]*)>", h):
        a = attrs(m.group(1))
        if "alt" not in a:
            add("A11Y-01", f"{rel(p)}: <img> without alt: {a.get('src','?')[:60]}")
    for m in re.finditer(r"<button\b([^>]*)>(.*?)</button>", h, re.S):
        a = attrs(m.group(1))
        inner = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if not inner and not a.get("aria-label") and not a.get("title") and not a.get("aria-labelledby"):
            add("A11Y-04", f"{rel(p)}: button with no accessible name: {m.group(1)[:60]}")
    for m in re.finditer(r'aria-labelledby="([^"]+)"', h):
        for ref in m.group(1).split():
            if ref not in ids[p]:
                add("A11Y-11", f"{rel(p)}: aria-labelledby -> missing id {ref!r}")

# ---------------------------------------------------------------- SEC ----
for p, h in text.items():
    for m in re.finditer(r'src="(http://[^"]+)"', h):
        add("SEC-02", f"{rel(p)}: mixed-content subresource {m.group(1)[:70]}")
    for m in re.finditer(r'<script[^>]*src="(https://[^"]+)"([^>]*)>', h):
        if "integrity=" not in m.group(2):
            add("SEC-04", f"{rel(p)}: CDN script without SRI: {m.group(1)[:70]}")

# ---------------------------------------------------------------- REF ----
for p, h in text.items():
    body = re.sub(r"<script.*?</script>", "", h, flags=re.S)
    for pat, cid in ((r"\?@[\w:-]+", "REF-01"), (r"\[@[\w:-]+\]", "REF-02")):
        for m in re.finditer(pat, body):
            add(cid, f"{rel(p)}: {m.group(0)}")

# ---------------------------------------------------------------- CNT ----
# CNT-04 orphan pages: reachable by URL but not linked from anywhere
linked = set()
for p, hrefs in links.items():
    for href in hrefs:
        r = resolve(p, href)
        if r and r[0] != p and r[0].exists() and r[0].suffix == ".html":
            linked.add(r[0])
pages_resolved = {p.resolve(): p for p in pages}
for rp, p in pages_resolved.items():
    if rp not in linked and rel(p) not in ("index.html",):
        add("CNT-04", f"orphan: {rel(p)}")

if not args.check_links:
    summary = sorted(((len(v), k) for k, v in F.items()), reverse=True)
    print("=== layer-2 findings by check id ===")
    for n, k in summary:
        print(f"  {k:9} {n:5}   e.g. {F[k][0][:96]}")
pathlib.Path(args.report).write_text(
    json.dumps({k: v for k, v in sorted(F.items())}, indent=1), encoding="utf-8")
print(f"\npages audited: {len(pages)}; external urls seen: {len(ext_urls)}")
print(f"full audit report: {args.report}")
if args.check_links:
    # LNK-10 is a subset of LNK-01; count each missing target only once.
    failures = [finding for code in ("LNK-01", "LNK-02") for finding in F[code]]
    for finding in failures:
        print(f"FAIL {finding}", file=sys.stderr)
    print(f"internal link check: {len(failures)} failure(s)")
    sys.exit(bool(failures))
