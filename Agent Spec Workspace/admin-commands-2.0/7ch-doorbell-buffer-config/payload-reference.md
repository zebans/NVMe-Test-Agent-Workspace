# Doorbell Buffer Config Buffer Layout Reference

| Entry | Offset in buffer | Meaning |
|---|---|---|
| Submission Queue 0 Tail | `00h` to `03h` | Admin SQ Tail Doorbell or EventIdx. |
| Completion Queue 0 Head | `00h + (1 * (4 << CAP.DSTRD))` to `03h + (1 * (4 << CAP.DSTRD))` | Admin CQ Head Doorbell or EventIdx. |
| Submission Queue 1 Tail | `00h + (2 * (4 << CAP.DSTRD))` to `03h + (2 * (4 << CAP.DSTRD))` | SQ 1 Tail Doorbell or EventIdx. |
| Completion Queue 1 Head | `00h + (3 * (4 << CAP.DSTRD))` to `03h + (3 * (4 << CAP.DSTRD))` | CQ 1 Head Doorbell or EventIdx. |
| Submission Queue y Tail | `00h + (2y * (4 << CAP.DSTRD))` to `03h + (2y * (4 << CAP.DSTRD))` | SQ y Tail Doorbell or EventIdx. |
| Completion Queue y Head | `00h + ((2y + 1) * (4 << CAP.DSTRD))` to `03h + ((2y + 1) * (4 << CAP.DSTRD))` | CQ y Head Doorbell or EventIdx. |

`y` is `max(NSQA, NCQA)`. Offsets are relative to `PRP1` for the Shadow Doorbell buffer and to `PRP2` for the EventIdx buffer.

