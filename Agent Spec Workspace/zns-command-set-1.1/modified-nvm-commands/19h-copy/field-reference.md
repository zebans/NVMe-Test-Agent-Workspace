# ZNS-Modified Copy Field Reference

ZNS does not redefine the base NVM Copy command fields or Source Range Entry structure. Use the NVM Command Set reference for byte-exact fields.

| ZNS-relevant value | Side | Meaning | Why it matters |
|---|---|---|---|
| Source Range Entry LBA/length | Source | Source range selected by the base Copy payload. | May cross zone boundary; may touch Offline source zone. |
| Destination LBA range | Destination | Destination range selected by the base Copy command. | May cross zone boundary; must respect destination zone state and write pointer. |
| Destination Write Pointer (`WP`) | Destination | Next valid write LBA. | Destination write not at `WP` can fail with Zone Invalid Write. |
| Zone State (`ZS`) | Source/destination | Current zone state. | Drives Full, Read Only, Offline statuses. |
| Active/Open resource counters | Destination / controller | Controller zone resource state. | Drives Too Many Active/Open Zones. |
