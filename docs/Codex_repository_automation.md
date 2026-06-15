# Codex repository automation

This note defines how Codex or similar coding agents may support the civic design intelligence repository.

For operational instructions that Codex should follow before editing, see `AGENTS.md`.

## Purpose

Codex may be used to help maintain the repository infrastructure around research knowledge.

It should support consistency, traceability and safe repository operation. It should not replace human judgement about research meaning, evidence maturity, review status or validation.

## Appropriate uses

Appropriate uses include:

- repository health checks
- schema and metadata consistency checks
- validation scripts
- index generation
- GitHub Pages statistics
- small administrative migrations
- pull request summaries
- repeatable research intake scaffolding

These tasks support the repository operating model without making Codex the authority on research interpretation.

## Where Codex should not be used unsupervised

Codex should not independently:

- rewrite user needs
- merge civic needs
- mark anything as validated
- decide that pain points are resolved
- remove duplicate objects without preserving supersession logic
- turn messy research into polished insights without traceability
- collapse uncertainty into confident claims

These are semantic research operations, not just coding operations.

## Main value

Codex could help move the repository from a manually maintained research repository to a semi-operational knowledge system.

The biggest gains are:

- less manual repository hygiene
- faster schema evolution
- safer migrations
- better GitHub Pages demos
- clearer pull request summaries
- repeatable research intake
- stronger consistency without heavy governance

## Working principle

Codex should maintain the infrastructure of meaning, not become the source of meaning.

Human review remains responsible for interpretation, evidence maturity, lifecycle decisions and validation.

Where Codex proposes or makes a material semantic change, the work may need an LLM intervention log and possibly an object change log.

## Required operating pattern

Codex should follow the repository branch and pull request workflow.

Before editing, Codex should:

1. Check the current branch and working tree status.
2. Create a focused `codex/*` branch if the checkout is on `main`.
3. Identify unrelated local changes and leave them untouched.
4. Read the relevant governance, schema, changelog and review guidance.
5. Decide whether the change is repository infrastructure, research content or both.

Before opening a pull request, Codex should:

1. Update `CHANGELOG.md` for repository-wide governance, template, validation, workflow, index or automation changes.
2. Use object-level changelogs only when research-object interpretation, evidence basis, maturity, review state or relationships change.
3. Use LLM intervention logs only for material semantic risk, following `docs/LLM_intervention_logging.md`.
4. Run the relevant validation checks.
5. Write the pull request body using the compliance checklist in `.github/pull_request_template.md`.

This makes Codex work reviewable by default and prevents administrative repository changes from being mixed silently with research interpretation changes.
