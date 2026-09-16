# Get Log Page Selector Reference

Source: NVMe Base Specification 2.0, section 5.16, Figure 202.

## Log Page Identifier Table

| LID | Scope | Log page | Source | Test/FW use |
|---|---|---|---|---|
| `00h` | Controller | Supported Log Pages | 5.16.1.1 | Discover supported LIDs and index-offset support. |
| `01h` | Controller | Error Information | 5.16.1.2 | Decode command failure history. |
| `02h` | Controller or Namespace | SMART / Health Information | 5.16.1.3 | Health, temperature, spare, media error, unsafe shutdown counters. |
| `03h` | Domain or NVM subsystem | Firmware Slot Information | 5.16.1.4 | Active firmware slot and pending activation slot. |
| `04h` | Controller | Changed Namespace List | 5.16.1.5 | Namespace inventory change notification handling. |
| `05h` | Controller | Commands Supported and Effects | 5.16.1.6 | Determine support/effects for Admin and I/O opcodes. |
| `06h` | Controller or Domain / NVM subsystem | Device Self-test | 5.16.1.7 | Current self-test progress and historical results. |
| `07h` | Vendor specific | Telemetry Host-Initiated | 5.16.1.8 | Telemetry log created by host action. |
| `08h` | Vendor specific | Telemetry Controller-Initiated | 5.16.1.9 | Controller-created telemetry. |
| `09h` | Domain or NVM subsystem | Endurance Group Information | 5.16.1.10 | Endurance group critical warning and counters. |
| `0Ah` | Domain or NVM subsystem | Predictable Latency Per NVM Set | 5.16.1.11 | Deterministic/predictable latency window state. |
| `0Bh` | Domain or NVM subsystem | Predictable Latency Event Aggregate | 5.16.1.12 | NVM Set IDs with latency events. |
| `0Ch` | Controller | Asymmetric Namespace Access | 5.16.1.13 | ANA group state and namespace membership. |
| `0Dh` | NVM subsystem | Persistent Event Log | 5.16.1.14 | Persistent event header and event list. |
| `0Eh` | I/O Command Set specific | I/O Command Set specific log | I/O command set spec | Base dispatch only; payload belongs outside Base. |
| `0Fh` | Domain or NVM subsystem | Endurance Group Event Aggregate | 5.16.1.15 | Endurance Group IDs with events. |
| `10h` | Domain or NVM subsystem | Media Unit Status | 5.16.1.16 | Media-unit configuration and health state. |
| `11h` | Domain or NVM subsystem | Supported Capacity Configuration List | 5.16.1.17 | Capacity configuration discovery. |
| `12h` | Controller | Feature Identifiers Supported and Effects | 5.16.1.18 | Determine Feature ID support/effects. |
| `13h` | Controller | NVMe-MI Commands Supported and Effects | 5.16.1.19 | Determine MI command support/effects. |
| `14h` | NVM subsystem | Command and Feature Lockdown | 5.16.1.20 | Check prohibited commands/features. |
| `15h` | Controller | Boot Partition | 5.16.1.21 | Read boot partition header/data. |
| `16h` | Endurance Group | Rotational Media Information | 5.16.1.22 | Rotational media details for endurance group. |
| `17h`-`6Fh` | Reserved | Reserved | Figure 202 | No Base-defined payload. |
| `70h` | Discovery/Fabrics boundary | Discovery | 5.16.1.23 | Discovery Log Page and entries. |
| `71h`-`7Fh` | Reserved | Reserved | Figure 202 | No Base-defined payload. |
| `80h` | Controller | Reservation Notification | 5.16.1.24 | Reservation-related async notification details. |
| `81h` | NVM subsystem | Sanitize Status | 5.16.1.25 | Sanitize progress, status, estimated times. |
| `82h`-`BFh` | I/O Command Set specific | I/O Command Set specific | I/O command set spec | Base dispatch only; payload belongs outside Base. |
| `C0h`-`FFh` | Vendor specific | Vendor specific | Vendor definition | Vendor-owned payload. |

## Selector Notes

| Selector | Meaning | Boundary |
|---|---|---|
| `LID` | Selects the log page. | Base owns Figure 202 dispatch; payload ownership may move to I/O command set, Fabrics/discovery, NVMe-MI, or vendor spec. |
| `LSP` | Per-LID action/subselector. | Only meaningful when the selected LID defines it. |
| Log Specific Identifier | Per-LID identifier in CDW11 bits 31:16. | Used as Endurance Group ID, NVM Set ID, or Domain ID depending on LID. |
| `CSI` | Command Set Identifier. | Used for command-set-specific log pages. |
| UUID Index | Vendor/log-specific UUID selection. | Do not use unless supported by the selected log page and UUID mechanism. |
