<% /* A facet with nothing in it yet would otherwise render as a bare header
      row. Quarto does emit its own `.listing-no-matching` div on every table
      listing, but only un-hides it from List.js's `updated` event, and that
      never fires on these pages: they carry `sort-ui: false` and get no
      filter box, so nothing ever updates the list. The message is therefore
      always present and always hidden. Say it here instead.

      Two notes for editors. The engine is lodash templates, not full EJS, so
      a hash-style template comment is a syntax error (it parses as a
      JavaScript `#`); write a JavaScript block comment inside a code tag,
      like this one. And a comment may not itself contain a closing tag
      delimiter: the scanner stops at the first one it sees. */ %>
<% if (items.length === 0) { %>
<p class="cj-listing-empty">Nobody has stated one yet. An empty facet is a research prompt, not an error: see <a href="/open-problems/all/index.qmd">all statements</a> for what is on the site so far.</p>
<% } else { %>
<table class="table cj-statement-table list">
<thead>
<tr>
<th class="sortable" data-sort="listing-badge_sigma">Status</th>
<th class="sortable" data-sort="listing-title">Statement</th>
<th class="sortable" data-sort="listing-category">Tags</th>
</tr>
</thead>
<tbody>
<% for (const item of items) { %>
<tr <%= metadataAttrs(item) %>>
<td class="listing-badge_sigma"><a href="<%= item.badge_legend_url %>" class="cj-status-link" aria-label="<%= item.badge_caption %> Click for the status badge legend."><svg class="cj-status-badge" viewBox="0 0 32 32" width="28" height="28" xmlns="http://www.w3.org/2000/svg" role="img"><% if (item.badge_sealed) { %><circle cx="16" cy="16" r="15" fill="none" stroke-width="1.5" class="cj-seal"/><% } %><circle cx="16" cy="16" r="13" fill="none" stroke-width="4" class="cj-ring-<%= item.badge_sigma %>"<% if (item.badge_dash) { %> stroke-dasharray="<%= item.badge_dash %>"<% } %>/><circle cx="16" cy="16" r="8" class="cj-disc-<%= item.badge_pi %>"/><text x="16" y="17" text-anchor="middle" dominant-baseline="central" class="cj-glyph" font-size="9"><%= item.badge_glyph %></text></svg></a></td>
<td class="listing-title">
<a href="<%- item.path %>"><%= item.short_title %></a><br/>
<span class="cj-status-summary"><%= item.status_summary %><% if (item.open_obligations > 0) { %> <span class="cj-open-count"><%= item.open_obligations %> open</span><% } %></span>
</td>
<td class="cj-tags">
<span class="cj-tag"><%= item.model %></span><span class="cj-tag"><%= item.form %></span><span class="cj-tag listing-category"><%= item.category %></span><% if (item.difficulty) { %><span class="cj-tag cj-tag-difficulty" title="<%= item.difficulty_note %>"><%= item.difficulty %><% if (item.difficulty_by === "ai") { %> (ai)<% } %></span><% } %>
</td>
</tr>
<% } %>
</tbody>
</table>
<% } %>
