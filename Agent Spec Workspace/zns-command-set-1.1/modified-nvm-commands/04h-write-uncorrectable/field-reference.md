# ZNS-Modified Write Uncorrectable Field Reference

ZNS does not redefine base NVM Write Uncorrectable command fields. Use the NVM Command Set reference for byte-exact fields.

| ZNS-relevant value | Meaning | Why it matters |
|---|---|---|
| Starting LBA | Start of the base range. | Determines target zone and boundary checks. |
| Number of Logical Blocks | Length of the base range. | Determines whether range crosses a zone boundary. |
| Write Pointer (`WP`) | Next valid write position. | Drives Zone Invalid Write where applicable. |
| Zone State (`ZS`) | Current target zone state. | Drives Full, Read Only, Offline status conditions. |
| Active/Open resource counters | Controller zone resource state. | Drives Too Many Active/Open Zones. |
