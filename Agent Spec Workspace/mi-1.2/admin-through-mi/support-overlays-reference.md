# Admin-Through-MI Support Overlays Reference

Status: `FIELD-INDEXED + ROUTING-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 6.3 through 6.5, Figures 121-125.

This file captures Admin-through-MI support overlays that further constrain or refine Figure 114.

## Figure 121 - Management Endpoint Log Page Support

Figure 121 defines log pages that are Mandatory, Optional, or Prohibited for SMBus/I2C and PCIe VDM Management Endpoints on NVMe Storage Devices and NVMe Enclosures.

Legend:

| Symbol | Meaning |
|---|---|
| `M` | Mandatory |
| `O` | Optional |
| `P` | Prohibited |

Columns:

```text
SMBus/I2C Storage Device
SMBus/I2C Enclosure
PCIe VDM Storage Device
PCIe VDM Enclosure
```

| LID | Log Page | SMBus/I2C Storage | SMBus/I2C Enclosure | PCIe VDM Storage | PCIe VDM Enclosure | Payload owner |
|---|---|---|---|---|---|---|
| `00h` | Supported Log Pages | M | M | M | M | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `01h` | Error Information | M | M | M | M | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `02h` | SMART / Health Information, Controller scope | M | O | M | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `02h` | SMART / Health Information, NVM Subsystem scope | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `03h` | Firmware Slot Information | M | O | M | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `04h` | Changed Namespace List | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `05h` | Commands Supported and Effects | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `06h` | Device Self-test | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `07h` | Telemetry Host-Initiated | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `08h` | Telemetry Controller-Initiated | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `09h` | Endurance Group Information | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `0Ah` | Predictable Latency Per NVM Set | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `0Bh` | Predictable Latency Event Aggregate | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `0Ch` | Asymmetric Namespace Access | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `0Dh` | Persistent Event | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `0Eh` | LBA Status Information | O | O | O | O | NVM Command Set |
| `0Fh` | Endurance Group Event Aggregate | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `10h` | Media Unit Status | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `11h` | Supported Capacity Configuration List | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `12h` | Feature Identifiers Supported and Effects | M | O | M | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `13h` | NVMe-MI Commands Supported and Effects | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` plus `..\MI_COMMAND_REFERENCE.md` |
| `14h` | Command and Feature Lockdown | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `15h` | Boot Partition | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `16h` | Rotational Media Information | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` |
| `70h` | Discovery | O | O | O | O | Fabrics / discovery owner |
| `80h` | Reservation Notification | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` plus Reservation references |
| `81h` | Sanitize Status | O | O | O | O | `..\..\admin-commands-2.0\02h-get-log-page\` plus Sanitize |
| `BFh` | Changed Zone List | O | O | O | O | ZNS Command Set |

## Figure 122 - Commands During Sanitize / Format NVM Processing

Figure 122 lists command messages that are allowed during a sanitize operation and during processing of a Format NVM command.

| Command family | Command messages | Allowed rule |
|---|---|---|
| Management Interface Command Set | Configuration Get/Set, Controller Health Status Poll, Management Endpoint Buffer Read/Write, NVM Subsystem Health Status Poll, Read NVMe-MI Data Structure, Reset, SES Receive/Send, Shutdown, VPD Read/Write | Yes |
| NVM Express Admin Command Set | Capacity Management, Device Self-test, Firmware Commit, Firmware Image Download, Format NVM, Get Features, Get Log Page, Identify, Namespace Attachment, Namespace Management, Sanitize, Security Receive/Send, Set Features, Vendor Specific, Virtualization Management | Same restrictions as the NVM Express Base Specification |
| PCIe Command Set | PCIe Configuration Read/Write, PCIe I/O Read, PCIe Memory Read/Write | Yes |

Note: Admin commands prohibited by Figure 114 are always prohibited, including during sanitize operation.

## Figures 123-124 - Controller Feature Support

| Controller type | Feature | FID | Feature Support | Logged in Persistent Event Log |
|---|---|---|---|---|
| I/O Controller | Enhanced Controller Metadata | `7Dh` | M | O |
| I/O Controller | Controller Metadata | `7Eh` | M | O |
| I/O Controller | Namespace Metadata | `7Fh` | M | O |
| Administrative Controller | Enhanced Controller Metadata | `7Dh` | M | O |
| Administrative Controller | Controller Metadata | `7Eh` | M | O |
| Administrative Controller | Namespace Metadata | `7Fh` | O | O |

## Figure 125 - Management Endpoint Feature Support

Columns:

```text
SMBus/I2C Storage Device
SMBus/I2C Enclosure
PCIe VDM Storage Device
PCIe VDM Enclosure
```

| FID | Feature | SMBus/I2C Storage | SMBus/I2C Enclosure | PCIe VDM Storage | PCIe VDM Enclosure | Notes |
|---|---|---|---|---|---|---|
| `01h` | Arbitration | P | P | P | P | Queue arbitration feature prohibited on Management Endpoint. |
| `02h` | Power Management | O | O | O | O | Optional. |
| `03h` | LBA Range Type | P | P | P | P | Prohibited. |
| `04h` | Temperature Threshold | O | O | O | O | Optional. |
| `05h` | Error Recovery | P | P | P | P | Prohibited. |
| `06h` | Volatile Write Cache | P | P | P | P | Prohibited. |
| `07h` | Number of Queues | P | P | P | P | Queue-related feature prohibited. |
| `08h` | Interrupt Coalescing | P | P | P | P | Prohibited. |
| `09h` | Interrupt Vector Configuration | P | P | P | P | Prohibited. |
| `0Ah` | Write Atomicity Normal | P | P | P | P | Prohibited. |
| `0Bh` | Asynchronous Event Configuration | P | P | P | P | Prohibited. |
| `0Ch` | Autonomous Power State Transition | O | O | O | O | Optional. |
| `0Dh` | Host Memory Buffer | P | P | P | P | Prohibited. |
| `0Eh` | Timestamp | O | O | O | O | Optional. |
| `0Fh` | Keep Alive Timer | P | P | P | P | Prohibited. |
| `10h` | Host Controlled Thermal Management | O | O | O | O | Optional. |
| `11h` | Non-Operational Power State Config | O | O | O | O | Optional. |
| `12h` | Read Recovery Level Config | P | P | P | P | Prohibited. |
| `13h` | Predictable Latency Mode Config | P | P | P | P | Prohibited. |
| `14h` | Predictable Latency Mode Window | P | P | P | P | Prohibited. |
| `15h` | LBA Status Information Attributes | P | P | P | P | Prohibited. |
| `16h` | Host Behavior Support | P | P | P | P | Prohibited. |
| `17h` | Sanitize Config | O | O | O | O | Optional. |
| `18h` | Endurance Group Event Configuration | P | P | P | P | Prohibited. |
| `19h` | I/O Command Set Profile | O | P | O | P | Enclosure prohibited. |
| `1Ah` | Spinup Control | O | O | O | O | Optional. |
| `20h` | Key Value Configuration | O | O | O | O | Optional. |
| `7Dh` | Enhanced Controller Metadata | O | O | O | O | Optional on Management Endpoint. |
| `7Eh` | Controller Metadata | O | O | O | O | Optional on Management Endpoint. |
| `7Fh` | Namespace Metadata | O | O | O | O | Optional on Management Endpoint. |

## Lookup Rule

Use this file after `MI_ADMIN_THROUGH_COMMAND_TABLE.md` when the Admin command is Get Log Page, Get Features, Set Features, Sanitize, or Format NVM and the question asks whether a selector/FID/log page is supported through a specific Management Endpoint path.

