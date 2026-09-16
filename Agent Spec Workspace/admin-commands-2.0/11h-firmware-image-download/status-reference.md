# Firmware Image Download Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Overlapping Range` | Firmware image has overlapping ranges; may indicate `FWUG` granularity/alignment mismatch. | Image range construction is invalid. |
| `Invalid Field in Command` | `NUMD` or `OFST` does not meet `FWUG` requirement. | Alignment/granularity validation failure. |

## Notes

`Overlapping Range` is the command-specific status listed for Firmware Image Download. `Invalid Field in Command` is explicitly called out by the `NUMD`/`OFST` field rules as an important validation result.

