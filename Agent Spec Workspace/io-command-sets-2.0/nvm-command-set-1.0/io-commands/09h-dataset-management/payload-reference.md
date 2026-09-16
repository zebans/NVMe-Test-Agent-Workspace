# NVM Dataset Management Payload Reference

Dataset Management transfers a list of 16-byte range descriptors from host to controller.

| Offset per descriptor | Field | Meaning | Important rules |
|---:|---|---|---|
| `03:00` | Context Attributes | Advisory attributes for the range. | Optional information; controller may take no specific action. |
| `07:04` | Length in logical blocks | Number of logical blocks in this range. | One-based value. |
| `15:08` | Starting LBA | First logical block in this range. | 64-bit value. |

## Deallocated Or Unwritten Logical Blocks

| Condition | Returned value / behavior |
|---|---|
| DULBE enabled and Copy/Read/Verify/Compare touches deallocated/unwritten block | Abort with Deallocated or Unwritten Logical Block status. |
| DULBE not enabled and `DLFEAT[2:0]=001b` | Read data/metadata bytes are `00h`. |
| DULBE not enabled and `DLFEAT[2:0]=010b` | Read data/metadata bytes are `FFh`. |
| DULBE not enabled and `DLFEAT[2:0]=000b` | Read data/metadata bytes are either all `00h` or all `FFh`. |
| Deallocated/unwritten PI field | Guard is `FFh` or CRC for returned data/metadata; Application Tag, Storage Tag, and Reference Tag are `FFh`. |

The value read from a deallocated logical block is deterministic until a write occurs to that logical block.
