# Zone Management Receive - Opcode 7Ah

ZNS 1.1 command reference for returning zone information from a zoned namespace.

Use this folder when the question is about `ZRA`, Reporting Options, Partial Report, `NUMD`, Report Zones, Extended Report Zones, Zone Descriptor fields, zone state, zone capacity, `ZSLBA`, or write pointer reporting.

## Read Path

| Need | Read |
|---|---|
| Command identity and transfer model | [command-facts.md](command-facts.md) |
| `ZRA`, Reporting Options, and Partial Report | [selector-reference.md](selector-reference.md) |
| Command field lookup | [field-reference.md](field-reference.md) |
| Returned report structures and Zone Descriptor fields | [payload-reference.md](payload-reference.md) |
| Completion and status lookup | [status-reference.md](status-reference.md) |
| Restrictions and result ordering | [restrictions.md](restrictions.md) |
| Base/ZNS/API ownership boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completion state of this folder | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Zone Management Receive is the command to ask "what does this zone currently look like?" For field meaning, go straight to `payload-reference.md`; for filtering and report shape, use `selector-reference.md`.
