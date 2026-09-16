# Base Spec 2.0 Index

This file is a reading map for the local NVMe Base Specification 2.0 source. It is not a replacement for the specification.

## Primary Source

```text
NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

Specification identity from the source front matter:

| Item | Value |
|---|---|
| Specification | NVM Express Base Specification |
| Revision | 2.0 |
| Date | May 13th, 2021 |
| Ratified source filename | `NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md` |

## High-Level Sections

| Topic | Section | Purpose For This Spec Layer |
|---|---:|---|
| Introduction and scope | 1 | Defines scope, conventions, terminology, and cross-spec relationships. |
| Theory of operation | 2 | Explains transport model, storage model, and controller model context. |
| NVMe architecture | 3 | Defines controllers, namespaces, queues, command submission/completion, resets, shutdown, and keep alive. |
| Data structures | 4 | Defines common data layout, features, identifiers, lists, and NQN concepts. |
| Admin command set | 5 | Defines Base Spec Admin commands and Admin opcode table. |
| Fabrics command set | 6 | Defines Fabrics command capsule and response behavior. |
| I/O commands | 7 | Defines I/O commands common to all I/O Command Sets. |
| Extended capabilities | 8 | Defines extended capabilities referenced by commands/features. |
| Error reporting and recovery | 9 | Defines high-level error reporting and recovery topics. |

## Core Command And Completion References

| Topic | Section / Figure | Notes |
|---|---|---|
| Submission Queue Entry | Section 3.3.3.1; Figure 86; Figure 87 | Common 64-byte command format, CDW0, NSID, MPTR, DPTR, CDW10-CDW15. |
| Vendor-specific command common format | Figure 88 | Optional Admin and NVM vendor-specific command format. |
| Completion Queue Entry | Section 3.3.3.2; Figure 89; Figure 90; Figure 91 | Common CQE layout, SQID/SQHD, status field, phase tag, CID. |
| Status Field | Section 3.3.3.2.1; Figure 92 | DNR, More, SCT, SC field definitions. |
| Status Code Type | Figure 93 | Generic, command specific, media/data integrity, path related, vendor specific. |
| Generic Command Status | Figure 94 | Generic status values. |
| Command Specific Status | Figure 95; Figure 96; Figure 97 | Admin, I/O command set, and Fabrics command-specific status values. |
| Media and Data Integrity Status | Figure 98 | Media and data integrity error values. |
| Path Related Status | Figure 99 | Path related status values. |

## Controller Property References

| Topic | Section / Figure | Notes |
|---|---|---|
| Controller Property model and map | Section 3.1.3; Figure 35 | Canonical route: `controller-properties-2.0\CONTROLLER_PROPERTY_INDEX.md`. |
| Core capability, configuration, and status properties | Sections 3.1.3.1-3.1.3.7, 3.1.3.20-3.1.3.21; Figures 36-49, 61-62 | `CAP`, `VS`, `CC`, `CSTS`, `NSSR`, `NSSD`, `CRTO`. |
| Interrupt and Admin Queue properties | Sections 3.1.3.3-3.1.3.4, 3.1.3.8-3.1.3.10; Figures 44-45, 49-51 | `INTMS`, `INTMC`, `AQA`, `ASQ`, `ACQ`. |
| CMB, Boot Partition, and PMR properties | Sections 3.1.3.11-3.1.3.19, 3.1.3.22-3.1.3.28; Figures 52-60, 63-69 | Canonical field lookup in `controller-properties-2.0\MEMORY_REGION_PROPERTIES.md`. |
| Transport-specific Controller Property space | Figure 35, starting `1000h` | Applicable transport owns the mapping; PCIe queue doorbells begin here. |

## Admin Command References

| Topic | Section / Figure | Notes |
|---|---|---|
| Admin command overview | Section 5 | Base Spec Admin command set. |
| Admin opcode table | Figure 138 | Source for `Admin_Command_Spec_Table.md`. |
| Sanitize/Format command allowance table | Figure 139 | Defines Admin commands allowed during sanitize and expected during Format NVM processing. |
| Abort | 5.1 | Admin command. |
| Asynchronous Event Request | 5.2 | Admin command. |
| Capacity Management | 5.3 | Admin command. |
| Create I/O Completion Queue | 5.4 | Admin command. |
| Create I/O Submission Queue | 5.5 | Admin command. |
| Delete I/O Completion Queue | 5.6 | Admin command. |
| Delete I/O Submission Queue | 5.7 | Admin command. |
| Doorbell Buffer Config | 5.8 | Admin command. |
| Device Self-test | 5.9 | Admin command. |
| Directive Receive | 5.10 | Admin command. |
| Directive Send | 5.11 | Admin command. |
| Firmware Commit | 5.12 | Admin command. |
| Firmware Image Download | 5.13 | Admin command. |
| Format NVM | 5.14 | Admin command. |
| Get Features | 5.15 | Admin command. |
| Get Log Page | 5.16 | Admin command. |
| Identify | 5.17 | Admin command. |
| Keep Alive | 5.18 | Admin command. |
| Lockdown | 5.19 | Admin command. |
| NVMe-MI Receive | 5.20 | Admin command. |
| NVMe-MI Send | 5.21 | Admin command. |
| Namespace Attachment | 5.22 | Admin command. |
| Namespace Management | 5.23 | Admin command. |
| Sanitize | 5.24 | Admin command. |
| Security Receive | 5.25 | Admin command. |
| Security Send | 5.26 | Admin command. |
| Set Features | 5.27 | Admin command. |
| Virtualization Management | 5.28 | Admin command. |

## I/O Command References

| Topic | Section / Figure | Notes |
|---|---|---|
| I/O command overview | Section 7 | I/O commands submitted to I/O Submission Queues. |
| Common I/O opcode table | Figure 390 | Source for `IO_Command_Spec_Table.md`. |
| Flush | 7.1 | Common I/O command. |
| Reservation Acquire | 7.2 | Common I/O command. |
| Reservation Register | 7.3 | Common I/O command. |
| Reservation Release | 7.4 | Common I/O command. |
| Reservation Report | 7.5 | Common I/O command. |

## Cross-Spec Boundaries

Base Spec 2.0 repeatedly delegates user data format, end-to-end protection information, and I/O Command Set-specific commands to applicable I/O Command Set specifications. When the Base Spec delegates behavior, mark it as delegated rather than filling the detail from memory.

## Current Command Folders

Command folders are organized as per-command reference material for later test-flow agents. They are not test scripts.

| Group | Folder | Scope |
|---|---|---|
| Admin commands | `admin-commands-2.0\` | Contains one folder for each Admin command row in Figure 138. Each command folder uses the canonical command reference split for precise command, field, status, payload, restriction, and boundary lookup. |
| I/O commands | `io-commands-2.0\` | Contains one folder for each common I/O command row in Figure 390. I/O Command Set-specific command details are routed to the command-set layer when Base delegates ownership. |
| I/O command-set boundary | `io-command-sets-2.0\` | Routes Base handoff points to NVM 1.0, Key Value 1.0, and ZNS 1.1 command-set sources and expanded detail folders. |
| NVM command-set details | `io-command-sets-2.0\nvm-command-set-1.0\` | Contains expanded NVM-specific I/O command folders and the NVM-owned Get LBA Status Admin hook. |
| Key Value command-set details | `io-command-sets-2.0\key-value-command-set-1.0\` | Contains expanded KV Store, Retrieve, List, Delete, and Exist command folders. |
| Fabrics commands | `fabrics-base-2.0\commands\` | Contains Base Spec section 6 Fabrics command folders keyed by `FCTYPE`. |
| ZNS commands | `zns-command-set-1.1\commands\` and `zns-command-set-1.1\modified-nvm-commands\` | Contains ZNS-owned commands and ZNS overlays for NVM commands. |
| NVMe-MI | `mi-1.2\` | Contains NVMe Management Interface Revision 1.2 source, native MI commands, Admin-through-MI, PCIe-through-MI, status, error, and in-band/out-of-band boundary references. |
| PCIe transport | `pcie-transport-1.0\` | Contains NVMe over PCIe transport source, register/capability, doorbell, queue, reset, interrupt, power, error, and host-flow references. |
| RDMA transport | `rdma-transport-1.0\` | Contains NVMe RDMA transport source index and boundary references. |
| TCP transport | `tcp-transport-1.0\` | Contains NVMe TCP transport source index and boundary references. |
| MCTP Base | `mctp-base-1.3.1\` | Contains MCTP Base DSP0236 Version 1.3.1 source index, EID/message/control/routing behavior reference, and NVMe-MI boundary map. |
| MCTP PCIe VDM binding | `mctp-pcie-vdm-1.0.1\` | Contains MCTP over PCIe VDM DSP0238 Version 1.0.1 source index and transport-binding behavior reference. |
| MCTP SMBus/I2C binding | `mctp-smbus-i2c-1.1.0\` | Contains MCTP over SMBus/I2C DSP0237 Version 1.1.0 source index and transport-binding behavior reference. |

## Expanded Command Folders

| Command | Folder | Scope |
|---|---|---|
| Identify | `admin-commands-2.0\06h-identify` | Base Spec 2.0-only Admin command reference using core plus specialized files. Command-set-specific Identify payloads are marked as delegated. |
| Get Log Page | `admin-commands-2.0\02h-get-log-page` | Base log-page selector, command fields, status, and high-value returned payload field lookup. Command-set-specific and vendor-specific logs are routed by boundary. |
| Directives | `admin-commands-2.0\19h-directive-send`, `admin-commands-2.0\1ah-directive-receive` | Directive command shell plus section 8.7 directive type/operation routing. |
| NVM command-set I/O | `io-command-sets-2.0\nvm-command-set-1.0\io-commands` | NVM-owned I/O command field/status/payload lookup for Write, Read, Compare, Verify, Copy, Dataset Management, Write Zeroes, and Write Uncorrectable. |
| Key Value command-set I/O | `io-command-sets-2.0\key-value-command-set-1.0\io-commands` | KV-owned I/O command field/status/payload lookup for Store, Retrieve, List, Delete, and Exist. |
| ZNS command-set commands | `zns-command-set-1.1\commands`, `zns-command-set-1.1\modified-nvm-commands` | ZNS-owned commands plus ZNS overlays for applicable NVM commands. |

## Canonical Command Folder Shape

Command folders use this shape when the command has Base-owned behavior:

```text
README.md
command-facts.md
field-reference.md
status-reference.md
cross-spec-boundary.md
COMMAND_CONTENT_AUDIT.md
selector-reference.md        # when selectors/actions/subselectors exist
payload-reference.md         # when command data or returned payload exists
restrictions.md              # when command-specific restrictions exist
```

Use `README.md` as the human entry point, then jump to the smallest reference file that matches the question. Boundary-only folders are complete when they precisely identify the Base-owned opcode surface and route delegated details without inventing external-spec behavior.
