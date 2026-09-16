# NVM Verify Payload Reference

Verify has no host data or metadata transfer.

| Surface | Meaning |
|---|---|
| Internal data/metadata read or integrity check | Controller verifies stored information for selected LBAs. |
| SMART/Health Data Units Read | Data read or integrity-checked by Verify is included in the Data Units Read field. |

Verify errors can differ from the errors a Read command would return for the same range.
