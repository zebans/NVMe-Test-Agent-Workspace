# NVM Compare Status Reference

| Value / status | Meaning | Test/FW interpretation |
|---|---|---|
| Compare Failure | Media data and comparison buffer differ. | Expected status for intentional miscompare tests. |
| `81h` Invalid Protection Information | `PRINFO` invalid for namespace PI format or `EILBRT` invalid. | Check PI format and expected tag fields. |
| Deallocated or Unwritten Logical Block | Enabled by Error Recovery feature DULBE and range includes deallocated/unwritten logical blocks. | Compare aborts instead of comparing DLFEAT-defined values. |
| Media/Data Integrity statuses | Includes read-path media/data errors such as Unrecovered Read Error. | Compare reads media before comparing. |

Common NVM generic, namespace, and controller-state statuses remain applicable.
