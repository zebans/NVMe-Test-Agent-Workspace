# Format NVM - Opcode 80h

Base Spec 2.0 Admin command reference for formatting NVM media and optionally performing secure erase.

Use this folder when a test or firmware question involves Format NVM scope, `NSID=FFFFFFFFh`, `FNA`, `SES`, `LBAF/LBAFU`, `PI`, `PIL`, `MSET`, `LBAFEE`, destructive behavior, Format in Progress, or `Invalid Format`.

## Read Path

| Need | Read |
|---|---|
| Opcode, transfer direction, and command dwords | [command-facts.md](command-facts.md) |
| Format selectors and scope rules | [selector-reference.md](selector-reference.md) |
| Data payload expectations | [payload-reference.md](payload-reference.md) |
| CDW10 fields and Identify dependencies | [field-reference.md](field-reference.md) |
| Format-specific restrictions | [restrictions.md](restrictions.md) |
| Command-specific statuses | [status-reference.md](status-reference.md) |
| I/O command set ownership | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Coverage status | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Format NVM is destructive. Always resolve scope first: whether the command affects one namespace, all namespaces attached to the controller, or all allocated namespaces in the NVM subsystem depends on `NSID`, secure erase selection, and Identify Controller `FNA` bits.
