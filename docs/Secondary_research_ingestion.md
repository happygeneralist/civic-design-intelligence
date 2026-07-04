# Secondary research ingestion

This note captures the working approach for bringing public secondary research into the Civic Design Intelligence repository.

It is a direction-setting note, not a schema change.

## Core principle

Keep the structured intelligence graph in this repository. Keep public secondary source material in a separate source archive where useful.

```text
Public secondary source archive
→ source record
→ evidence extracts
→ candidate needs, pain points, behaviours, civic needs and insights
→ cross-source patterns
```

The structured repository should not become a raw document dump.

## Companion source archive

The companion public source archive is:

```text
happygeneralist/civic-design-secondary-research
```

Use that repository for raw or lightly processed public secondary source material. Use this repository for the structured research intelligence derived from those sources.

Current first source example in the companion archive:

```text
SRC_001_ofsted_essex_area_send_inspection_jan_2026
```

This source represents a public Ofsted and Care Quality Commission Area SEND inspection report, using the public file URL as the source reference. It is an example of public inspection-report provenance, not proprietary council, employer or unpublished research material.

## Why separate source storage helps

Public secondary sources such as Ofsted reports, inspection reports, local authority strategies, charity reports, academic papers and policy documents can be large, numerous and unevenly useful.

A separate public secondary-research repository can hold or index the source material without making this repository harder to review, search or maintain.

This repository should hold the structured intelligence derived from those sources:

- source records
- source metadata
- evidence extracts
- citations and source locations
- links to the source archive or public URL
- derived user needs, civic needs, pain points, behaviours, insights and themes

## Recommended split

Use this repository for:

```text
001_Research_studies/   source records and source metadata
002_Evidence/           selected evidence extracts
003_User_needs/         derived user and civic needs
004_Behaviours/         derived behaviours
005_Pain_point/         derived pain points
006_Insights/           derived insights
007_Themes/             derived themes
```

Use the public secondary-research repository for:

```text
raw or lightly processed public reports
source inventories
download metadata
publisher metadata
checksums, where useful
source grouping by topic, place or publisher
bulk files that should not live in the structured intelligence repo
```

Where possible, this repository should link to a public source URL as well as any archived copy.

## Source records

A public secondary source should normally have a source or research-study record before its findings are used as evidence.

Example:

```yaml
type: research_source
id: RS_014
source_type: inspection_report
title: Ofsted local area SEND inspection report
publisher: Ofsted
publication_date:
source_url:
source_archive_ref: happygeneralist/civic-design-secondary-research/sources/SRC_001_ofsted_essex_area_send_inspection_jan_2026/
retrieved_date:
geographic_scope:
  - local_authority
service_contexts:
  - SEND
evidence_status: captured
review_status: not_reviewed
```

The source record is not itself the evidence claim. It records where the evidence came from and how to find it again.

## Evidence extracts

Only selected parts of a source should become evidence notes.

Create evidence notes where the extract helps answer questions about:

- visible user needs
- civic needs or institutional obligations
- unresolved pain
- behaviours
- service or operational conditions
- evidence gaps
- recurring patterns

Example:

```yaml
type: evidence
id: EVID_082
source: "[[RS_014_ofsted_local_area_send_inspection]]"
source_archive_ref: happygeneralist/civic-design-secondary-research/sources/SRC_001_ofsted_essex_area_send_inspection_jan_2026/
evidence_type: secondary_report_finding
source_type: inspection_report
reported_voice: inspector_synthesis
source_location: "page 12 / section: Area SEND findings"
service_contexts:
  - SEND
locality_contexts:
  - East Merseyside
evidence_basis: traceable
evidence_strength: weak
review_status: not_reviewed
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
```

Use direct quotations only where short, lawful, necessary and useful. Otherwise paraphrase the finding and preserve the source location.

## Evidence maps

Each source folder in the companion archive should include an `evidence-map.md` file.

That file is the bridge from the public source archive back to this repository. It should list:

- the matching source or research-study record in this repository
- evidence objects created from the source
- linked user needs, civic needs, pain points, behaviours, insights and themes
- current ingestion status
- what has and has not been extracted

The map should be updated when structured evidence or analysis objects are created, changed or superseded.

## Secondary evidence is not the same as primary evidence

An inspection finding, literature review or policy report is often a synthesis produced by another organisation.

It can be useful evidence, but it should not automatically validate a need.

A report finding may support:

- a candidate user need
- a civic need
- a pain point
- a service condition
- an evidence gap
- an emerging pattern

But it should be marked conservatively unless the underlying evidence is clear and reviewed.

## Reported voice

Capture whose voice the evidence represents.

Possible values may later include:

```text
direct_user_voice
professional_observation
inspector_synthesis
researcher_synthesis
administrative_data
policy_statement
third_sector_synthesis
```

Do not finalise these as required controlled values yet. Use them cautiously as working labels where they help interpret the evidence.

## Creating or updating needs from secondary evidence

Do not convert report language directly into canonical user-need wording without interpretation.

Avoid making the source organisation's framing the need itself.

For example, a report may say:

```text
Families do not understand the local offer.
```

A safer candidate need might be:

```text
Need to know what support is available locally.
```

The evidence can then support or contextualise that need:

```yaml
supporting_evidence:
  - "[[EVID_082_parent_confusion_about_local_offer]]"
```

The need should remain conservative unless reviewed by a human.

## Relationship to context and pattern sensemaking

Secondary sources can help identify patterns across places and services.

A need may first be observed in one local inspection report, then recur in reports from other councils, charities or national reviews.

Preserve the source context, but do not make the first source context the permanent boundary of the need.

Use `docs/Context_and_pattern_sensemaking.md` alongside this note.

## Minimum viable ingestion workflow

For the first secondary-research ingestion PR:

1. Add one source record.
2. Add 5 to 10 evidence extracts.
3. Create or link 2 to 4 candidate pain points, behaviours, user needs or civic needs.
4. Preserve source URL, archive reference and source location.
5. Mark all derived objects conservatively.
6. Do not mark anything reviewed or validated unless human review has happened.
7. Record uncertainties in the PR summary.
8. Update the source `evidence-map.md` in the companion archive.
9. Do not ingest an entire report exhaustively.

The goal is to test the workflow, not to complete the whole SEND evidence base in one PR.

## Future sync possibility

A future workflow may help keep the roadmap, source inventory or evidence maps in sync across repositories.

Possible later automation:

- read source folders from `civic-design-secondary-research`
- detect source folders without matching source records in this repository
- detect evidence maps that reference missing or renamed evidence objects
- update a generated source inventory
- open a pull request rather than writing directly to `main`

Do not build this yet. Test the manual workflow first with a small number of sources.

## What not to do yet

Do not immediately:

- import a large corpus of reports into this repository
- create evidence notes for every paragraph of a report
- treat inspection findings as validated user needs
- create a full source ontology
- create strict validator rules for secondary evidence before examples exist
- build automated ingestion before the manual pattern is clear
- duplicate large public documents in this repository

## Open questions

These should be resolved through worked examples:

- Should source archive references use URLs, relative paths, checksums or source IDs?
- Which secondary evidence types need controlled values?
- When is a report finding strong enough to upgrade evidence strength?
- How should conflicting findings across reports be represented?
- When does a recurring secondary finding become an established pattern rather than an emerging one?
- What should be generated automatically once several sources have been ingested?
