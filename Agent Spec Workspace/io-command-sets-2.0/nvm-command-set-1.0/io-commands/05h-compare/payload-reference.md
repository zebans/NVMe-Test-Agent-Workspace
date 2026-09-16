# NVM Compare Payload Reference

| Payload surface | Direction | Meaning |
|---|---|---|
| Comparison data buffer | Host to controller | Expected user data for the selected LBA range. |
| Metadata buffer | Host to controller, if applicable | Expected metadata, excluding protection information. |
| Protection information fields | Command fields / metadata path | Checked according to `PRINFO`, `STC`, and expected tag fields. |

No command-specific returned data buffer is defined for successful Compare completion.
