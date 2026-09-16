# Property Get Status Reference

## Completion

Property Get response returns the requested property value and command status.

| Response field | Meaning |
|---|---|
| `VALUE` | Requested property value. |
| `SQHD` | Current Submission Queue Head pointer for the associated Submission Queue. |
| `CID` | Completed command identifier. |
| `STS` | Command status. |

## Status

| Status | When it applies |
|---|---|
| Invalid Field in Command | Invalid property or invalid offset. |
| Invalid Field in Command | Reserved `FCTYPE`. |
| Invalid Field in Command | Sent on an I/O Queue even though the command is not supported on I/O Queues. |

Figure 97 does not define a Property Get-specific command-specific status.
