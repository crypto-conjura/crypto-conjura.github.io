// Use Quarto's existing List.js instance so sorting and pagination stay in sync.
document.addEventListener("DOMContentLoaded", () => {
  const list = window["quarto-listings"]?.["listing-all-statements"];
  const controls = document.getElementById("problem-list-controls");
  if (!list || !controls) return;

  const select = document.getElementById("problem-page-size");
  const count = document.getElementById("problem-list-count");
  const pagination = document.getElementById("all-statements-pagination");
  // Keep the page-size choice beside Quarto's page navigation below the table.
  if (pagination) {
    const footer = document.createElement("div");
    footer.className = "d-flex flex-wrap align-items-center gap-3 mt-3";
    pagination.before(footer);
    footer.append(pagination, controls);
    pagination.classList.add("m-0");
    pagination.querySelector(".pagination")?.classList.add("m-0");
  }
  const storageKey = "aicr.problem-page-size";
  const pageKey = "listing-all-statements-page";
  const choices = new Set(["20", "100", "all"]);
  let choice = "20";
  try {
    const saved = localStorage.getItem(storageKey);
    if (choices.has(saved)) choice = saved;
  } catch (_) {
    // Browsing still works when storage is unavailable.
  }
  select.value = choice;

  function replacePageHash(page) {
    const url = new URL(window.location.href);
    const params = new URLSearchParams(url.hash.slice(1));
    if (!params.has(pageKey)) return;
    params.set(pageKey, String(page));
    url.hash = params.toString();
    window.history.replaceState(null, "", url);
  }

  function refresh() {
    const total = list.matchingItems.length;
    // A bookmarked page may exceed the range after restoring a larger size.
    if (total && list.i > total) {
      const lastPage = Math.ceil(total / list.page);
      replacePageHash(lastPage);
      list.show((lastPage - 1) * list.page + 1, list.page);
      return;
    }
    const first = list.visibleItems.length ? list.i : 0;
    const last = first ? first + list.visibleItems.length - 1 : 0;
    count.textContent = `Showing ${first}–${last} of ${total}`;
    if (pagination) pagination.hidden = total <= list.page;
  }

  function applySize(page) {
    const size = select.value === "all" ? Math.max(1, list.items.length) : Number(select.value);
    const lastPage = Math.max(1, Math.ceil(list.matchingItems.length / size));
    const target = Math.min(Math.max(1, page), lastPage);
    replacePageHash(target);
    list.show((target - 1) * size + 1, size);
  }

  list.on("updated", refresh);
  select.addEventListener("change", () => {
    try {
      localStorage.setItem(storageKey, select.value);
    } catch (_) {
      // Only persistence is lost; the selection still applies to this page.
    }
    applySize(1);
  });
  const params = new URLSearchParams(window.location.hash.slice(1));
  const requested = Number(params.get(pageKey));
  applySize(Number.isInteger(requested) && requested > 0 ? requested : 1);
  controls.hidden = false;
});
