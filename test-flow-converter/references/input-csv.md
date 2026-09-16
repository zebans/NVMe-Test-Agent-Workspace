# CSV Input

Use this reference for `.csv` files and spreadsheet-like test schedules.

## Detection

Treat input as CSV when any of these are true:

- Extension is `.csv`.
- Content has delimiter-separated rows with a consistent header.
- Headers resemble `Function`, `Check`, `Parameter`, `Transport`, `Input`,
  `Output`, `ExpectedValue`, `Condition`, `Thread`, `Description`, `Step`, or
  `Command`.

Use a structured CSV parser when possible. Do not split rows with ad hoc string
logic because quoted commas and empty cells are common. If the CSV cannot be
read directly, convert it with `markitdown` and use the resulting Markdown table
while preserving original row numbers.

## Header Mapping

Map common columns as follows:

- `Function`, `Command`, `Action`, `Step`: step command/action name.
- `Check`: whether the row has an explicit check. Preserve markers such as `v`.
- `Parameter`, `Params`, `Arguments`: source parameter string. Preserve names
  and values exactly.
- `Transport`: bus, interface, port, or target path.
- `Input`: input data, file, payload, or source fixture.
- `Output`: output data, expected artifact, or captured field.
- `ExpectedValue`, `Expected`, `Result`: expected result or pass criterion.
- `Condition`: branch condition, skip condition, prerequisite, or guard.
- `Thread`: concurrency group, execution lane, or ordering hint.
- `Description`: human-readable title, purpose detail, or expectation.

If headers are absent, infer columns only when the pattern is obvious and flag
the inference.

## Row Handling

- Ignore fully empty rows but record that trailing empty rows were ignored when
  relevant.
- Preserve one-based source row numbers after the header, or spreadsheet row
  numbers if available.
- Convert each non-empty row into one step unless the row is a continuation of
  the previous command.
- Merge continuation rows only when source formatting clearly indicates they are
  continued parameters or expected results.
- Preserve repeated commands as separate steps unless the source explicitly
  marks them as a loop.

## Parameter Handling

Parse key/value pairs such as `CA=1 FS=2`, `TXLEN=20000 FILE=FW/CA.bin`, or
`TIME=2`. Preserve the original token names and values.

Only reinterpret values when source context supports it. For example, if a CSV
description says `20000` means 128K, document that `TXLEN=20000` is interpreted
as `0x20000` bytes and flag the source-backed assumption. Do not silently change
decimal-looking values to hexadecimal.

## Field Mapping

- Purpose: filename, sheet title, first descriptive rows, or repeated function
  family.
- Setup: prerequisite rows, `PreTest`, transport/device columns, fixture files,
  input files, and dangerous operation context.
- Steps: each effective row in source order.
- Commands/actions: `Function` plus parameter columns.
- Expected results: `ExpectedValue`, `Output`, `Check`, `Condition`, and
  description text.
- Timing: `SLEEP`, `WAIT`, `DELAY`, `TIME=<value>`, timeout parameters, and
  reset wait rows.
- Pass/fail criteria: check markers, expected values, final rows, and explicit
  result columns.
- Cleanup: `PostTest`, `Cleanup`, `TearDown`, reset/recover rows, or final
  state requirements.

## Ambiguity And Unsupported Logic

Flag these conditions:

- Missing headers with multiple plausible column meanings.
- Check marker present but no expected value or description of what to verify.
- Parameters whose base, unit, or encoding is unclear.
- Rows that invoke fixture-specific functions with unknown semantics.
- Concurrent `Thread` groups without ordering rules.
- Destructive commands without fixture/safety/cleanup context.

Ask for clarification only when missing row semantics block required expected
results, safety gates, or cleanup.
