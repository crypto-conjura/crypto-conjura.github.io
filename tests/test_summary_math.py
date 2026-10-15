"""Regression cases for source markup and rendered catalogue math."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from summary_math import (audit_site, check_statement_math, check_summary, parse_summary,
                          rendered_errors, rendered_title_errors)
from plain_search_titles import update_search_titles


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
                path.write_text('---\ntitle: Title\nstatus_summary: Open.\n---\n')
                page = site / 'c' / leaf / 'index.html'
                page.parent.mkdir(parents=True)
                page.write_text('<h1 class="title">Title</h1>')
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


    def test_title_source_validation_and_short_title_fallback(self):
        fm = {'title': 'Plain title', 'status_summary': 'Open.'}
        self.assertEqual(check_statement_math(fm), ([], []))
        for field in ('title', 'short_title'):
            for value in (None, '', 2, '$n', '$$n$$', '$n^{2$', 'Title\nline'):
                with self.subTest(field=field, value=value):
                    errors, _ = check_statement_math({**fm, field: value})
                    self.assertTrue(any(field in e for e in errors))
            errors, warnings = check_statement_math({**fm, field: 'AES 2^-128-close'})
            self.assertFalse(errors)
            self.assertTrue(any(field in w for w in warnings))
        for title, plain in (('AES $2^{-128}$-close', 'AES 2^(-128)-close'),
                             ('Tight $k$-collision tradeoff', 'Tight k-collision tradeoff')):
            self.assertEqual(check_statement_math({**fm, 'title': title, 'pagetitle': plain}), ([], []))
            self.assertTrue(check_statement_math({**fm, 'title': title})[0])
        for plain in (None, '', '$k$', r'\(k\)', r'\tau', '<b>k</b>', 'k\n'):
            self.assertTrue(check_statement_math({**fm, 'title': '$k$', 'pagetitle': plain})[0])

    def test_title_yaml_escape_corruption_is_rejected_by_index(self):
        from build_index import validate_leaf
        for field in ('title', 'short_title'):
            fm = yaml.safe_load(field + r': "Use $\tau$"')
            errors = []
            validate_leaf(fm, Path('c/0001/index.qmd'), errors)
            self.assertTrue(any(field in e and 'control character' in e for e in errors))

    def test_rendered_title_math_and_plain_metadata(self):
        html = r'''<title>AES 2^(-128)-close – AICR</title>
<meta property="og:title" content="AES 2^(-128)-close">
<meta name="twitter:title" content="AES 2^(-128)-close">
<script src="/assets/mathjax/tex-chtml-full.js"></script>
<h1 class="title">AES <span class="math inline">\(2^{-128}\)</span>-close</h1>'''
        def check(value):
            return rendered_title_errors(value, 'AES $2^{-128}$-close', 'AES 2^(-128)-close', 'AICR')
        self.assertEqual(check(html), [])
        for broken in (
            html.replace(r'\(2^{-128}\)', r'\(2^{-12}\)'),
            html.replace('math inline', 'plain'),
            html.replace('<script src="/assets/mathjax/tex-chtml-full.js"></script>', ''),
            html.replace('<h1 class="title">', '<h1 class="other">'),
            html + '<h1 class="title">Another</h1>',
            html.replace('content="AES 2^(-128)-close"', r'content="AES \(2^{-128}\)-close"'),
            html.replace(' – AICR</title>', r' \(k\)</title>'),
            html.replace('<meta name="twitter:title" content="AES 2^(-128)-close">', ''),
        ):
            with self.subTest(broken=broken):
                self.assertTrue(check(broken))
        # Formulae in body content must not substitute for lost title math.
        broken = html.replace('math inline', 'plain') + r'<p><span class="math inline">\(2^{-128}\)</span></p>'
        self.assertTrue(check(broken))
        self.assertTrue(rendered_title_errors(html, 'Plain title'))
        self.assertEqual(rendered_title_errors('<h1 class="title">Plain</h1>', 'Plain'), [])

    def test_listing_title_math_is_separate_from_summary_and_other_links(self):
        html = r'''<script src="/assets/mathjax/tex-chtml-full.js"></script>
<table class="cj-statement-table"><tr><td class="listing-title">
<a href="/c/0003/">Tight <span class="math inline">\(k\)</span>-collisions</a>
<span class="cj-status-summary">Open <a href="/c/0002/"><span class="math inline">\(n\)</span></a></span>
</td><td><a href="/c/0002/"><span class="math inline">\(m\)</span></a></td></tr></table>'''
        def check(value, title='Tight $k$-collisions'):
            return rendered_errors(value, {'0003': 'Open $n$'}, ['0003'], {'0003': title})
        self.assertEqual(check(html), ([], 1))
        for broken in (html.replace(r'\(k\)', r'\(n\)'),
                       html.replace('<span class="math inline">\\(k\\)</span>', 'k'),
                       html.replace('<script src="/assets/mathjax/tex-chtml-full.js"></script>', '')):
            self.assertTrue(check(broken)[0])
        self.assertTrue(check(html, 'Plain title')[0])
        # A title alone, even with a plain summary, still needs MathJax.
        title_only = '<table class="cj-statement-table"><tr><td class="listing-title"><a href="/c/0003/"><span class="math inline">\\(k\\)</span></a><span class="cj-status-summary">Open.</span></td></tr></table>'
        self.assertTrue(any('no MathJax' in e for e in rendered_errors(title_only, {'0003': 'Open.'}, ['0003'], {'0003': '$k$'})[0]))

    def test_site_title_fallback_metadata_and_search_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site = root / '_site'
            source = root / 'c/0001/index.qmd'
            source.parent.mkdir(parents=True)
            fm = {'title': 'Tight $k$-collisions', 'pagetitle': 'Tight k-collisions', 'status_summary': 'Open.'}
            source.write_text('---\n' + yaml.safe_dump(fm) + '---\n')
            listing = root / 'problems/all/index.qmd'
            listing.parent.mkdir(parents=True)
            listing.write_text('---\nlisting:\n  template: ../../_listing-templates/statement-table.ejs.md\n  contents: ../../_generated/all.yml\n---\n')
            index = root / '_generated/all.yml'
            index.parent.mkdir()
            index.write_text('- id: "0001"\n')
            page = site / 'c/0001/index.html'
            page.parent.mkdir(parents=True)
            header = '<script src="/mathjax/tex.js"></script><h1 class="title">Tight <span class="math inline">\\(k\\)</span>-collisions</h1><title>Tight k-collisions</title><meta property="og:title" content="Tight k-collisions"><meta name="twitter:title" content="Tight k-collisions">'
            page.write_text(header)
            output = site / 'problems/all/index.html'
            output.parent.mkdir(parents=True)
            output.write_text('<script src="/mathjax/tex.js"></script><table class="cj-statement-table"><tr><td class="listing-title"><a href="/c/0001/">Tight <span class="math inline">\\(k\\)</span>-collisions</a><span class="cj-status-summary">Open.</span></td></tr></table>')
            entries = [{'href': 'c/0001/index.html' + suffix, 'title': r'Tight \\(k\\)-collisions', 'text': 'Unchanged body', 'section': suffix} for suffix in ('', '#proof')]
            entries.append({'href': 'unrelated.html', 'title': 'Unrelated'})
            search = site / 'search.json'
            search.write_text(json.dumps(entries))
            self.assertTrue(any('search title differs' in e for e in audit_site(root, site)[0]))
            self.assertEqual(update_search_titles(root, site), 2)
            self.assertEqual(update_search_titles(root, site), 0)
            fixed = json.loads(search.read_text())
            self.assertEqual(fixed[-1], entries[-1])
            self.assertEqual(fixed[0]['text'], entries[0]['text'])
            self.assertEqual(fixed[1]['section'], entries[1]['section'])
            self.assertEqual(audit_site(root, site), ([], [], 1, 1))
            # An explicit short title changes which formula the listing must carry.
            fm['short_title'] = 'Plain short title'
            source.write_text('---\n' + yaml.safe_dump(fm) + '---\n')
            self.assertTrue(any('listing title' in e for e in audit_site(root, site)[0]))
            del fm['short_title']
            source.write_text('---\n' + yaml.safe_dump(fm) + '---\n')
            page.unlink()
            self.assertTrue(any('statement page missing' in e for e in audit_site(root, site)[0]))
            page.write_text('<h1 class="title">Math was lost</h1>')
            self.assertTrue(any('title: rendered math differs' in e for e in audit_site(root, site)[0]))
            page.write_text(header)
            search.write_text('[]')
            self.assertTrue(any('no search entry' in e for e in audit_site(root, site)[0]))
            search.unlink()
            self.assertTrue(any('search index missing' in e for e in audit_site(root, site)[0]))



if __name__ == '__main__':
    unittest.main()
