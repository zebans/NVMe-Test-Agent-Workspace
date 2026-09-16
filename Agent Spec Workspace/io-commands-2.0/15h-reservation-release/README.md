# Reservation Release - Opcode 15h

Base Spec 2.0 common I/O command reference for releasing or clearing a namespace reservation.

Use this folder when a test or firmware question involves `RRELA`, `RTYPE`, `IEKEY`, `CRKEY`, release-vs-clear behavior, or reservation type mismatch.

## Read Path

| Need | Read |
|---|---|
| Opcode, transfer direction, and command dwords | [command-facts.md](command-facts.md) |
| Release action and reservation type selectors | [selector-reference.md](selector-reference.md) |
| Host-to-controller data structure | [payload-reference.md](payload-reference.md) |
| CDW10/data structure fields | [field-reference.md](field-reference.md) |
| Explicit status behavior | [status-reference.md](status-reference.md) |
| Boundary to reservation-state rules | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Coverage status | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Reservation Release layout is simple, but Release and Clear are different state operations. For `RRELA=Release`, `RTYPE` shall match the current reservation type.
