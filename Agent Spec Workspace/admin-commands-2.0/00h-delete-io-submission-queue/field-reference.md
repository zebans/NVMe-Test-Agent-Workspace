# Delete I/O Submission Queue Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW10` | `QID` | I/O Submission Queue Identifier to delete. | `0h` shall not be specified. | Queue deletion target and invalid-queue tests. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |
