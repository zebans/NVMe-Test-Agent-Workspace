# Device Self-test Payload / Log Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | None | Device Self-test has no data transfer. |
| Completion | CQE on Admin Completion Queue | Posted after the actions defined by command processing are taken. |
| Device Self-test Log | Log Identifier `06h` | Stores current self-test status and previous self-test results. |

## Command Processing Summary

| Self-test in progress | New `STC` | Controller action |
|---|---|---|
| Yes | `1h` short or `2h` extended | Abort new Device Self-test command with `Device Self-test in Progress`. |
| Yes | `Eh` vendor specific | Vendor specific. |
| Yes | `Fh` abort | Abort current self-test, create newest result log entry, set Current Device Self-test Status to `0h`, complete successfully. |
| No | `1h` short | Validate parameters, set Current Device Self-test Status to `1h`, start self-test, complete successfully. |
| No | `2h` extended | Validate parameters, set Current Device Self-test Status to `2h`, start self-test, complete successfully. |
| No | `Eh` vendor specific | Vendor specific. |
| No | `Fh` abort | Complete successfully; Device Self-test Log is not modified. |

