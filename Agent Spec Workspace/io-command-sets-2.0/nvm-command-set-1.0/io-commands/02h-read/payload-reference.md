# NVM Read Payload Reference

| Payload surface | Direction | Meaning |
|---|---|---|
| User data buffer | Controller to host | Data read from the selected LBA range. |
| Metadata buffer | Controller to host, if applicable | Metadata associated with each logical block. |
| Protection information | Controller to host or checked according to `PRINFO` | PI behavior is controlled by namespace PI format and command PI fields. |

For deallocated or unwritten logical blocks, returned data behavior depends on DULBE and `DLFEAT`; see Dataset Management deallocated/unwritten logical block rules.
