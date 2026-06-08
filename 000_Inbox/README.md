# Inbox

Use this folder for loose capture and first-pass research breakdown work.

The inbox is for material that is useful but not yet ready to become a structured research object.

## What belongs here

Use the inbox for:

- loose research notes
- anonymised working notes
- meeting or workshop notes
- imported summaries
- LLM extraction outputs
- first-pass candidate breakdowns
- temporary synthesis notes

## What does not belong here

Do not add:

- raw transcripts
- recordings
- identifiable participant data
- unredacted case details
- special category personal data that has not been anonymised
- validated findings

## Workflow

1. Capture loose material here.
2. Use `Templates/Loose_capture_template.md` where useful.
3. Ask an LLM to structure the material into candidate evidence, user needs, behaviours, pain points and insights.
4. Move useful structured objects into the relevant numbered folders.
5. Keep weak or unlinked objects marked as assumptions or candidates.
6. Preserve source traceability back to the inbox note or source study where possible.
7. Deepen evidence only when the work requires it.
8. Resolve the inbox note.

## Default status for inbox material

```yaml
status: captured
analysis_state: captured
review_status: not_reviewed
```

## Default status for LLM-created candidate objects

```yaml
status: assumption
analysis_state: candidate
evidence_basis: indicative
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed
```

Do not use:

```yaml
evidence_basis: validated
```

unless a human reviewer has explicitly completed validation.

## Source traceability

When structured notes are created from inbox material, link back to the inbox note or related research study where possible.

Examples:

```yaml
source_note: "[[000_Inbox/example_note]]"
source_study: "[[RS_000]]"
```

## Exit rule

The inbox is a staging area, not a dumping ground.

After first-pass breakdown, choose one of these outcomes:

- keep the inbox note as source context and link structured objects back to it
- move useful objects into structured folders
- archive or delete temporary LLM output that no longer has value
- add a follow-up note explaining what still needs processing

Do not leave inbox notes in an ambiguous state after they have been processed.
