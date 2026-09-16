# NVM Write Zeroes Command Facts

| Item | Value |
|---|---|
| Command | Write Zeroes |
| Opcode | `08h` |
| Source | NVM Command Set 1.0 section 3.2.8, Figures 71-76 |
| Data direction | No user data transfer |
| Queue | I/O Submission Queue / I/O Completion Queue |
| NSID | Uses Namespace Identifier |
| Payload | No command data payload; command writes zero values through controller behavior |

Write Zeroes sets a range of logical blocks to zero. After successful completion, subsequent reads of the range return all bytes cleared to `0h` until a write occurs to the range.
