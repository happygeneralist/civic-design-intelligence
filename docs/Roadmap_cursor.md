# Roadmap cursor

Last updated: 2026-06-17

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
- companion public secondary-research repository now exists: `happygeneralist/civic-design-secondary-research`
- first companion source archive example now exists: `SRC_001_ofsted_essex_area_send_inspection_jan_2026`
- first bounded primary-research ingestion slice from `RS_002` / `EVID_003` has been merged and is paused for team review
- public roadmap and changelog communication page has been added so progress can be shared without creating another research dependency

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
- distinguish lived-experience needs from service, organisation and locality context
- preserve where evidence came from without treating the first observed context as the permanent boundary of a need
- treat public secondary research as source material that must be broken into source records and selected evidence extracts before it supports needs, pain points or insights
- keep the structured intelligence graph in this repository, while using `civic-design-secondary-research` for raw or lightly processed public sources where useful
- update companion `evidence-map.md` files when source records, evidence objects or analysis objects are created from archived sources
- leave uncertain material in `000_Inbox/`
- avoid marking anything reviewed or validated unless human review has happened

## Current ingestion emphasis

During the next research breakdown, test whether the repository can connect evidence, user needs, behaviours, pain points, civic needs and insights into a coherent problem-space graph.

Pay particular attention to:

- preserving pure user-need wording from the person's perspective
- capturing policy, service, organisation and locality as context or external reference, not as the framing of the need
- identifying where generic `related_*` links are not expressive enough
- noting candidate relationship types that may be useful later, such as `blocked_by`, `supports`, `evidenced_by`, `challenged_by`, `local_variant_of` or `addressed_by`
- creating civic needs only where the evidence points to institutional obligation, equity, access, rights, accountability or public value

## Immediate next actions

1. Review and use the MVP public roadmap and changelog page as the current non-dependent communication slice.
2. Review the first bounded primary-research ingestion slice with the team before adding more research objects.
3. Select the next bounded SEND pathway-planning source or extract after team feedback.
4. If using the Essex Ofsted Area SEND report, create a matching source record in this repository for `SRC_001_ofsted_essex_area_send_inspection_jan_2026`.
5. During future ingestion, watch for service, organisation and locality context without creating a full taxonomy yet.
6. If using an Ofsted report or other secondary source, create a source record first, then selected evidence extracts, then derived analysis objects.
7. Update the companion source `evidence-map.md` after structured objects are created.
8. Note any object relationships that need more precision than generic `related_*` links, but do not change the schema until real examples show the smallest useful convention.
9. Review future ingestion PRs to see which template, context, secondary-evidence, relationship or validation changes are genuinely needed.

## Guardrails for the next PRs

For the next few PRs:

- keep PRs small and reviewable
- do not do another broad filename migration unless validation or Obsidian use reveals a concrete problem
- do not add strict validator checks before the ingestion workflow has been tested
- do not create a large change-event system before there are real semantic-change examples
- do not build an API/database layer yet
- do not build cross-repository sync yet
- do not force loose research into canonical folders too early
- do not encode service ownership, department names or locality into canonical need wording unless the evidence shows the need is inherently specific to that service or place
- do not import large public reports or raw document corpora into this repository
- do not treat report findings or inspection summaries as validated user needs without further review
- do not enforce typed relationships before there are enough real ingestion examples to justify the minimum useful vocabulary

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
- full locality, service-area or organisation taxonomy
- full source ontology for public secondary research
- automated ingestion of secondary research corpora
- automated cross-repository source or roadmap sync
- enforced typed-relationship schema

## Decision rule

When deciding what to do next, prefer work that helps answer:

- Can we break real research into defensible structured objects?
- Can we preserve evidence, uncertainty and review state?
- Can Obsidian users navigate and query the repository easily?
- Can LLM-assisted work create useful objects without semantic drift or naming debt?
- Can the repository distinguish evidence origin from need applicability?
- Can locally observed needs later become wider cross-service or cross-locality patterns without losing provenance?
- Can public secondary research be used as traceable evidence without turning the repository into a raw document archive?
- Can companion source archive references and evidence maps make cross-repository provenance reviewable?
- Can the repository remain Markdown-first while preparing for future data/API use?
- Can the repository identify where future graph-ready relationship types are needed without overbuilding the schema now?

If a proposed change does not help with those questions, defer it.

## Next review point

Review this cursor after the first bounded safe-ingestion PR.

At that point, decide whether the next step should be:

- template updates
- validator tightening
- Obsidian dashboard improvements
- change-event scaffolding
- more research ingestion
- lightweight context fields for locality, service areas or organisation mappings
- lightweight source and evidence fields for secondary research ingestion
- lightweight relationship-type conventions based on real object examples
- cross-repository source inventory or evidence-map checks
