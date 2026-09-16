# Property Set Status Reference

## Completion

Property Set response provides status for the Property Set command.

| Response field | Meaning |
|---|---|
| `SQHD` | Current Submission Queue Head pointer for the associated Submission Queue. |
| `CID` | Completed command identifier. |
| `STS` | Command status. |

## Status

| Status | When it applies |
|---|---|
| Invalid Field in Command | Invalid property or invalid offset. |
| Invalid Field in Command | Reserved `FCTYPE`. |
| Invalid Field in Command | Sent on an I/O Queue even though the command is not supported on I/O Queues. |

Figure 97 does not define a Property Set-specific command-specific status.
