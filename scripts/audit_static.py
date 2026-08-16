#!/usr/bin/env python3
"""Layer-2 audit of the built site against CHECKS.md IDs. Findings are
hypotheses until confirmed in a browser (layer 3)."""
import collections, html, json, pathlib, re, sys, urllib.parse

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
SITE_URL = "https://crypto-conjura.github.io"
pages = sorted(ROOT.rglob("*.html"))
text = {}
for p in pages:
    try:
        text[p] = p.read_text(errors="ignore")
    except Exception:
        pass

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

# id set per page, for fragment resolution
ids = {}
for p, h in text.items():
    ids[p] = set(re.findall(r'\bid="([^"]+)"', h)) | set(re.findall(r"\bid='([^']+)'", h))

# ---------------------------------------------------------------- LNK ----
def resolve(src, href):
    """Return (path, frag) inside ROOT, or None if external/unresolvable."""
    if href.startswith(("http://", "https://", "mailto:", "data:", "javascript:", "#")):
        return None
    u = urllib.parse.urlparse(href)
    if u.scheme or u.netloc:
        return None
    target = u.path
    if not target:
        return (src, u.fragment)
    base = ROOT if target.startswith("/") else src.parent
    q = (base / target.lstrip("/")).resolve()
    if q.is_dir():
        q = q / "index.html"
    return (q, u.fragment)

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

        r = resolve(p, href)
        if r is None:
            continue
        q, frag = r
        if not q.exists():
            add("LNK-01", f"{rel(p)}: -> {href} (no such file)")
            continue
        if frag:
            fr = urllib.parse.unquote(frag)
            if q in ids and fr not in ids[q] and frag not in ids[q]:
                add("LNK-02", f"{rel(p)}: -> {href} (no such anchor)")

        if label.lower() in ("here", "this", "link", "click here", "read more"):
            add("A11Y-08", f"{rel(p)}: non-descriptive link text {label!r}")

# non-HTML assets referenced (LNK-10)
for p, h in text.items():
    for href in re.findall(r'href="([^"]+\.(?:pdf|lean|tex|json|bib))"', h):
        r = resolve(p, html.unescape(href))
        if r and not r[0].exists():
            add("LNK-10", f"{rel(p)}: missing asset {href}")

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
for p, h in text.items():
    for href in re.findall(r'href="([^"]+)"', h):
        r = resolve(p, html.unescape(href))
        if r and r[0].exists() and r[0].suffix == ".html":
            linked.add(r[0])
pages_resolved = {p.resolve(): p for p in pages}
for rp, p in pages_resolved.items():
    if rp not in linked and rel(p) not in ("index.html",):
        add("CNT-04", f"orphan: {rel(p)}")

print(json.dumps({k: v for k, v in sorted(F.items())}, indent=1)[:200])
summary = sorted(((len(v), k) for k, v in F.items()), reverse=True)
print("\n=== layer-2 findings by check id ===")
for n, k in summary:
    print(f"  {k:9} {n:5}   e.g. {F[k][0][:96]}")
pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "/tmp/audit.json").write_text(
    json.dumps({k: v for k, v in sorted(F.items())}, indent=1))
print(f"\npages audited: {len(pages)}; external urls seen: {len(ext_urls)}")
