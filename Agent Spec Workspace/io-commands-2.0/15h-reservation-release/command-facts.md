# Reservation Release Command Facts

Source: NVMe Base Specification 2.0, section 7.4, Figures 398-400.

| Item | Value |
|---|---|
| Command | Reservation Release |
| I/O opcode | `15h` |
| Queue type | I/O Submission Queue |
| Data transfer | Host to controller |
| Data pointer | Used |
| NSID | Used; `FFFFFFFFh` is not supported unless explicitly stated |
| Primary selectors | `RRELA`, `RTYPE`, `IEKEY` |

## Required Behavior

- Uses CDW10 and an 8-byte Reservation Release data structure.
- If PRPs are used, PRP Entry 1 and PRP Entry 2 are used.
- If SGLs are used, SGL Entry 1 is used.
- If `IEKEY=1`, controller shall return `Invalid Field in Command`.
- If `IEKEY=0`, `CRKEY` is checked.
- If `RRELA=Release`, `RTYPE` specifies the reservation type being released and shall match current reservation type.
- All other command-specific fields are reserved.
