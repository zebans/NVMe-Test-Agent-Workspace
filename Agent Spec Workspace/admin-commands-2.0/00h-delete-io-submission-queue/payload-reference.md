# Delete I/O Submission Queue Payload Reference

Delete I/O Submission Queue transfers no command data payload.

## Completion

| Completion behavior | Meaning |
|---|---|
| CQE posted to Admin Completion Queue | Posted after prior commands are completed or aborted and the queue is deleted. |
| Deleted SQ completions | Controller shall not post completion status for commands submitted to the deleted SQ after successful deletion. |
| PRP List lifetime | PRP List that described the SQ may be deallocated after command completion. |
