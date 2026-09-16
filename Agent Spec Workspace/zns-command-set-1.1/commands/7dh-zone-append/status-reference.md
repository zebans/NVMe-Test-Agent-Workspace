# Zone Append Status Reference

## Completion

| CQE field | Meaning |
|---|---|
| Dword 0 | `ALBA[31:00]`, lowest LBA containing the data written by the command. |
| Dword 1 | `ALBA[63:32]`, upper bits of the assigned LBA. |

If the command does not complete successfully, the contents of `ALBA` are undefined.

## ZNS Command-Specific Status Values

| Value | Status | Meaning |
|---:|---|---|
| `B8h` | Zone Boundary Error | The command specifies logical blocks in more than one zone. |
| `B9h` | Zone Is Full | The accessed zone is in the `ZSF:Full` state. |
| `BAh` | Zone Is Read Only | The accessed zone is in the `ZSRO:Read Only` state. |
| `BBh` | Zone Is Offline | The accessed zone is in the `ZSO:Offline` state. |
| `BDh` | Too Many Active Zones | The controller does not allow additional active zones. |
| `BEh` | Too Many Open Zones | The controller does not allow additional open zones. |

## Other Status Sources

| Status | When it applies |
|---|---|
| Invalid Field in Command | The specified zone is not Sequential Write Required. |
| Invalid Field in Command | `ZSLBA` does not specify the lowest logical block for a zone. |
| Invalid Protection Information | `PIREMAP` violates the PI format-specific rule. |
