# Delete I/O Completion Queue Payload Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | None | This command has no data transfer. |
| Completion | CQE on Admin Completion Queue | Reports command completion status. |
| PRP List lifetime | Describes deleted CQ memory, when applicable | May be deallocated after Delete I/O Completion Queue completion. |

## Completion Ordering

The controller posts completion for this command to the Admin Completion Queue. Queue memory / PRP List cleanup belongs after command completion, not before.
