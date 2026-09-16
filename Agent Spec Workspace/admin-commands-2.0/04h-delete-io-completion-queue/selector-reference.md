# Delete I/O Completion Queue Selector Reference

| Selector | Location | Meaning | Validity rule | Status on violation |
|---|---|---|---|---|
| Completion Queue Identifier | `CDW10.QID` | Selects the I/O Completion Queue to delete. | Shall identify a valid I/O CQ. `0h` / Admin CQ shall not be specified. | `Invalid Queue Identifier` |
| Queue association state | Controller queue state | Whether any I/O SQ is still associated with the CQ. | All associated I/O SQs shall be deleted first. | `Invalid Queue Deletion` |

## Lookup Notes

- Use `QID` for target selection.
- Use queue association state to decide whether the target CQ is legally deletable.
