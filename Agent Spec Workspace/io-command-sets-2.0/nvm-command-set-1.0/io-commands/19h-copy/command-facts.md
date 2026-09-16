# NVM Copy Command Facts

| Item | Value |
|---|---|
| Command | Copy |
| Opcode | `19h` |
| Source | NVM Command Set 1.0 section 3.2.2, Figures 27-37 |
| Data direction | Host to controller command data payload |
| Queue | I/O Submission Queue / I/O Completion Queue |
| NSID | Uses Namespace Identifier |
| Payload | Source Range Entry list |

Copy copies data from one or more source logical block ranges to one consecutive destination logical block range starting at `SDLBA`.
