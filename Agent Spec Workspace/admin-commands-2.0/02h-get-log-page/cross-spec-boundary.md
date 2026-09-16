# Get Log Page Cross-Spec Boundary

Source: NVMe Base Specification 2.0, section 5.16.

## Base-Owned

| Area | Base ownership |
|---|---|
| Command opcode and dwords | `02h`, DPTR, CDW10-CDW14. |
| `LID` dispatch | Figure 202 log page identifier table. |
| Standard Base log payloads | Supported Log Pages, Error Information, SMART / Health, Firmware Slot, Commands Supported and Effects, Device Self-test, ANA, Persistent Event Log framework, Reservation Notification, Sanitize Status, and other Base section 5.16.1 payloads. |
| Command-specific status | `Invalid Log Page`, `I/O Command Set Not Supported`. |

## External Or Shared Ownership

| Area | Boundary |
|---|---|
| I/O Command Set specific logs (`0Eh`, `82h`-`BFh`) | Base only defines the dispatch range. Payload fields belong to the selected I/O Command Set spec and `CSI`. |
| Vendor specific logs (`C0h`-`FFh`) | Base only reserves the vendor range. Payload fields belong to vendor documentation. |
| Discovery Log Page transport fields | Base defines the Discovery Log Page entry layout; transport-specific details such as RDMA/TCP/FC interpretation require the relevant transport spec. |
| NVMe-MI Commands Supported and Effects (`13h`) | Base defines the log structure; command meanings require NVMe-MI command definitions. |
| Command and Feature Lockdown (`14h`) | Base defines the returned log and selectors; prohibited settings may be configured through NVMe-MI. |
| Reservation Notification (`80h`) | Base defines the log payload; event meaning depends on Reservation commands/features. |
| Sanitize Status (`81h`) | Base defines status payload; operation meaning depends on Sanitize command parameters. |

## API Boundary

This folder does not define PyNVMe call syntax. When generating PyNVMe tests, use this folder for expected spec behavior and field meanings, then use the API layer documentation for how to call `getlogpage` or parse buffers.
