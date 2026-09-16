# Delete I/O Completion Queue Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW10` | `QID` | I/O Completion Queue Identifier to delete. | `0h` shall not be specified; Admin CQ cannot be deleted. | Queue deletion target and invalid-queue tests. |
| Controller state | Associated I/O SQs | I/O Submission Queues using this CQ. | Must be deleted before this CQ. | `Invalid Queue Deletion` tests. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |
