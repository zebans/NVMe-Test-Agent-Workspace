# Delete I/O Completion Queue Command Facts

| Item | Value |
|---|---|
| Command | Delete I/O Completion Queue |
| Opcode | `04h` |
| Source | NVMe Base Spec 2.0 section 5.6 |
| Command set | Admin |
| Data transfer | No data transfer |
| Completion queue | Admin Completion Queue |

## Core Behavior

The Delete I/O Completion Queue command deletes an I/O Completion Queue.

The Admin Completion Queue is not deleted by this command. A host shall delete all I/O Submission Queues associated with the I/O Completion Queue before deleting the I/O Completion Queue.

After the command completes, the PRP List that described the deleted I/O Completion Queue may be deallocated by host software.
