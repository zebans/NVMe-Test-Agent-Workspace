# ZNS-Modified Read Field Reference

ZNS does not redefine base NVM Read command fields. Use the NVM Command Set reference for byte-exact Read fields.

| ZNS-relevant value | Meaning | Why it matters |
|---|---|---|
| Starting LBA | Start of the base Read range. | Determines target zone and boundary checks. |
| Number of Logical Blocks | Length of the base Read range. | Determines whether range crosses a zone boundary. |
| Zone State (`ZS`) | Current target zone state. | Offline state drives `Zone Is Offline`. |
