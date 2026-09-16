# ZNS-Modified Write Field Reference

ZNS does not redefine the base NVM Write command fields. Use the NVM Command Set reference for byte-exact Write fields.

| ZNS-relevant field / derived value | Meaning | Why it matters |
|---|---|---|
| Starting LBA | Start of the base Write range. | Determines target zone and whether write starts at `WP`. |
| Number of Logical Blocks | Length of the base Write range. | Determines whether range crosses a zone boundary. |
| Zone State (`ZS`) | Current target zone state. | Drives Full, Read Only, Offline status conditions. |
| Write Pointer (`WP`) | Next valid write LBA for Sequential Write Required zones. | Write not at `WP` can fail with Zone Invalid Write. |
| Active/Open resource counters | Controller zone resource state. | Drives Too Many Active/Open Zones. |
