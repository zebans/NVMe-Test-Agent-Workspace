# NVM Verify Status Reference

| Value / status | Meaning | Test/FW interpretation |
|---|---|---|
| `81h` Invalid Protection Information | `PRINFO` invalid for namespace PI format or `EILBRT` invalid. | Check PI format and expected tag fields. |
| Media/Data Integrity statuses applicable to Read | Verify may use Read-like media/data integrity statuses, such as Unrecovered Read Error. | Integrity verification failed. |
| Deallocated or Unwritten Logical Block | Enabled by Error Recovery feature DULBE and range includes deallocated/unwritten logical blocks. | Verify aborts on deallocated/unwritten block. |
| Invalid Field in Command | `PRACT` not cleared or VSL hard limit exceeded. | Command field/limit violation. |

Common NVM generic, namespace, and controller-state statuses remain applicable.
