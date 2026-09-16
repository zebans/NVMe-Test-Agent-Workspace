# NVM Write Uncorrectable Command Facts

| Item | Value |
|---|---|
| Command | Write Uncorrectable |
| Opcode | `04h` |
| Source | NVM Command Set 1.0 section 3.2.7, Figures 68-70 |
| Data direction | No data transfer |
| Queue | I/O Submission Queue / I/O Completion Queue |
| NSID | Uses Namespace Identifier |
| Payload | No command data payload |

Write Uncorrectable marks a range of logical blocks as invalid. Reads after this operation fail with Unrecovered Read Error until a write operation clears the invalid logical block status.
