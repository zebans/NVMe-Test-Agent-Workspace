# ZNS-Modified Compare Field Reference

ZNS does not redefine base NVM Compare command fields. Use the NVM Command Set reference for byte-exact Compare fields.

| ZNS-relevant value | Meaning | Why it matters |
|---|---|---|
| Starting LBA | Start of the base Compare range. | Determines target zone and boundary checks. |
| Number of Logical Blocks | Length of the base Compare range. | Determines whether range crosses a zone boundary. |
| Zone State (`ZS`) | Current target zone state. | Drives Full, Read Only, Offline status conditions. |
| Active/Open resource counters | Controller zone resource state. | Drives Too Many Active/Open Zones. |
