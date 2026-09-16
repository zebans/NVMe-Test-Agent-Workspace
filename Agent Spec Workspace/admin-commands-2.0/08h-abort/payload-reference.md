# Abort Payload / Completion Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | None | Abort has no data transfer. |
| Abort completion | CQE on Admin Completion Queue | Reports Abort command status and result. |
| Abort CQE DW0 bit 0 | Abort result | `0` means target command was aborted; `1` means target command was not aborted. |
| Aborted target completion | CQE on target command's completion queue | If target is aborted, this CQE is posted before Abort command completion. |

