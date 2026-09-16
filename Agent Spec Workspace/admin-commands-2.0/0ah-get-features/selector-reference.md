# Get Features Selector Reference

Source: NVMe Base Specification 2.0, section 5.15, Figures 192 and 194.

## Select Field

| SEL | Meaning | Returned value |
|---|---|---|
| `000b` | Current | Current operating attribute value for selected `FID`. |
| `001b` | Default | Default attribute value for selected `FID`. |
| `010b` | Saved | Last saved value for selected `FID`. If feature is not saveable or has no saved value, behaves as default. |
| `011b` | Supported Capabilities | CQE Dword 0 capability bits from Figure 195. |
| `100b`-`111b` | Reserved | Invalid. |

## Feature Identifier Table

| FID | Feature | Source | Typical return |
|---|---|---|---|
| `01h` | Arbitration | 5.27.1.1 | CQE DW0 attributes. |
| `02h` | Power Management | 5.27.1.2 | CQE DW0 selected power state. |
| `04h` | Temperature Threshold | 5.27.1.3 | CQE DW0 selected threshold. |
| `06h` | Volatile Write Cache | 5.27.1.4 | CQE DW0 `WCE`. |
| `07h` | Number of Queues | 5.27.1.5 | CQE DW0 allocated SQ/CQ counts. |
| `08h` | Interrupt Coalescing | 5.27.1.6 | CQE DW0 coalescing settings. |
| `09h` | Interrupt Vector Configuration | 5.27.1.7 | CQE DW0 vector config for CDW11 vector. |
| `0Bh` | Asynchronous Event Configuration | 5.27.1.8 | CQE DW0 event mask. |
| `0Ch` | Autonomous Power State Transition | 5.27.1.9 | CQE DW0 `APSTE` plus APST data buffer. |
| `0Dh` | Host Memory Buffer | 5.27.1.10 | HMB attributes data buffer. |
| `0Eh` | Timestamp | 5.27.1.11 | Timestamp data buffer. |
| `0Fh` | Keep Alive Timer | 5.27.1.12 | CQE DW0 `KATO`. |
| `10h` | Host Controlled Thermal Management | 5.27.1.13 | CQE DW0 `TMT1/TMT2`. |
| `11h` | Non-Operational Power State Config | 5.27.1.14 | CQE DW0 `NOPPME`. |
| `12h` | Read Recovery Level Config | 5.27.1.15 | CQE DW0/CDW-specific value. |
| `13h` | Predictable Latency Mode Config | 5.27.1.16 | CQE DW0 plus threshold data. |
| `14h` | Predictable Latency Mode Window | 5.27.1.17 | CQE DW0 window select. |
| `16h` | Host Behavior Support | 5.27.1.18 | 512-byte data buffer. |
| `17h` | Sanitize Config | 5.27.1.19 | CQE DW0 `NODRM`. |
| `18h` | Endurance Group Event Configuration | 5.27.1.20 | CQE DW0 event mask. |
| `19h` | I/O Command Set Profile | 5.27.1.21 | CQE DW0 selected combination index. |
| `1Ah` | Spinup Control | 5.27.1.22 | CQE DW0 enable bit. |
| `20h` | I/O Command Set specific feature | I/O command set spec | External. |
| `7Dh` | Enhanced Controller Metadata | 5.27.1.23.1 | Host metadata data buffer. |
| `7Eh` | Controller Metadata | 5.27.1.23.2 | Host metadata data buffer. |
| `7Fh` | Namespace Metadata | 5.27.1.23.3 | Host metadata data buffer. |
| `80h` | Software Progress Marker | 5.27.1.24 | CQE DW0 `PBSLC`. |
| `81h` | Host Identifier | 5.27.1.25 | Host Identifier data buffer. |
| `82h` | Reservation Notification Mask | 5.27.1.26 | CQE DW0 mask bits. |
| `83h` | Reservation Persistence | 5.27.1.27 | CQE DW0 `PTPL`. |
| `84h` | Namespace Write Protection Config | 5.27.1.28 | CQE DW0 write protection state. |
| `C0h`-`FFh` | Vendor specific | Vendor definition | Vendor-owned. |
