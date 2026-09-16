# Fabrics Status Reference

Status: `STATUS-REFERENCE-COMPLETE`

Source: Base Spec 2.0 Figure 97, "Status Code - Command Specific Status Values, Fabrics Commands".

| Value | Name | Commands affected | Meaning |
|---:|---|---|---|
| `80h` | Incompatible Format | Connect, Disconnect | The NVM subsystem does not support the record format specified by the host. |
| `81h` | Controller Busy | Connect, Disconnect | For Connect: controller already associated with a host or no controller is available. For Disconnect: controller cannot disconnect the I/O Queue at the current time. |
| `82h` | Connect Invalid Parameters | Connect | One or more parameters such as Host NQN, Subsystem NQN, Host Identifier, Controller ID, or Queue ID are not valid. |
| `83h` | Connect Restart Discovery | Connect | The requested NVM subsystem is not available; host should restart discovery. |
| `84h` | Connect Invalid Host | Connect | Host is not allowed to establish an association to any controller or to the specified controller. |
| `85h` | Invalid Queue Type | Disconnect | Command was sent on the wrong queue type, such as Disconnect sent on Admin Queue. |
| `86h`-`8Fh` | Reserved | Fabrics | Reserved. |
| `90h` | Discover Restart | Get Log Page | Discovery Log Page snapshot is invalid or out of date; host should re-read it. |
| `91h` | Authentication Required | All commands other than Connect, Authentication Send, and Authentication Receive | NVMe in-band authentication is required and the queue has not yet been authenticated. |
| `92h`-`AFh` | Reserved | Fabrics | Reserved. |
| `B0h`-`BFh` | Transport Specific | Transport-specific | Status values in this range are NVMe Transport specific. Refer to the applicable NVMe Transport binding specification. |

Notes:

- Figure 97 is a Base Spec status table for Fabrics command-specific status values.
- Transport-specific status values are intentionally not expanded in this Base Fabrics layer.

