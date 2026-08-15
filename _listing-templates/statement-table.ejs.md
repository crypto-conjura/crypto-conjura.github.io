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
<span class="cj-tag"><%= item.model %></span><span class="cj-tag"><%= item.form %></span><span class="cj-tag listing-category"><%= item.category %></span>
</td>
</tr>
<% } %>
</tbody>
</table>
