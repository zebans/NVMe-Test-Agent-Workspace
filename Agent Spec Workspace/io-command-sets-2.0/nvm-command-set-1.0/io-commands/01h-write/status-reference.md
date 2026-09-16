# NVM Write Status Reference

| Value / status | Meaning | Test/FW interpretation |
|---|---|---|
| `20h` Namespace is Write Protected | Command is prohibited while namespace is write protected. | Namespace protection blocks write. |
| `80h` Conflicting Attributes | DSM attributes conflict. | Check `CDW13` DSM hints. |
| `81h` Invalid Protection Information | `PRINFO` invalid for namespace PI format or `ILBRT` invalid. | Check PI format, `PRINFO`, and tag fields. |
| `82h` Attempted Write to Read Only Range | LBA range contains read-only blocks, excluding namespace write-protection-state cases. | Media/read-only range blocks write. |

Common NVM media/data integrity and generic status values remain applicable through Base/common NVMe rules.
