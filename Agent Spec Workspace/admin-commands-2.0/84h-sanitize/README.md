# Sanitize - Opcode 84h

Base Spec 2.0 Admin command reference for starting sanitize operations or recovering from failed sanitize operations.

Use this folder when a test or firmware question involves `SANACT`, `AUSE`, `OWPASS`, `OIPBP`, `NDAS`, `OVRPAT`, PMR restrictions, pending firmware activation, Sanitize Status log behavior, sanitize failure recovery, or background sanitize progress.

## Read Path

| Need | Read |
|---|---|
| Opcode, transfer direction, and command dwords | [command-facts.md](command-facts.md) |
| Sanitize action selector | [selector-reference.md](selector-reference.md) |
| Data payload expectations | [payload-reference.md](payload-reference.md) |
| CDW10/CDW11 field meanings | [field-reference.md](field-reference.md) |
| Sanitize restrictions and state behavior | [restrictions.md](restrictions.md) |
| Command-specific statuses | [status-reference.md](status-reference.md) |
| Boundary to section 8.21 and Sanitize Status Log | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Coverage status | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Sanitize command completion only means the command was accepted or rejected. It does not mean the sanitize operation is complete. Use Get Log Page `LID=81h` Sanitize Status to observe operation progress and final state.
