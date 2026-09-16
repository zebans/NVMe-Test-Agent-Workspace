# Firmware Commit Command Facts

| Item | Value |
|---|---|
| Command | Firmware Commit |
| Opcode | `10h` |
| Source | NVMe Base Spec 2.0 section 5.12, Figures 181-183 |
| Command set | Admin |
| Data transfer | No data transfer |
| Completion queue | Admin Completion Queue |

## Core Behavior

Firmware Commit modifies a firmware image or Boot Partition. For firmware image updates, it verifies that a valid image has been downloaded and commits that revision to a firmware slot. It may also select an image for activation at a reset or attempt immediate activation.

For Boot Partitions, the command may replace a Boot Partition or mark a Boot Partition as active.

Firmware Commit uses `CDW10`. Other command-specific fields are reserved.
