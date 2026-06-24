# Roadmap cursor

Last updated: 2026-06-23

This cursor records the current operational focus for the repository.

It is intentionally shorter than the full roadmap. Use it to decide what to do next, what to avoid overbuilding, and when the roadmap has moved to a new phase.

## Current phase

The repository is moving from structural normalisation into safe-enough, non-linear research ingestion.

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
- first bounded primary-research ingestion slice from `RS_002` / `EVID_003` has been merged and reviewed as safe enough to continue cautiously
- public roadmap and changelog communication page has been added so progress can be shared without creating another research dependency
- non-linear ingestion guidance now documents how partially structured research knowledge can enter before full traceability is complete

The system is ready to continue using real research, provided ingestion includes reconciliation with existing objects and does not become unreviewed object dumping.

## Active focus

The next focus is:

```text
Use the repository on SEND pathway-planning research inputs while supporting non-linear capture, backward evidence-linking and reconciliation against the existing object landscape.
```

This means:

- continue ingestion because captured and draft objects have value before maturity
- recognise that knowledge may enter as evidence, source material, need-shaped input, workshop output, collaborator observation, research summary or candidate object
- keep traceability as the preferred state without blocking useful capture when provenance is incomplete
- make gaps in evidence linkage, provenance, confidence or review state visible
- generate full ingestion slices from partially structured inputs rather than copying them directly into canonical folders
- compare candidate objects with existing user needs, civic needs, behaviours, pain points, insights, themes and evidence before finalising a PR
- use conservative metadata where provenance, interpretation or object boundaries remain uncertain
- use `short_name` and ID-prefixed readable filenames at creation time
- distinguish lived-experience needs from service, organisation and locality context
- preserve where evidence came from without treating the first observed context as the permanent boundary of a need
- treat public secondary research as source material that should be broken into source records and selected evidence extracts before it supports needs, pain points or insights where possible
- keep the structured intelligence graph in this repository, while using `civic-design-secondary-research` for raw or lightly processed public sources where useful
- update companion `evidence-map.md` files when source records, evidence objects or analysis objects are created from archived sources
- leave unresolved or immature material in `000_Inbox/` when it cannot yet be responsibly reconciled
- avoid marking anything reviewed or validated unless human review has happened

Use `docs/Non_linear_research_ingestion.md` as the current operating guide for this phase.

## Current ingestion emphasis

During the next research breakdown, test whether the repository can connect evidence, user needs, behaviours, pain points, civic needs and insights into a coherent problem-space graph.

Pay particular attention to:

- treating ingestion as extraction plus reconciliation, not extraction alone
- preserving user-need wording from the person's perspective while recognising functional, emotional, social, relational, experiential and civic-adjacent needs
- following `docs/User_needs_writing_rules.md` when deriving or refining candidate user needs
- avoiding solution-shaped user needs
- not flattening emotional or social needs into functional task language where that changes meaning
- checking neighbouring objects before creating new user needs, behaviours or pain points
- treating severity, scope and lifecycle judgements as relative where they depend on comparison with existing objects
- capturing policy, service, organisation and locality as context or external reference, not as the framing of the need
- identifying where generic `related_*` links are not expressive enough
- noting candidate relationship types that may be useful later, such as `blocked_by`, `supports`, `evidenced_by`, `challenged_by`, `local_variant_of` or `addressed_by`
- observing where a user need may be a context-specific expression of a wider reusable need pattern
- watching where small wording changes alter the solution vector or outcome strategy
- treating personas, segments and journey maps as generated or contextual views over evidence-backed objects, not as fixed canonical artefacts too early
- creating civic needs only where the evidence points to institutional obligation, equity, access, rights, accountability or public value

## Immediate next actions

1. Use the non-linear ingestion guidance as the operating model for the next ingestion work.
2. Use existing quote evidence and partially structured need-shaped research summaries to create a few more ingestion slices.
3. For each slice, produce reconciliation notes before finalising the PR.
4. Check candidate user needs against `docs/User_needs_writing_rules.md` and nearby existing user needs.
5. Identify where existing objects should be linked, updated, split, merged, superseded or left unchanged.
6. Record unresolved provenance or evidence-linking questions rather than pretending they are solved.
7. If using the Essex Ofsted Area SEND report, create a matching source record in this repository for `SRC_001_ofsted_essex_area_send_inspection_jan_2026`.
8. During future ingestion, watch for service, organisation and locality context without creating a full taxonomy yet.
9. If using an Ofsted report or other secondary source, create a source record first, then selected evidence extracts, then derived analysis objects where possible.
10. Update the companion source `evidence-map.md` after structured objects are created.
11. Note any object relationships that need more precision than generic `related_*` links, but do not change the schema until real examples show the smallest useful convention.
12. Note any candidate need patterns, solution-vector sensitivity or segmentation dimensions that appear during ingestion, but do not add required fields until examples stabilise.
13. Review future ingestion PRs to see which template, context, secondary-evidence, relationship, need-pattern, persona/journey or validation changes are genuinely needed.

## Guardrails for the next PRs

For the next few PRs:

- keep PRs small and reviewable
- do not do another broad filename migration unless validation or Obsidian use reveals a concrete problem
- do not add strict validator checks before the ingestion workflow has been tested
- do not create a large change-event system before there are real semantic-change examples
- do not build an API/database layer yet
- do not build automated cross-repository sync yet
- do not force loose research into canonical folders too early
- do not require linear source-to-evidence-to-object ordering when the work starts from partially structured knowledge
- do not copy need-shaped inputs directly into first-class objects without an ingestion and reconciliation step
- do not encode service ownership, department names or locality into canonical need wording unless the evidence shows the need is inherently specific to that service or place
- do not import large public reports or raw document corpora into this repository
- do not treat report findings or inspection summaries as validated user needs without further review
- do not enforce typed relationships before there are enough real ingestion examples to justify the minimum useful vocabulary
- do not create canonical personas or fixed journey maps before the underlying evidence, needs, behaviours, pain points and contexts are mature enough to support them
- do not introduce a required need-pattern schema before reusable patterns have been tested through real object examples

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
- dedicated need-pattern object type
- formal causal or theory-of-change layer

## Decision rule

When deciding what to do next, prefer work that helps answer:

- Can we break real research and partially structured knowledge into defensible structured objects?
- Can we preserve evidence, uncertainty and review state?
- Can we work backwards from useful knowledge to source and evidence links without overclaiming?
- Can Obsidian users navigate and query the repository easily?
- Can LLM-assisted work create useful ingestion slices without semantic drift, object sprawl or naming debt?
- Can the repository distinguish evidence origin from need applicability?
- Can locally observed needs later become wider cross-service or cross-locality patterns without losing provenance?
- Can public secondary research be used as traceable evidence without turning the repository into a raw document archive?
- Can companion source archive references and evidence maps make cross-repository provenance reviewable?
- Can the repository remain Markdown-first while preparing for future data/API use?
- Can the repository identify where future graph-ready relationship types are needed without overbuilding the schema now?
- Can the repository identify reusable need patterns without flattening situated needs?
- Can the repository show when need wording changes the solution vector and outcome strategy?
- Can personas, segments and journeys be generated from evidence-backed objects rather than becoming stale static artefacts?

If a proposed change does not help with those questions, defer it.

## Next review point

Review this cursor after two or three non-linear ingestion slices using existing quote evidence and partially structured need-shaped research summaries.

At that point, decide whether the next step should be:

- template updates
- validator tightening
- Obsidian dashboard improvements
- change-event scaffolding
- more research ingestion
- lightweight context fields for locality, service areas or organisation mappings
- lightweight source and evidence fields for secondary research ingestion
- lightweight relationship-type conventions based on real object examples
- need-pattern conventions based on real object examples
- segmentation and generated-view guidance for personas and journeys
- cross-repository source inventory or evidence-map checks
