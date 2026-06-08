# Repository validation

This file explains how to use lightweight tests to keep the research repository consistent as notes are migrated, normalised or added.

## Purpose

Validation gives contributors a test-driven way to clean up the repository.

Instead of manually guessing whether the repo is consistent, run the validator and make changes until the checks pass.

The first validation layer focuses on:

- YAML frontmatter presence
- required fields on structured notes
- canonical ID format
- ID prefix matching object type
- duplicate IDs
- controlled values
- lifecycle safety rules
- unresolved wikilinks
- unresolved relationship links

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

Warnings can be promoted to errors later by using `--warnings-as-errors`.

## Incremental adoption

The validator is intentionally lightweight and should support incremental cleanup.

The repository does not need to be perfect before the validator is useful.

A good migration workflow is:

1. Run the validator.
2. Fix high-confidence errors first.
3. Leave ambiguous items for later audit.
4. Commit fixes in focused batches.
5. Tighten warnings only when the repository is ready.

## What the validator does not do yet

The first version does not fully check:

- semantic quality of user needs
- whether evidence genuinely supports a claim
- whether an insight is well interpreted
- whether personal data has been fully anonymised
- whether a note should be split or merged
- whether a relationship is conceptually correct

These still need human review.

## Recommended migration order

Use the tests to clean up in this order:

1. Duplicate or missing IDs.
2. Invalid ID prefixes.
3. Missing required frontmatter fields.
4. Invalid controlled values.
5. Validated/review lifecycle contradictions.
6. Broken source and relationship links.
7. Filename and ID mismatches.
8. Warnings that remain after migration.

## Practical rule

The validator should support judgement, not replace it.

If a test failure reveals an ambiguous research or evidence issue, document the ambiguity rather than forcing a mechanical fix.
