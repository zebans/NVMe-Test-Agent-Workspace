# Delete I/O Completion Queue Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Invalid Queue Identifier` | `QID` is invalid or refers to the Admin Completion Queue. | Target selection is illegal. |
| `Invalid Queue Deletion` | The I/O Completion Queue still has associated I/O Submission Queues. | Delete associated SQs first, then retry CQ deletion. |

## Notes

Generic status values may still apply for common command processing failures. This file lists command-specific status meanings for this command.
