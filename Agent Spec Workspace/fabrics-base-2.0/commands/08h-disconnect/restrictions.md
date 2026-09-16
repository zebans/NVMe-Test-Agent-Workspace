# Disconnect Restrictions

Status: `COMMAND-CONTROL-COMPLETE`

- Disconnect is used to delete the I/O Queue on which the command is submitted.
- If submitted on an Admin Queue, the controller shall abort the command with `Invalid Queue Type`.
- The NVMe Transport connection is not deleted by issuing Disconnect.
- The controller shall not process commands on an I/O Queue after sending the Disconnect completion.
- Host software should not submit commands to an I/O Submission Queue after submitting Disconnect to that queue; doing so results in undefined behavior.

