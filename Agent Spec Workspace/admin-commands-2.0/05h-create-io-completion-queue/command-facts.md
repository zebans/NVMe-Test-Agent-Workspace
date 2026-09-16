# Create I/O Completion Queue Command Facts

| Item | Value |
|---|---|
| Command | Create I/O Completion Queue |
| Opcode | `05h` |
| Source | NVMe Base Spec 2.0 section 5.4 |
| Command set | Admin |
| Data transfer | `01b`, host to controller |
| Completion queue | Admin Completion Queue |

## Core Behavior

The Create I/O Completion Queue command creates an I/O Completion Queue. The Admin Completion Queue is created by specifying its base address in `ACQ`, not by this command.

The command uses `PRP1`, `CDW10`, and `CDW11`. `PRP1` describes the CQ memory. Other command-specific fields are reserved.

If a PRP List describes a non-contiguous CQ, host software shall keep that PRP List at the same host physical memory location and shall not modify its values until the corresponding Delete I/O Completion Queue completes successfully or controller reset. If modified, behavior is undefined.
