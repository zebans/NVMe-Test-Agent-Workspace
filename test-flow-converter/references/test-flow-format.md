# Standard Test Flow Format

Use this reference for every conversion. It defines the normalized intermediate
structure, output files, required fields, and validation checks.

## Intermediate Structure

Normalize every source into this structure before writing the final flow:

```yaml
manifest_version: 1
title: "<test flow title>"
source:
  path: "<original path or user input description>"
  input_type: "shell | iol | csv | text | converted"
  converted_markdown: "<converted.md when used>"
  parser_mode: "<direct parsing, markitdown, heuristic text, etc.>"
purpose: "<what the test validates>"
preconditions:
  - "<setup, environment, fixture, DUT, tool, safety, or capability requirement>"
defaults_and_artifacts:
  parameters:
    <name>: "<default, allowed value, or source expression>"
  artifacts:
    - "<file or directory produced or consumed>"
common_verify:
  - "<verification applied to all relevant commands>"
safety:
  mode: "<read-only, state-changing, destructive, firmware-lab, etc.>"
  requirements:
    - "<gates or abort conditions>"
steps:
  - id: 1
    source_ref: "<row, line, label, section, or user step>"
    title: "<short imperative title>"
    kind: "command | action | wait | decision | loop | cleanup"
    command: "<exact command when single command>"
    commands:
      - "<exact command when multiple commands>"
    inputs:
      <source_parameter_name>: "<source value or normalized value>"
    timing:
      wait_seconds: "<number or source expression>"
      timeout: "<source expression>"
    parser:
      - "<field parsing needed before verification>"
    verify:
      - "<expected result, field check, status check, or pass criterion>"
    pass_fail:
      pass: "<condition>"
      fail: "<condition>"
      skip: "<condition when applicable>"
    artifacts:
      - "<step artifact>"
    cleanup:
      - "<step cleanup or rollback>"
    safety: "<step-specific safety note>"
    flags:
      - "<ambiguous, unsupported, inferred, destructive, etc.>"
cleanup:
  - "<global cleanup or explicit none>"
final_verify:
  - "<end-of-test checks>"
ambiguities_unsupported_logic:
  - "<source-backed issue and requested clarification if needed>"
validation:
  status: "pass | needs_clarification | blocked"
  notes:
    - "<validation notes>"
```

Omit empty keys in final artifacts, but do not omit required information.

## `flow.md`

Use this section order unless the source strongly benefits from a smaller
format:

```markdown
# <Title> Test Flow

Source <type>:
`<path or user-supplied description>`

Conversion: `<direct parsing | markitdown output in converted.md | heuristic>`

## Purpose

<One concise paragraph.>

## Preconditions

- <Setup and safety gates.>

## Defaults And Artifacts

- `<PARAMETER_NAME>=<value>`.
- Output/artifact expectations.

## Common Verify

- <Verification that applies across commands.>

## Flow

### Step 1: <Title>

Source <row/line/label/step>: <identifier>.

Command:

- `<exact command>`

Inputs:

- PARAMETER = `<exact or normalized value>`

Timing:

- Wait `<duration>` or timeout `<duration>`.

Verify:

- <Expected result or pass criterion.>

Artifacts:

- `<artifact>`

Safety:

- <Abort gate or cleanup note.>

## Cleanup

- <Cleanup steps or "No cleanup required by source.">

## Final Verify

- <End state and pass/fail criteria.>

## Ambiguities And Unsupported Logic

- <Only include when non-empty.>

## Validation

- Required fields: pass | needs clarification.
- Unsupported logic: none | listed above.
- Source coverage: pass | gaps listed.
```

For concise flows, omit empty optional subsections inside a step. Keep
`Command`, `Inputs`, `Timing`, `Verify`, `Artifacts`, and `Safety` labels when
they exist in the source.

## `manifest.yaml`

Create `manifest.yaml` when files are requested or when the flow is complex.
Use stable field names from the intermediate structure. Preserve source values
as strings if type conversion could lose meaning, such as `20000`, `001b`,
`0x05`, or variable expressions.

Rules:

- Use `manifest_version: 1`.
- Store source path, conversion mode, and input type under `source`.
- Use one-based step IDs in source order.
- Include `source_ref` for every step: row number, line range, label, heading,
  or user step.
- Use `inputs` for command parameters, CSV parameters, function arguments, and
  environment defaults.
- Use `flags` for inferred, ambiguous, unsupported, or unsafe behavior.
- Include `safety` whenever the test can modify device state, firmware,
  reservations, persistent settings, namespaces, or power/reset state.

## `coverage-matrix.md`

Map source material to generated flow checks:

```markdown
# <Title> Coverage Matrix

| Source item | Generated flow coverage | Checks | Safety | Notes |
|---|---|---|---|---|
| Row 3 / Step A / line 42 | Step 3 | <verify summary> | <safety> | <gap or pass> |

## Reviewer Checks

| Check | Status | Notes |
|---|---|---|
| Required fields present | pass | <note> |
| Original commands preserved | pass | <note> |
| Unsupported logic flagged | pass | <note> |
```

## `test-template.md`

Use this compact implementation template:

```markdown
# Test Flow Step Template

## Step

- Step ID:
- Source reference:
- Title:
- Kind:
- Command/action:
- Parameters:
- Timing:

## Expected Result

- Completion/status:
- Parsed fields:
- Pass criteria:
- Fail/skip criteria:

## Safety And Cleanup

- Fixture requirement:
- Abort criteria:
- Cleanup:

## Artifacts

- Inputs:
- Outputs:
- Logs:
```

## `index.md`

Summarize the artifact directory:

- Source and conversion mode.
- Files produced.
- High-level purpose.
- Safety mode.
- Known ambiguities or "None".

## Clarification Policy

Ask only for missing required fields. Do not ask about optional formatting.
Prefer an explicit `Ambiguities And Unsupported Logic` section for issues that
do not block a useful test flow.

Ask when:

- A command/action is present but no expected result or pass/fail criterion is
  available.
- A destructive or device-state-changing flow lacks setup, safety gate, or
  cleanup intent.
- A source references external macros/includes/files that define required steps
  and those files are unavailable.
- The source cannot be read or converted.

Do not ask when:

- A title can be inferred from file name plus first step.
- Timing is absent for steps that do not require timing.
- Cleanup is clearly not needed because all steps are read-only.
- A parameter has no default but is passed through as a required runtime input.

## Validation Checklist

Before returning, verify:

- Input type was detected and the matching reference was used.
- Non-text input was converted with `markitdown`, or a conversion failure was
  reported.
- Purpose/title is present.
- Preconditions/setup include tool, DUT, fixture, and safety constraints when
  relevant.
- Every source step is represented or explicitly skipped with reason.
- Every state-changing or checked step has expected results or pass/fail
  criteria.
- Original commands and parameter names are preserved.
- Timing, waits, retries, loops, and branch conditions are represented.
- Cleanup is present or explicitly marked not required.
- Ambiguous or unsupported logic is flagged.
- Final verify states the overall pass/fail outcome.
- Manifest and coverage matrix agree with `flow.md` when files are produced.
