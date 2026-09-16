# NVM Write Payload Reference

| Payload surface | Direction | Meaning |
|---|---|---|
| User data buffer | Host to controller | Data written into the selected LBA range. |
| Metadata buffer | Host to controller, if applicable | Metadata associated with each logical block. |
| Protection information | Host to controller or generated/checked according to `PRINFO` | PI behavior is controlled by namespace PI format and command PI fields. |

No command-specific returned data buffer is defined for successful Write completion.
