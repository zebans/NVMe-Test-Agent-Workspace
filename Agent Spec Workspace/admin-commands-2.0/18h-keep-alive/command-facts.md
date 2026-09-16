# Keep Alive Command Facts

| Item | Value |
|---|---|
| Command | Keep Alive |
| Opcode | `18h` |
| Source | NVMe Base Spec 2.0 section 5.18; related section 3.9 |
| Command set | Admin |
| Data transfer | No data transfer |
| Completion queue | Admin Completion Queue |

## Core Behavior

Keep Alive is used by the host to determine that the controller is operational and by the controller to determine that the host is operational.

If Keep Alive Timeout is enabled on the Admin Queue, the Keep Alive Timer is restarted when a Keep Alive command is processed. If `TBKAS` is set and an Admin or I/O command is processed during the Keep Alive Timeout Interval, the timer is restarted at the end of the Keep Alive Timeout.

The controller indicates Keep Alive Timer granularity in Identify Controller `KAS`.
