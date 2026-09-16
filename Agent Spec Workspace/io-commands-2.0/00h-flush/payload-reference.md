# Flush Payload / Completion Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | None | Flush has no data transfer. |
| Completion | CQE on associated I/O Completion Queue | Reports Flush command status. |

## Cache State Behavior

| Condition | Behavior |
|---|---|
| Volatile write cache enabled | Commit data and metadata for specified namespace(s) to non-volatile media. |
| Volatile write cache absent or disabled, sanitize not in progress | Shall complete successfully with no effect. |
| Volatile write cache absent or disabled, sanitize in progress | May complete successfully with no effect. |

