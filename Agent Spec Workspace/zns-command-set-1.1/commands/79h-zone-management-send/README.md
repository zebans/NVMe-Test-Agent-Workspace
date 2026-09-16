# Zone Management Send - Opcode 79h

ZNS 1.1 command reference for requesting an action on one or more zones.

Use this folder when the question is about `ZSA`, Select All, `SLBA`, zone state transition validity, Set Zone Descriptor Extension, active/open resource failures, `Zone Capacity Changed`, or Zone Management Send-specific statuses.

## Read Path

| Need | Read |
|---|---|
| Command identity and transfer model | [command-facts.md](command-facts.md) |
| `ZSA`, Select All, and action/state matrix | [selector-reference.md](selector-reference.md) |
| Command field lookup | [field-reference.md](field-reference.md) |
| Data payload behavior | [payload-reference.md](payload-reference.md) |
| Completion and status lookup | [status-reference.md](status-reference.md) |
| Restrictions and undefined ordering | [restrictions.md](restrictions.md) |
| Base/NVM/ZNS/API ownership boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completion state of this folder | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Zone Management Send is a zone state command. Most questions should start from `selector-reference.md`, because `ZSA` plus the current zone state determines whether the command is a valid transition, a no-op, or an invalid transition.
