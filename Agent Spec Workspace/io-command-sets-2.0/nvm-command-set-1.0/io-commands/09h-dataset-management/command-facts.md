# NVM Dataset Management Command Facts

| Item | Value |
|---|---|
| Command | Dataset Management |
| Opcode | `09h` |
| Source | NVM Command Set 1.0 section 3.2.3, Figures 38-43 |
| Data direction | Host to controller |
| Queue | I/O Submission Queue / I/O Completion Queue |
| NSID | Uses Namespace Identifier |
| Payload | List of 16-byte range descriptors |

Dataset Management is advisory. A compliant controller may choose to take no action based on the attributes provided, except where specific deallocation/read behavior is defined.
