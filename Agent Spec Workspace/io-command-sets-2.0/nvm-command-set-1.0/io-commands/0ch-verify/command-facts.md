# NVM Verify Command Facts

| Item | Value |
|---|---|
| Command | Verify |
| Opcode | `0Ch` |
| Source | NVM Command Set 1.0 section 3.2.5, Figures 53-58 |
| Data direction | No data transfer |
| Queue | I/O Submission Queue / I/O Completion Queue |
| NSID | Uses Namespace Identifier |
| Payload | No user data or metadata transferred to host |

Verify reads or checks stored data/metadata integrity for the selected LBA range without transferring data or metadata to the host.
