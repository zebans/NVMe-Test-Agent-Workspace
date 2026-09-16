# NVM Write Zeroes Status Reference

| Value / status | Meaning | Test/FW interpretation |
|---|---|---|
| `20h` Namespace is Write Protected | Command is prohibited while namespace is write protected. | Namespace protection blocks Write Zeroes. |
| `81h` Invalid Protection Information | `PRINFO` invalid for namespace PI format or `ILBRT` invalid. | Check PI format and tag fields. |
| `82h` Attempted Write to Read Only Range | LBA range contains read-only blocks, excluding namespace write-protection-state cases. | Media/read-only range blocks Write Zeroes. |
| Invalid Field in Command | `PRCHK` is not `000b`, `STC` is not cleared, or WZSL limit is exceeded when ONCS bit 3 is clear. | Command field/limit violation. |

Common NVM generic, namespace, and controller-state statuses remain applicable.
