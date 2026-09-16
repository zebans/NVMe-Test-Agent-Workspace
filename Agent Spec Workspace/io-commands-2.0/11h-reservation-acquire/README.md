# Reservation Acquire - Opcode 11h

Base Spec 2.0 common I/O command reference for acquiring, preempting, or preempting and aborting a namespace reservation.

Use this folder when a test or firmware question involves `RACQA`, `RTYPE`, `IEKEY`, `CRKEY`, `PRKEY`, reservation type encoding, preempt/preempt-and-abort behavior, or reservation-state conflicts.

## Read Path

| Need | Read |
|---|---|
| Opcode, transfer direction, and command dwords | [command-facts.md](command-facts.md) |
| Reservation action and type selectors | [selector-reference.md](selector-reference.md) |
| Host-to-controller data structure | [payload-reference.md](payload-reference.md) |
| CDW10/data structure fields | [field-reference.md](field-reference.md) |
| Explicit status behavior | [status-reference.md](status-reference.md) |
| Boundary to reservation-state rules | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Coverage status | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Reservation Acquire command layout is simple, but the behavior is stateful. Use this folder for command fields and valid selector values; use section 8.19 rules for reservation conflict, key ownership, and access-permission behavior.
