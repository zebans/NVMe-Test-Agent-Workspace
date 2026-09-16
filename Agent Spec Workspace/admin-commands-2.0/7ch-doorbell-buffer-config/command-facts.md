# Doorbell Buffer Config Command Facts

| Item | Value |
|---|---|
| Command | Doorbell Buffer Config |
| Opcode | `7Ch` |
| Source | NVMe Base Spec 2.0 section 5.8, Figures 167-169 |
| Command set | Admin |
| Data transfer | No command data buffer; uses PRP1/PRP2 buffer pointers |
| NSID usage | No |
| Completion queue | Admin Completion Queue |

## Core Behavior

Doorbell Buffer Config configures the Shadow Doorbell buffer and EventIdx buffer. `PRP1` points to the Shadow Doorbell buffer; `PRP2` points to the EventIdx buffer.

The Shadow Doorbell buffer is updated by the host. The EventIdx buffer is updated by the para-virtualized controller. Both buffers shall be memory page aligned.
