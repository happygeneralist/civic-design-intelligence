# Validation baseline report

This report records the repository validation baseline before ID, filename or link migration begins.

No research notes should be changed as part of this baseline report.

## How to generate the baseline

Run from the repository root:

```bash
python3 tools/validate_repository.py
```

Optionally save the output:

```bash
python3 tools/validate_repository.py > migration/validation-baseline-output.txt
```

Do not use `--warnings-as-errors` for the first baseline. The first pass should separate hard errors from warnings and migration signals.

## Baseline status

```text
Baseline run date: Pending CI run
Run by: GitHub Actions validation workflow
Branch or commit: audit/validation-baseline
Validator command: python3 tools/validate_repository.py
Errors: Pending
Warnings: Pending
```

## Summary

| Finding group | Count | Severity | Migration action |
|---|---:|---|---|
| Missing required fields | Pending | Error | Fix in metadata batch |
| Invalid ID format | Pending | Error | Fix in ID batch |
| Duplicate IDs | Pending | Error | Human review before migration |
| Wrong ID prefix for type | Pending | Error | Fix in ID batch |
| Invalid controlled values | Pending | Error | Fix in metadata batch |
| Lifecycle contradictions | Pending | Error | Human review before promotion/demotion |
| `evidence_basis: validated` without review | Pending | Error | Human review before correction |
| Unresolved wikilinks | Pending | Warning | Link mapping batch |
| Unresolved relationship links | Pending | Warning | Link mapping batch |
| Filename/ID mismatch | Pending | Warning | Filename migration batch |

## Full validator output

Validator output will be populated from the GitHub Actions run for this branch.

```text
Pending CI run
```

## Findings by file

| File | Finding | Severity | Proposed class | Proposed action | Notes |
|---|---|---|---|---|---|
| Pending | Pending | Pending | Pending | Pending | Pending |

## Finding classes

Use these classes when interpreting results.

| Class | Meaning | Typical action |
|---|---|---|
| Structural error | Breaks schema, IDs, controlled values or lifecycle consistency | Fix in early migration batch |
| Link integrity warning | Broken wikilink or relationship reference | Map before fixing |
| Filename/ID warning | File name does not match canonical ID | Include in ID mapping |
| Ambiguous object | Type, source or canonical status unclear | Human review before migration |
| Acceptable immaturity | Candidate or assumption is incomplete but honestly labelled | Leave as-is for now |

## Recommended migration batches

Use the baseline to decide the safest order.

### Batch 1: structural metadata fixes

Use for low-risk missing fields, invalid controlled values, and clear schema issues.

### Batch 2: ID normalisation

Use for invalid IDs, wrong prefixes and duplicate IDs after human review.

### Batch 3: link repair

Use for unresolved wikilinks, `source_study`, `source_note`, `related_*`, `parent_needs`, `child_needs`, `supersedes` and `superseded_by` links.

### Batch 4: filename normalisation

Use when filenames should match canonical IDs and link updates have been mapped.

### Batch 5: ambiguous or high-risk items

Use for items where type, source, evidence basis, review state or canonical status requires judgement.

## Do not mechanically fix

Record findings that should not be fixed without judgement.

| Finding | Why mechanical fixing is risky | Required review |
|---|---|---|
| Pending | Pending | Pending |

## Audit decision

```text
Baseline reviewed by:
Review date:
Decision: proceed to mapping | rerun baseline | fix validator | split audit | pause migration
Notes:
```
