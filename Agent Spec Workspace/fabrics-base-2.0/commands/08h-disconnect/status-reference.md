# Disconnect Status Reference

## Completion

Disconnect response provides status for the command. Its CQE shall be the last entry submitted to the I/O Completion Queue by the controller.

## Command-Specific Status Values

| Value | Status | Applicability |
|---:|---|---|
| `80h` | Incompatible Format | Unsupported `RECFMT`. |
| `81h` | Controller Busy | Controller cannot disconnect the I/O Queue at the current time. |
| `85h` | Invalid Queue Type | Disconnect was sent on the Admin Queue. |

## Post-Completion Rule

The controller shall not process commands on an I/O Queue after sending the Disconnect completion.
