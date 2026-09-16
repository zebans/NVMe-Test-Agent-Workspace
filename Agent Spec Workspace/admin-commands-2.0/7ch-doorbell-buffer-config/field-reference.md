# Doorbell Buffer Config Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `PRP1` bits 63:00 | Shadow Doorbell buffer base | Base memory address pointer. | Shall be memory page aligned. | Host-updated shadow doorbells. |
| `PRP2` bits 63:00 | EventIdx buffer base | Base memory address pointer. | Shall be memory page aligned. | Controller-updated EventIdx values. |
| Buffer offset formula | Entry stride | Offset uses `(4 << CAP.DSTRD)` increments. | Applies relative to `PRP1` for Shadow Doorbell and `PRP2` for EventIdx. | Buffer entry lookup. |
| `y` | Queue max index | `y = max(NSQA, NCQA)`. | Determines final SQ/CQ entries represented. | Buffer sizing. |

