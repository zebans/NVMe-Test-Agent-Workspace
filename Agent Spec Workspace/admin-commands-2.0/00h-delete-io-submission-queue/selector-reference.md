# Delete I/O Submission Queue Selector Reference

| Selector | Meaning | Important rule |
|---|---|---|
| `CDW10.QID` | Submission Queue Identifier to delete. | `0h` shall not be specified because it identifies the Admin Submission Queue. |

## Negative Cases

| Case | Expected status direction |
|---|---|
| `QID=0h` | `Invalid Queue Identifier`. |
| `QID` invalid or not an I/O SQ | `Invalid Queue Identifier`. |
