# Reservation Acquire Command Facts

Source: NVMe Base Specification 2.0, section 7.2, Figures 391-394.

| Item | Value |
|---|---|
| Command | Reservation Acquire |
| I/O opcode | `11h` |
| Queue type | I/O Submission Queue |
| Data transfer | Host to controller |
| Data pointer | Used |
| NSID | Used; `FFFFFFFFh` is not supported unless explicitly stated |
| Primary selectors | `RACQA`, `RTYPE`, `IEKEY` |

## Required Behavior

- Uses CDW10 and a 16-byte Reservation Acquire data structure.
- If PRPs are used, PRP Entry 1 and PRP Entry 2 are used.
- If SGLs are used, SGL Entry 1 is used.
- If `IEKEY=1`, controller shall return `Invalid Field in Command`.
- If `IEKEY=0`, `CRKEY` is checked.
- `PRKEY` is used only for Preempt and Preempt and Abort.
- All other command-specific fields are reserved.
