# NVM Get LBA Status - Admin Opcode 86h

NVM Command Set 1.0 detail reference for the Get LBA Status Admin command.

Use this folder when the question is about `SLBA`, `MNDW`, `ATYPE`, `RL`, LBA Status Descriptor List, Completion Condition, Tracked LBAs, Untracked LBAs, or the relationship between Get Log Page `LID=0Eh` and Get LBA Status.

## Read Path

| Need | Read |
|---|---|
| Command identity and source | [command-facts.md](command-facts.md) |
| CDW and field meanings | [field-reference.md](field-reference.md) |
| `ATYPE` / range selectors | [selector-reference.md](selector-reference.md) |
| Returned data buffer layout | [payload-reference.md](payload-reference.md) |
| Completion and status behavior | [status-reference.md](status-reference.md) |
| Restrictions and sequencing | [restrictions.md](restrictions.md) |
| Base / ZNS / API boundaries | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completeness state | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Quick Meaning

Get LBA Status asks the controller to report LBAs in a selected range that may become unrecoverable when read. It is normally used after the host reads the NVM LBA Status Information log page (`LID=0Eh`) and receives LBA ranges that should be examined.
