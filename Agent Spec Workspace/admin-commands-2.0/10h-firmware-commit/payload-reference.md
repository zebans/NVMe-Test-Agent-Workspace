# Firmware Commit Payload / Completion Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | None | Firmware Commit has no data transfer. |
| Completion | CQE on Admin Completion Queue | Reports Firmware Commit command status. |
| CQE DW0 bits 01:00 | `MUD` | Reports overlapping firmware/boot partition update command sequence detection. |

## `MUD` Bits

| Bit | Meaning |
|---|---|
| 1 | Overlapping update sequence detected due to processing a command from a Management Endpoint. |
| 0 | Overlapping update sequence detected due to processing a command from an Admin Submission Queue on a controller. |

If Identify Controller `SMUD` is cleared, `MUD` shall be cleared to `00b`.

