# NVM Write - Opcode 01h

NVM Command Set 1.0 detail reference for the Write I/O command.

Use this folder when the question is about `SLBA`, `NLB`, `PRINFO`, `FUA`, `LR`, `DTYPE`, `DSPEC`, DSM hints, metadata/protection information, write-protection status, or NVM write payload ownership.

## Read Path

| Need | Read |
|---|---|
| Command identity and source | [command-facts.md](command-facts.md) |
| CDW and field meanings | [field-reference.md](field-reference.md) |
| Selectors and hints | [selector-reference.md](selector-reference.md) |
| Data/metadata payload | [payload-reference.md](payload-reference.md) |
| Shared PI / metadata behavior | [..\..\NVM_PI_METADATA_REFERENCE.md](..\..\NVM_PI_METADATA_REFERENCE.md) |
| Completion and status | [status-reference.md](status-reference.md) |
| Restrictions | [restrictions.md](restrictions.md) |
| NVM/ZNS/API boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completeness state | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Write transfers host data to the namespace LBA range. ZNS write pointer and zone-state rules are not defined here; use the ZNS overlay when the namespace uses `CSI=02h`.
