"""Regression cases for source markup and rendered catalogue math."""
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from summary_math import audit_site, check_summary, parse_summary, rendered_errors


class SummaryMathTests(unittest.TestCase):
    def test_folded_yaml_and_generated_index_preserve_tex(self):
        source = r'''status_summary: >-
  Use $O(\tau)$, $(S^2T^4/C^2)^S$,
  $2^{n^{0.01}}$ and $\tilde{O}(n^{1/2})$.
'''
        summary = yaml.safe_load(source)['status_summary']
        self.assertEqual(check_summary(summary), ([], []))
        exported = yaml.safe_load(yaml.safe_dump({'status_summary': summary}))
        self.assertEqual(exported['status_summary'], summary)
        self.assertEqual(parse_summary(summary)[0], [
            r'O(\tau)', r'(S^2T^4/C^2)^S', r'2^{n^{0.01}}', r'\tilde{O}(n^{1/2})'])

    def test_bad_delimiters_and_braces_fail(self):
        for text in ('$n^2', '$$n^2$$', '$ n^2$', '$n^2 $', '$n^{2$', '$n}^2{$', '$n$2'):
            with self.subTest(text=text):
                self.assertTrue(check_summary(text)[0])

    def test_missing_or_non_string_summary_fails(self):
        for text in (None, '', ' ', 12, []):
            with self.subTest(text=text):
                self.assertTrue(check_summary(text)[0])

    def test_yaml_escape_corruption_fails(self):
        # In a double-quoted YAML scalar, \t silently becomes a tab.
        text = yaml.safe_load(r'status_summary: "Use $O(\tau)$ bits."')['status_summary']
        self.assertTrue(check_summary(text)[0])

    def test_unmarked_notation_warns_without_failing(self):
        for text in ('O(tau)', 'S^2T^4/C^2', 'n_{i}', 'Theta(log n)', r'Use \lambda', 'n >= 2'):
            with self.subTest(text=text):
                errors, warnings = check_summary(text)
                self.assertFalse(errors)
                self.assertTrue(warnings)

    def test_prose_code_and_escaped_currency_are_allowed(self):
        text = r'An open conjecture, with `$n^2` shown as code and a \$5 fee.'
        self.assertEqual(check_summary(text), ([], []))
        self.assertEqual(parse_summary(text)[0], [])

    def test_escaped_braces_and_dollars_in_tex(self):
        text = r'Use $\{x\}$ and $\$5$.'
        self.assertEqual(check_summary(text), ([], []))

    def test_rendered_expressions_survive_template(self):
        summary = r'Use $O(\tau)$ and $2^{n^{0.01}}$.'
        html = r'''<script src="../../assets/mathjax/tex-chtml-full.js"></script>
<table class="cj-statement-table"><tbody><tr><td class="listing-title"><a href="../../c/0072/">Title</a><br>
<span class="cj-status-summary">Use <span class="math inline">\(O(\tau)\)</span>
and <span class="math inline">\(2^{n^{0.01}}\)</span>.
<span class="cj-open-count">4 open</span></span></td></tr></tbody></table>'''
        self.assertEqual(rendered_errors(html, {'0072': summary}), ([], 1))
        for broken in (
            html.replace(r'\(O(\tau)\)', r'\(O(tau)\)'),
            html.replace('math inline', 'plain'),
            html.replace('<script src="../../assets/mathjax/tex-chtml-full.js"></script>', ''),
            html.replace('c/0072/', 'c/9999/'),
        ):
            with self.subTest(html=broken):
                self.assertTrue(rendered_errors(broken, {'0072': summary})[0])

    def test_original_caret_corruption_is_detected(self):
        html = '''<table class="cj-statement-table"><tr><td class="listing-title"><a href="/c/0052/">Sponge</a>
<span class="cj-status-summary">S<sup>2T</sup>4/C^2</span></td></tr>'''
        self.assertTrue(rendered_errors(html, {'0052': '$S^2T^4/C^2$'})[0])

    def test_non_math_summary_and_entities(self):
        html = '''<table class="cj-statement-table"><tr><td class="listing-title"><a href="/c/0001/">Title</a>
<span class="cj-status-summary">Open &amp; unreviewed.</span></td></tr>'''
        self.assertEqual(rendered_errors(html, {'0001': 'Open & unreviewed.'}), ([], 1))

    def test_yaml_newline_escapes_fail_source_and_render_checks(self):
        from build_index import validate_leaf
        for command in (r'\neq', r'\nu'):
            with self.subTest(command=command):
                summary = yaml.safe_load('status_summary: "Use $x ' + command + ' y$."')['status_summary']
                self.assertIn('\n', summary)
                self.assertTrue(check_summary(summary)[0])
                errors = []
                validate_leaf({'status_summary': summary}, Path('c/0001/index.qmd'), errors)
                self.assertTrue(any('line break' in error for error in errors))
                expression = parse_summary(summary)[0][0]
                html = ('<table class="cj-statement-table"><tr><td class="listing-title">'
                        '<a href="/c/0001/">Title</a><span class="cj-status-summary">'
                        '<span class="math inline">\\(' + expression + '\\)</span></span></td></tr></table>')
                self.assertTrue(any('line break' in error for error in rendered_errors(html, {'0001': summary})[0]))

    def test_summary_cross_links_do_not_change_row_identity(self):
        html = r'''<script src="/assets/mathjax/tex-chtml-full.js"></script>
<table class="cj-statement-table"><tr><td class="listing-title">
<a href="/c/0001/">Title</a><span class="cj-status-summary">
See <a href="/c/0002/">another statement</a> for <span class="math inline">\(n\)</span>.
</span></td><td><a href="/c/0002/">Related</a></td></tr></table>'''
        self.assertEqual(rendered_errors(html, {'0001': 'See another statement for $n$.', '0002': '$m$'}, ['0001']), ([], 1))

    def test_missing_and_duplicate_summary_fail_even_without_math(self):
        template = ('<table class="cj-statement-table"><tr><td class="listing-title">'
                    '<a href="/c/0001/">Title</a>CONTENT</td></tr></table>')
        for content in ('', '<span class="cj-status-summary">Open.</span>' * 2):
            with self.subTest(content=content):
                errors, _ = rendered_errors(template.replace('CONTENT', content), {'0001': 'Open.'}, ['0001'])
                self.assertTrue(any('exactly one summary' in error for error in errors))

    def test_site_gate_rejects_missing_rows_summaries_and_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site = root / '_site'
            for leaf in ('0001', '0002'):
                path = root / 'c' / leaf / 'index.qmd'
                path.parent.mkdir(parents=True)
                path.write_text('---\nstatus_summary: Open.\n---\n')
            source = root / 'problems/all/index.qmd'
            source.parent.mkdir(parents=True)
            source.write_text('---\nlisting:\n  template: ../../_listing-templates/statement-table.ejs.md\n  contents: ../../_generated/all.yml\n---\n')
            index = root / '_generated/all.yml'
            index.parent.mkdir()
            items = [{'id': leaf} for leaf in ('0001', '0002')]
            index.write_text(yaml.safe_dump(items))
            output = site / 'problems/all/index.html'
            output.parent.mkdir(parents=True)
            rows = [f'<tr><td class="listing-title"><a href="/c/{leaf}/">Title</a>'
                    '<span class="cj-status-summary">Open.</span></td></tr>' for leaf in ('0001', '0002')]
            def write(rows):
                output.write_text('<table class="cj-statement-table">' + ''.join(rows) + '</table>')
            write(rows)
            self.assertEqual(audit_site(root, site), ([], [], 2, 1))
            # A whole span disappears while the statement row remains.
            write([rows[0], rows[1].replace('<span class="cj-status-summary">Open.</span>', '')])
            self.assertTrue(any('exactly one summary' in error for error in audit_site(root, site)[0]))
            # Removing the row, duplicating another row or dropping the entire
            # table must not turn partial coverage into a passing check.
            for broken in ([rows[0]], [rows[0], rows[0]], []):
                write(broken)
                self.assertTrue(any('membership' in error for error in audit_site(root, site)[0]))
            write(rows[:1])
            index.write_text(yaml.safe_dump(items[:1]))
            self.assertTrue(any('browsable source' in error for error in audit_site(root, site)[0]))
            index.write_text(yaml.safe_dump(items))
            output.unlink()
            self.assertTrue(any('rendered listing missing' in error for error in audit_site(root, site)[0]))
            index.unlink()
            self.assertTrue(any('generated listing index missing' in error for error in audit_site(root, site)[0]))



if __name__ == '__main__':
    unittest.main()
