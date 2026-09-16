# ZNS-Modified Write - Opcode 01h

ZNS 1.1 overlay reference for the NVM Write command.

Use this folder when the question is about ZNS-specific Write behavior: zone boundary, target zone state, write pointer requirement, active/open resource limits, or ZNS status values `B8h`-`BEh`.

## Read Path

| Need | Read |
|---|---|
| Overlay identity and ownership | [command-facts.md](command-facts.md) |
| ZNS condition selectors | [selector-reference.md](selector-reference.md) |
| ZNS-relevant field meaning | [field-reference.md](field-reference.md) |
| Payload ownership | [payload-reference.md](payload-reference.md) |
| ZNS status lookup | [status-reference.md](status-reference.md) |
| Restrictions | [restrictions.md](restrictions.md) |
| NVM/ZNS/API boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completion state | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Write remains an NVM command. This folder only captures the ZNS-added rules: the write range must stay inside one zone, Sequential Write Required zones must be written at the write pointer, and zone state/resource limits can add ZNS statuses.
