# NVM Write Zeroes - Opcode 08h

NVM Command Set 1.0 detail reference for the Write Zeroes I/O command.

Use this folder when the question is about zeroing an LBA range, `DEAC`, `SLBA`, `NLB`, `PRINFO`, `FUA`, `LR`, `WZSL`, PI behavior, or read-after-write-zeroes behavior.

## Read Path

| Need | Read |
|---|---|
| Command identity and source | [command-facts.md](command-facts.md) |
| CDW and field meanings | [field-reference.md](field-reference.md) |
| Selectors | [selector-reference.md](selector-reference.md) |
| Payload / resulting data | [payload-reference.md](payload-reference.md) |
| Shared PI / metadata behavior | [..\..\NVM_PI_METADATA_REFERENCE.md](..\..\NVM_PI_METADATA_REFERENCE.md) |
| Completion and status | [status-reference.md](status-reference.md) |
| Restrictions | [restrictions.md](restrictions.md) |
| NVM/ZNS/API boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completeness state | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |
