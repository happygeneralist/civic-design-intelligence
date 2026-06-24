# Source capture workflow

This document describes how source material should be captured, referenced and prepared for ingestion.

It should be read alongside:

- `docs/Input_and_evidence_classification.md`
- `docs/Ingestion_slice_workflow.md`
- `docs/Non_linear_research_ingestion.md`
- `docs/Secondary_research_ingestion.md`
- `docs/Safe_research_ingestion_MVP.md`

## Purpose

Source capture is the step before evidence extraction and object creation.

It helps the repository:

- preserve provenance
- separate raw or lightly processed material from structured intelligence
- make public secondary sources reviewable
- avoid importing large raw document corpora into the intelligence repository
- support later evidence extraction and ingestion slices
- prepare for future automation without automating interpretation

## Core rule

```text
Capture sources so they can be reviewed. Do not treat source capture as evidence interpretation.
```

A captured source is not a user need, pain point, behaviour, civic need or insight.

A source may later support selected evidence extracts. Those extracts may then support or challenge derived objects.

## Repository split

Use the two repositories differently.

```text
civic-design-secondary-research
→ raw or lightly processed public source material
→ source-level documentation
→ candidate extracts or notes
→ evidence-map.md references back to structured objects

civic-design-intelligence
→ source records
→ research-study records
→ selected evidence extracts
→ structured knowledge objects
```

Do not use the intelligence repository as a bulk document archive.

## Known trade-offs and risks

This split is intended to keep the intelligence repository focused and reviewable, but it has costs.

### Cross-repository overhead

Using two repositories means source material and structured intelligence can drift apart.

Long-term risk:

- source folders may exist without matching source records
- source records may point to missing or renamed archive folders
- evidence maps may become stale
- reviewers may need to open multiple repositories to understand provenance

Mitigation:

- use stable source IDs
- keep evidence maps lightweight
- add future checks for missing or broken cross-repository references
- avoid creating source folders unless they are likely to support evidence or ingestion work

### Evidence-map duplication

Evidence maps are useful navigation aids, but they can duplicate information already held in source records, evidence objects, PRs and backlinks.

Long-term risk:

- evidence maps become another manual place to update
- contributors may treat evidence maps as canonical history
- stale maps may reduce trust in provenance

Mitigation:

- treat evidence maps as navigational summaries, not the source of truth
- keep them short
- use them where cross-repository provenance needs to be reviewable
- rely on Git and object links for detailed history

### Source capture can become a dumping ground

A source archive can gradually become a place where material is stored because it might be useful someday.

Long-term risk:

- source volume grows faster than ingestion capacity
- important sources become hard to find
- the archive creates a false sense that evidence has been analysed
- maintenance work increases without improving intelligence

Mitigation:

- capture sources because they support a likely evidence, sensemaking or ingestion workflow
- do not archive material just because it exists
- use source-capture PR notes to say why the source was captured
- review orphaned sources later if they are never used

### Selected extraction can introduce bias

The workflow deliberately avoids extracting everything. That keeps the system lightweight, but it introduces selection risk.

Long-term risk:

- extracts may over-represent striking examples
- quieter or contradictory evidence may be missed
- later users may mistake selected extracts for the full source picture

Mitigation:

- record why extracts were selected
- preserve source location where possible
- allow evidence relationships such as `limits`, `challenges` and `contradicts`
- use review to ask what important evidence may have been left out

### Public secondary sources can dominate lived experience

Public reports and inspections are easier to capture than primary lived-experience research.

Long-term risk:

- institutional voice may outweigh direct lived experience
- report findings may shape user need wording too strongly
- secondary-source availability may distort the apparent evidence base

Mitigation:

- classify evidence voice before decomposition
- do not create user needs directly from public reports
- distinguish institutional framing from lived-experience evidence
- use secondary sources to support, contextualise or challenge objects rather than automatically validate them

### Markdown-first workflows may limit future scale

Markdown and Git make the work transparent and reviewable, but they are not the final product architecture.

Long-term risk:

- cross-repository linking may become hard to query
- evidence maps may not scale
- public or partner contribution may need interfaces that non-technical contributors can use
- future automation may need a more explicit data contract

Mitigation:

- keep frontmatter consistent enough for future export
- avoid hiding meaning only in prose
- keep source IDs stable
- introduce automation and data/API layers only after real examples show the minimum useful structure

### Conservative interpretation can slow throughput

The workflow deliberately avoids automatic validation and premature object creation.

Long-term risk:

- ingestion may remain slower than desired
- too much material may sit in partial states
- reviewers may become bottlenecks

Mitigation:

- automate low-risk capture, mapping and checks first
- use guided contributor workflows later
- reserve human review for semantic risk, object boundaries, review status and public accountability
- accept that some partial knowledge is useful if its limits are visible

## When to capture a source

Capture a source when it is likely to be used as evidence, context or provenance for future analysis.

Common examples:

- public inspection reports
- government guidance
- local authority strategies
- parliamentary reports
- charity or third-sector reports
- research publications
- evaluation reports
- public datasets
- uploaded source files that need later extraction
- primary research transcripts, where safe and appropriate
- workshop or collaborator materials that need provenance

Do not capture a source just because it exists. Capture it because it supports a likely evidence, sensemaking or ingestion workflow.

## Source types

### Public secondary source

Examples:

- Ofsted area SEND inspection report
- government consultation response
- statutory guidance
- published local authority strategy
- charity report
- parliamentary committee report

Preferred route:

```text
public source
→ source folder in civic-design-secondary-research where useful
→ source metadata
→ evidence-map.md stub
→ source record in civic-design-intelligence
→ selected evidence extracts
→ ingestion slice
```

### Primary research source

Examples:

- interview transcript
- observation notes
- workshop notes
- survey free-text export

Preferred route:

```text
primary research source
→ research-study record or source record
→ anonymised selected evidence extracts
→ candidate objects
→ reconciliation
```

Primary research may need stricter privacy and consent handling. Do not add raw sensitive material to public repositories.

### Collaborator or partner material

Examples:

- third-sector submission
- practitioner note
- parent forum summary
- collaborator briefing
- review comment with evidence

Preferred route:

```text
collaborator material
→ source or contribution note
→ provenance and role context
→ selected evidence or candidate object interpretation
→ review
```

Preserve who the material represents and whether it is direct experience, professional interpretation, synthesis or hearsay.

### Generated or LLM-assisted source material

Examples:

- LLM-generated summaries
- LLM-assisted extraction notes
- generated candidate need lists

Preferred route:

```text
LLM-assisted material
→ input or working note
→ classify as LLM-assisted synthesis
→ link to underlying sources where possible
→ review before creating or changing objects
```

Generated material should not be treated as source evidence unless it is clearly derived from source material and the source trail is visible.

## Minimal source capture package

For a public secondary source, the useful minimum package is:

```text
source folder in civic-design-secondary-research
source metadata note
source file or source link
candidate extraction notes, where useful
evidence-map.md stub
matching source record in civic-design-intelligence
```

Do not require all pieces before any useful work can happen. Non-linear ingestion means structured knowledge may sometimes exist before the source package is complete.

When that happens, record the gap and complete source capture later.

## Source folder naming

Use a stable source ID and readable slug.

Example:

```text
SRC_001_ofsted_essex_area_send_inspection_jan_2026/
```

The folder name should support:

- stable cross-repository reference
- human browsing
- Obsidian search
- future automation

Avoid vague folder names such as:

```text
report/
send-report/
essex/
```

## Source metadata

A source metadata note should capture enough information for review.

Suggested fields:

```yaml
id: SRC_000
type: source
source_type: public_secondary_source
status: captured
review_status: not_reviewed
title:
publisher:
publication_date:
source_url:
source_archive_ref:
retrieved_date:
licence_or_reuse_notes:
related_service_area:
related_locality:
notes:
```

Not every field is required immediately. Use what is known and mark uncertainty clearly.

## Evidence-map stub

Each captured public source folder should have an `evidence-map.md` when the source is expected to connect back to structured intelligence objects.

The map should answer:

- what source is this?
- why was it captured?
- what structured source record represents it?
- which selected evidence extracts have been created?
- which user needs, civic needs, pain points, behaviours, insights or themes are linked later?
- what remains unresolved?

Suggested structure:

```markdown
# Evidence map: [source title]

## Source

Source ID:
Source record:
Source folder:
Original URL:

## Why this source was captured

## Selected evidence extracts

## Derived or linked objects

### User needs

### Civic needs

### Behaviours

### Pain points

### Insights and themes

## Unresolved questions

## Update notes
```

The evidence map is a navigation and provenance aid. It is not a replacement for source records, evidence objects or PR history.

## Source record in civic-design-intelligence

When a public secondary source is used to support structured intelligence, create a matching source record in `civic-design-intelligence`.

The source record should:

- point to the source archive folder where relevant
- include the original source URL where known
- distinguish source metadata from evidence interpretation
- link to selected evidence extracts once they exist
- avoid claims that the source validates derived objects

A source record may be created before selected evidence extracts. That is acceptable when the source is expected to support future ingestion.

## Selected evidence extracts

Do not extract everything.

Create selected evidence extracts when material is useful for understanding user needs, civic needs, behaviours, pain points, insights, themes or service context.

Each extract should preserve:

- source record or research-study link
- location in the source, where possible
- evidence voice
- source type
- whether the material is direct evidence, reported evidence, institutional framing or synthesis
- any relevant limits

A selected extract may support, illustrate, contextualise, limit, challenge or contradict an object. Do not assume every extract strongly supports an object.

## Public secondary source route

For sources such as inspection reports, use this route where possible:

```text
1. Add or reference the source in civic-design-secondary-research.
2. Create source metadata.
3. Create an evidence-map.md stub.
4. Create a matching source record in civic-design-intelligence.
5. Select a small number of evidence extracts.
6. Classify evidence voice and overclaiming risk.
7. Run an ingestion slice.
8. Update the evidence map with structured object links.
```

This route can happen over multiple PRs. It does not all need to happen at once.

## Primary research source route

For primary research, protect privacy and consent before structure.

Use this route:

```text
1. Confirm the material is safe to use.
2. Create or confirm the research-study record.
3. Create anonymised evidence extracts only where useful.
4. Classify evidence voice.
5. Run a bounded ingestion slice.
6. Preserve unresolved interpretation questions.
```

Do not place raw sensitive transcripts in public repositories.

## Uploaded files

When a source arrives as an uploaded file, first decide what kind of source it is.

Ask:

- is it public or private?
- is it primary research, secondary research, operational material or collaborator material?
- can the file itself be stored publicly?
- should the file live in the source archive repository, the intelligence repository, or outside both?
- what metadata is needed before extraction?
- what evidence or object extraction is safe?

Do not extract directly into objects until the source route is clear.

## Backward source capture

Sometimes structured knowledge already exists before a source has been captured.

Use backward source capture when:

- an existing object references a source that has not been archived
- a need-shaped input is research-derived but lacks a source record
- a secondary source was used informally before the workflow existed
- older notes contain source references that need reconstruction

Backward source capture should:

- create or link the source record
- add source archive references where possible
- update evidence maps where useful
- make unresolved provenance gaps visible
- avoid changing review or validation state automatically

## Automation opportunities

Good candidates for future automation:

- creating source folders
- generating source metadata stubs
- downloading or linking public source files where permitted
- creating `evidence-map.md` stubs
- checking source IDs and folder names
- creating matching source records
- warning when a source is referenced without a record
- warning when an evidence map references missing objects
- generating PR body source-capture summaries

These are support tasks. They should not interpret the source or validate derived objects.

## What not to automate yet

Do not automatically:

- decide which findings are validated user needs
- promote evidence strength
- infer civic needs from a source without review
- decide pain point severity from a report alone
- merge, split or supersede objects
- mark source interpretation reviewed
- treat a report as direct lived-experience evidence
- treat a source archive reference as proof of validity

## PR expectations

A source capture PR should explain:

- what source was captured
- why it was captured
- where raw or lightly processed material lives
- what source record was created or linked
- whether selected evidence extracts were created
- what was not interpreted yet
- what remains unresolved
- whether a later ingestion slice is needed

Suggested PR section:

```markdown
## Source capture notes

- Source captured:
- Source type:
- Repository location:
- Matching source record:
- Evidence-map status:
- Selected evidence extracts created:
- Interpretation deliberately deferred:
- Follow-up ingestion slice needed:
- Unresolved provenance or reuse questions:
```

## Guardrails

Do not:

- bulk import large public reports into the intelligence repository
- treat source capture as evidence interpretation
- treat secondary-source findings as validated user needs
- extract everything just because the source exists
- hide missing source or evidence links
- store raw sensitive primary research in public repositories
- mark review or validation complete because a source has been captured

## Done criteria

Source capture is good enough when:

- the source type is clear
- the source location is reviewable
- the source metadata is sufficient for future use
- cross-repository references are clear where relevant
- selected evidence extraction has either happened or been explicitly deferred
- interpretation has not been overclaimed
- unresolved provenance or reuse issues are visible
