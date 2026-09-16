# Authentication Send Status Reference

## Completion

Authentication Send response provides status for the command.

| Response field | Meaning |
|---|---|
| Response bytes `07:00` | Reserved. |
| `SQHD` | Current Submission Queue Head pointer for the associated Submission Queue. |
| `CID` | Completed command identifier. |
| `STS` | Command status. |

## Status

| Status | When it applies |
|---|---|
| Invalid Parameter | Reserved `SECP` value. |

Figure 97 note excludes Authentication Send from the `Authentication Required` status condition.

Transport-specific status values `B0h` to `BFh` are owned by the applicable NVMe Transport binding specification.
