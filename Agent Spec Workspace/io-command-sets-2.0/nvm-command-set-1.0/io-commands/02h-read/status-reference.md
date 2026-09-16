# NVM Read Status Reference

| Value / status | Meaning | Test/FW interpretation |
|---|---|---|
| `80h` Conflicting Attributes | DSM attributes conflict. | Check `CDW13` DSM hints. |
| `81h` Invalid Protection Information | `PRINFO` invalid for namespace PI format or `EILBRT` invalid. | Check PI format and expected tag fields. |
| Media/Data Integrity statuses | Includes read-path media/data errors such as Unrecovered Read Error. | Returned through common NVM media/data integrity status surface. |
| Deallocated or Unwritten Logical Block | Enabled by Error Recovery feature DULBE and range includes deallocated/unwritten logical blocks. | Read aborts instead of returning DLFEAT-defined deterministic values. |

Common NVM generic, namespace, and controller-state statuses remain applicable.
