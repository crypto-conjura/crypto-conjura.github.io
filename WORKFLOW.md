# Running HARNESS.md under Claude Code

## 1. What the "clean session" requirement actually is

HARNESS 3.5.1 asks for a verifier whose context contains the Contract, the
source cards, and the artifact, and nothing else. That is a condition on the
verifier's *view*, not on which application window produced it. A browser tab
is one way to realise the condition and the least checkable one: you cannot
diff what you pasted against what you meant to paste, you cannot record which
model version answered, and the drag-and-drop step is precisely where
provenance leaks back in.

Making the view a file makes the condition auditable. The blind prompt becomes
bytes on disk under version control; the verdict becomes a file; the model, the
cost and the session id come back in a JSON envelope. The invariant stops being
a promise and becomes a property you can inspect after the fact.

## 2. The mechanism

Claude Code's `--bare` flag skips auto-discovery of hooks, skills, plugins, MCP
servers, auto memory, and `CLAUDE.md`. Combined with `-p` (one prompt in, one
result out, process exits) and an empty working directory, one invocation is
exactly one blind referee.

Two consequences worth stating explicitly.

**`--bare` does not read OAuth credentials or the keychain.** It needs
`ANTHROPIC_API_KEY`. Five xhigh passes over a long proof are billed to the API,
not to a subscription. Price this before you build the habit.

**Subagents are isolated but not blank.** Every custom subagent loads the whole
`CLAUDE.md` hierarchy, including `~/.claude/CLAUDE.md`, plus a git status
snapshot; only the built-in Explore and Plan agents skip them. So a subagent
verifier reads whatever your project file says about the campaign. HARNESS
3.5.1 already says this in prose; the docs confirm the mechanism. The practical
rule follows:

> Keep `CLAUDE.md` purely procedural: directory layout, file conventions,
> naming discipline. Put every campaign belief in `LEDGER.md`, which is loaded
> explicitly by the agents that are entitled to see it. Anything you write into
> `CLAUDE.md` about what you think is true contaminates every in-loop verifier.

## 3. What to automate

Automate the parts that are bookkeeping, control flow, or context hygiene.

| Harness element | Mechanism | Why |
|---|---|---|
| 3.5.1 external blind review | `blind-verify.sh`, `claude --bare -p` per pass | the manual step; five processes replace five browser tabs |
| 3.5 to 3.7 loop | `verify-loop.sh` | a fixed point with three stopping rules; a shell counts better than a chat window |
| 2.3 effort and tool contracts | subagent frontmatter `model`, `effort`, `tools`, `disallowedTools` | "turn off web for Prover, Triage, Reviser, Lifter, Ledger" is an allowlist, not an instruction |
| 2.2 atomic units | one `-p` process per unit | exit 0 with a file written, or the unit did not happen |
| budget state GREEN/AMBER/RED | `total_cost_usd` in the JSON envelope | a computed number, not something you tell the agent |
| 2.4 freeze | `assert_not_frozen` in the scripts | re-verification thrash becomes a hard error, not a temptation |
| 3.12 checkpoint | `/checkpoint` slash command | cheap, so make it one keystroke |

The single largest reliability gain is the third row combined with the second:
right now the loop control is being executed by a language model inside a chat
window, which is why tallies drift and cycles get miscounted.

## 4. What not to automate

**The human gates.** The Case Planner ladder approval, the Weakener menu
choice, and reading the frozen proof are marked human in the harness for a
reason. Automating them turns the protocol into the thing section 5 warns
against: a system whose only external grounding signal is another instance of
the same model.

**Five passes are not five referees.** Five samples from one model with one
prompt are one referee sampled five times, and the errors that matter are
exactly the correlated ones. Vary `--model` across passes; for at least one
certifying pass, shell out to a different vendor's CLI on the same blind
prompt. The Ledger should record which passes were cross-family, since they are
worth more.

**Cheap verification invites the thing 2.4 forbids.** Once the loop is one
command, the marginal cost of re-verifying a settled statement drops to almost
nothing, and the discipline that kept the active workload the size of one
statement stops being enforced by inconvenience. Hence the freeze guard.

**The cognitive well gets deeper, not shallower, with automation.** Iterative
refinement converging to a confident wrong fixed point is a property of the
loop, and a faster loop reaches the fixed point sooner. The defences are fresh
verifiers each round, different families, and a human reading the artifact
before it is called proved. Keep all three.

## 5. Editor choice

Terminal or the VS Code extension: same binary, the IDE only changes where the
pane sits. For a LaTeX campaign the editor is worth having anyway, since the
revised artifacts are `.tex` and you get diffs against the superseded id for
free. But the substantive change is CLI plus files, not the editor.

## 6. Order of adoption

1. `blind-verify.sh` alone, against one already-completed intermediate, and
   compare its verdicts with the ones you got by hand. One evening.
2. The subagent definitions, so the effort and tool table in 2.3 stops being
   something you set by hand each time.
3. `verify-loop.sh`, only after you trust the tally.
4. Overnight runs, only for the climb from a frozen rung to the next, never
   across a human gate.

## 7. Skills versus subagents versus processes

The three mechanisms are not interchangeable, and the difference matters
exactly where the harness is most demanding.

A **skill** injects its body into whatever context is active. That makes it the
right home for the proving discipline, which should shape work already in
progress, and the wrong home for blindness, which is defined by what a context
does *not* contain. A skill can trigger a blind run; it cannot be one.

A **subagent** starts a fresh context, but not a blank one: it loads every
level of the CLAUDE.md hierarchy the main conversation loads, plus a git status
snapshot. Only the built-in Explore and Plan agents skip both. So a subagent
verifier reads whatever your project file says about the campaign.

A **`--bare -p` process** loads none of it: no CLAUDE.md, no auto memory, no
skills, no plugins, no MCP servers, no hooks. This is the only mechanism that
satisfies 3.5.1, and it is the only one whose verdicts belong in the tally.

Two couplings worth knowing before you edit the frontmatter:

- `disable-model-invocation: true` also prevents a skill from being preloaded
  into subagents. The `prove` skill therefore stays model-invocable, so that
  the `prover` subagent's `skills:` field can preload it and the discipline has
  one source of truth. `audit` and `checkpoint` set it, because you never want
  Claude deciding on its own to spend five verification passes or to rewrite
  the ledger.
- Skill content stays in context for the rest of the session once loaded, and
  the file is not re-read on later turns. Edit `prove/SKILL.md` mid-session and
  the running session keeps the old copy; re-invoke it to pick up the change.
