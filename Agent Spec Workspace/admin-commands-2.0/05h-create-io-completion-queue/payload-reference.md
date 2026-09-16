# Create I/O Completion Queue Payload Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data / queue memory | `PRP1` | This command uses host memory described by `PRP1`; there is no separate structured command payload table. |
| `PRP1` | CQ memory base or PRP List pointer | Describes the memory used for the new CQ. |
| Completion | CQE on Admin Completion Queue | Reports command completion status. |

## PRP / Queue Memory Rules

| Condition | Rule |
|---|---|
| `PC=1` | `PRP1` is the physically contiguous CQ base address. |
| `PC=0` | `PRP1` is a PRP List pointer for a non-contiguous CQ. |
| Non-zero PRP offset | Should return `PRP Offset Invalid`. |
| PRP List-backed CQ | PRP List shall remain at the same physical location and unmodified until matching Delete I/O CQ completion or controller reset. |
