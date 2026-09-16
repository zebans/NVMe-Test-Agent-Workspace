# Firmware Commit Status Reference

| Status | Meaning |
|---|---|
| `Invalid Firmware Slot` | Firmware slot is invalid, read only, or exceeds supported slot count. |
| `Invalid Firmware Image` | Firmware image specified for activation is invalid and not loaded. |
| `Firmware Activation Requires Conventional Reset` | Commit succeeded, but activation requires Conventional Reset. |
| `Firmware Activation Requires NVM Subsystem Reset` | Commit succeeded, but activation requires NVM Subsystem Reset. |
| `Firmware Activation Requires Controller Level Reset` | Image cannot be activated without Controller Level Reset; should be returned only for `CA=011b`. |
| `Firmware Activation Requires Maximum Time Violation` | Immediate activation would exceed Identify Controller `MTFA`; re-issue and activate using reset. |
| `Firmware Activation Prohibited` | Image activation is prohibited by vendor specific controller reasons. |
| `Overlapping Range` | Firmware image has overlapping ranges. |
| `Boot Partition Write Prohibited` | Command attempts to modify a locked Boot Partition. |

