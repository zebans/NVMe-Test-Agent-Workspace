# Zone Append - Opcode 7Dh

ZNS 1.1 command reference for appending data to a Sequential Write Required zone.

Use this folder when the question is about `ZSLBA`, controller-assigned write LBA, `ALBA`, `NLB`, `PIREMAP`, Zone Boundary Error, zone full/read-only/offline status, active/open resource limits, or Zone Append ordering.

## Read Path

| Need | Read |
|---|---|
| Command identity and transfer model | [command-facts.md](command-facts.md) |
| Command selectors and PI-specific selector behavior | [selector-reference.md](selector-reference.md) |
| Command field lookup | [field-reference.md](field-reference.md) |
| Data/metadata and PI payload behavior | [payload-reference.md](payload-reference.md) |
| Completion `ALBA` and status lookup | [status-reference.md](status-reference.md) |
| Zone, ordering, PI, and atomicity restrictions | [restrictions.md](restrictions.md) |
| Base/NVM/ZNS/API ownership boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completion state of this folder | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Zone Append is not a normal Write with a different opcode. The host chooses the zone through `ZSLBA`, but the controller chooses the actual written LBA and returns it as `ALBA`.
