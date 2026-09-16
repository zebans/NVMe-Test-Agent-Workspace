# Flush Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 7.1 |
| Command | Flush |
| Opcode | `00h` |
| State | COMPLETE |

## Coverage Checklist

- [x] Command purpose and no data transfer.
- [x] `NSID` and `VWC[2:1]` behavior.
- [x] `NSID=FFFFFFFFh` cases.
- [x] Volatile write cache enabled/disabled behavior.
- [x] Sanitize interaction note.
- [x] Status and completion behavior.
- [x] SPEC/API/test-flow boundary stated.
