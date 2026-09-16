# NVM Dataset Management Status Reference

| Value / status | Meaning | Test/FW interpretation |
|---|---|---|
| `20h` Namespace is Write Protected | Command is prohibited while namespace is write protected. | Namespace protection blocks command. |
| `80h` Conflicting Attributes | Attributes in command conflict. | Check `AD/IDW/IDR` and context attributes. |
| `82h` Attempted Write to Read Only Range | Optional status if Deallocate is attempted for a read-only range, excluding namespace write-protection-state cases. | Read-only range blocks deallocation. |
| `83h` Command Size Limit Exceeded | Dataset Management processing limits `DMRL`, `DMRSL`, or `DMSL` exceeded when ONCS bit 2 is clear. | Check Identify Controller limits. |

Common NVM generic, namespace, and controller-state statuses remain applicable.
