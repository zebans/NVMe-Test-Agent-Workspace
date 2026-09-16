# NVM Copy Payload Reference

Copy transfers a Source Range Entry list from host to controller.

## Descriptor Format 0h

| Offset per entry | Field | Meaning |
|---:|---|---|
| `07:00` | Reserved | Reserved. |
| `15:08` | Starting LBA | Source range start. |
| `19:16` | Read Parameters | Includes zero-based `NLB`. |
| `27:24` | `ELBST` / `EILBRT` portion | Source read PI expected tag fields. |
| `29:28` | `ELBAT` | Expected Application Tag. |
| `31:30` | `ELBATM` | Expected Application Tag Mask. |

## Descriptor Format 1h

| Offset per entry | Field | Meaning |
|---:|---|---|
| `07:00` | Reserved | Reserved. |
| `15:08` | Starting LBA | Source range start. |
| `19:16` | Read Parameters | Includes zero-based `NLB`. |
| `35:26` | `ELBST` / `EILBRT` portion | Source read PI expected tag fields. |
| `37:36` | `ELBAT` | Expected Application Tag. |
| `39:38` | `ELBATM` | Expected Application Tag Mask. |

The destination LBAs are written consecutively starting at `SDLBA`, in the same order as the Source Range Entries.
