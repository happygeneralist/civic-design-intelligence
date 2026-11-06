# Naming and linking contract

Use stable IDs for traceability, readable filenames for humans, frontmatter for queryable data and resolvable links for navigation. Read `Needs_semantic_contract.md` for the distinction between an object's identity and its presentations.

The contract supports Obsidian, GitHub review, future APIs/databases and LLM-assisted handling without repeated filename migrations or silent semantic changes.

## Canonical identity and meaning

Every structured object has one stable frontmatter `id`, a filename beginning with that ID and canonical meaning in its fields/body. Do not infer the entire meaning from the filename or a short map label.

For user needs, `need` is the persisted current working interpretation and `short_name` is the compact map/navigation affordance. Evidence language, user-facing text, value-oriented views and structured relationships are not independent replacements for that interpretation.

A saved derivative should identify the object and the relevant source revisions, using Git commit/blob references where sufficient. Do not regenerate canonical wording on display or present an older derivative as current after a material change.

## IDs and growth

Use an uppercase type prefix, underscore and **at least three ASCII numeric digits**. Three digits are minimum padding, not a maximum corpus size:

```text
UN_001
UN_999
UN_1000
UN_10000
```

Existing IDs stay unchanged. Do not repad or renumber the collection as it grows, recycle retired IDs, or create leading-zero variants of an existing identity. Check the full type namespace and pending branches before allocating the next free number; concurrent allocation must be reconciled before merge. Sort numeric suffixes numerically where sequence matters, not as ordinary text.

| Object type | Prefix |
| --- | --- |
| Research study | RS_ |
| Evidence | EVID_ |
| User need | UN_ |
| Civic need | CN_ |
| Behaviour | BEH_ |
| Pain point | PP_ |
| Insight | INS_ |
| Theme | TH_ |
| Journey | JNY_ |
| Opportunity | OPP_ |
| Claim | CLM_ |
| Value dimension | VAL_ |
| Review note | REV_ |

A prefix convention is not permission to create a new object type or bypass a deferred modelling decision. Use `SCHEMA.md`, templates and current task controls.

## Filenames and slugs

Use:

```text
<ID>_<readable_slug>.md
UN_001_need_to_identify_matching_options.md
EVID_1000_public_source_extract.md
```

Bare ID names remain valid for temporary or transitional files. Prefer a readable slug once a useful stable label exists. Slugs use lower-case ASCII words separated by underscores, no punctuation/apostrophes, and no date unless the date is part of the object's identity.

Do not use a full sentence, a vague `new_note`/`final` label or an unearned validation claim. For user needs derive the initial slug from `short_name`, not the full `need`. A later wording refinement is not a reason to rename the file automatically. Preserve identity and links.

## Frontmatter and body

Frontmatter holds type, ID, canonical wording, compact labels, lifecycle/evidence/review metadata and existing relationship fields. The body carries evidence fit, interpretation, contexts, tensions, value and other detail not yet formalised in the schema.

Future tools must read the actual fields/body rather than assume a filename or graph edge contains a complete semantic claim. Missing relationships and optional fields can remain unknown. Do not invent a new mandatory representation or context field solely for a generated view.

## Obsidian links

Acceptable forms include:

```markdown
[[UN_001_need_to_identify_matching_options]]
[[UN_001_need_to_identify_matching_options|Need to identify matching options]]
[[UN_001]]
```

Use ID-only links where stability matters. Display text provides the human affordance without changing the referenced object. Keep related fields as resolvable links where appropriate; the relation's meaning may require an accompanying body note.

## Aliases

Retain aliases needed for old names, migrated IDs and users' navigation. Aliases support continuity; they are not substitutes for stable frontmatter IDs. Do not remove aliases during the same change that introduces a rename.

The current validator resolves object IDs and filenames. Obsidian alias behaviour must not be assumed to be fully checked by that script; inspect actual links when changing alias-dependent navigation.

## Creation checks

Check the correct folder, object type and prefix; ID uniqueness; matching ID-prefixed filename; appropriate short label; conservative lifecycle/evidence/review state; source provenance or explicit assumption; and relevant nearby objects. Keep LLM assistance visible.

Use the inbox for material whose identity or classification is unresolved. Do not require an evidence-complete record before keeping a meaningful candidate in an authorised structured location.

## Rename and semantic-change checks

Distinguish administrative filename/link maintenance from a meaning change. Do not combine broad renaming with semantic rewriting unless explicitly authorised. Preserve IDs, aliases, evidence and statuses during a naming-only migration; use Git and the PR summary instead of duplicative object change logs.

When meaning changes, follow the object changelog and LLM-intervention rules. Adding a child, context or audience view does not automatically replace the parent. A true split, merger or supersession needs explicit lineage and preservation of the earlier interpretation.

## PR reporting

State which paths, IDs, labels, aliases or links changed, whether the change is administrative or semantic, any effect on review/evidence metadata, and what checks actually ran. Never make a naming change look like human research validation.

Run the repository validator and relevant regression tests. Larger IDs are supported by the validator; this is an addressability correction, not proof that every future interface or analysis has been benchmarked at 10,000 objects.
