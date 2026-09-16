# Asynchronous Event Request Command Facts

| Item | Value |
|---|---|
| Command | Asynchronous Event Request |
| Opcode | `0Ch` |
| Source | NVMe Base Spec 2.0 section 5.2, Figures 142-148 |
| Command set | Admin |
| Data transfer | No data transfer |
| Completion queue | Admin Completion Queue, when an event is reported |
| Timeout | No command timeout |

## Core Behavior

Host software submits one or more AER commands to enable asynchronous event reporting. The controller completes an AER command when it has an asynchronous event to report.

Host software may submit multiple AER commands to reduce reporting latency. Outstanding AER commands are limited by Identify Controller `AERL`.

After an AER completion is posted for an event type, subsequent events of that type are automatically masked until the host clears that event. Unless otherwise stated, clearing is done by reading the associated log page with Get Log Page.
