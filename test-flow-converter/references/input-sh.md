# Shell Script Input

Use this reference for `.sh` files and shell-like inputs.

## Detection

Treat input as shell when any of these are true:

- Extension is `.sh`.
- First line contains `#!/bin/sh`, `#!/usr/bin/env bash`, or another shell
  shebang.
- Content includes shell functions, `set -`, `if [`, `[[`, `case`, `for`,
  `while`, `trap`, command substitutions, or environment default patterns such
  as `NAME="${NAME:-value}"`.

For shell scripts, read the script text directly. `markitdown` is not required
unless the script is embedded in a non-text container.

## Extraction

Read the script in this order:

1. Header comments: purpose, usage, high-level step list, environment variables,
   fixture requirements, and warnings.
2. Preflight checks: root checks, required tools, argument validation, device
   existence, file existence, and capability gates.
3. Defaults and parameters: CLI arguments, environment defaults, local
   constants, output directories, filenames, generated keys, and random choices.
4. Helper functions: command wrappers, parsers, verification functions,
   counters, summary writers, cleanup traps, and not-applicable exits.
5. Main execution: section logs, command calls, loops, branch conditions, and
   final summary.

Preserve exact command names, options, variable names, parameter names, and
source expressions. Normalize only when adding explanatory context, such as
mapping `--rrela=1` to `RRELA=001b Clear` while keeping the original option.

## Field Mapping

- Purpose: header title, comments after "Test flow", or the script filename.
- Setup: root/tool checks, required arguments, DUT/fixture checks, required
  files, capability checks, and environment variables.
- Steps: section markers, numbered comments, `log_section` calls, or main-order
  command groups.
- Commands: exact external command invocation, including redirection targets
  when relevant.
- Parameters: CLI args, environment variables, derived variables, constants,
  option values, and parser inputs.
- Expected results: `verify_*` calls, `record_pass`, `record_fail`, assertions,
  comparisons, parsed field checks, expected exit status, and summary result.
- Timing: `sleep`, timeout variables, retry loops, polling intervals, and waits
  after reset or activation.
- Pass/fail criteria: exit code, counters, `summary.json`, `PASS`/`FAIL` text,
  skip/not-applicable branches, and fatal error paths.
- Cleanup: `trap`, `rm`, rollback commands, clear/unregister operations, reset
  recovery, and final state checks.
- Artifacts: logs, binary dumps, JSON outputs, temp files, output directories,
  decoded command output, and reports.

## Control Flow

Represent loops and branches explicitly:

- For bounded loops over ports, namespaces, rows, slots, or directions, write a
  loop step or "repeat steps X-Y" with roles and stop condition.
- For capability gates, write the skip/not-applicable condition and downstream
  impact.
- For random selection, preserve the random behavior and list the candidate
  set. Flag it if deterministic test selection is required.
- For helper functions used repeatedly, summarize the common verify behavior
  once, then reference it from steps.

## Ambiguity And Unsupported Logic

Flag these conditions:

- `eval`, dynamically generated commands, or commands assembled from unknown
  external data.
- `source` or `.` includes that are unavailable.
- External helper programs whose behavior defines pass/fail but whose source is
  unavailable.
- Runtime-discovered device topology where the exact selected device cannot be
  known from static input.
- Destructive cleanup without an ownership or isolation gate.
- Randomized selection without seed or deterministic override.
- Parser assumptions based on command output formats that may vary.

If flagged logic does not block a useful flow, include it in
`Ambiguities And Unsupported Logic` and continue. Ask for clarification only if
it removes a required command, expected result, safety gate, or cleanup decision.
