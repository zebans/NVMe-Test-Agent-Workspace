# Reservation Report - Opcode 0Eh

Base Spec 2.0 common I/O command reference for returning reservation status information for a namespace.

Use this folder when the question is about `NUMD`, `EDS`, 64-bit versus 128-bit Host Identifier format, `GEN`, `RTYPE`, `REGCTL`, `PTPLS`, registered controller entries, or `Host Identifier Inconsistent Format`.

## Read Path

| Need | Read |
|---|---|
| Command identity and transfer model | [command-facts.md](command-facts.md) |
| `NUMD` / `EDS` selection rules | [selector-reference.md](selector-reference.md) |
| Returned reservation structures | [payload-reference.md](payload-reference.md) |
| Field meaning lookup | [field-reference.md](field-reference.md) |
| Status expectations | [status-reference.md](status-reference.md) |
| Boundaries with reservation state and Host Identifier feature | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completion state of this folder | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Reservation Report is a readback command. The returned payload shape depends on the controller Host Identifier size and the `EDS` bit. If `EDS` does not match the Host Identifier format, the command should fail with `Host Identifier Inconsistent Format`.
