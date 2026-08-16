# Rulesets

The desired state of this repository's branch protection, kept as JSON because
GitHub's settings UI records what a rule is and never why it was chosen. Each
file here is one ruleset. `scripts/rulesets.py` applies them and checks the live
repository against them.

These files are the source of truth. If you change protection through the web
UI, change it here too, or the next `--check` will report the drift and the next
`--apply` will undo you.

## Why this exists at all

GitHub has no path-scoped write permission: repository roles apply to the whole
repository. The only path-aware rule GitHub offers, "Restrict file paths", lives
in a *push* ruleset, and push rulesets are documented as applying to "a private
or internal repository and that repository's entire fork network". This
repository is public, so that rule is unavailable here regardless of plan.

What is available is a *branch* ruleset, which public repositories get on the
Free plan. So access control here is: nobody is granted the write role except
maintainers, everyone else contributes by fork and pull request, and `main`
itself accepts nothing that has not been through a pull request with green
checks.

## protect-main.json

Four rules, each with a reason and, for two of them, a trap worth knowing.

- **`pull_request` with `required_approving_review_count: 0`.** The zero is
  deliberate and is the trap. GitHub does not let you approve your own pull
  request, so on a repository with a single maintainer any non-zero count blocks
  every pull request permanently, including the one that would relax the rule.
  Zero still forces every change through a pull request and its checks, while
  leaving a solo maintainer able to merge. Raise it the day a second maintainer
  exists, not before.
- **`required_status_checks` on the context `checks`.** That is the job id of
  the `checks` job in `.github/workflows/checks.yml`, which runs the four gates
  and a full render. It triggers on `pull_request` with no path filter, which
  matters: a required check that never runs on some pull requests would block
  those merges forever with no way to satisfy it.
- **`non_fast_forward`.** Blocks force-pushes to `main`. Published history stays
  published.
- **`deletion`.** Blocks deleting `main`.

**Bypass.** Organization admins bypass all of it. The ruleset therefore
constrains collaborators rather than owners, which is its purpose, and it
removes any way to lock the owner out of their own default branch. To make it
bind on everyone, set `bypass_actors` to `[]` and re-apply. Note that an admin
can still edit or delete the ruleset, so this is a guardrail against accident
and against collaborators, not a control over someone with admin rights.

## Usage

```sh
python3 scripts/rulesets.py --check    # compare live repository against these files
python3 scripts/rulesets.py --apply    # create or update to match
python3 scripts/rulesets.py --show     # print what is live right now
```

`--check` and `--show` need only read access. `--apply` needs repository admin.
All three go through `gh`, so authentication is whatever `gh auth status`
reports.

To remove a ruleset, delete it in the web UI or by id, and delete its file here:

```sh
gh api repos/crypto-conjura/crypto-conjura.github.io/rulesets --jq '.[] | "\(.id) \(.name)"'
gh api repos/crypto-conjura/crypto-conjura.github.io/rulesets/<id> -X DELETE
```

`--apply` never deletes. A ruleset that exists on the repository but has no file
here is reported by `--check` and otherwise left alone, so this directory can be
adopted incrementally without it treating unmanaged rulesets as drift to erase.
