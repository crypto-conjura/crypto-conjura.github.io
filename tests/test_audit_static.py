"""Black-box tests for the rendered-site link gate, using tiny HTML fixtures."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_static.py"

# The alias stub emitted by the pinned Quarto version. The map varies by page.
QUARTO_REDIRECT = '''<html><head><title>Redirect</title>
<script type="text/javascript">
    var redirects = MAP;
    var hash = window.location.hash.startsWith('#') ? window.location.hash.slice(1) : window.location.hash;
    var redirect = redirects[hash] || redirects[""] || "/";
    window.document.title = 'Redirect to  ' +  redirect;
    if (!redirects[hash]) {
      redirect = redirect + window.location.hash;
    }
    redirect = redirect + window.location.search;
    window.location.replace(redirect);
</script></head><body></body></html>'''


class LinkAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.site = self.root / "_site"
        self.site.mkdir()
        self.report = self.root / "report.json"

    def write(self, path, body):
        target = self.site / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")

    def redirect(self, path, mapping):
        self.write(path, QUARTO_REDIRECT.replace("MAP", json.dumps(mapping)))

    def run_audit(self, absolute=False, gate=True, default_root=False):
        args = [sys.executable, str(SCRIPT)]
        if not default_root:
            args += [str(self.site) if absolute else "_site", str(self.report)]
        if gate:
            args += ["--check-links"]
        result = subprocess.run(args, cwd=self.root, capture_output=True, text=True)
        findings = json.loads(self.report.read_text()) if self.report.exists() else {}
        return result, findings

    def test_missing_same_page_and_cross_page_fragments(self):
        self.write("index.html", '<a href="#missing">Same page</a>'
                   '<a href="other.html#missing">Other page</a>')
        self.write("other.html", '<h1 id="present">Present</h1>')
        for absolute in (False, True):
            with self.subTest(absolute=absolute):
                result, findings = self.run_audit(absolute=absolute)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertEqual(len(findings.get("LNK-02", [])), 2)
                self.assertIn("index.html: -> #missing", result.stderr)
                self.assertIn("other.html#missing", result.stderr)

    def test_valid_fragment_forms_and_encoded_paths(self):
        self.write("index.html", '''
            <h1 id="a&amp;b">Section</h1><a name='legacy'></a>
            <a href='#a%26b'>Encoded ID</a><a href="#legacy">Named anchor</a>
            <a href="#top">Top</a><a href="#TOP">Top</a>
            <a href=other.html#target>Unquoted</a>
            <a href="other.html?view=1&amp;sort=2#target">Query</a>
            <a href="/dir/../other.html#target">Root and dot segments</a>
            <a href="space%20name.html#caf%C3%A9">Encoded filename and ID</a>
            <a href="#a%26b:~:text=Section">Text fragment with anchor</a>
            <a href="#:~:text=Section">Text fragment only</a>
            <a href="paper.pdf#page=3">PDF fragment</a>
            <a href="https://aicr.info/other.html#target">Absolute self-link</a>
            <a href="//aicr.info/other.html#target">Protocol-relative self-link</a>
        ''')
        self.write("other.html", '<h1 id=target>Target</h1>')
        self.write("space name.html", '<h1 id="café">Target</h1>')
        self.write("paper.pdf", "fixture")
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(findings.get("LNK-01"))
        self.assertFalse(findings.get("LNK-02"))

    def test_missing_files_and_directory_index(self):
        self.write("index.html", '<a href="missing.html">Missing page</a>'
                   "<a href='missing.lean'>Missing source</a>"
                   '<a href="empty/">Directory without an index</a>')
        (self.site / "empty").mkdir()
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(findings.get("LNK-01", [])), 3)
        self.assertEqual(len(findings.get("LNK-10", [])), 1)

    def test_site_absolute_urls_are_checked_but_external_urls_are_not(self):
        self.write("index.html", '''
            <a href="https://aicr.info/target.html#missing">Missing anchor</a>
            <a href="//aicr.info/missing.html">Missing page</a>
            <a href="https://example.invalid/missing#missing">External</a>
            <a href="mailto:person@example.invalid">Mail</a>
            <a href="javascript:void(0)">Control</a>
            <a href="data:text/plain,hello">Data</a>
            <a href="#">Control</a><a href="">Control</a>
            <script>const sample = '<a href="fake.html">Example</a>';</script>
            <!-- <a href="comment.html">Comment</a> -->
        ''')
        self.write("target.html", '<h1 id="present">Present</h1>')
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(findings.get("LNK-01", [])), 1)
        self.assertEqual(len(findings.get("LNK-02", [])), 1)

    def test_directory_links_and_parent_paths(self):
        self.write("index.html", '<h1 id="home">Home</h1><a href="nested/">Nested</a>')
        self.write("nested/index.html", '<a href="../#home">Home</a>')
        result, _ = self.run_audit()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_quarto_redirect_preserves_and_remaps_fragments(self):
        self.write("index.html", '<a href="/old/#difficulty-legend">Old URL</a>'
                   '<a href="/old/#renamed">Renamed section</a>')
        self.redirect("old/index.html", {"": "../middle/index.html",
                                       "renamed": "../current/index.html#new"})
        self.redirect("middle/index.html", {"": "../current/index.html"})
        self.write("current/index.html", '<h1 id="difficulty-legend">Difficulty</h1>'
                   '<h2 id="new">New</h2>')
        result, _ = self.run_audit()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_redirect_does_not_hide_missing_target_or_section(self):
        self.write("index.html", '<a href="/old/#missing">Missing section</a>'
                   '<a href="/gone/">Missing page</a>')
        self.redirect("old/index.html", {"": "../current/index.html"})
        self.redirect("gone/index.html", {"": "../missing.html"})
        self.write("current/index.html", "<h1>Current</h1>")
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(findings.get("LNK-01", [])), 1)
        self.assertEqual(len(findings.get("LNK-02", [])), 1)

    def test_redirect_cycles_and_excessive_chains_fail(self):
        self.write("index.html", '<a href="a.html">Cycle</a><a href="hop0.html">Long chain</a>')
        self.redirect("a.html", {"": "b.html"})
        self.redirect("b.html", {"": "a.html"})
        for i in range(21):
            self.redirect(f"hop{i}.html", {"": f"hop{i+1}.html"})
        self.write("hop21.html", "<h1>End</h1>")
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(findings.get("LNK-01", [])), 2)
        self.assertIn("redirect cycle", result.stderr)
        self.assertIn("redirect limit exceeded", result.stderr)

    def test_default_ports_and_case_do_not_bypass_internal_checking(self):
        self.write("index.html", '''
            <a href="https://AICR.info/missing.html">Case</a>
            <a href="https://aicr.info:443/missing.html">Default HTTPS port</a>
            <a href="http://AICR.info:80/missing.html">Default HTTP port</a>
            <a href="https://AICR.info:443/index.html#present">Valid</a>
            <a href="https://aicr.info:8443/missing.html">Other service</a>
            <h1 id="present">Present</h1>
        ''')
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(findings.get("LNK-01", [])), 3)

    def test_encoded_dot_segments_cannot_escape_the_url_root(self):
        self.write("index.html", '''
            <a href="%2e%2e/index.html#home">Parent of root</a>
            <a href="a/%2E%2e/../index.html#home">Mixed dots</a>
            <a href="a/.%2E/index.html#home">Mixed dot encoding</a>
            <a href="https://aicr.info/a/%2e./index.html#home">Absolute URL</a>
            <a href="a/%2e%2e/#home">Directory target</a>
            <h1 id="home">Home</h1>
        ''')
        result, _ = self.run_audit()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_trailing_slash_cannot_turn_a_file_into_a_directory(self):
        self.write("index.html", '<a href="paper.pdf/">Wrong</a>'
                   '<a href="paper.pdf/%2e">Also wrong</a>'
                   '<a href="paper.pdf#page=1">Valid</a>')
        self.write("paper.pdf", "fixture")
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(findings.get("LNK-01", [])), 2)

    def test_named_anchor_is_a_fragment_target_but_not_an_aria_id(self):
        self.write("index.html", '''
            <a name="legacy"></a><a href="#legacy">Valid fragment</a>
            <div aria-labelledby="legacy">Invalid label reference</div>
            <h1 id="real-id">Real label</h1>
            <div aria-labelledby="real-id">Valid label reference</div>
        ''')
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(findings.get("LNK-02"))
        self.assertEqual(len(findings.get("A11Y-11", [])), 1)
        self.assertIn("'legacy'", findings["A11Y-11"][0])

    def test_missing_or_empty_render_fails(self):
        for exists in (True, False):
            with self.subTest(exists=exists):
                if not exists:
                    self.site.rmdir()
                result, _ = self.run_audit()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("no HTML pages found", result.stderr)

    def test_default_invocation_fails_for_broken_links(self):
        self.write("index.html", '<a href="#missing">Broken</a>')
        # No positional arguments: exactly the command used in CI.
        result, _ = self.run_audit(default_root=True)
        self.assertEqual(result.returncode, 1, result.stderr)

    def test_invalid_html_encoding_cannot_silently_reduce_coverage(self):
        (self.site / "index.html").write_bytes(b"\xff")
        result, _ = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot read", result.stderr)

    def test_same_page_links_do_not_hide_orphans(self):
        self.write("index.html", "<h1>Home</h1>")
        self.write("orphan.html", '<h1 id="section">Section</h1>'
                   '<a href="#section">Self-link</a>')
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("orphan: orphan.html", findings.get("CNT-04", []))

    def test_advisory_findings_do_not_fail_the_link_gate(self):
        self.write("index.html", '<html><body>No title, metadata or heading.</body></html>')
        result, findings = self.run_audit()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(findings.get("MET-01"))

    def test_report_only_mode_preserves_non_failing_behavior(self):
        self.write("index.html", '<a href="#missing">Broken</a>')
        result, findings = self.run_audit(gate=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(findings.get("LNK-02", [])), 1)


if __name__ == "__main__":
    unittest.main()
