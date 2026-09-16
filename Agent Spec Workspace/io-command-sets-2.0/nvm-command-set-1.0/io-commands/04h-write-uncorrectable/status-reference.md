# NVM Write Uncorrectable Status Reference

| Value / status | Meaning | Test/FW interpretation |
|---|---|---|
| `20h` Namespace is Write Protected | Command is prohibited while namespace is write protected. | Namespace protection blocks command. |
| `82h` Attempted Write to Read Only Range | LBA range contains read-only blocks, excluding namespace write-protection-state cases. | Read-only range blocks marking. |
| Invalid Field in Command | WUSL hard limit exceeded when ONCS bit 1 is clear. | Command range exceeds supported limit. |

Common NVM generic, namespace, and controller-state statuses remain applicable.
