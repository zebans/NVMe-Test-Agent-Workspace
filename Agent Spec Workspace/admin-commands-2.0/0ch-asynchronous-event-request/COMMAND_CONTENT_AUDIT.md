# Asynchronous Event Request Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.2 |
| Figures | 142-148 |
| Command | Asynchronous Event Request |
| Opcode | `0Ch` |
| State | COMPLETE |

## Coverage Checklist

- [x] No command-specific input fields.
- [x] No timeout behavior.
- [x] Identify Controller `AERL` limit.
- [x] AER completion DW0 bit fields.
- [x] Event type values.
- [x] Event information values from Figures 144-148.
- [x] Event masking, retention, and clearing behavior.
- [x] Command-specific status.
- [x] SPEC/API/test-flow boundary stated.
