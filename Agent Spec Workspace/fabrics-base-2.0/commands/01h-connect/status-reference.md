# Connect Status Reference

## Completion

| Completion fact | Meaning |
|---|---|
| Successful Connect | Returns allocated Controller ID in the response. |
| Failed Connect | Controller shall not return `Invalid Field in Command`. |
| Failed Connect | Controller shall not add an Error Information Log entry. |
| Authentication response | `AUTHREQ` indicates whether NVMe in-band authentication and secure channel establishment are required. |

## Command-Specific Status Values

| Value | Status | Applicability |
|---:|---|---|
| `80h` | Incompatible Format | Unsupported `RECFMT`. |
| `81h` | Controller Busy | Controller already associated with a host, or no controller is available. |
| `82h` | Connect Invalid Parameters | Invalid Host NQN, Subsystem NQN, Host Identifier, Controller ID, Queue ID, `SQSIZE`, or similar parameter. |
| `83h` | Connect Restart Discovery | Requested NVM subsystem is not available; host should restart discovery. |
| `84h` | Connect Invalid Host | Host not allowed to establish an association to any controller or to the specified controller. |

## Other Relevant Status

| Status | Typical condition |
|---|---|
| Command Sequence Error | Host sends Connect for a Queue ID already created. |

## Important Negative Rule

For a failed Connect command, do not expect `Invalid Field in Command`; Connect uses its own status surface.
