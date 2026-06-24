# Repository validation

This file explains how to use lightweight tests to keep the research repository consistent as notes are migrated, normalised or added.

## Purpose

Validation gives contributors a test-driven way to clean up the repository.

Instead of manually guessing whether the repo is consistent, run the validator and make changes until the checks pass.

The default validation layer focuses on real repository content notes, not templates, documentation examples or migration scaffolds.

Naming and link checks should be read alongside `docs/Naming_and_linking_contract.md`, which defines the repository contract for stable IDs, ID-prefixed readable filenames, aliases and Obsidian links.

User need quality warnings should be read alongside `docs/User_need_quality_tests.md` and `docs/User_needs_writing_rules.md`.

It checks:

- YAML frontmatter presence
- required fields on structured notes
- canonical ID format
- ID prefix matching object type
- duplicate IDs
- controlled values
- lifecycle safety rules
- unresolved wikilinks
- unresolved relationship links
- user need wording smells that need human review

## Validation philosophy

The validator does not exist to make every research object complete before it can be committed.

The repository is allowed to contain incomplete knowledge, weak signals, placeholders and LLM-assisted candidate objects.

The validator exists to stop incomplete knowledge being mistaken for reviewed or validated knowledge.

In short:

```text
Allow incomplete objects.
Block misleading objects.
Warn about likely quality smells.
```

A candidate user need can exist without direct evidence links if it is clearly marked as a candidate or assumption.

A user need must not be treated as reviewed, validated or decision-ready unless the required traceability, review state and evidence basis are present.

The validator should therefore protect against category errors such as:

- draft treated as validated
- assumption treated as evidence
- LLM output treated as research
- weak traceability treated as strong evidence basis
- review state hidden or misrepresented
- wrong ID or type making an object hard to trace
- solution-shaped or bundled user needs entering without review visibility

## Default validation scope

By default, the validator checks research and problem-space content folders, including:

- `001_Research_studies/`
- `002_Evidence/`
- `003_User_needs/`
- `004_Behaviours/`
- `005_Pain_point/`
- `006_Insights/`
- `007_Themes/`
- `008_Personas/`
- `009_Journeys/`

By default, it skips:

- `Templates/`
- `000_Inbox/`
- `docs/`
- `migration/`

This avoids treating template placeholders, documentation examples and audit scaffolds as real research notes.

## Optional validation scopes

To include templates:

```bash
python3 tools/validate_repository.py --include-templates
```

Template validation is template-aware. It checks that templates have valid
frontmatter structure, IDs, required fields and controlled-value options, but it
does not treat template filenames such as `User_need_template.md` as object
filename violations. It also allows frontmatter option lists such as
`status: assumption | draft | reviewed | validated | deprecated` in templates,
while continuing to warn if a real content note uses an option list instead of a
selected value.

To include documentation, migration notes and inbox notes:

```bash
python3 tools/validate_repository.py --include-docs
```

To include both:

```bash
python3 tools/validate_repository.py --include-templates --include-docs
```

These flags are useful for separate quality checks, but they should not be used for the normal research-note migration baseline unless that is intentional.

Use `--include-templates` after changing templates, schema fields or controlled
values. Use `--include-docs` when intentionally cleaning documentation examples,
migration records or inbox scaffolds.

## Three validation layers

### 1. Structural checks

These are suitable for automated validation.

Examples:

- duplicate IDs
- invalid ID format
- missing required fields
- invalid controlled values
- ID prefix does not match object type
- unresolved internal links

Readable filenames are allowed when they preserve the stable object ID at the start of the filename. For example, both `UN_001.md` and `UN_001_need_to_match_options.md` are valid. Filenames that do not begin with the frontmatter ID should be treated as migration warnings because they make objects harder to trace. For user needs, the readable slug should normally derive from `short_name`, not from the full canonical need.

### 2. Governance checks

These are partly automatable.

Examples:

- `status: validated` requires `human_reviewed: true`
- `evidence_basis: validated` requires `review_status: reviewed`
- validated objects need a defensible evidence basis
- LLM-generated objects should not appear human-reviewed unless a review has been explicitly completed

### 3. User need quality warnings

These are automated smell checks, not automated semantic judgements.

The validator can warn when a user need may need review because it appears to:

- use a cognitive verb such as `need to know` or `need to understand`
- name a likely container solution such as a dashboard, portal, app, toolkit, checklist, page, form or guide
- bundle known mixed objects such as `steps, rights and adjustments`
- contain several `and` joins in the main need statement
- use a cognitive verb in `short_name`

These warnings should trigger review against `docs/User_need_quality_tests.md`.

They do not automatically mean the need is wrong. A cognitive verb may be appropriate for rights, consent, safety or informed decision-making. A list may be acceptable when the listed items are criteria for one coherent job. The warning means the need should be checked for solution-shaping, bundling or poor granularity.

### 4. Decision-readiness checks

These are not fully automated in the first version.

Decision-readiness means an object is being used for a higher-consequence purpose, such as:

- page or content design
- service design
- policy challenge
- prioritisation
- stakeholder synthesis
- value assessment
- ministerial or senior decision support
- validation

The validator can check whether minimum conditions are present, but it cannot judge whether the research interpretation is substantively correct.

The long-term pattern should be:

```text
machine checks presence, consistency and obvious smells
human checks meaning and judgement
```

A future validator mode may check notes marked with fields such as:

```yaml
intended_use:
  - policy_challenge
  - service_design
```

or:

```yaml
decision_use: true
```

and require stricter metadata such as:

- reviewed or validated status
- traceable or substantiated evidence basis
- human review
- linked evidence
- need level
- parent needs where relevant
- caveats or uncertainty
- review notes for higher-risk claims

Do not apply decision-readiness checks to every loose or candidate object.

## Running the validator

From the repository root, run:

```bash
python3 tools/validate_repository.py
```

To treat warnings as errors:

```bash
python3 tools/validate_repository.py --warnings-as-errors
```

## How to use during migration

Use this sequence:

```text
run validator -> review failures -> update notes -> rerun validator -> repeat until clean enough
```

This is especially useful for:

- ID normalisation
- source-link migration
- template migration
- adding new structured notes
- checking LLM-generated candidate objects
- checking candidate user need wording before it shapes the object landscape

## Error versus warning

### Errors

Errors indicate something that should normally be fixed before merging migration work.

Examples:

- missing required field
- invalid ID format
- duplicate ID
- ID prefix does not match type
- invalid controlled value
- validated item without human review
- `evidence_basis: validated` without review

### Warnings

Warnings identify problems that may be acceptable temporarily during migration.

Examples:

- filename does not match ID
- unresolved wikilink
- relationship link target does not resolve
- `evidence_strength: strong` with weak evidence basis
- user need uses a cognitive verb that may hide a more actionable need
- user need appears to name a container solution
- user need appears to bundle multiple jobs or solution vectors

Warnings can be promoted to errors later by using `--warnings-as-errors`.

## What should not be blocked by default

Do not block ordinary commits merely because:

- a candidate user need has no direct evidence link yet
- a placeholder object has no parent need yet
- an LLM-assisted object is not reviewed yet
- an insight is still a draft
- a value dimension is indicative rather than substantiated
- a user need triggers a wording-smell warning that has been reviewed and deliberately accepted

These are acceptable if the metadata makes the incompleteness or review need visible.

Block or fail only when the metadata overclaims reliability, review state or traceability.

## Incremental adoption

The validator is intentionally lightweight and should support incremental cleanup.

The repository does not need to be perfect before the validator is useful.

A good migration workflow is:

1. Run the validator.
2. Fix high-confidence errors first.
3. Review wording-smell warnings before creating or promoting user needs.
4. Leave ambiguous items for later audit.
5. Commit fixes in focused batches.
6. Tighten warnings only when the repository is ready.

## What the validator does not do yet

The validator does not fully check:

- whether evidence genuinely supports a claim
- whether a user need has the right final wording
- whether an insight is well interpreted
- whether personal data has been fully anonymised
- whether a note should be split or merged
- whether a relationship is conceptually correct
- whether an object is substantively decision-ready

It can flag likely user need quality smells, but these still need human review.

## Recommended migration order

Use the tests to clean up in this order:

1. Duplicate or missing IDs.
2. Invalid ID prefixes.
3. Missing required frontmatter fields.
4. Invalid controlled values.
5. Validated/review lifecycle contradictions.
6. Broken source and relationship links.
7. Filename and ID mismatches.
8. User need wording-smell warnings.
9. Warnings that remain after migration.

## Practical rule

The validator should support judgement, not replace it.

If a test failure reveals an ambiguous research or evidence issue, document the ambiguity rather than forcing a mechanical fix.
