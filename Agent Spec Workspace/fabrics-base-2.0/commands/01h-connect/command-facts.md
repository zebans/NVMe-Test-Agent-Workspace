# Connect Command Facts

Source: NVMe Base Spec 2.0 section 6.3, Figures 380-383, Figure 375, and Figure 97.

| Item | Value |
|---|---|
| Command | Connect |
| Fabrics opcode | `OPC=7Fh` |
| Fabrics command type | `FCTYPE=01h` |
| Purpose | Creates a Submission Queue and Completion Queue pair. |
| I/O Queue support | Supported on I/O Queues. |
| Main SQE fields | `RECFMT`, `QID`, `SQSIZE`, `CATTR`, `KATO`. |
| Main data fields | `HOSTID`, `CNTLID`, `SUBNQN`, `HOSTNQN`. |

## Required Command Behavior

| Area | Requirement |
|---|---|
| Admin Queue Connect | Establishes an association between host and controller. |
| I/O Queue Connect | Requires the host to already have an association with a controller and the controller to be enabled. |
| Queue creation | Connect is submitted and completed on the same queue that the Connect command creates. |
| Successful response | Returns allocated Controller ID and authentication/security requirement information. |
| Failed response | Controller shall not return `Invalid Field in Command` and shall not add an Error Information Log entry. |
