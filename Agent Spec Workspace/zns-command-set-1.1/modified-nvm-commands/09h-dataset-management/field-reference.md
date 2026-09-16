# ZNS-Modified Dataset Management Field Reference

ZNS does not redefine base Dataset Management command fields or data structures.

| ZNS-relevant value | Meaning | Why it matters |
|---|---|---|
| Dataset-specified LBA range / zone | Zone affected by the Dataset Management operation. | Offline state drives `Zone Is Offline`. |
| Zone State (`ZS`) | Current zone state. | `ZSO:Offline` can abort the command. |
