# Firmware Commit Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.12 |
| Figures | 181-183 |
| Command | Firmware Commit |
| Opcode | `10h` |
| State | COMPLETE |

## Coverage Checklist

- [x] `CDW10.FS`, `CDW10.CA`, and `CDW10.BPID`.
- [x] Commit Action value table.
- [x] Firmware Commit CQE DW0 `MUD`.
- [x] Firmware activation reset requirement statuses.
- [x] Boot Partition status boundary.
- [x] SPEC/API/test-flow boundary stated.
