# Repository governance

This file defines the practical governance rules for the research repository.

For the legal basis and data protection rationale, see `docs/Governance_legal_basis.md`.

## Governance purpose

The repository exists to support evidence-based service design and public decision-making by making anonymised research knowledge reusable, traceable and reviewable.

Governance should ensure that:

- evidence is handled safely
- assumptions are clearly marked
- insights remain traceable to evidence
- material changes are reviewed
- LLM-generated content is controlled
- validated findings are not changed without a clear review trail

## Roles

### Repository owner

Responsible for repository structure, access, permissions and overall quality.

### Research lead

Responsible for research integrity, interpretation quality and whether evidence supports a finding.

### Contributor

May add evidence, draft notes, suggest links and create synthesis outputs within the repository rules.

### Reviewer

Reviews draft or assumption-based material and decides whether it can be promoted, revised, rejected or kept as an assumption.

### LLM assistant

May help draft, classify, summarise and link material, but cannot validate research findings.

## What may be stored

The repository may store:

- anonymised quotes
- anonymised observations
- survey findings
- coded evidence
- study summaries
- user needs
- behaviours
- pain points
- insights
- themes
- personas
- journeys
- review notes
- synthesis outputs

## What must not be stored

The repository must not store:

- raw transcripts
- audio or video recordings
- names or direct identifiers of participants
- contact details for participants
- identifiable special category data
- unredacted case details
- unsupported claims presented as validated findings

## Evidence and interpretation

Evidence and interpretation must be kept distinct.

Evidence notes should capture what was observed, said or measured.

Interpretive notes, such as needs, behaviours, pain points and insights, should link back to evidence.

A claim without evidence may still be useful, but it must be marked as an assumption.

## Validation authority

Only a human reviewer may mark an item as validated.

An item can be validated only when:

- the claim is clear
- linked evidence supports the claim
- uncertainty and limitations are documented
- anonymisation has been checked where relevant
- the item has been reviewed
- the changelog has been updated

## Change control

Changes are classified as:

- `minor`: spelling, formatting, metadata correction or link fix
- `material`: changes interpretation, linked evidence, confidence, status or evidence strength
- `major`: substantially reframes a finding, alters validated content or affects published outputs

Material and major changes require a review trail.

## LLM-assisted changes

LLM-assisted changes must follow `llm-instructions.md`.

LLMs may create drafts and suggest changes, but they must not:

- validate findings
- upgrade evidence strength
- remove caveats
- materially alter validated notes without review
- silently rewrite participant evidence

LLM-generated content should be marked with:

```yaml
llm_generated: true
human_reviewed: false
review_status: not_reviewed
```

## Pull request expectations

Repository changes should be made through branches and pull requests where possible.

A pull request should explain:

- what changed
- why it changed
- whether research content changed
- whether assumptions were introduced
- whether evidence links were added or changed
- whether any status or evidence strength changed
- what still requires review

## Audit and review

The repository should be reviewed periodically for:

- unsupported validated claims
- weakly sourced insights
- assumptions that have not been reviewed
- evidence without source studies
- notes missing required metadata
- identifiable or sensitive material
- broken or inconsistent IDs

Findings from audits should be recorded in `CHANGELOG.md` or review notes, depending on scope.
