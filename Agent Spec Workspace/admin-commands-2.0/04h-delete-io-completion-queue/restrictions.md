# Delete I/O Completion Queue Restrictions

| Restriction | Meaning | Violation result |
|---|---|---|
| Admin CQ cannot be deleted | `QID=0h` / Admin Completion Queue is excluded. | `Invalid Queue Identifier` |
| Associated I/O SQs must be deleted first | A CQ cannot be deleted while SQs still target it. | `Invalid Queue Deletion` |
| Queue cleanup after completion | PRP List / queue memory cleanup is allowed after completion. | Cleanup before completion risks undefined host/controller behavior. |
