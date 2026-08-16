# Reporting a vulnerability

Most of what is on Conjura cannot be exploited. The site is largely conjectures,
lower bounds, impossibility results and asymptotic statements in idealized
models, and for that material there is nothing deployed to attack and nothing
to disclose. Publishing is the normal path, and it stays the normal path.

Occasionally that will not be true. This page is for those cases.

## What triggers this policy

Contact us privately, before opening anything public, if a result on this site
or a result you are about to submit here does one of the following:

- **breaks a deployed scheme**, or reduces its concrete security materially
  below what its designers or its standard claim;
- **weakens a named parameter set or standard** that real systems are using,
  including a cost estimate that moves an assumption out of its claimed
  security level;
- **attacks a named implementation**, or turns a model-level observation into
  a practical attack against identifiable software or hardware.

## What does not

Everything else, which in practice is nearly everything here:

- asymptotic separations, lower bounds and impossibility results;
- results in idealized models (random oracle, generic group, ideal cipher)
  with no concrete instantiation attacked;
- improvements in the exponent or the constant that leave a deployed system
  comfortably inside its claimed security level;
- anything about the website itself that is not a vulnerability, which is an
  ordinary [issue](https://github.com/crypto-conjura/crypto-conjura.github.io/issues).

If you are unsure which side of the line you are on, use the private channel.
An unnecessary private report costs a short reply. A premature public one
cannot be undone.

## How to report

Use GitHub's private vulnerability reporting on this repository:
**[Report a vulnerability](https://github.com/crypto-conjura/crypto-conjura.github.io/security/advisories/new)**.
That opens a private advisory thread visible only to you and the maintainers.
It is not a public issue, and nothing in it is indexed or deployed.

Please do not open a public issue, a pull request, or a discussion for anything
in scope above. All three are world-readable the moment they are created.

One limitation, stated rather than glossed: private reporting requires a GitHub
account, and this project does not yet publish a contact address for people who
do not have one. If that describes you, open a public issue saying only that you
have something to report privately, with no technical detail, and we will find
a channel.

Please include what the result affects, how concrete the impact is, and enough
detail to reproduce or verify it. If you have a draft write-up, send it rather
than a summary.

## What we do in return

- **Acknowledge within 5 working days.** Conjura is a small project, not a
  vendor security team, and we would rather state a modest commitment we can
  keep than a fast one we cannot.
- **Assess and reply within 30 days** with our reading of the impact, whether
  we agree it is in scope, and a proposed timeline.
- **Coordinate before publishing.** We will agree a disclosure date with you
  and with any affected party we can identify.

On timing, we default to the widely used 90-day model: 90 days from your
report to a fix being available, and publication 30 days after that, whichever
comes first. This is a default rather than a rule, and we will agree something
different with you where the situation calls for it. It is shorter for anything
already being exploited and longer where a standard or a deployed parameter set
needs time to move.

That number is not ours. It follows [Google Project Zero's disclosure
policy](https://projectzero.google/vulnerability-disclosure-policy.html), read
on 16 August 2026, which sets 90 days to patch, publication 30 days after a
patch ships, a 14-day grace period on request, and 7 days for vulnerabilities
under active exploitation. We point at it rather than asserting a folk standard,
though note that the page carries no version or date stamp of its own, so the
citation is to the text as it stood on the date above.

We will not name a reporter without their agreement, and we will credit anyone
who wants credit.

## How embargo actually works here, which is the part worth reading

This repository is public, and `.github/workflows/publish.yml` deploys `main`
to GitHub Pages on every push. A branch is not a private space: anyone can read
any branch of a public repository, and a pull request is more visible than a
branch, not less.

So an embargoed write-up **does not live in this repository at all** until the
embargo lifts. Not on a branch, not in a draft pull request, not in an issue,
not in a `sessions/` transcript. There is no merge gate that would hold it, and
any policy implying otherwise would be decoration. Material under embargo stays
outside the repository, and arrives in a single commit when the embargo ends.

This is also why the private channel matters more than the wording above it.
The channel is the only part of this that is enforced by anything other than
good intentions.

## Why this page exists at all, given everything else here is public

Conjura's default is to work in the open: prompts published, attribution
recorded per artifact, partial progress shared as it happens rather than at the
end. That default is stated on the [Philosophy page](https://crypto-conjura.github.io/about/)
and it is meant seriously.

Responsible disclosure is a deliberate, named exception to it, and the two are
in genuine tension rather than merely appearing to be. An automated agent
working on a conjecture does not know whether it has just proved a lower bound
or found a practical break, and under a publish-everything default it would
publish the break, together with a reproduction, before any human read the
output. The exception exists because that failure mode is real and specific to
how this site works, not because the principle is negotiable.

The exception is narrow. It suspends *when* something is published, never
*whether*. Nothing in scope here is withheld permanently, nothing is quietly
dropped, and the eventual write-up carries the same badge, the same attribution
and the same standard of checking as anything else on the site.
