# Firmware Commit Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Firmware Slot | `CDW10.FS` bits 02:00 | Firmware slot used for the commit action; `0h` lets the controller choose a slot. |
| Commit Action | `CDW10.CA` bits 05:03 | Action applied to a downloaded or existing image / Boot Partition. |
| Boot Partition ID | `CDW10.BPID` bit 31 | Boot Partition used for Boot Partition commit actions. |

## Commit Action Values

| `CA` | Meaning |
|---|---|
| `000b` | Replace image in specified Firmware Slot; do not activate. |
| `001b` | Replace image in specified Firmware Slot; activate at next Controller Level Reset. |
| `010b` | Activate existing image in specified Firmware Slot at next Controller Level Reset. |
| `011b` | Replace image and activate immediately, or activate existing image immediately if no newly downloaded image exists. |
| `100b`-`101b` | Reserved. |
| `110b` | Replace Boot Partition specified by `BPID`. |
| `111b` | Mark Boot Partition specified by `BPID` as active and update `BPINFO.ABPID`. |

