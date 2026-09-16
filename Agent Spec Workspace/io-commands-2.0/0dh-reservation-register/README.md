# Reservation Register - Opcode 0Dh

Base Spec 2.0 common I/O command reference for registering, unregistering, or replacing a reservation key for a namespace.

Use this folder when a test or firmware question involves `RREGA`, `CPTPL`, `IEKEY`, `CRKEY`, `NRKEY`, PTPL state, or reservation key registration.

## Read Path

| Need | Read |
|---|---|
| Opcode, transfer direction, and command dwords | [command-facts.md](command-facts.md) |
| Register action and PTPL selectors | [selector-reference.md](selector-reference.md) |
| Host-to-controller data structure | [payload-reference.md](payload-reference.md) |
| CDW10/data structure fields | [field-reference.md](field-reference.md) |
| Explicit status behavior | [status-reference.md](status-reference.md) |
| Boundary to reservation-state rules | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Coverage status | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Reservation Register changes registrant keys and may change PTPL state. Use this folder for field semantics; use section 8.19 for reservation-state behavior and access conflicts.
