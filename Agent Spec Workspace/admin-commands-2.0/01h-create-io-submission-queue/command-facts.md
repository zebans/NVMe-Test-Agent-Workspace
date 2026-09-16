# Create I/O Submission Queue Command Facts

| Item | Value |
|---|---|
| Command | Create I/O Submission Queue |
| Opcode | `01h` |
| Source | NVMe Base Spec 2.0 section 5.5 |
| Command set | Admin |
| Data transfer | `01b`, host to controller |
| Completion queue | Admin Completion Queue |

## Core Behavior

The Create I/O Submission Queue command creates an I/O Submission Queue. The Admin Submission Queue is created by specifying its base address in `ASQ`, not by this command.

The command uses `PRP1`, `CDW10`, `CDW11`, and `CDW12`. `PRP1` describes the SQ memory. Other command-specific fields are reserved.

If a PRP List describes a non-contiguous SQ, host software shall keep that PRP List at the same host physical memory location and shall not modify its values until the corresponding Delete I/O Submission Queue completes or controller reset. If modified, behavior is undefined.
