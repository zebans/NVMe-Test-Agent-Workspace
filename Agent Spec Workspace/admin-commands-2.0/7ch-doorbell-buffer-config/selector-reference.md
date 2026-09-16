# Doorbell Buffer Config Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Shadow Doorbell buffer | `PRP1` | 64-bit base memory address pointer to Shadow Doorbell buffer. |
| EventIdx buffer | `PRP2` | 64-bit base memory address pointer to EventIdx buffer. |
| Doorbell stride | `CAP.DSTRD` | Determines spacing between doorbell/EventIdx entries. |
| Queue range | `max(NSQA, NCQA)` | Highest queue index `y` covered by buffer layout. |

