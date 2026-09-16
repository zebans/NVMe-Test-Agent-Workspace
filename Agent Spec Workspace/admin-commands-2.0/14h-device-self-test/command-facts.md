# Device Self-test Command Facts

| Item | Value |
|---|---|
| Command | Device Self-test |
| Opcode | `14h` |
| Source | NVMe Base Spec 2.0 section 5.9, Figures 170-173 |
| Command set | Admin |
| Data transfer | No data transfer |
| NSID usage | Yes |
| Completion queue | Admin Completion Queue |

## Core Behavior

The Device Self-test command starts a short, extended, or vendor specific device self-test operation, or aborts a device self-test operation already in progress.

The operation is performed by the controller that received the command. `NSID` controls which namespaces are included in the test. `CDW10.STC` controls which self-test action is requested.

Device self-test operation details and result history are reflected through the Device Self-test Log.
