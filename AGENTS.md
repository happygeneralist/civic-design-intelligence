# Codex Instructions

These instructions apply to Codex and other LLM coding agents working in this repository.

## Start-of-work checks

Before editing files:

1. Read `CONTRIBUTING.md`, `GOVERNANCE.md`, `llm-instructions.md` and any task-relevant docs.
2. Check the current branch and working tree status.
3. If on `main`, create a focused `codex/*` branch before making changes.
4. Identify unrelated local changes and leave them untouched.
5. Confirm whether the work changes research meaning, repository infrastructure or both.
6. For non-trivial work, check whether there is a linked issue before editing. If there is no issue, ask whether one should be created first.

Typo fixes and tiny obvious edits do not need an issue. Use an issue when work is likely to touch multiple files, affect repository conventions, templates, roadmap, evidence handling, object meaning or validation, or needs clear scope boundaries.

Issues should define the purpose, scope, out of scope items and acceptance criteria for the work. Git remains the technical audit trail for edits; issues are for work definition, sequencing and prioritisation, not edit history.

## Needs and civic intelligence

For discovery, formulation, decomposition, relationship analysis or generated needs views, read `docs/Needs_semantic_contract.md`, `docs/User_needs_writing_rules.md` and the current `docs/Roadmap_cursor.md` before acting. The contract clarifies older guidance that implies small output quotas, one strict needs hierarchy, mandatory context in every sentence or validation before exploratory use.

Build useful, revisable candidate knowledge, not perfect sentences. Bound a run's source scope and execution effort, not the number of needs a source is allowed to reveal. Record tensions, alternatives and omissions. Keep source evidence distinct from inferred hypotheses, and expose higher-level human experience, capabilities and rights without inventing their applicability.

Preserve stable IDs and current formulations. Short labels, user-facing text and value views are role-specific affordances, not opportunities to regenerate a different need on every query. Retain useful parents when decomposing; do not automatically deprecate them. Keep context and pain identifiable without forcing them into the statement.

CDI owns knowledge semantics and objects. AI Capability Layer owns the reusable skill, reviewer interface and execution/evaluation tooling. Do not build a parallel review application here or move private evidence into public CDI. Do not treat an LLM check or a passing validator as independent human validation or legal approval.

## Branch and pull request workflow

LLM-assisted changes should happen on a branch and be reviewed through a pull request.

Use focused branches, for example:

```text
codex/template-metadata-hygiene
codex/obsidian-gitignore-bases-hygiene
codex/codex-workflow-guardrails
```

Do not commit directly to `main`.

Do not stage unrelated local changes.

Default to draft pull requests unless the user explicitly asks for a ready-for-review PR.

## Changelog rules

Use the lightest audit record that preserves meaning and accountability.

- Repository-wide changes belong in `CHANGELOG.md`.
- Template, schema, validation, governance, workflow, index and automation changes usually need a `CHANGELOG.md` entry.
- Research-object semantic changes belong in the object's `## Changelog`.
- Formatting, metadata hygiene and administrative migrations usually rely on Git history and the pull request summary unless they affect interpretation.
- Material LLM semantic changes may need an object changelog and an LLM intervention log. Follow `docs/LLM_intervention_logging.md`.

## Research safety rules

Codex must not independently:

- mark anything as reviewed or validated
- upgrade evidence strength or confidence on research objects
- rewrite participant evidence except for explicit anonymisation work
- remove caveats or uncertainty
- merge, split, supersede or deprecate research objects without preserving the review trail
- treat LLM-generated text as evidence

If research meaning changes, keep the item as draft, assumption or needs review unless a human reviewer has explicitly completed the review.

## Pull request body requirements

Every Codex PR should say:

- what changed
- why it changed
- whether research content changed
- whether validated notes changed
- whether assumptions were introduced
- whether evidence links changed
- whether status, analysis state, evidence strength or confidence changed
- whether any objects were split, merged, superseded or deprecated
- whether LLMs generated or materially shaped content
- what changelog or LLM intervention log was used
- what validation was run
- what needs human review

## Validation

Run the most relevant validation before committing.

For ordinary repository work, run:

```bash
python3 tools/validate_repository.py
```

For template work, also run:

```bash
python3 tools/validate_repository.py --include-templates
```

For validator changes, run its regression tests. Report error and warning counts in the pull request. Distinguish tests actually executed from prepared cases, and structural validity from research reliability.
