---
name: test-flow-converter
description: Convert shell scripts (.sh), plain text test descriptions, IOL files, and CSV files into standardized test flows. Use when Codex needs to detect a test input type, extract purpose, setup, steps, commands, parameters, expected results, timing, pass/fail criteria, and cleanup, normalize them into a common structure, preserve original commands and parameter names, flag ambiguous or unsupported logic, ask clarification only for missing required fields, and validate the final test flow.
---

# Test Flow Converter

Convert test source inputs into a standardized test flow while preserving source
traceability and original command/parameter names.

## Workflow

1. Read `references/test-flow-format.md` for the common intermediate structure,
   output artifacts, and validation checklist.
2. Detect the input type from extension and content:
   - `.sh`, shebangs, shell functions, `set -`, or shell control syntax: read
     `references/input-sh.md`.
   - `.iol` extension or IOL/procedure-style syntax: read
     `references/input-iol.md`.
   - `.csv` extension, delimited rows, or spreadsheet-style headers: read
     `references/input-csv.md`.
   - Unstructured requirements, screenshots converted to text, numbered steps,
     or prose: read `references/input-text.md`.
3. If the input is not directly readable text, convert it with `markitdown`
   first. Save or reference the converted Markdown as `converted.md`, then use
   that text as the source while retaining the original file path.
4. Extract purpose, setup, steps, commands/actions, parameters, expected results,
   timing, pass/fail criteria, artifacts, safety gates, and cleanup.
5. Normalize the extracted content into the intermediate structure from
   `test-flow-format.md`.
6. Generate the standardized flow. Preserve original commands, option spelling,
   parameter names, register names, enum values, row numbers, labels, and source
   identifiers. Expand implied verification only when it is strongly supported
   by the source or domain context.
7. Flag ambiguity or unsupported logic instead of silently resolving it.
8. Ask the user for clarification only when a required field is missing and a
   safe, source-backed default cannot be inferred.
9. Validate the final flow against the checklist before returning it.

## Required Fields

Ask for clarification if any of these are missing after source extraction and
cannot be safely inferred:

- Test title or purpose.
- At least one executable step, command, or action.
- Expected result or pass/fail criterion for each state-changing or checked
  step.
- Setup/safety constraints for destructive, firmware, reservation, reset, or
  device-state-changing flows.
- Cleanup requirement, or an explicit statement that cleanup is not required.

## Output

When creating files, produce a skill-consistent artifact directory containing:

- `flow.md`: human-readable standardized test flow.
- `manifest.yaml`: machine-readable normalized flow.
- `coverage-matrix.md`: source-to-flow coverage and reviewer checks.
- `test-template.md`: per-step implementation template.
- `index.md`: short artifact index.
- `converted.md`: only when the input required conversion or the converted text
  is useful for traceability.

When answering inline, return the `flow.md` content and a short validation note.

Do not execute generated test commands unless the user explicitly asks.
