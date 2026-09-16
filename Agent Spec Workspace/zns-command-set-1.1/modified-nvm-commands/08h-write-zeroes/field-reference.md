# ZNS-Modified Write Zeroes Field Reference

ZNS does not redefine the base NVM Write Zeroes command fields. Use the NVM Command Set reference for byte-exact Write Zeroes fields.

| ZNS-relevant field / derived value | Meaning | Why it matters |
|---|---|---|
| Starting LBA | Start of the base Write Zeroes range. | Determines target zone and boundary checks. |
| Number of Logical Blocks | Length of the base Write Zeroes range. | Determines whether range crosses a zone boundary. |
| Deallocate behavior | Whether Write Zeroes deallocates logical blocks. | ZNS model has additional behavior boundaries here. |
| Zone State (`ZS`) | Current target zone state. | Drives Full, Read Only, Offline status conditions. |
| Write Pointer (`WP`) | Next valid write position. | Drives Zone Invalid Write where applicable. |
| Active/Open resource counters | Controller zone resource state. | Drives Too Many Active/Open Zones. |
