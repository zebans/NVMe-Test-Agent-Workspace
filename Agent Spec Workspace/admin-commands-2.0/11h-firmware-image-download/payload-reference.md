# Firmware Image Download Payload / Completion Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | Firmware or Boot Partition image portion | Transferred from host to controller using `DPTR`. |
| Completion | CQE on Admin Completion Queue | Reports download command status. |
| Firmware Commit CQE DW0 `MUD` | Referenced for overlapping update sequence detection | Same `MUD` format as Firmware Commit may report overlap detection for update sequences. |

## Image Piece Rules

| Condition | Rule |
|---|---|
| Multiple firmware pieces | May be downloaded with separate commands. |
| Firmware image pieces | May be submitted out of order. |
| Boot Partition image pieces | Shall be submitted in order. |
| Overlapping dword ranges | Controller may return `Overlapping Range`. |
| `NUMD` / `OFST` not conforming to `FWUG` | Firmware update may abort/fail with `Invalid Field in Command` or overlap-related status. |

