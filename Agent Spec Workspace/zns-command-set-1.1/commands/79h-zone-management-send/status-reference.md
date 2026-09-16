# Zone Management Send Status Reference

## Completion

| CQE field | Meaning |
|---|---|
| Dword 0 bit 0 | Zone Capacity Changed. Set when zone capacity changed for one or more zones specified by the command; cleared when capacity did not change due to this command. |

If zone capacity changed, the host may use Zone Management Receive to determine what changed.

## ZNS Command-Specific Status Values

| Value | Status | Relevant condition |
|---:|---|---|
| `BAh` | Zone Is Read Only | Zone is in `ZSRO:Read Only`; may occur during command processing. |
| `BBh` | Zone Is Offline | Zone is in `ZSO:Offline`; may occur during command processing. |
| `BDh` | Too Many Active Zones | Controller does not allow additional active zones. |
| `BEh` | Too Many Open Zones | Controller does not allow additional open zones. |
| `BFh` | Invalid Zone State Transition | Requested action is not a valid zone state transition. |

## Other Status Sources

| Status | When it applies |
|---|---|
| Invalid Field in Command | `SLBA` is not the starting LBA of a zone while Select All is clear. |
| Invalid Field in Command | Set Zone Descriptor Extension requested while Zone Descriptor Extension Size is `0h`. |
| Invalid Field in Command | Select All is set for Set Zone Descriptor Extension. |
| Namespace is Write Protected | The zoned namespace containing the specified zone is write protected. |

## No-Transition Rule

If the command fails due to insufficient active/open resources, no zone state transition occurs.
