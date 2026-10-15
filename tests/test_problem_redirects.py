"""Keep published Problems bookmarks working through full/partial rebuilds."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("problem_redirects", ROOT / "scripts/problem_redirects.py")
redirects = importlib.util.module_from_spec(spec)
spec.loader.exec_module(redirects)


class ProblemRedirectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.site = Path(self.temp.name).resolve()
        for path, text in {
            "problems/all/index.html": "<h1>Research problems</h1>",
            "reviews/status-badge/index.html": '<h2 id="status-legend">Status badge</h2>',
            "problems/latex-templates/index.html": "<h1>LaTeX templates</h1>",
        }.items():
            target = self.site / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        self.generated_aliases()

    def generated_aliases(self):
        for path, default in (("problems/index.html", "all/index.html"),
                              ("open-problems/index.html", "../problems/all/index.html")):
            page = self.site / path
            page.parent.mkdir(parents=True, exist_ok=True)
            # The redirect script produced by the pinned Quarto version.
            page.write_text('''<script>
    var redirects = MAP;
    var hash = window.location.hash.startsWith('#') ? window.location.hash.slice(1) : window.location.hash;
    var redirect = redirects[hash] || redirects[""] || "/";
    window.document.title = 'Redirect to  ' + redirect;
    if (!redirects[hash]) {
      redirect = redirect + window.location.hash;
    }
    redirect = redirect + window.location.search;
    window.location.replace(redirect);
    </script>'''.replace('MAP', json.dumps({"": default})))

    def test_unmapped_bookmarks_fail_before_repair(self):
        with self.assertRaisesRegex(ValueError, "incorrect"):
            redirects.update_redirects(self.site, check=True)

    def test_every_published_section_and_default_is_preserved(self):
        redirects.update_redirects(self.site)
        expected = {
            "": "problems/all/index.html",
            "browse": "problems/all/index.html",
            "the-status-badge": "reviews/status-badge/index.html#status-legend",
            "latex-templates": "problems/latex-templates/index.html",
        }
        for legacy in ("problems/index.html", "open-problems/index.html"):
            page = self.site / legacy
            mapping = json.loads(redirects.MAP.search(page.read_text())[1])
            for fragment, target in expected.items():
                with self.subTest(legacy=legacy, fragment=fragment):
                    actual = (page.parent / mapping[fragment]).resolve()
                    self.assertEqual(actual, self.site / target)
        redirects.update_redirects(self.site, check=True)

    def test_executed_redirect_preserves_queries_and_sections(self):
        node = shutil.which("node")
        self.assertIsNotNone(node, "Install Node.js 22 to run redirect execution tests")
        redirects.update_redirects(self.site)
        runner = """
const vm = require('node:vm');
const location = new URL(process.argv[2]);
location.replace = target => process.stdout.write(target);
vm.runInNewContext(process.argv[1], {URL, window: {location, document: {}}});
"""
        for legacy in ("problems/index.html", "open-problems/index.html"):
            script = (self.site / legacy).read_text().split("<script>")[1].split("</script>")[0]
            for query in ("", "?source=review&term=a%20b"):
                for fragment, target in {
                    "": "/problems/all/index.html",
                    "#browse": "/problems/all/index.html",
                    "#the-status-badge": "/reviews/status-badge/index.html#status-legend",
                    "#latex-templates": "/problems/latex-templates/index.html",
                    "#listing-all-statements-page=2": "/problems/all/index.html#listing-all-statements-page=2",
                }.items():
                    with self.subTest(legacy=legacy, query=query, fragment=fragment):
                        url = "https://aicr.info/" + legacy + query + fragment
                        actual = subprocess.check_output([node, "-e", runner, script, url], text=True)
                        path, separator, section = target.partition("#")
                        self.assertEqual(actual, "https://aicr.info" + path + query + separator + section)

    def test_check_rejects_regressed_query_handling(self):
        redirects.update_redirects(self.site)
        page = self.site / "problems/index.html"
        page.write_text(page.read_text().replace(redirects.QUERY_FIX, redirects.QUERY_LINE))
        with self.assertRaisesRegex(ValueError, "incorrect query/fragment handling"):
            redirects.update_redirects(self.site, check=True)

    def test_partial_render_replacing_aliases_is_repaired_again(self):
        redirects.update_redirects(self.site)
        self.generated_aliases()
        redirects.update_redirects(self.site)
        redirects.update_redirects(self.site, check=True)

    def test_partial_output_is_repaired_without_requiring_other_pages(self):
        (self.site / "problems/latex-templates/index.html").unlink()
        (self.site / "open-problems/index.html").unlink()
        self.assertEqual(redirects.update_redirects(self.site), 1)
        with self.assertRaisesRegex(ValueError, "missing redirect destination"):
            redirects.update_redirects(self.site, check=True)

    def test_render_without_any_aliases_is_a_noop_but_check_requires_them(self):
        for legacy in redirects.LEGACY_PAGES:
            (self.site / legacy).unlink()
        self.assertEqual(redirects.update_redirects(self.site), 0)
        with self.assertRaises(FileNotFoundError):
            redirects.update_redirects(self.site, check=True)

    def test_moved_or_deleted_destination_fails(self):
        redirects.update_redirects(self.site)
        legend = self.site / "reviews/status-badge/index.html"
        legend.write_text('<h2 id="renamed">Status badge</h2>')
        with self.assertRaisesRegex(ValueError, "missing redirect section"):
            redirects.update_redirects(self.site, check=True)
        legend.write_text('<h2 id="status-legend">Status badge</h2>')
        (self.site / "problems/latex-templates/index.html").unlink()
        with self.assertRaisesRegex(ValueError, "missing redirect destination"):
            redirects.update_redirects(self.site, check=True)

    def test_never_overwrites_a_content_page(self):
        page = self.site / "problems/index.html"
        page.write_text("<h1>Unexpected real page</h1>")
        with self.assertRaisesRegex(ValueError, "expected a Quarto alias page"):
            redirects.update_redirects(self.site)
        self.assertEqual(page.read_text(), "<h1>Unexpected real page</h1>")


if __name__ == "__main__":
    unittest.main()
