# Reservation Register Command Facts

Source: NVMe Base Specification 2.0, section 7.3, Figures 395-397.

| Item | Value |
|---|---|
| Command | Reservation Register |
| I/O opcode | `0Dh` |
| Queue type | I/O Submission Queue |
| Data transfer | Host to controller |
| Data pointer | Used |
| NSID | Used; `FFFFFFFFh` is not supported unless explicitly stated |
| Primary selectors | `RREGA`, `CPTPL`, `IEKEY` |

## Required Behavior

- Uses CDW10 and a 16-byte Reservation Register data structure.
- If PRPs are used, PRP Entry 1 and PRP Entry 2 are used.
- If SGLs are used, SGL Entry 1 is used.
- `IEKEY=1` causes actions that use `CRKEY` to succeed regardless of the `CRKEY` value.
- If Reservation Persistence Feature is saveable, PTPL changes from `CPTPL` apply to both current and saved values.
- All other command-specific fields are reserved.
