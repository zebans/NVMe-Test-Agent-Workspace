# Virtualization Management Payload / Completion Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | None | No data transfer. |
| Completion | CQE on Admin Completion Queue | Reports command status. |
| CQE DW0 bits 15:00 | `NRM` | Number of Controller Resources Modified for Primary Controller Flexible Allocation and Secondary Controller Assign. |

## Completion Note

`NRM` may be smaller or larger than the requested `NR`; do not assume exact equality unless the operation requires it elsewhere.

