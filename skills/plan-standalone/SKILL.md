---
name: plan-standalone
description: "Create concise, actionable implementation plans with optional requirements interviews or plan review. Use when the user wants a plan before implementation or an evaluation of an existing plan."
---

# Plan (standalone)

Adapted from the MIT-licensed oh-my-codex `plan` skill. See [LICENSE](LICENSE).
This skill uses the host's file, conversation, and optional subagent tools; it does not require an OMX runtime or other installed skills.

<Purpose>
Plan creates concise, actionable work plans. Auto-detect interview vs direct mode; support `--interview` for Socratic clarification and `--review` for evaluation.
</Purpose>

<Use_When>
- Planning before implementation — "plan this", "let's plan"
- Requirements are vague and need scoping — use `--interview`
- Reviewing an existing plan — use `--review`
</Use_When>

<Do_Not_Use_When>
- The user wants direct execution of a scoped task — use the host's ordinary implementation workflow
- A simple focused fix has obvious scope — skip planning
</Do_Not_Use_When>

<Execution_Policy>
- Auto-detect interview vs direct; `--interview` forces clarification and `--direct` skips the interview.
- Reuse requirements and decisions already provided in the conversation or an interview specification; do not ask the user to repeat them.
- Ask one question at a time. Gather codebase facts with normal file/search tools before asking informed follow-ups.
- Plans must be evidence-backed: aim for 80%+ of codebase claims citing actual file/line evidence and 90%+ of acceptance criteria being testable. For new work, distinguish proposed paths and assumptions from existing evidence; never invent files, lines, or test results.
- Right-size steps to scope; save plans to `.plan/` in the user's project directory.
- Keep explanations concise and use the user's language.
- Planning may inspect the project and write planning artifacts. It does not itself implement the plan. An explicit implementation request ends planning and continues through the host's ordinary workflow within that request's scope.
</Execution_Policy>

<Steps>

### Mode Selection

| Mode | Trigger | Behavior |
|------|---------|----------|
| Interview | `--interview` or a broad request with unclear requirements | Socratic requirements gathering |
| Direct | `--direct` or a sufficiently detailed request | Generate a plan immediately |
| Review | `--review` | Evaluate an existing plan |

### Interview (`--interview`)
1. Classify the request and inspect relevant project facts.
2. Ask one focused question using the host's structured user-input tool when available, otherwise ordinary chat. Wait for the answer before the next question.
3. Build on the answers and check for hidden requirements; optionally consult an analysis subagent if available and useful.
4. Create the plan when requirements are clear or the user signals readiness. Do not prolong the interview once enough is known to plan.

### Direct (`--direct`)
1. Perform a quick analysis of the supplied requirements and relevant project evidence; an analysis subagent is optional.
2. Generate the plan immediately. State unresolved assumptions and decision points without starting an interview.
3. Review the plan critically if requested.

### Review (`--review`)
1. Read the supplied plan or the clearly identified relevant plan in `.plan/`. If the target cannot be determined, ask which plan to review.
2. Evaluate clarity, evidence, testability, risks, and verification steps. Return `APPROVED`, `REVISE`, or `REJECT`, with concrete reasons and needed changes.
3. Prefer an independent reviewer subagent when available, especially if the current agent wrote the plan. Provide the full plan and relevant evidence. Whenever no independent reviewer actually performs the review, explicitly label the result as self-review; do not claim independent approval.

### Output

Every plan includes:
- Requirements Summary
- Acceptance Criteria (testable)
- Implementation Steps (with relevant file references; adaptive count)
- Risks and Mitigations
- Verification

Use natural section names in the user's language. Save to `.plan/{task-slug}.md` and give the user a short summary and the file path. Preserve unrelated plans; if writing is unavailable, provide the full plan in the conversation and disclose that it was not saved.

For review, report the verdict and findings without silently rewriting the original plan. Save a review alongside the plan when possible.

If the user says `continue`, continue the current branch rather than restarting. Apply newer task updates without discarding earlier, still-relevant decisions.

</Steps>

<Tool_Usage>
- Use available file/search tools for project facts.
- Use structured user input or ordinary chat for interview questions.
- Use analysis or reviewer subagents when useful and available; their absence does not prevent ordinary planning.
</Tool_Usage>

<Escalation_And_Stop_Conditions>
- Stop interviewing when requirements are clear — do not over-interview.
- Surface irreconcilable trade-offs that require a user decision. In direct mode, mark them as unresolved rather than choosing silently.
- "Just do it" / "skip planning" ends planning and routes the scoped request to the host's ordinary implementation workflow; do not invoke another skill automatically.
- After delivering a plan or review, stop unless the user has also requested implementation or another follow-up.
</Escalation_And_Stop_Conditions>

<Final_Checklist>
- [ ] Acceptance criteria are testable (90%+ concrete).
- [ ] Codebase claims have file/line evidence where applicable (80%+).
- [ ] Proposed files and assumptions are distinguished from existing facts.
- [ ] Risks have mitigations rather than vague labels.
- [ ] The plan is saved to `.plan/`, or a saving limitation is disclosed.
</Final_Checklist>

<Advanced>

## Question Classification

| Type | Examples | Action |
|------|----------|--------|
| Codebase Fact | "Where is X?" | Inspect first; do not ask the user to locate it |
| User Preference | "Priority?" | Ask in interview mode; state assumptions or open decisions in direct mode |
| Scope Decision | "Include Y?" | Ask in interview mode; mark unresolved scope in direct mode |

## Review Quality Criteria

| Criterion | Standard |
|-----------|----------|
| Clarity | 80%+ of applicable codebase claims cite file/line evidence |
| Testability | 90%+ of criteria are concrete |
| Verification | Referenced existing files exist; proposed files are labeled; checks have observable outcomes |

</Advanced>
