# Disconnect Payload Reference

Disconnect has no data transfer.

## Response Fields

| Response field | Meaning |
|---|---|
| Response bytes `07:00` | Reserved. |
| `SQHD` | Current Submission Queue Head pointer for the associated Submission Queue. |
| `CID` | Completed command identifier. |
| `STS` | Command status. |

## Completion Ordering

The Disconnect completion queue entry shall be the last entry submitted to the I/O Completion Queue by the controller.
