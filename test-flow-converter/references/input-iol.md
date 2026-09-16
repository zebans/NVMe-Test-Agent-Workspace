# IOL Input

Use this reference for `.iol` files and IOL/procedure-style test inputs.

## Detection

Treat input as IOL when any of these are true:

- Extension is `.iol`.
- Content is a line-oriented test procedure with labels, blocks, macro calls,
  command/function invocations, parameter lists, `WAIT`/`SLEEP`, `EXPECT`,
  `CHECK`, `VERIFY`, `IF`/`ELSE`, `LOOP`, `CALL`, `INCLUDE`, or fixture
  directives.
- The user identifies the source as IOL.

If the IOL file is encoded or embedded in a non-text container, convert it with
`markitdown` first. If conversion loses columns, indentation, or block
structure, ask for a text export or the original IOL schema.

## Parsing Strategy

Prefer a provided IOL schema or local examples when available. If no schema is
provided, treat IOL as a test DSL and preserve source tokens exactly.

Read in this order:

1. File header and comments for purpose, fixture, transport, DUT, and safety.
2. Global declarations for variables, defaults, aliases, ports, slots,
   namespaces, timing constants, and includes.
3. Procedure blocks, labels, or sections for step boundaries.
4. Command/action statements and their parameter lists.
5. Verification statements such as `EXPECT`, `CHECK`, `VERIFY`, comparisons,
   output captures, and status checks.
6. Control flow such as branches, loops, retries, subroutine calls, and cleanup
   blocks.

## Field Mapping

- Purpose: file header, procedure name, first title/comment, or filename.
- Setup: global fixture declarations, includes, required devices, transport,
  environment, and preconditions.
- Steps: procedure statements in execution order. Preserve labels as
  `source_ref`.
- Commands/actions: command-like statements, fixture operations, function calls,
  reset operations, sends/receives, waits, and sleeps.
- Parameters: exact source parameter names and values from calls or assignments.
- Expected results: `EXPECT`, `CHECK`, `VERIFY`, compare statements, status
  expectations, output matching, and error handling blocks.
- Timing: `WAIT`, `SLEEP`, timeout values, retry counts, polling loops, and
  delay annotations.
- Pass/fail criteria: explicit PASS/FAIL statements, expected status, branch to
  failure labels, assertion outcomes, and final result variables.
- Cleanup: cleanup labels, teardown procedures, rollback calls, reset/recover
  blocks, and fixture release operations.

## Control Flow

Represent IOL control flow without flattening away meaning:

- For `IF`/`ELSE`, include the condition and both outcomes when both affect
  test behavior.
- For loops and retries, include iteration bounds, timeout, break condition,
  and failure condition.
- For `CALL` or macro expansion, inline the called steps only when the called
  content is present. Otherwise preserve the call as a step and flag missing
  expansion.
- For `INCLUDE`, parse included files when available. If unavailable and the
  include defines required commands or checks, ask for the file.

## Ambiguity And Unsupported Logic

Flag these conditions:

- Unknown IOL dialect or missing schema for non-obvious syntax.
- Missing includes, macros, libraries, or fixture definitions.
- Binary payload references that cannot be inspected.
- Branch conditions that rely on runtime data with no expected outcome.
- Commands whose side effects are destructive but have no safety gate.
- Expected results implied by naming only, with no check or pass/fail statement.

Continue with a best-effort flow when source order and required fields remain
clear. Ask for clarification when missing IOL definitions block required steps,
expected results, safety gates, or cleanup.
