# NVM Compare Command Facts

| Item | Value |
|---|---|
| Command | Compare |
| Opcode | `05h` |
| Source | NVM Command Set 1.0 section 3.2.1, Figures 19-26 |
| Data direction | Host to controller |
| Queue | I/O Submission Queue / I/O Completion Queue |
| NSID | Uses Namespace Identifier |
| Payload | Comparison data buffer and optional metadata |

Compare reads the specified logical blocks and compares the media data to the host-provided comparison buffer. Any miscompare completes with Compare Failure.
