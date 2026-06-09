# Object change logs

Use object change logs to record material changes in meaning, interpretation, maturity, evidence basis, lifecycle state, relationships or decision relevance.

Do not use object change logs to recreate Git history. Git and pull request summaries are enough for formatting, metadata hygiene and administrative migration notes.

## Core rule

```text
If the change affects how the object should be interpreted, used, trusted or acted on, record it.

If the change only affects formatting, metadata or validation hygiene, rely on Git and the pull request summary.
```

## When an object change log is required

Add or update the object change log when a change affects:

- user need wording
- civic need framing
- pain point interpretation
- evidence-derived insight
- evidence basis
- evidence strength
- confidence
- status
- analysis state
- review status
- lifecycle or recurrence state
- relationships between objects
- value-delivery interpretation
- decision relevance
- whether an object is active, unresolved, resolved, dormant, recurring, deprecated or superseded

## When an object change log is not required

Do not add an object change log entry for routine changes such as:

- spelling corrections that do not affect meaning
- formatting
- YAML field ordering
- link repair
- file moves
- metadata normalisation
- template alignment
- validation hygiene

Record these in the pull request summary instead.

## Recommended format

Use `## Changelog` to stay consistent with existing templates.

```markdown
## Changelog

### YYYY-MM-DD

- Changed:
- Reason:
- Effect:
- Changed by:
```

Use a single-line entry only for simple creation or minor notes.

```markdown
## Changelog

- YYYY-MM-DD: Created as candidate user need. Status: assumption. Analysis state: candidate. Evidence basis: none.
```

## Optional fields for material changes

Use these only when they help preserve meaning.

```markdown
- Previous interpretation:
- New interpretation:
- Evidence affected:
- Review status:
- Supersedes:
- Superseded by:
```

## LLM-assisted semantic changes

Where an LLM proposes or makes a material semantic change, record that in the object change log.

Example:

```markdown
### 2026-06-09

- Changed: Reworded the need to distinguish parental understanding from professional assessment.
- Reason: Source evidence suggests the issue is not only lack of information, but uncertainty about what counts as sufficient evidence.
- Effect: The need should now be interpreted as a confidence and evidence-readiness need, not only an information-access need.
- Changed by: LLM-assisted draft, pending human review.
```

A separate LLM intervention log is not required for routine extraction, formatting, metadata cleanup or first-pass candidate creation.

Use a separate LLM intervention log only when the LLM materially changes the repository model, reframes evidence across multiple objects, proposes a synthesis that could shape decisions, or changes the implied solution or intervention space.

## Status and review changes

Always record changes that promote, demote, deprecate, supersede or validate an object.

Do not mark an object as reviewed or validated unless human review has explicitly happened.

## Pain points

Treat pain points as condition or risk objects, not disposable defects.

Resolved pain points may remain important if they explain previous burden, show a dependency, reveal a recurring risk or indicate where value delivery could fail again.

Record material changes to pain point state, recurrence risk or value impact in the object change log.

## Administrative migrations

For broad administrative migrations, use the pull request summary rather than adding detailed object change logs to every affected file.

Examples:

- folder renaming
- field order normalisation
- template formatting
- bulk metadata cleanup

If the migration changes interpretation, maturity, evidence basis or decision relevance, add object change log entries to the affected objects.
