# Create I/O Submission Queue Payload Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data / queue memory | `PRP1` | This command uses host memory described by `PRP1`; there is no separate structured command payload table. |
| `PRP1` | SQ memory base or PRP List pointer | Describes the memory used for the new SQ. |
| Completion | CQE on Admin Completion Queue | Reports command completion status. |

## PRP / Queue Memory Rules

| Condition | Rule |
|---|---|
| `PC=1` | `PRP1` is the physically contiguous SQ base address. |
| `PC=0` | `PRP1` is a PRP List pointer for a non-contiguous SQ. |
| Non-zero PRP offset | Should return `PRP Offset Invalid`. |
| PRP List-backed SQ | PRP List shall remain at the same physical location and unmodified until matching Delete I/O SQ completion or controller reset. |
