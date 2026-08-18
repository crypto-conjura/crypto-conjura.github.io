<% /* The flat view of the UC encyclopedia: every functionality, across all
      nine layers, in one sortable and filterable table.

      Why a template rather than `fields: [title, layer, status, definition]`
      with the built-in table: `layer` is a bare integer in each entry's
      frontmatter, so the built-in renders a column of digits where the layer
      pages carry names. The map below turns the number into the layer's name
      and links it to that layer's own index, which is the one thing this
      page can offer that nine separate tables cannot -- seeing which layer
      an entry belongs to without navigating to it.

      The layer's URL is derived from the item's own path rather than
      hardcoded, so renaming a layer directory cannot leave a dead link here;
      only the display names below would need touching.

      Editor's note, inherited from statement-table.ejs.md: the engine is
      lodash templates, not full EJS, so a hash-style comment is a syntax
      error -- write a JavaScript block comment inside a code tag, as here --
      and a comment may not contain a closing tag delimiter. */ %>
<% const LAYER_NAMES = {
     0: "Idealized Setup and Resources",
     1: "Channels, Agreement, Ledgers",
     2: "Cryptographic Library and Symmetric Primitives",
     3: "Public-Key Primitives, Key Exchange, Messaging",
     4: "Commitments and Proofs",
     5: "Oblivious Transfer and Correlated Randomness",
     6: "Secret Sharing, Threshold Cryptography, MPC",
     7: "Privacy and Anonymity",
     8: "Time and Application Composites",
   }; %>
<% /* The hidden spans are how the Layer and Definition columns sort. List.js
      only knows the value names Quarto registers from the listing's own
      fields -- listing-title, listing-layer, listing-status,
      listing-definition -- so an invented sort-only key is silently
      inert, and the header must point at the registered name. List.js reads
      the whole cell's text, so a hidden digit at the front of the cell is
      what actually orders it: "0Idealized Setup..." sorts before
      "1Channels...", and the layer numbers stay single digits.

      Sorting the Definition column alphabetically would put "Defined" next
      to "Definition"-like values and bury the distinction a reader wants,
      which is written-versus-not. These keys sort it by how much of an entry
      exists instead: written first, then the slots, then the entries where
      the literature has nothing to transcribe. Both hidden keys ride in a
      d-none span, which List.js reads and neither the page nor the
      accessibility tree shows. */ %>
<% const DEFINITION_ORDER = {
     "Defined": 0,
     "No canonical definition": 1,
     "Not yet written": 2,
   }; %>
<% /* Two class names are doing two different jobs on the headers. `sort` is
      List.js's own binding class -- it attaches the click handler when the
      list is constructed, so adding it later does nothing -- and `sortable`
      is what this site's CSS styles. A header with only `sortable` looks
      clickable and is inert, which is what the statements table has been
      shipping.

      `list` goes on the tbody, not the table. List.js treats the children of
      the element carrying that class as the items to sort and filter, so on
      the table it sees exactly two "items" -- thead and tbody -- and every
      sort and every search silently does nothing. Verified in a headless
      browser rather than by reading the markup, because nothing about the
      page looks wrong when it is broken. */ %>
<% if (items.length === 0) { %>
<p class="cj-listing-empty">No functionalities matched.</p>
<% } else { %>
<table class="table cj-functionality-table">
<thead>
<tr>
<th class="sortable sort" data-sort="listing-title">Functionality</th>
<th class="sortable sort" data-sort="listing-layer">Layer</th>
<th class="sortable sort" data-sort="listing-status">Status</th>
<th class="sortable sort" data-sort="listing-definition">Definition</th>
</tr>
</thead>
<tbody class="list">
<% for (const item of items) { %>
<%
   const m = String(item.path || "").match(/(layer-\d+-[^\/]+)/);
   const layerHref = m ? ("/uc/" + m[1] + "/") : null;
   const layerName = LAYER_NAMES[item.layer] !== undefined
     ? LAYER_NAMES[item.layer] : ("Layer " + item.layer);
%>
<tr <%= metadataAttrs(item) %>>
<td class="listing-title"><a href="<%- item.path %>"><%= item.title %></a></td>
<td class="listing-layer"><span class="cj-sortkey d-none"><%= item.layer %></span><% if (layerHref) { %><a href="<%- layerHref %>"><%= layerName %></a><% } else { %><%= layerName %><% } %></td>
<td class="listing-status"><%= item.status %></td>
<td class="listing-definition"><span class="cj-sortkey d-none"><%= DEFINITION_ORDER[item.definition] !== undefined ? DEFINITION_ORDER[item.definition] : 9 %></span><span class="cj-definition cj-definition-<%= (item.definition || "").toLowerCase().replace(/[^a-z]+/g, "-") %>"><%= item.definition %></span></td>
</tr>
<% } %>
</tbody>
</table>
<% } %>
