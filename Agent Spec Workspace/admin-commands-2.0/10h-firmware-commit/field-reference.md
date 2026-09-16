# Firmware Commit Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW10` bits 02:00 | `FS` | Firmware Slot. | `0h` means controller chooses slot 1-7; non-zero selects slot. | Slot validity and image activation target. |
| `CDW10` bits 05:03 | `CA` | Commit Action. | See [selector-reference.md](selector-reference.md). | Replace, activate, immediate activation, or Boot Partition operation. |
| `CDW10` bits 30:06 | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |
| `CDW10` bit 31 | `BPID` | Boot Partition ID. | Applies to Boot Partition commit actions. | Boot Partition replace/active selection. |
| Firmware Commit CQE DW0 bits 01:00 | `MUD` | Multiple Update Detected. | Valid if command is successful or aborted; depends on Identify Controller `SMUD`. | Overlapping update diagnostics. |

