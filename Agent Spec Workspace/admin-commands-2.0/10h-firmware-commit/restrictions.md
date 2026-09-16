# Firmware Commit Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| Firmware slot must be valid | `FS` cannot exceed supported slot count or refer to read-only invalid slot. | `Invalid Firmware Slot`. |
| Image must be valid before activation | Activation actions require a valid downloaded or placed image. | `Invalid Firmware Image`. |
| Immediate activation may be refused | Reset type, max activation time, or vendor policy may block immediate activation. | Firmware activation reset/prohibited statuses. |
| Boot Partition must be unlocked for modification | Locked Boot Partition cannot be written. | `Boot Partition Write Prohibited`. |
| Overlapping update sequences should not be used | Multiple firmware/boot update sequences may be detected. | `MUD` in CQE DW0 and/or overlap-related status. |

