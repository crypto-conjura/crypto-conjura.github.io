# Conjura wiki platform — implementation plan

Companion document: [wiki-features.md](wiki-features.md) (what we are building and why). This document says how, in what order, and what changes in this repo.

## Ground rules

- Quarto + GitHub Pages remain the canonical publish path. No content moves out of git.
- All backend code lives in a new `worker/` directory (Cloudflare Worker + D1 migrations), deployed by its own GitHub Action with a path filter — the API deploy is decoupled from the site deploy.
- The Worker is the only holder of secrets (GitHub OAuth app secret, GitHub App private key). The browser never calls GitHub directly.
- Git/GitHub is the source of truth for content and PR state; D1 caches it. A nightly reconcile job re-lists open PRs and re-fetches `conjura.json` to heal missed webhook events.
- Each phase below is independently shippable and useful on its own.

## GitHub write path

Register a GitHub App (**conjura-platform**) installed on the repo. The Worker mints installation tokens. Platform-mediated edits: the App commits to a branch in a dedicated bot fork with `Co-authored-by: <user>` and opens a PR. Benefits: login needs only `read:user` OAuth scope, per-PR provenance is preserved, the App's webhooks feed the proposal lifecycle, and pausing the App is a one-click kill switch.

## Phases

### P0 — Auth + comments + recent changes (~2–3 weeks)

The read-only social layer: discussion on every page.

- Worker skeleton at `api.conjura.org`; GitHub OAuth flow; session cookies; D1 migrations for `users`, `sessions`, `comments`, `flags`.
- Section-level comment threads (no text-quote anchors yet), comment kinds, flagging, steward hide.
- Per-page meta tags (`cj-page-id`, `cj-revision`, `cj-statement-sha`, `cj-areas`) injected by a post-render script reading `conjura.json` (alongside `scripts/strip_polyfill.py` — no frontmatter churn across 250+ files).
- `assets/conjura-social.js` widget injected via `_quarto.yml` `include-after-body`.
- `/changes/` page fed from push webhooks.

### P1 — Profiles + reputation ledger + watchlists (~2 weeks)

- Profile page (`/u/`), ORCID OAuth linking, expertise areas.
- Append-only `reputation_events` ledger with manual steward grants; badges.
- Watches + in-app inbox; `publish.yml` gains a `conjura.json`-diff step that POSTs signed `content_events` to the Worker → transition notifications.
- Review-request queue (typed asks against status fields) — cheap and high leverage for the review-credibility problem.

### P2 — In-browser edit → PR (~3–4 weeks)

- GitHub App + bot fork; webhook endpoint driving the `edit_proposals` lifecycle.
- Prose lane first: in-page editor, client-side frontmatter/schema lint (mirror of the `--check` rules) run in the Worker *before* any PR is opened.
- Then the statement-revision lane (legal transitions only) and the successor-statement scaffold (new id + withdrawn + superseded-by in one PR).
- Proof-submission form gated behind the `needs-blind-verify` label.
- History tab (versioning UI) lands here — it shares the Worker's cached GitHub proxy.

### P3 — Trust-tier automation + review gating (~2 weeks)

- Automatic area-scoped tier computation from the ledger.
- New CI gate `scripts/check_review_policy.py --check`: reads a Worker endpoint (PR author tier + approvals) and passes/fails the PR — **the merge policy lives in CI like every other gate**, not in webhook side effects.
- Blind-verify results posted as system comments (verdict, referee model id, package sha).
- `proof_review: ai → human` flip flow driven by T3 approvals, recorded with name + date in frontmatter via the normal PR pipeline.

### P4 — Delivery channels + extras (~2 weeks)

- Email digests (Email Workers or Resend), Zulip outbound webhooks + linkifier, Atom feed.
- Text-quote inline anchors with graceful degradation.
- Claim board, bounty chips, harvest triage queue.

## Risks & mitigations

| Risk | Mitigation |
|---|---|
| Spam / PR flood | Tiered rate limits; all platform PRs come from the bot fork so pausing the App stops everything; new-account cooldown (GitHub account age ≥ 1 week); schema lint in the Worker before a PR is ever opened |
| GitHub API rate limits | App installation tokens (12.5k/hr); Worker-side KV caching (≈5-min TTL) of commits/blobs; conditional requests with ETags; browser never calls GitHub |
| CORS / cookies | API on `api.conjura.org` → first-party cookie `Domain=.conjura.org; HttpOnly; Secure; SameSite=Lax`; explicit `Access-Control-Allow-Origin: https://conjura.org`; CSRF double-submit token on mutating routes |
| D1 ↔ git drift | Doctrine: git is truth, D1 caches; webhooks best-effort + nightly reconcile; content never stored in D1 |
| Deploy race (comment anchored to a revision the CDN hasn't shown yet) | Anchors carry `statement_sha`; mismatch degrades gracefully by design |
| Blind-verify cost / abuse | Runs only on labeled PRs; label applied by the Worker under rate limit; re-runs restricted to T3/steward |

## Repo changes required

- **`_quarto.yml`**: add `include-after-body` for `assets/conjura-social.js` (deferred module script).
- **Post-render script** (new, alongside `scripts/strip_polyfill.py`): inject the `cj-*` meta tags into built pages from `conjura.json`.
- **`scripts/build_index.py`**: give `conjura.json` a versioned envelope (`{"schema": 2, "generated_at", "commit", ...}`), per-statement `sections` (stable section keys), and a `citation` stanza.
- **`.github/workflows/publish.yml`**: post-deploy `conjura.json`-diff → signed POST to the Worker (P1).
- **New workflow `worker-deploy.yml`**: wrangler deploy of `worker/`, path-filtered.
- **New `scripts/check_review_policy.py`** with `--check` mode wired into `checks.yml` (P3).
- **New directories**: `worker/` (API source + D1 migrations), `assets/conjura-social.js` source.
- **Governance/privacy pages** the trust tiers and moderation rules reference, published on the site.

## Cost & operations

Cloudflare Workers + D1 free tier covers this traffic for the foreseeable future; D1 is SQLite, so the schema migrates trivially to Postgres if we later pivot to a fully dynamic app. Zero servers to patch. The only recurring operational duties are steward moderation, tuning reputation point values, and rotating the GitHub App key.
