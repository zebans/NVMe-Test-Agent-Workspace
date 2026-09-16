# Asynchronous Event Request Payload / Event Reference

## Completion DW0 Layout

| Bits | Field | Meaning |
|---|---|---|
| 31:24 | Reserved | Reserved. |
| 23:16 | Log Page Identifier | Associated log page. |
| 15:08 | Asynchronous Event Information | Event-specific value. |
| 07:03 | Reserved | Reserved. |
| 02:00 | Asynchronous Event Type | Event category. |

## Error Status Event Information (`AET=000b`)

| Value | Meaning |
|---|---|
| `00h` | Write to Invalid Doorbell Register. |
| `01h` | Invalid Doorbell Write Value. |
| `02h` | Diagnostic Failure. |
| `03h` | Persistent Internal Error. |
| `04h` | Transient Internal Error. |
| `05h` | Firmware Image Load Error. |
| `06h`-`FFh` | Reserved. |

## SMART / Health Status Event Information (`AET=001b`)

| Value | Meaning |
|---|---|
| `00h` | NVM subsystem Reliability. |
| `01h` | Temperature Threshold. |
| `02h` | Spare Below Threshold. |
| `03h`-`FFh` | Reserved. |

## Notice Event Information (`AET=010b`)

| Value | Meaning | Clearing / boundary |
|---|---|---|
| `00h` | Namespace Attribute Changed. | Clear through Changed Namespace List log page with Retain Asynchronous Event cleared. |
| `01h` | Firmware Activation Starting. | Clear by reading Firmware Slot Information log page. |
| `02h` | Telemetry Log Changed. | Clear by reading Telemetry Controller-Initiated log with Retain Asynchronous Event cleared. |
| `03h` | Asymmetric Namespace Access Change. | Clear by reading ANA log with Retain Asynchronous Event cleared. |
| `04h` | Predictable Latency Event Aggregate Log Change. | Related to Predictable Latency Event Aggregate log. |
| `05h` | LBA Status Information Alert. | I/O Command Set specific definition. |
| `06h` | Endurance Group Event Aggregate Log Page Change. | Clear by reading Endurance Group Event Aggregate log with Retain Asynchronous Event cleared. |
| `07h`-`EEh` | Reserved. | Reserved. |
| `EFh` | Zone Descriptor Changed. | Zoned Namespace Command Set specific definition. |
| `F0h` | Discovery Log Page Change. | Host should submit Get Log Page to receive updated Discovery Log Pages. |
| `F1h`-`FFh` | Reserved for future NVMe over Fabrics AENs. | Fabrics future boundary. |

## I/O Command Specific Status Event Information (`AET=110b`)

| Value | Meaning |
|---|---|
| `00h` | Reservation Log Page Available. |
| `01h` | Sanitize Operation Completed. |
| `02h` | Sanitize Operation Completed With Unexpected Deallocation. |
| `03h`-`FFh` | Reserved. |

## Immediate Event Information (`AET=011b`)

| Value | Meaning |
|---|---|
| `00h` | NVM Subsystem Normal Shutdown. |
| `01h`-`FFh` | Reserved. |

