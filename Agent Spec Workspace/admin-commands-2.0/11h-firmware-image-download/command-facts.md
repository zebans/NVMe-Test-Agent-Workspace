# Firmware Image Download Command Facts

| Item | Value |
|---|---|
| Command | Firmware Image Download |
| Opcode | `11h` |
| Source | NVMe Base Spec 2.0 section 5.13, Figures 184-187 |
| Command set | Admin |
| Data transfer | `01b`, host to controller |
| Completion queue | Admin Completion Queue |

## Core Behavior

Firmware Image Download downloads all or part of an image for a future controller update. The new image is not activated by this command; Firmware Commit is required for commit/activation.

An image may be downloaded in multiple pieces. `NUMD` and `OFST` define the dword range for each piece. Firmware portions may be submitted out of order for firmware images, but host software shall submit image portions in order when updating a Boot Partition.

The first Firmware Image Download after a Firmware Commit causes the controller to discard remaining portions of previously downloaded images. If reset occurs between download and Firmware Commit completion, downloaded portions are discarded.
