# Delete I/O Submission Queue Restrictions

| Restriction | Meaning |
|---|---|
| Admin SQ cannot be deleted | `QID=0h` shall not be specified. |
| Completion ordering | Completion is posted only after prior commands are completed/aborted and queue deletion occurs. |
| Deleted queue completions | No completion status is posted for commands submitted to the deleted SQ after successful deletion. |
| PRP List deallocation | Host may deallocate the SQ PRP List after completion. |
