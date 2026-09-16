# Zone Append Command Facts

Source: ZNS 1.1 section 3.4.1, Figures 22-30, and Figure 12 opcode table.

| Item | Value |
|---|---|
| Command | Zone Append |
| Opcode | `7Dh` |
| Command set | Zoned Namespace Command Set |
| CSI | `02h` |
| Submission queue | I/O Submission Queue |
| Data transfer | Host to controller |
| Support | Optional for ZNS controllers |
| Namespace | `NSID` used; `FFFFFFFFh` not supported unless explicitly allowed |
| Main fields | `ZSLBA`, `NLB`, `PIREMAP`, `ALBA` completion |

## Required Command Behavior

| Area | Requirement |
|---|---|
| Purpose | Writes data and metadata, if applicable, to the zone indicated by `ZSLBA`. |
| Actual write LBA | Controller assigns the actual LBAs within the zone. |
| Completion result | Lowest LBA written is returned as `ALBA` in the CQE. |
| Target zone type | The specified zone shall be Sequential Write Required. |
| `ZSLBA` | Shall be the lowest logical block of the target zone. |
| Ordering | Multiple outstanding Zone Append commands to the same zone have undefined ordering. |
| Atomicity | NVM atomicity parameters apply as defined by the NVM Command Set. |

## Key Difference From Write

The host does not specify the final write LBA. It specifies the target zone, and the controller chooses the write location.
