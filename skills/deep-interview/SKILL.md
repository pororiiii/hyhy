---
name: deep-interview
description: Socratic deep interview with mathematical ambiguity gating before execution
argument-hint: "[--quick|--standard|--deep] <idea or vague description>"
---

<!--
Standalone port of the oh-my-codex `deep-interview` skill (MIT License, Copyright (c) 2026 Yeachan-Heo,
https://github.com/Yeachan-Heo/oh-my-codex). The interview method, scoring, gates and spec format are kept
as close to the original as possible. Only the parts that require the oh-my-codex runtime were replaced:
`omx question` -> one plain chat question per round, `omx state` / `.omx/` -> files under `.deep-interview/runs/{interview_id}/`,
and `$ralplan/$autopilot/$team/$ultragoal/$autoresearch` handoffs -> a user-chosen next step.
Following OMX 0.21.14's session-scoped state principle, each standalone interview has its own run directory.
Context, transcript and spec also stay in that directory. This file-based protocol does not reproduce OMX's runtime ownership checks or write locks.
It sets no model and installs nothing. See LICENSE-oh-my-codex in this folder.
-->

<Purpose>
Deep Interview is an intent-first Socratic clarification loop before planning or implementation. It turns vague ideas into execution-ready specifications by asking targeted questions about why the user wants a change, how far it should go, what should stay out of scope, and what the agent may decide without confirmation.
</Purpose>

<Use_When>
- The request is broad, ambiguous, or missing concrete acceptance criteria
- The user says "deep interview", "interview me", "ask me everything", "don't assume", or "ouroboros"
- The user wants to avoid misaligned implementation from underspecified requirements
- You need a requirements artifact before planning or implementation (for example before the structure discussion or the first build step)
</Use_When>

<Do_Not_Use_When>
- The request already has concrete file/symbol targets and clear acceptance criteria
- The user explicitly asks to skip planning/interview and execute immediately
- The user asks for lightweight brainstorming only (use a lighter planning prompt instead)
- A complete PRD/plan already exists and execution should start
</Do_Not_Use_When>

<Why_This_Exists>
Execution quality is usually bottlenecked by intent clarity, not just missing implementation detail. A single expansion pass often misses why the user wants a change, where the scope should stop, which tradeoffs are unacceptable, and which decisions still require user approval. This workflow applies Socratic pressure + quantitative ambiguity scoring so orchestration modes begin with an explicit, testable, intent-aligned spec.
</Why_This_Exists>

<Depth_Profiles>
- **Quick (`--quick`)**: fast pre-PRD pass; target threshold `<= 0.30`; max rounds 5
- **Standard (`--standard`, default)**: full requirement interview; target threshold `<= 0.20`; max rounds 12
- **Deep (`--deep`)**: high-rigor exploration; target threshold `<= 0.15`; max rounds 20

Profile `max rounds` is a hard cap, not a target. Do not continue only to reach a numbered round count. Extra Socratic rigor does not override the active threshold unless the profile/config changes.

If no flag is provided, use **Standard**.

</Depth_Profiles>

<Execution_Policy>
- Talk to the user in the user's own language (for example Korean); keep labels such as `[from-user]` unchanged
- Ask ONE question per round (never batch multiple interview rounds into one message or form)
- Ask about intent and boundaries before implementation detail
- Target the weakest clarity dimension each round after applying the stage-priority rules below
- Treat every answer as a claim to pressure-test before moving on: the next question should usually demand evidence or examples, expose a hidden assumption, force a tradeoff or boundary, or reframe root cause vs symptom
- Do not rotate to a new clarity dimension just for coverage when the current answer is still vague; stay on the same thread until one layer deeper, one assumption clearer, or one boundary tighter
- Before crystallizing, complete at least one explicit pressure pass that revisits an earlier answer with a deeper, assumption-focused, or tradeoff-focused follow-up
- Gather codebase facts by inspecting the repository (read files, search) before asking the user about internals
- Always run a preflight context intake before the first interview question
- For brownfield work, preflight must include doc/context grounding before user-facing questions: inspect applicable `AGENTS.md` files, README/getting-started docs, relevant `docs/` contracts/plans/ADRs, the selected interview's context snapshots, and any project-local glossary/context files such as `CONTEXT.md` or `CONTEXT-MAP.md` when present.
- Treat existing repo language as evidence, not authority: if the user uses a fuzzy, overloaded, or conflicting term, surface the specific doc/code wording and ask which meaning should govern before implementation.
- Cross-check user claims about current behavior against code or documented contracts when discoverable. If docs and code disagree, ask a confirmation question that names both sources instead of silently choosing one.
- Use scenario-based edge-case grilling when relationships, boundaries, or handoff behavior are unclear: invent one concrete scenario that stresses the ambiguous boundary, then ask one focused question about the expected outcome.
- Durable docs, glossary, ADR, or memory updates are opt-in and public-safe only. Deep-interview may recommend such updates in the handoff summary, but must not automatically create or dump public docs from interview transcripts unless the user explicitly chooses that as in-scope.
- If initial context is oversized or would exceed the prompt budget, do not paste or forward the raw payload into interview prompts; request and record a prompt-safe initial-context summary first
- The oversized initial-context summary gate is blocking: wait for the concise summary before ambiguity scoring, crystallizing artifacts, or any downstream execution handoff
- The summary must preserve goals, constraints, success criteria, non-goals, decision boundaries, and references to any full source documents so downstream consumers receive a prompt-safe but faithful context
- Keep total prompt payloads within a safe budget by summarizing or trimming retained history; preserve newest/highest-signal answers and never let raw oversized context crowd out the current question
- Reduce user effort: ask only the highest-leverage unresolved question, and never ask the user for codebase facts that can be discovered directly
- For brownfield work, prefer evidence-backed confirmation questions such as "I found X in Y. Should this change follow that pattern?"
- Route facts before judgment in the Ouroboros style: before presenting a user-facing interview round, classify whether the needed information is a discoverable fact, a fact needing confirmation, or a human decision. The interview is with the human for judgment, not for facts the agent can inspect.
- When unresolved ambiguity depends on current external best practices, official/upstream guidance, standards, or version-aware behavior, gather bounded evidence with the tools that are allowed in the current environment and label it `[from-research]` before crystallizing requirements; if no such tool is allowed, record it as an assumption or ask the user.
- Use these transcript/spec labels only:
  - `[from-code][auto-confirmed]` — exact, high-confidence codebase facts from manifests/configs or direct source evidence, with no prescription attached.
  - `[from-code]` — codebase findings that are useful but inferred, pattern-based, or low/medium confidence and therefore need a confirmation-style user-facing round before being treated as settled.
  - `[from-research]` — externally sourced facts such as API limits, compatibility, or public documentation; facts only, not decisions.
  - `[from-user]` — goals, preferences, business logic, scope, non-goals, acceptance criteria, tradeoffs, and any decision-bearing interpretation.
- Treat `[from-code][auto-confirmed]` and other non-user fact discoveries as context/transcript updates, not interview rounds: do not ask the user about them, and do not increment the user-facing round number for facts the agent can safely establish.
- Auto-confirm only descriptive facts. If a finding implies what the new feature should do, which pattern it should follow, which tradeoff to accept, or what should stay in/out of scope, route the entire decision-bearing question to the user as `[from-user]` even when code or research facts are available.
- Ask every interview round as exactly one concise question in the chat (or the environment's native structured question UI if one exists), then stop and wait for the user's answer before scoring ambiguity or asking anything else
- Re-score ambiguity after each answer and show progress transparently
- Once ambiguity is at or below the active profile threshold, stop ordinary questioning. Run the practical closure audit: crystallize/handoff when readiness gates pass; otherwise ask only the final closure question needed to satisfy a named gate.
- Treat `max_rounds` as a stop cap, not evidence that more rounds are needed.
- Do not hand off to execution while ambiguity remains above threshold unless user explicitly opts to proceed with warning
- Do not crystallize or hand off while `Non-goals` or `Decision Boundaries` remain unresolved, even if the weighted ambiguity threshold is met
- Treat early exit as a safety valve, not the default success path
- Persist mode state for resume safety in `{run_dir}/state.json`; only the selected run's current writer updates it. Follow Run Scope and Resume below.
</Execution_Policy>

<Steps>

## Run Scope: select before writing

For a **new interview**, generate a fresh UUID as `interview_id` and reserve `.deep-interview/runs/{interview_id}/` with an exclusive directory creation operation (fail if it already exists). This is `run_dir`, relative to the actual project root. On a collision, generate another UUID; never merge into or clear an existing run. Use a fresh UUID even if the task slug or current chat is the same. If the host cannot create a separate run, report that persistence is unavailable; do not fall back to a shared state file.

For **resume**, select the existing run using the Resume section before Phase 0. Do not allocate or initialize a replacement run except for the explicit legacy import described there.

- Keep state, context snapshots, transcripts and specs inside this run. Do not maintain a shared `latest` pointer or write `.deep-interview/state.json`. Other runs may be read as relevant evidence; their answers and ownership are not automatically this interview's answers or ownership.
- Choose a unique `owner_id` for this conversation and keep it stable while writing this run. It is a coordination label, not proof of host-session identity or a permission grant. Before each update, re-read state and verify that its `interview_id` matches the directory and its owner is still this writer with status `held`. If identity changed, stop writing and resolve the handoff; do not overwrite the other writer's changes.
- All write targets must resolve inside the selected run; do not follow symlinks or saved artifact paths into another run. Save state as valid JSON, preserving prior rounds, by writing a unique temporary file in this run and replacing its own `state.json`. This prevents a partial JSON write, but is not a lock against two writers.
- When stopping or handing off, finish pending file writes before setting `owner_status` to `released` with `released_at`. Waiting for the next answer alone does not release ownership. An interrupted run may still say `held`; age, an ID or `active: false` alone does not prove that its previous writer stopped.

## Phase 0: Preflight Context Intake

1. Parse `{{ARGUMENTS}}` and derive a short task slug.
2. On resume, load the context snapshot recorded in this run's state. On a new interview, gather context for the new task; reuse an earlier snapshot only when clearly relevant, as read-only evidence with its source recorded. Do not select another interview merely because it is the newest or has the same slug.
3. Check whether the provided initial context or loaded snapshot is too large for safe prompt use. If it is oversized, the first interview round must ask for a concise prompt-safe summary instead of scoring ambiguity or continuing to downstream handoff.
4. If no snapshot exists, create a minimum context snapshot with:
   - Task statement
   - Desired outcome
   - Stated solution (what the user asked for)
   - Probable intent hypothesis (why they likely want it)
   - Known facts/evidence
   - Constraints
   - Unknowns/open questions
   - Decision-boundary unknowns
   - Likely codebase touchpoints
   - Relevant repo docs/rules/context inspected
   - Terminology or doc/code conflicts found
   - Prompt-safe initial-context summary status (`not_needed`, `needed`, or `recorded`)
5. For brownfield tasks, inspect the applicable documentation/rule surface before the first user-facing round. Prefer exact, nearby sources over broad scans:
   - governing `AGENTS.md` files and template/runtime instruction surfaces that apply to the touched paths
   - README/getting-started docs and relevant docs under `docs/`, especially contracts, plans, ADR-like records, and workflow docs
   - this run's context/spec artifacts and other clearly relevant interview or planning records as read-only evidence
   - project-local glossary/context files such as `CONTEXT.md`, `CONTEXT-MAP.md`, or context-specific docs when they exist
6. Save a new or refreshed snapshot to `{run_dir}/context/{slug}-{timestamp}.md` (UTC `YYYYMMDDTHHMMSSZ`) and reference it in mode state. Preserve earlier snapshots; add a unique suffix if the filename already exists. On resume, keep the recorded snapshot unless the context needs refreshing.

## Phase 1: Initialize

1. Parse `{{ARGUMENTS}}` and depth profile (`--quick|--standard|--deep`).
2. Detect project context:
   - Inspect the repository to classify **brownfield** (existing codebase target) vs **greenfield**.
   - For brownfield, collect relevant codebase context before questioning.
3. **New interviews only:** create `{run_dir}/state.json` without overwriting an existing file, using the reserved `interview_id` and current `owner_id`. On resume, preserve the existing rounds, scores, profile, gates and context instead of resetting this template. Fill threshold and max rounds from the selected profile.

```json
{
  "active": true,
  "current_phase": "deep-interview",
  "state": {
    "interview_id": "<uuid>",
    "owner_id": "<current writer uuid>",
    "owner_status": "held",
    "released_at": null,
    "profile": "quick|standard|deep",
    "type": "greenfield|brownfield",
    "initial_idea": "<user input>",
    "rounds": [],
    "current_ambiguity": 1.0,
    "threshold": 0.3,
    "max_rounds": 5,
    "challenge_modes_used": [],
    "codebase_context": null,
    "current_stage": "intent-first",
    "current_focus": "intent",
    "context_snapshot_path": "<run_dir>/context/<slug>-<timestamp>.md"
  }
}
```

4. Announce kickoff with profile, threshold, and current ambiguity. Show this interview's run path once so it can be resumed in another chat.

## Phase 2: Socratic Interview Loop

Repeat until ambiguity `<= threshold`, the pressure pass is complete, the readiness gates are explicit, the user exits with warning, or max rounds are reached. This is a stop condition: below threshold, do not open a new ordinary interview branch.

### 2a) Generate next question
If the initial context is oversized and no prompt-safe summary has been recorded yet, the next question must be only a summary request. Do not score ambiguity, do not run readiness gates, and do not hand off to planning or implementation until that summary answer is captured.

Use:
- Original idea
- Prior Q&A rounds
- Current dimension scores
- Brownfield context (if any)
- Doc/context grounding notes, including existing terminology, governing rules, and any doc/code mismatch
- Activated challenge mode injection (Phase 3)

Target the lowest-scoring dimension, but respect stage priority:
- **Stage 1 — Intent-first:** Intent, Outcome, Scope, Non-goals, Decision Boundaries
- **Stage 2 — Feasibility:** Constraints, Success Criteria
- **Stage 3 — Brownfield grounding:** Context Clarity (brownfield only)

Follow-up pressure ladder after each answer:
1. Ask for a concrete example, counterexample, or evidence signal behind the latest claim
2. Probe the hidden assumption, dependency, or belief that makes the claim true
3. Force a boundary or tradeoff: what would you explicitly not do, defer, or reject?
4. Challenge fuzzy or conflicting terms against the repo's documented language and current code behavior
5. Stress-test the boundary with one concrete scenario or edge case when a relationship or handoff remains ambiguous
6. If the answer still describes symptoms, reframe toward essence / root cause before moving on

Prefer staying on the same thread for multiple rounds when it has the highest leverage. Breadth without pressure is not progress.

Maintain a **Breadth Ledger** across independent ambiguity tracks: scope, constraints, outputs, verification, brownfield integration, and any user-mentioned deliverable tracks. The ledger is a guard, not a mandatory rotation rule: stay deep on the current thread until it has been pressure-tested, then zoom out only when another material track remains unresolved and would change execution.

Maintain a **Docs/Terminology Ledger** for brownfield interviews:
- repo docs/rules/context sources inspected, with path references
- canonical terms already used by the repo and terms to avoid or disambiguate
- user terms that conflict with docs or current code behavior
- doc/code mismatches that require a human decision before implementation
- optional durable-doc follow-ups that are safe to propose but not auto-apply

Detailed dimensions:
- Intent Clarity — why the user wants this
- Outcome Clarity — what end state they want
- Scope Clarity — how far the change should go
- Constraint Clarity — technical or business limits that must hold
- Success Criteria Clarity — how completion will be judged
- Context Clarity — existing codebase understanding (brownfield only)

`Non-goals` and `Decision Boundaries` are mandatory readiness gates. Ask about them early and keep revisiting them until they are explicit.

### 2b) Ask the question
Ask every interview round as exactly one question in the chat and wait for the answer. If the environment offers a native structured question UI, you may use it, but still one round at a time. Present:

```
Round {n} | Target: {weakest_dimension} | Ambiguity: {score}%

{question}
```

Question-shape guidance (kept from the original structured-question rules):
- Deep-interview is Socratic: ask one focused round at a time. Never combine multiple interview rounds into one message.
- **Single-answer rounds** — use when exactly one answer should drive the next branch, the options are mutually exclusive, or choosing more than one would blur the decision boundary (for example: choosing the primary failure mode, or which of several competing interpretations is correct). Present 2–4 numbered options and say "pick one".
- **Multi-answer rounds** — use when several options may all be true at once and you need a bounded set of coexisting constraints, non-goals, risks, or acceptance checks (for example: all out-of-scope items, all success metrics that must hold). Present numbered options and say "pick all that apply".
- If one selected option would immediately require a follow-up to disambiguate the others, prefer a single-answer round now and ask the follow-up next. Do not hide a branching interview tree inside one overloaded multi-answer round.
- Keep options bounded and concrete. Offer a free-text "other" only when the interview genuinely needs an answer that cannot be enumerated in advance.
- When you have a recommended answer, mark it, so the user can accept it with a short reply.
- Record the user's exact choice (and every selected item for multi-answer rounds) in the transcript/spec.

### 2c) Score ambiguity
Score each weighted dimension in `[0.0, 1.0]` with justification + gap.

Greenfield: `ambiguity = 1 - (intent × 0.30 + outcome × 0.25 + scope × 0.20 + constraints × 0.15 + success × 0.10)`

Brownfield: `ambiguity = 1 - (intent × 0.25 + outcome × 0.20 + scope × 0.20 + constraints × 0.15 + success × 0.10 + context × 0.10)`

Readiness gate:
- `Non-goals` must be explicit
- `Decision Boundaries` must be explicit
- A pressure pass must be complete: at least one earlier answer has been revisited with an evidence, assumption, or tradeoff follow-up
- A practical closure audit must pass: another question would change execution materially, not merely polish wording or chase a narrow edge case
- If either gate is unresolved, or the pressure pass is incomplete, continue below threshold only with a final closure question that names the unresolved gate and would materially change execution.
- Treat a low ambiguity score as permission to audit closure, not permission to keep drilling indefinitely. If remaining uncertainty would not change implementation, crystallize the spec instead of opening a new branch.
- If ambiguity is `<= 0.10`, another user-facing question is allowed only as that final closure question; otherwise crystallize immediately.

### 2d) Report progress
Show weighted breakdown table, readiness-gate status (`Non-goals`, `Decision Boundaries`), and the next focus dimension.

### 2e) Persist state
Append round result and updated scores to `{run_dir}/state.json` under Run Scope's single-writer procedure. Keep the same `interview_id` and run directory throughout this interview.

### 2f) Round controls
- Do not offer early exit before the first explicit assumption probe and one persistent follow-up have happened
- Apply a **Dialectic Rhythm Guard**: track consecutive non-user fact discoveries and confirmation-style answers (`[from-code][auto-confirmed]`, `[from-code]`, or `[from-research]`). After 3 consecutive non-user or confirmation answers, the next material user-facing round must solicit direct human judgment (`[from-user]`) unless the closure audit says the interview is ready to crystallize.
- Round 4+: allow explicit early exit with risk warning
- Soft warning at profile midpoint (e.g., round 3/6/10 depending on profile)
- Hard cap at profile `max_rounds`; never treat this cap as a desired interview length or quota

## Phase 3: Challenge Modes (assumption stress tests)

Use each mode once when applicable. These are normal escalation tools, not rare rescue moves:

- **Contrarian** (round 2+ or immediately when an answer rests on an untested assumption): challenge core assumptions
- **Terminologist** (brownfield, whenever a key term is fuzzy, overloaded, or conflicts with repo docs/code): force a canonical meaning against existing project language before implementation
- **Simplifier** (round 4+ or when scope expands faster than outcome clarity): probe minimal viable scope
- **Ontologist** (round 5+ and ambiguity > 0.25, or when the user keeps describing symptoms): ask for essence-level reframing

Track used modes in state to prevent repetition.

## Phase 4: Crystallize Artifacts

When threshold is met (or user exits with warning / hard cap):

1. Write interview transcript summary to:
   - `{run_dir}/interviews/{slug}-{timestamp}.md`
2. Write execution-ready spec to:
   - `{run_dir}/specs/deep-interview-{slug}.md`

Record the exact transcript and spec paths in this run's state and next-step handoff. Preserve earlier transcripts with a unique suffix if needed. A refined spec may update this run's own spec; it must not replace another run's spec with the same slug.

Spec should include:
- Metadata (profile, rounds, final ambiguity, threshold, context type)
- Context snapshot reference/path (for downstream planning reuse)
- Prompt-safe initial-context summary when oversized context was provided, plus references to any full source documents
- Clarity breakdown table
- Intent (why the user wants this)
- Desired Outcome
- In-Scope
- Out-of-Scope / Non-goals
- Decision Boundaries (what the agent may decide without confirmation)
- Constraints
- Testable acceptance criteria
- Assumptions exposed + resolutions
- Pressure-pass findings (which answer was revisited, and what changed)
- Brownfield evidence vs inference notes for any repository-grounded confirmation questions
- Docs/Terminology Ledger with inspected repo docs/rules/context, term conflicts, and any doc/code mismatch decisions
- Scenario/edge-case pressure findings that materially shaped scope or acceptance criteria
- Optional durable documentation recommendations, explicitly marked opt-in and public-safe; do not include raw private transcript dumps
- Technical context findings
- Full or condensed transcript

## Phase 5: Execution Bridge

Present the next-step options after artifact generation. Treat the deep-interview spec as the current requirements source of truth and preserve intent, non-goals, decision boundaries, acceptance criteria, docs/terminology grounding, and any residual-risk warnings across the handoff. Wait for the user's explicit choice.

### 1. **Plan first** (recommended when architecture/test-shape review is still needed)
- **Input Artifact:** This run's recorded `{run_dir}/specs/deep-interview-{slug}.md`
- **Consumer Behavior:** Do not repeat the interview. Propose structure options (input -> processing -> output), risks, and test shape around the clarified intent and boundaries, and let the user choose.
- **Best When:** Requirements are clear enough to stop interviewing, but the structure is not yet agreed.

### 2. **Implement in small steps**
- **Input Artifact:** This run's recorded `{run_dir}/specs/deep-interview-{slug}.md`
- **Consumer Behavior:** Turn the spec into the next single build instruction (this task only / input / output / constraints / done criteria with input, expected value and test command). Implement only after the user approves that instruction, one task at a time, with the spec's non-goals and decision boundaries as binding constraints.
- **Best When:** The clarified spec is already strong enough for direct implementation.

### 3. **Refine further**
- **Input Artifact:** Existing transcript, context snapshot, and current spec draft
- **Consumer Behavior:** Re-enter questioning to resolve the highest-leverage remaining uncertainty
- **Best When:** Residual ambiguity is still too high, the user wants stronger clarity, or the above-threshold / early-exit warning indicates too much risk to proceed cleanly

**Residual-Risk Rule:** If the interview ended via early exit, hard-cap completion, or above-threshold proceed-with-warning, explicitly preserve that residual-risk state in the handoff so the next step knows it inherited a partially clarified brief.

**IMPORTANT:** Deep-interview is a requirements mode. **Do NOT implement directly** inside deep-interview; start implementation only after the user explicitly chooses it.

</Steps>

<Tool_Usage>
- Inspect the repository (read files, search) for codebase fact gathering
- Ask each interview round as one plain chat question (or the native structured question UI if available) and wait for the answer
- Keep resumable mode state in `{run_dir}/state.json`; if a required question round cannot be asked, record `"active": false, "current_phase": "blocked"` there and release ownership after pending writes finish
- Read/write this run's context snapshots under `{run_dir}/context/`
- Read applicable repo docs/rules/context during preflight; write durable docs, glossary, ADR, or memory updates only when the user explicitly opts in and the content is public-safe
- Record whether the oversized-context summary gate is not needed, pending, or satisfied before any scoring or handoff step
- Save transcript/spec artifacts under `{run_dir}/interviews/` and `{run_dir}/specs/`
- This skill sets no model and changes no tool configuration
</Tool_Usage>

<Escalation_And_Stop_Conditions>
- User says stop/cancel/abort -> persist state, release this run after pending writes finish, and stop
- Ambiguity stalls for 3 rounds (+/- 0.05) -> force Ontologist mode once
- Max rounds reached -> proceed with explicit residual-risk warning
- All dimensions >= 0.9 -> allow early crystallization even before max rounds
</Escalation_And_Stop_Conditions>

<Final_Checklist>
- [ ] One run was selected before writing; its ID and current writer match state
- [ ] Preflight context snapshot exists under `{run_dir}/context/{slug}-{timestamp}.md`
- [ ] Oversized initial context, if present, has a prompt-safe summary recorded before ambiguity scoring or downstream handoff
- [ ] Ambiguity score shown each round
- [ ] Intent-first stage priority used before implementation detail
- [ ] Weakest-dimension targeting used within the active stage
- [ ] At least one explicit assumption probe happened before crystallization
- [ ] At least one persistent follow-up / pressure pass deepened a prior answer
- [ ] Challenge modes triggered at thresholds (when applicable)
- [ ] Transcript written to `{run_dir}/interviews/{slug}-{timestamp}.md`
- [ ] Spec written to `{run_dir}/specs/deep-interview-{slug}.md` and its exact path passed to the next step
- [ ] Brownfield questions use evidence-backed confirmation when applicable
- [ ] Brownfield preflight inspected applicable repo docs/rules/context before user-facing questions
- [ ] Fuzzy or conflicting terminology was challenged against repo language/current code behavior when applicable
- [ ] Scenario-based edge-case grilling was used when boundary ambiguity would materially affect implementation
- [ ] Durable docs/ADR/memory updates, if any, were explicitly opted into and public-safe
- [ ] Next-step options provided (Plan first / Implement in small steps / Refine further) and the user chose explicitly
- [ ] No direct implementation performed in this mode
</Final_Checklist>

<Advanced>
## Default settings

| Profile | Threshold | Max rounds |
|---|---|---|
| quick | 0.30 | 5 |
| standard (default) | 0.20 | 12 |
| deep | 0.15 | 20 |

Challenge modes are enabled by default. The user may override the profile in the request (for example "quick로 해").

## Resume

If interrupted, the user can ask to continue with the run path shown at kickoff or a clearly identified interview from this conversation.

1. Use that exact run. If the target is unclear, read candidate states without changing them and show short topic/round/owner summaries; ask which interview to resume. Do not choose by newest timestamp or slug alone, and do not initialize over an existing state.
2. Check the directory's `interview_id`, state and recorded artifact paths. If this is still the same conversation's known writer, retain its `owner_id`. A different conversation may take over only after the previous writer's release or stop has been confirmed. If it is active or uncertain, leave the run untouched and resolve the handoff with the user. For either a released run's same-writer resume or a confirmed transfer, re-read immediately before claiming it, set the current `owner_id`, `owner_status: held` and `released_at: null`, then resume ordinary updates. Do not let two chats knowingly take over the same run. This is coordination, not an automatic lock or OMX's runtime session validation.
3. Restore the selected run's profile, rounds, scores, gates and snapshots/spec. Continue from its recorded progress; do not repeat initialization or reset question counts. Apply a profile change only if the user requested it.
4. **Legacy records:** if the user wants to resume an old `.deep-interview/state.json`, first identify that interview and confirm its prior writer stopped. Allocate a fresh run, copy its progress and relevant context/transcript/spec into that run, give it the new directory's ID and current owner with `owner_status: held` and `released_at: null`, and rewrite artifact paths to the copied files. Preserve the legacy source paths/old ID as provenance, not as write targets or ownership proof. Keep the old files unchanged. If a referenced artifact is missing, mark that gap and resolve it rather than selecting some other interview's newest file.
</Advanced>
