# Abort Command Facts

| Item | Value |
|---|---|
| Command | Abort |
| Opcode | `08h` |
| Source | NVMe Base Spec 2.0 section 5.1, Figures 140-141 |
| Command set | Admin |
| Data transfer | No data transfer |
| Completion queue | Admin Completion Queue |

## Core Behavior

Abort attempts to abort a previously submitted command identified by `CDW10.SQID` and `CDW10.CID`.

Abort is best effort. Successful completion of the Abort command does not by itself prove that the target command was aborted. The Abort command completion reports the abort result in CQE Dword 0 bit 0.

If the target command is successfully aborted, the aborted command completion is posted to the appropriate Admin or I/O Completion Queue before the Abort command completion is posted to the Admin Completion Queue.
