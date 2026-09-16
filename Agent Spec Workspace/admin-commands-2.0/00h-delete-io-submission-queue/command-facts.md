# Delete I/O Submission Queue Command Facts

Source: NVMe Base Spec 2.0 section 5.7, Figures 165-166.

| Item | Value |
|---|---|
| Command | Delete I/O Submission Queue |
| Opcode | `00h` |
| Command set | Admin |
| Data transfer | No data transfer |
| Main field | `CDW10.QID` |

## Required Behavior

| Area | Requirement |
|---|---|
| Purpose | Deletes an I/O Submission Queue. |
| Admin SQ | The Admin Submission Queue cannot be deleted. |
| Completion timing | CQE is posted to the Admin Completion Queue after prior commands are completed/aborted and the queue is deleted. |
| Deleted SQ completions | After successful SQ deletion, controller shall not post completion status for commands submitted to the deleted SQ. |
| PRP List lifetime | After completion, the PRP List that described the SQ may be deallocated by host software. |
