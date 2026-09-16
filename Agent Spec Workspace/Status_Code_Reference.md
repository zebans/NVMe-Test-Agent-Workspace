# Status Code Reference - NVMe Base Spec 2.0

This file is a global status-code dictionary for the local NVMe Base Specification 2.0 source.

Primary source:

```text
NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

Source anchors: Section 3.3.3.2.1 and Figures 92-99.

This file is not a command-specific status matrix. Command references should cite only the status values explicitly relevant to that command and refer back here for global definitions.

## Completion Queue Status Field

The Completion Queue Entry Status Field is defined in section 3.3.3.2.1 and Figure 92.

| Field | Bits | Meaning |
|---|---:|---|
| Do Not Retry (DNR) | 31 | Indicates whether resubmitting the same command is expected to fail. |
| More (M) | 30 | Indicates more status information is available when defined by the command/status context. |
| Status Code Type (SCT) | 27:25 | Identifies the status-code category. |
| Status Code (SC) | 24:17 | Identifies detailed status information. |

The Phase Tag and Command Identifier are outside the Status Field and are defined in Figure 91.

## Status Code Type Values

Source: Figure 93.

| SCT | Type | Summary |
|---|---|---|
| `0h` | Generic Command Status | Generic across command types, including success, unsupported opcode, and invalid field. |
| `1h` | Command Specific Status | Specific to a command opcode or command family. |
| `2h` | Media and Data Integrity Errors | Media-specific or data-integrity errors. |
| `3h` | Path Related Status | Path/connection/ANA-related status. |
| `4h`-`6h` | Reserved | Reserved. |
| `7h` | Vendor Specific | Vendor-specific. |

Status code value ranges are:

| SC Range | Meaning |
|---|---|
| `00h`-`7Fh` | Admin Command Set or status across multiple command sets. |
| `80h`-`BFh` | I/O Command Set-specific status codes. |
| `C0h`-`FFh` | Vendor-specific status codes. |

Unless otherwise specified, if multiple status codes apply, the controller selects the status code returned.

## Generic Command Status Values

Source: Figure 94.

| SC | Name | Notes |
|---|---|---|
| `00h` | Successful Completion | Command completed without error. |
| `01h` | Invalid Command Opcode | Reserved or unsupported opcode. |
| `02h` | Invalid Field in Command | Reserved or unsupported value in a defined field other than opcode. |
| `03h` | Command ID Conflict | Command identifier already in use. |
| `04h` | Data Transfer Error | Data or metadata transfer error. |
| `05h` | Commands Aborted due to Power Loss Notification | Command aborted due to power loss notification. |
| `06h` | Internal Error | Command not completed due to internal error. |
| `07h` | Command Abort Requested | Command aborted by Abort command. |
| `08h` | Command Aborted due to SQ Deletion | Submission queue was deleted. |
| `09h` | Command Aborted due to Failed Fused Command | Other command in fused operation failed. |
| `0Ah` | Command Aborted due to Missing Fused Command | Adjacent fused command missing. |
| `0Bh` | Invalid Namespace or Format | Namespace or namespace format is invalid. |
| `0Ch` | Command Sequence Error | Protocol violation in a multi-command sequence. |
| `0Dh` | Invalid SGL Segment Descriptor | Invalid SGL Last Segment or SGL Segment descriptor. |
| `0Eh` | Invalid Number of SGL Descriptors | Invalid number/location of SGL descriptors. |
| `0Fh` | Data SGL Length Invalid | Data SGL length is invalid. |
| `10h` | Metadata SGL Length Invalid | Metadata SGL length is invalid. |
| `11h` | SGL Descriptor Type Invalid | Unsupported descriptor type/subtype. |
| `12h` | Invalid Use of Controller Memory Buffer | Attempted CMB usage not supported. |
| `13h` | PRP Offset Invalid | PRP offset field is invalid. |
| `14h` | Atomic Write Unit Exceeded | I/O Command Set-specific; NVM/ZNS. |
| `15h` | Operation Denied | Command denied due to lack of access rights. |
| `16h` | SGL Offset Invalid | SGL descriptor offset is invalid. |
| `17h` | Reserved | Reserved. |
| `18h` | Host Identifier Inconsistent Format | Simultaneous 64-bit and 128-bit Host Identifier use detected. |
| `19h` | Keep Alive Timer Expired | Keep Alive Timer expired. |
| `1Ah` | Keep Alive Timeout Invalid | Keep Alive Timeout value invalid. |
| `1Bh` | Command Aborted due to Preempt and Abort | Reservation Acquire with Preempt and Abort caused abort. |
| `1Ch` | Sanitize Failed | Most recent sanitize failed and recovery has not completed. |
| `1Dh` | Sanitize In Progress | Requested function is prohibited during sanitize. |
| `1Eh` | SGL Data Block Granularity Invalid | I/O Command Set-specific; NVM/ZNS. |
| `1Fh` | Command Not Supported for Queue in CMB | Command submission/completion using CMB queue not supported. |
| `20h` | Namespace is Write Protected | Command prohibited by namespace write-protection state. |
| `21h` | Command Interrupted | Processing interrupted; host should retry. |
| `22h` | Transient Transport Error | Transient transport error detected. |
| `23h` | Command Prohibited by Command and Feature Lockdown | Command execution prohibited by lockdown. |
| `24h` | Admin Command Media Not Ready | Admin command requires media access and media is not ready. |
| `25h`-`7Fh` | Reserved | Reserved. |
| `80h` | LBA Out of Range | I/O Command Set-specific; NVM/ZNS. |
| `81h` | Capacity Exceeded | Namespace utilization exceeded namespace capacity. |
| `82h` | Namespace Not Ready | Namespace not ready for access, excluding ANA conditions. |
| `83h` | Reservation Conflict | Command conflicted with a namespace reservation. |
| `84h` | Format In Progress | Format NVM command in progress on namespace. |
| `85h` | Invalid Value Size | I/O Command Set-specific; KV. |
| `86h` | Invalid Key Size | I/O Command Set-specific; KV. |
| `87h` | KV Key Does Not Exist | I/O Command Set-specific; KV. |
| `88h` | Unrecovered Error | I/O Command Set-specific; KV. |
| `89h` | Key Exists | I/O Command Set-specific; KV. |
| `90h`-`BFh` | Reserved | Reserved. |
| `C0h`-`FFh` | Vendor Specific | Vendor-specific. |

## Command Specific Status Values

Source: Figure 95.

| SC | Name | Commands Affected |
|---|---|---|
| `00h` | Completion Queue Invalid | Create I/O Submission Queue |
| `01h` | Invalid Queue Identifier | Create I/O SQ, Create I/O CQ, Delete I/O CQ, Delete I/O SQ |
| `02h` | Invalid Queue Size | Create I/O SQ, Create I/O CQ |
| `03h` | Abort Command Limit Exceeded | Abort |
| `04h` | Reserved | Reserved |
| `05h` | Asynchronous Event Request Limit Exceeded | Asynchronous Event Request |
| `06h` | Invalid Firmware Slot | Firmware Commit |
| `07h` | Invalid Firmware Image | Firmware Commit |
| `08h` | Invalid Interrupt Vector | Create I/O Completion Queue |
| `09h` | Invalid Log Page | Get Log Page |
| `0Ah` | Invalid Format | Format NVM, Namespace Management |
| `0Bh` | Firmware Activation Requires Conventional Reset | Firmware Commit, Sanitize |
| `0Ch` | Invalid Queue Deletion | Delete I/O Completion Queue |
| `0Dh` | Feature Identifier Not Saveable | Set Features |
| `0Eh` | Feature Not Changeable | Set Features |
| `0Fh` | Feature Not Namespace Specific | Set Features |
| `10h` | Firmware Activation Requires NVM Subsystem Reset | Firmware Commit, Sanitize |
| `11h` | Firmware Activation Requires Controller Level Reset | Firmware Commit, Sanitize |
| `12h` | Firmware Activation Requires Maximum Time Violation | Firmware Commit |
| `13h` | Firmware Activation Prohibited | Firmware Commit |
| `14h` | Overlapping Range | Firmware Commit, Firmware Image Download, Set Features |
| `15h` | Namespace Insufficient Capacity | Namespace Management |
| `16h` | Namespace Identifier Unavailable | Namespace Management |
| `17h` | Reserved | Reserved |
| `18h` | Namespace Already Attached | Namespace Attachment |
| `19h` | Namespace Is Private | Namespace Attachment |
| `1Ah` | Namespace Not Attached | Namespace Attachment |
| `1Bh` | Thin Provisioning Not Supported | Namespace Management |
| `1Ch` | Controller List Invalid | Namespace Attachment |
| `1Dh` | Device Self-test In Progress | Device Self-test |
| `1Eh` | Boot Partition Write Prohibited | Firmware Commit |
| `1Fh` | Invalid Controller Identifier | Virtualization Management |
| `20h` | Invalid Secondary Controller State | Virtualization Management |
| `21h` | Invalid Number of Controller Resources | Virtualization Management |
| `22h` | Invalid Resource Identifier | Virtualization Management |
| `23h` | Sanitize Prohibited While Persistent Memory Region is Enabled | Sanitize |
| `24h` | ANA Group Identifier Invalid | Namespace Management |
| `25h` | ANA Attach Failed | Namespace Attachment |
| `26h` | Insufficient Capacity | Capacity Management |
| `27h` | Namespace Attachment Limit Exceeded | Namespace Attachment |
| `28h` | Prohibition of Command Execution Not Supported | Lockdown |
| `29h` | I/O Command Set Not Supported | Namespace Attachment, Namespace Management |
| `2Ah` | I/O Command Set Not Enabled | Namespace Attachment |
| `2Bh` | I/O Command Set Combination Rejected | Set Features |
| `2Ch` | Invalid I/O Command Set | Identify, Namespace Management |
| `2Dh` | Identifier Unavailable | Capacity Management |
| `2Eh`-`6Fh` | Reserved | Reserved |
| `70h`-`7Fh` | Directive Specific | See section 8.7 |
| `80h`-`BFh` | I/O Command Set Specific | See Figure 96 |
| `C0h`-`FFh` | Vendor Specific | Vendor-specific |

## I/O Command Set-Specific Command Status Values

Source: Figure 96.

| SC | Name |
|---|---|
| `80h` | Conflicting Attributes |
| `81h` | Invalid Protection Information |
| `82h` | Attempted Write to Read Only Range |
| `83h` | Command Size Limit Exceeded |
| `84h`-`B7h` | Reserved |
| `B8h` | Zoned Boundary Error |
| `B9h` | Zone Is Full |
| `BAh` | Zone Is Read Only |
| `BBh` | Zone Is Offline |
| `BCh` | Zone Invalid Write |
| `BDh` | Too Many Active Zones |
| `BEh` | Too Many Open Zones |
| `BFh` | Invalid Zone State Transition |

## Fabrics Command-Specific Status Values

Source: Figure 97.

| SC | Name | Commands Affected |
|---|---|---|
| `80h` | Incompatible Format | Connect, Disconnect |
| `81h` | Controller Busy | Connect, Disconnect |
| `82h` | Connect Invalid Parameters | Connect |
| `83h` | Connect Restart Discovery | Connect |
| `84h` | Connect Invalid Host | Connect |
| `85h` | Invalid Queue Type | Disconnect |
| `86h`-`8Fh` | Reserved | Reserved |
| `90h` | Discover Restart | Get Log Page |
| `91h` | Authentication Required | All commands except Connect, Authentication Send, Authentication Receive |
| `92h`-`AFh` | Reserved | Reserved |
| `B0h`-`BFh` | Transport Specific | NVMe Transport binding specification |

## Media And Data Integrity Error Values

Source: Figure 98.

| SC | Name | Notes |
|---|---|---|
| `00h`-`7Fh` | Reserved | Reserved. |
| `80h` | Write Fault | Write data could not be committed to media. |
| `81h` | Unrecovered Read Error | Read data could not be recovered from media. |
| `82h` | End-to-end Guard Check Error | Guard check failure. |
| `83h` | End-to-end Application Tag Check Error | Application tag check failure. |
| `84h` | End-to-end Reference Tag Check Error | Reference tag check failure. |
| `85h` | Compare Failure | NVM Command Set-specific. |
| `86h` | Access Denied | Access denied due to lack of access rights. |
| `87h` | Deallocated or Unwritten Logical Block | NVM Command Set-specific. |
| `88h` | End-to-End Storage Tag Check Error | Storage tag check failure. |
| `89h`-`BFh` | Reserved | Reserved. |
| `C0h`-`FFh` | Vendor Specific | Vendor-specific. |

## Path Related Status Values

Source: Figure 99.

| SC | Name | Notes |
|---|---|---|
| `00h` | Internal Path Error | Controller-specific internal path error. |
| `01h` | Asymmetric Access Persistent Loss | ANA persistent loss state; do not resubmit to same controller. |
| `02h` | Asymmetric Access Inaccessible | ANA inaccessible state; do not resubmit to same controller. |
| `03h` | Asymmetric Access Transition | ANA transition state; retry after transition completes. |
| `04h`-`5Fh` | Reserved | Reserved. |
| `60h` | Controller Pathing Error | Pathing error detected by controller. |
| `61h`-`6Fh` | Reserved | Reserved. |
| `70h` | Host Pathing Error | Pathing error detected by host. |
| `71h` | Command Aborted By Host | Command aborted due to host action. |
| `72h`-`7Fh` | Reserved | Reserved. |
| `80h`-`BFh` | I/O Command Set Specific | I/O Command Set-specific. |
| `C0h`-`FFh` | Vendor Specific | Vendor-specific. |

