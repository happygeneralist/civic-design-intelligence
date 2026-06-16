# Roadmap cursor

Last updated: 2026-06-16

This cursor records the current operational focus for the repository.

It is intentionally shorter than the full roadmap. Use it to decide what to do next, what to avoid overbuilding, and when the roadmap has moved to a new phase.

## Current phase

The repository is moving from structural normalisation into safe research ingestion.

Recent work has largely completed the first naming and file-structure stabilisation pass:

- core filename conventions are now clearer
- early user needs have been cleaned up and renamed
- readable filenames now preserve stable IDs
- Obsidian use has been prioritised through readable names, aliases and links
- frontmatter is being treated as the future data/API contract
- LLM handling rules have been strengthened so future AI-assisted work should not recreate naming debt
- Obsidian workflow and validation docs now point contributors to the naming contract

The system is close enough to start using it with real research again.

## Active focus

The next focus is:

```text
Use the repository on a bounded SEND pathway-planning research sample without creating new naming, metadata or evidence-maturity debt.
```

This means:

- start with a small sample
- create only useful evidence-derived objects
- use conservative metadata
- preserve links to evidence
- use `short_name` and ID-prefixed readable filenames at creation time
- leave uncertain material in `000_Inbox/`
- avoid marking anything reviewed or validated unless human review has happened

## Immediate next actions

1. Select one bounded SEND pathway-planning research source or extract for ingestion.
2. Create a small ingestion PR with evidence, candidate needs, behaviours and pain points.
3. Review the ingestion PR to see which template or validation changes are genuinely needed.

## Guardrails for the next PRs

For the next few PRs:

- keep PRs small and reviewable
- do not do another broad filename migration unless validation or Obsidian use reveals a concrete problem
- do not add strict validator checks before the ingestion workflow has been tested
- do not create a large change-event system before there are real semantic-change examples
- do not build an API/database layer yet
- do not force loose research into canonical folders too early

## Things that can wait

These are important, but not next:

- strict validator enforcement for all naming and link rules
- full change-event folder and logging system
- pain point recurrence fields across all pain points
- generated journeys or prototypes
- opportunity pipeline
- persona or segment modelling
- API/database implementation
- cross-government taxonomy expansion

## Decision rule

When deciding what to do next, prefer work that helps answer:

- Can we break real research into defensible structured objects?
- Can we preserve evidence, uncertainty and review state?
- Can Obsidian users navigate and query the repository easily?
- Can LLM-assisted work create useful objects without semantic drift or naming debt?
- Can the repository remain Markdown-first while preparing for future data/API use?

If a proposed change does not help with those questions, defer it.

## Next review point

Review this cursor after the first bounded safe-ingestion PR.

At that point, decide whether the next step should be:

- template updates
- validator tightening
- Obsidian dashboard improvements
- change-event scaffolding
- more research ingestion
