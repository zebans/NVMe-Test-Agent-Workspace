# Zone Management Send Payload Reference

Most Zone Management Send actions do not require a command data payload.

| `ZSA` | Payload requirement | Notes |
|---:|---|---|
| `01h` Close Zone | No action-specific payload. | Uses `SLBA` or Select All. |
| `02h` Finish Zone | No action-specific payload. | Uses `SLBA` or Select All. |
| `03h` Open Zone | No action-specific payload. | Uses `SLBA` or Select All. |
| `04h` Reset Zone | No action-specific payload. | Uses `SLBA` or Select All. |
| `05h` Offline Zone | No action-specific payload. | Uses `SLBA` or Select All. |
| `10h` Set Zone Descriptor Extension | Host-to-controller Zone Descriptor Extension data. | Select All shall be clear; target zone shall be Empty. |

## Set Zone Descriptor Extension

| Requirement | Meaning |
|---|---|
| Target state | The target zone shall be Empty. |
| Result | Zone transitions to Closed and descriptor extension data is associated with the zone. |
| Extension support | Zone Descriptor Extension Size shall be non-zero. |
| Select All | Shall not be set. |

The shared Zone Descriptor Extension model is summarized in `..\..\zns-model.md`.
