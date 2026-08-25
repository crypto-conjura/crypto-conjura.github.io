# Conjura wiki platform — feature specification

Companion document: [wiki-implementation-plan.md](wiki-implementation-plan.md) (how and in what order we build this).

## Purpose

Evolve Conjura from a PR-only static archive into a wiki-like collaborative platform: user profiles, discussion anchored to statements and proofs, in-browser editing, and a reputation system whose trust tiers reduce review friction for proven contributors — without weakening the guarantees the archive is built on (allocate-once ids, sha-pinned statements, CI-gated generators, blind verification for mathematical claims).

## Architecture overview

**Git stays canonical for all content. A thin backend holds all social data.**

- The Quarto site and GitHub Pages publish path are unchanged. Every content change — including ones initiated in the browser — lands as a git commit via PR and passes the existing CI gates (`scripts/status_badge.py --check`, `build_index.py`, `check_relations.py`, `gen_topics.py --check`, …).
- A Cloudflare Worker at `api.conjura.org` (with a D1 database) handles auth, profiles, comments, reputation, watches, notifications, and turns in-browser edits into PRs via a GitHub App. Being a subdomain of `conjura.org`, its session cookie is first-party (`Domain=.conjura.org; HttpOnly; Secure; SameSite=Lax`) — no third-party-cookie problems.
- The static site gains one small JS bundle (`assets/conjura-social.js`, no framework) injected site-wide via `_quarto.yml` `include-after-body`. It reads page identity from meta tags (`cj-page-id`, `cj-revision`, `cj-statement-sha`, `cj-areas`) injected at post-render time from `conjura.json`.
- **Sync doctrine: git/GitHub is the source of truth for content and PR state; D1 only caches/indexes it.** Never store content in D1. This keeps a later pivot to a fully dynamic app cheap: the social schema is clean relational SQL, and content remains addressable by `(id, revision, statement_sha)`.

## Feature inventory

### Identity & profiles

- Sign-in via **GitHub OAuth** (authorization-code flow handled entirely by the Worker; no scopes beyond `read:user` at login). Sessions are HttpOnly cookies.
- Profile page at `/u/?login=<github_login>` — one static Quarto page, filled client-side. Fields: GitHub identity (canonical), display name, affiliation, homepage, expertise areas (from the fixed 19 area slugs), opt-in notification email, and **verified ORCID** (linked via ORCID OAuth) so academics can stake their names.
- Steering-committee members (see `participate/index.qmd`) are flagged `role=steward` in the database.

### Discussion (comments on statements, proofs, and every other page)

- Threads are keyed by a **stable anchor**: `(page_id, section_key, optional text-quote selector)`. `page_id` is `c/<id>`, `p/<slug>`, or a `uc/` path — ids never change, so no thread is ever orphaned. `section_key` is one of the fixed tab/section identifiers already enforced by `scripts/tab_structure.py`: `statement`, `proof`, `status`, `lean`, `general`.
- Fine-grained inline comments store a W3C-style text quote `{exact, prefix, suffix}` plus the `revision` and `statement_sha` current at write time. On render, the widget re-attaches the quote to the live text; if a revision bump changed the wording, the comment **degrades gracefully** to its section thread with a badge "written against revision N (sha …)" linking to the pinned blob on GitHub. Comments are never deleted or hidden by drift — mirroring the archive's immutability ethos.
- Comment kinds: **plain**, **question**, **objection** (flags a possible error; surfaces to maintainers), **review note** (reviewer tier and up, rendered distinctly), and **system** (blind-verify verdicts, status transitions — machine-posted, citable).

### Editing (in-browser edit → PR)

Three lanes matching the site's own risk model. All three produce PRs; CI generators remain the mechanical gatekeepers, and the editor's job is to produce PRs that pass them on the first try (client-side frontmatter lint against `schema/` before submit).

1. **Prose edits** (UC pages, problem-hub prose, `status_summary` wording): "Suggest an edit" opens an in-page markdown editor on the raw `.qmd` at the deployed sha. Submit → the GitHub App commits to a bot fork and opens a PR with `Co-authored-by:` the user. Users who prefer direct authorship get a pre-filled fork/github.dev link instead.
2. **Statement edits**: the editor exposes **only legal transitions** — revision bump for wording (CI recomputes `statement_sha` and badge), metadata/status/relations changes. Meaning changes are refused in-UI, quoting the rule; instead the UI offers a **"Propose successor statement"** flow that scaffolds a new `c/<next-id>/index.qmd` from `_templates/statement.qmd` plus the `withdrawn` + `superseded-by` edit to the old one, in a single PR.
3. **Proof/resolution submissions**: structured form (claim, proof body, sources, optional Lean stub) → PR labeled `needs-blind-verify`. **Never merged on trust alone.**

Proposal lifecycle, tracked in D1 and mirrored from the PR (the PR is truth):
`draft → submitted → ci-passed → in-review → blind-verify (statements/proofs) → merged | rejected | withdrawn`.
GitHub webhooks (`pull_request`, `check_suite`) update D1; a nightly reconcile heals missed events.

### Reputation & badges

- **Append-only ledger** (`reputation_events`); profiles show the ledger, not just a number — auditable by design. No decay: review competence doesn't expire, and decay punishes exactly the busy senior academics the project needs.
- **Area-scoped**: events carry the statement's `areas`; review privileges are per-area, UX privileges use the max across areas.
- Earning events (initial values, tunable): accepted prose edit +2 · accepted statement revision +10 · accepted new statement +25 · steward-endorsed review +15 · review that catches a later-confirmed error +40 · proof passing blind verification and human review +100 · steward endorsement of an artifact +20 · upheld flag +2 · abusive flag −10.
- **Tiers and what they unlock** in the review pipeline:

| Tier | Threshold | Unlocks |
|---|---|---|
| T0 visitor | signed in | comment, flag, watch, suggest prose edits (needs 1 maintainer approval + CI) |
| T1 contributor | ≥25 | prose PRs auto-request review from page watchers instead of maintainers; propose statement revisions |
| T2 trusted (per area) | ≥150 in area | prose edits in that area merge on CI-green + 1 T2 peer approval; post review notes; triage flags |
| T3 reviewer (per area) | ≥400 + steward endorsement | their approval flips `proof_review: ai → human` (recorded with name + date in frontmatter); can trigger blind-verify runs |
| Steward | appointed | merge rights, moderation, endorsements, governance |

- **Invariant regardless of tier**: any diff touching statement text, proof text, the `status:` block, or `lean/` runs full CI **and** blind verification. Tiers change only how many humans must additionally sign off, and how fast.
- **Badges**: first accepted edit, per-area badges, verified reviewer, resolved-a-conjecture, ORCID-linked. Stored in D1; durable ones (e.g. "human-reviewed by X") also materialize into frontmatter via the normal PR pipeline so the static record keeps them permanently.

### Moderation & governance

- Flag queue (spam / abuse / mathematical error / license) with T2+ triage, steward resolution, and appeal to a second steward.
- Tiered rate limits (e.g. T0: 5 comments/hr, 1 PR/day). Spam is shadow-quarantined (visible only to its author) rather than deleted; hard deletion only for legal/abuse content, logged in a moderation ledger.
- Editorial actions (Contested, Retracted) are **content states, not database states**: stewards effect them through PRs so `git log` remains the record.

### Notifications & watchlists

- Watch a statement, problem, area, user — or a **status transition** ("notify me when anything in `lattices` reaches `proof_review: human`"), possible because status is structured.
- Content-change events come from a post-deploy job that diffs old vs new `conjura.json` and POSTs a signed payload to the Worker; social events come from D1 directly.
- Delivery: in-app inbox, optional email digest, optional Zulip DM. Digest is the default.

### Recent changes & versioning UI

- `/changes/` — a wiki-style RecentChanges page, client-rendered from a merged feed of content events and social events, filterable by area/type; also exposed as Atom.
- **History tab** on statement pages: git history for the page via a Worker-proxied, cached GitHub API (avoids rate limits and CORS), with rendered diffs per revision bump. The `statement_sha` chain gives a semantic history distinct from commit noise — show both. Withdrawn/superseded statements render a prominent successor pointer.

## Conjura-specific extras

1. **Structured review requests**: a typed "Request review" (naming the status field, e.g. `proof_review`) feeding an open **review queue** page sorted by area.
2. **Bounties on open obligations**: users pledge recognition (or link external GitHub Sponsors — the platform never touches funds) against a specific obligation; rendered as a chip; fulfilled by the PR that flips the field.
3. **Blind-verify results as system comments**: `blind-verify.sh` / `verify-loop.sh` verdicts post into the proof's thread with referee model id and package sha — the AI referee's assent/dissent becomes public and citable.
4. **Zulip bridge**: outbound webhooks per area stream (new statements, status flips, review requests) and a Zulip linkifier for `c/NNNN`. No bidirectional comment mirroring; each thread links to the other side.
5. **Cite this revision**: per-statement citation stanza (id, revision, statement_sha, date), also added to `conjura.json`.
6. **Incubator vs archive lanes**: `category: research-open` + `proof_review: ai` items accept T0 engagement freely; archive-lane changes require the full tier machinery. Lane rendered via the existing badge system.
7. **Claim board**: soft "I'm working on this" claims (auto-expire after 60 days) beside the difficulty box.
8. **Harvest triage queue**: candidates from `scripts/harvest_conjectures.py` graded by T2+ users *before* a statement id is allocated — protects the allocate-once id space.

## Data model (D1 / SQLite)

```sql
users(id PK, github_id UNIQUE, login, display_name, orcid, affiliation,
      email, email_verified, role,           -- 'user'|'steward'|'admin'
      created_at, banned_at)
sessions(id PK, user_id FK, created_at, expires_at, last_seen)
comments(id PK, user_id FK, page_id,         -- 'c/0042' | 'p/<slug>' | 'uc/<path>'
      section_key,                           -- 'statement'|'proof'|'status'|'lean'|'general'
      anchor_exact, anchor_prefix, anchor_suffix,   -- nullable text-quote selector
      anchored_revision, anchored_sha,
      parent_id FK NULL, kind,               -- 'plain'|'question'|'objection'|'review'|'system'
      body_md, created_at, edited_at, hidden_at, hidden_by)
edit_proposals(id PK, user_id FK, page_id, kind,   -- 'prose'|'statement-revision'|'successor'|'proof'|'metadata'
      pr_number, branch, state, base_sha, created_at, updated_at, decided_by, decided_at)
reputation_events(id PK, user_id FK, kind, points, area,
      subject_type, subject_id, actor_id, created_at)   -- append-only
badges(id PK, slug, name, criteria_md)
user_badges(user_id, badge_id, awarded_at, evidence_url, PK(user_id, badge_id))
watches(id PK, user_id FK, target_type,     -- 'statement'|'problem'|'area'|'user'|'transition'
      target_id, filter_json, channel, created_at,
      UNIQUE(user_id, target_type, target_id, channel))
notifications(id PK, user_id FK, event_type, payload_json, created_at, read_at, emailed_at)
content_events(id PK, page_id, event_type,  -- 'revision-bump'|'status-change'|'new-statement'|'withdrawn'…
      old_json, new_json, commit_sha, created_at)
flags(id PK, user_id FK, subject_type, subject_id, reason, state,
      resolved_by, resolved_at, created_at)
```

Anchor survival: comments store `(section_key, text-quote, anchored_revision, anchored_sha)`. Re-attachment is attempted against the live section text; failure degrades to the section thread with a revision badge. Section keys are fixed and statement ids are allocate-once, so the worst case is section-level, never lost. No diff-based anchor migration in v1 — deliberately simple.
