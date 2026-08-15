<table class="table cj-statement-table list">
<thead>
<tr>
<th class="sortable" data-sort="listing-status_badge">Status</th>
<th class="sortable" data-sort="listing-title">Statement</th>
<th class="sortable" data-sort="listing-model">Model</th>
<th class="sortable" data-sort="listing-form">Form</th>
<th class="sortable" data-sort="listing-category">Category</th>
<th class="sortable" data-sort="listing-open_obligations">Open</th>
</tr>
</thead>
<tbody>
<% for (const item of items) { %>
<tr <%= metadataAttrs(item) %>>
<td class="listing-status_badge"><%- item.status_badge %></td>
<td class="listing-title">
<a href="<%- item.path %>"><%= item.short_title %></a><br/>
<span class="cj-status-summary"><%= item.status_summary %></span>
</td>
<td class="listing-model"><%= item.model %></td>
<td class="listing-form"><%= item.form %></td>
<td class="listing-category"><%= item.category %></td>
<td class="listing-open_obligations"><%= item.open_obligations %></td>
</tr>
<% } %>
</tbody>
</table>
