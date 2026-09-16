# NVM Command Set 1.0 Index

Status: `COMMAND-INDEX-COMPLETE`

Primary source:

```text
..\NVMe Base Spec\2.0\NVM-Express-NVM-Command-Set-Specification-2021.06.02-Ratified-1.md
```

## Identity

| Item | Value |
|---|---|
| Command set | NVM Command Set |
| CSI | `00h` |
| Base referenced revision | Revision 1.0 |
| Local source scope | NVM I/O commands, NVM features, NVM log pages, NVM Identify structures, NVM Namespace Management hooks, NVM media/data behavior. |

## I/O Command Index

Source: NVM Command Set Figure 18.

| Opcode | Command | Reference | Data direction | NSID rule |
|---:|---|---|---|---|
| `00h` | Flush | Base Specification | No data transfer | Uses NSID rules from Base / applicable command set. |
| `01h` | Write | `nvm-command-set-1.0\io-commands\01h-write` | Host to controller | Uses NSID. |
| `02h` | Read | `nvm-command-set-1.0\io-commands\02h-read` | Controller to host | Uses NSID. |
| `04h` | Write Uncorrectable | `nvm-command-set-1.0\io-commands\04h-write-uncorrectable` | No data transfer | Uses NSID. |
| `05h` | Compare | `nvm-command-set-1.0\io-commands\05h-compare` | Host to controller | Uses NSID. |
| `08h` | Write Zeroes | `nvm-command-set-1.0\io-commands\08h-write-zeroes` | No data transfer | Uses NSID. |
| `09h` | Dataset Management | `nvm-command-set-1.0\io-commands\09h-dataset-management` | Host to controller | Uses NSID. |
| `0Ch` | Verify | `nvm-command-set-1.0\io-commands\0ch-verify` | No data transfer | Uses NSID. |
| `0Dh` | Reservation Register | Base Specification | Host to controller | Uses NSID. |
| `0Eh` | Reservation Report | Base Specification | Controller to host | Uses NSID. |
| `11h` | Reservation Acquire | Base Specification | No data transfer / Base-defined | Uses NSID. |
| `15h` | Reservation Release | Base Specification | No data transfer / Base-defined | Uses NSID. |
| `19h` | Copy | `nvm-command-set-1.0\io-commands\19h-copy` | Host to controller command data payload | Uses NSID. |
| `80h`-`FFh` | Vendor specific | Vendor specific | Command-specific | Command-specific. |

All NVM Command Set commands use the Namespace Identifier field. `FFFFFFFFh` is not supported unless a figure footnote explicitly allows it.

## Expanded NVM Command Folders

| Command | Folder | Use when you need |
|---|---|---|
| Write | `nvm-command-set-1.0\io-commands\01h-write` | `SLBA`, `NLB`, `PRINFO`, `FUA`, `LR`, `DTYPE`, `DSPEC`, DSM hints, write status. |
| Read | `nvm-command-set-1.0\io-commands\02h-read` | `SLBA`, `NLB`, `PRINFO`, `FUA`, `LR`, DSM read hints, read payload/status. |
| Write Uncorrectable | `nvm-command-set-1.0\io-commands\04h-write-uncorrectable` | Marking LBAs invalid, `WUSL`, Unrecovered Read Error aftermath. |
| Compare | `nvm-command-set-1.0\io-commands\05h-compare` | Compare buffer payload, Compare Failure, PI checking, DULBE interaction. |
| Write Zeroes | `nvm-command-set-1.0\io-commands\08h-write-zeroes` | `DEAC`, zero readback behavior, `WZSL`, PI restrictions. |
| Dataset Management | `nvm-command-set-1.0\io-commands\09h-dataset-management` | Range descriptors, `AD`, context attributes, `DMRL/DMRSL/DMSL`, DULBE/DLFEAT. |
| Verify | `nvm-command-set-1.0\io-commands\0ch-verify` | No-transfer integrity check, `VSL`, Read-like media/data status behavior. |
| Copy | `nvm-command-set-1.0\io-commands\19h-copy` | `SDLBA`, source range entries, descriptor format, `MSRC/MSSRL/MCL`, copy failure CQE Dword 0. |

## Shared NVM Behavior References

| Reference | Use when you need |
|---|---|
| `nvm-command-set-1.0\NVM_PI_METADATA_REFERENCE.md` | Shared Protection Information and metadata behavior across Write, Read, Compare, Verify, Copy, and Write Zeroes: `PRINFO`, `PRACT`, `PRCHK`, `STC`, `PIF`, `STS`, `LBSTM`, Storage Tag / Reference Tag split, metadata placement, and PI status mapping. |

## NVM Feature Index

Source: NVM Command Set Figure 79.

| FID | Feature | Persistent | Memory Buffer |
|---:|---|---|---|
| `03h` | LBA Range Type | Yes | Yes |
| `05h` | Error Recovery | No | No |
| `0Ah` | Write Atomicity Normal | No | No |
| `15h` | LBA Status Information Report Interval | No | No |

### NVM Feature Field Snapshot

| FID | Field / payload | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `03h` LBA Range Type | Data buffer entries | LBA range type descriptors. | Namespace-specific; Set with `NSID=FFFFFFFFh` is invalid. | Dataset/LBA range behavior. |
| `05h` Error Recovery | CDW11 / CQE DW0 | Error recovery timeout / DULBE-related behavior. | Tied to namespace deallocated/unwritten logical block behavior. | Error recovery and DULBE tests. |
| `0Ah` Write Atomicity Normal | CDW11 / CQE DW0 | Write atomicity normal setting. | Controls whether normal atomic write unit behavior applies. | Atomic write tests. |
| `15h` LBA Status Information Report Interval | CDW11 / CQE DW0 | Interval for LBA Status Information reporting. | Supports Get LBA Status / LBA Status Information log behavior. | Potentially Unrecoverable LBA reporting. |
| `16h` Host Behavior Support byte `02` | `LBAFEE` | Enables extended LBA formats for NVM when supported. | `1h` enables extended LBA formats and related PI formats; `0h` limits reported LBA formats/granularity to legacy-size views. | Namespace Management, Format NVM, PI format selection. |

## NVM Log Page Index

Source: NVM Command Set Figure 89.

| LID | Log Page | Reference |
|---:|---|---|
| `01h` | Controller Error Information | 4.1.4.1 |
| `02h` | Controller or NVM Subsystem SMART / Health Information | 4.1.4.2 |
| `06h` | Controller Device Self-test | 4.1.4.3 |
| `0Eh` | Controller LBA Status Information | 4.1.4.5 |

## Identify CNS Index

Source: NVM Command Set Figure 96.

| CNS | Meaning | Reference | CSI used |
|---:|---|---|---|
| `00h` | Identify I/O Command Set Specific Namespace data structure for controller processing command | 4.1.5.1 | Yes |
| `01h` | Identify Controller data structure for controller processing command | 4.1.5.2 | No |
| `05h` | I/O Command Set specific Identify Namespace data structure for specified NSID and CSI | 4.1.5.3 | Yes |
| `06h` | I/O Command Set Specific Controller data structure | 4.1.5.4 | Yes |
| `11h` | Identify Namespace data structure for specified allocated NSID | 4.1.5.5 | No |
| `16h` | Namespace Granularity List | 4.1.5.6 | No |

### NVM Identify Structure Snapshot

| CNS | Structure | High-value fields | Affects |
|---:|---|---|---|
| `00h` / `11h` | NVM Identify Namespace | `NSZE`, `NCAP`, `NUSE`, `NSFEAT`, `NLBAF`, `FLBAS`, `MC`, `DPC`, `DPS`, `NMIC`, `RESCAP`, `FPI`, `NAWUN`, `NAWUPF`, `NACWU`, `NABSN`, `NABO`, `NABSPF`, `NOIOB`, `ANAGRPID`, `NSATTR`, `NVMSETID`, `ENDGID`, `NGUID`, `EUI64`, LBA Format table. | Namespace capacity, format, protection information, sharing, reservations, ANA, atomicity, optimal I/O. |
| `05h` | I/O Command Set specific Identify Namespace for CSI `00h` | `LBSTM`, `PIC`, Extended LBA Format entries. | Storage Tag mask, PI format capability, extended LBA format parsing. |
| `06h` | NVM Identify Controller for CSI `00h` | NVM command-set controller-specific capability fields. | NVM command support and command-set-specific capabilities. |
| `16h` | Namespace Granularity List | Namespace Granularity Attributes and up to 16/64 granularity descriptors depending on `LBAFEE`. | Namespace Management create `NSZE`/`NCAP` granularity validation. |

### NVM Extended LBA Format Entry

Source: NVM Figures 100-101.

| Bits / bytes | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| Identify CNS `05h` bytes `07:00` | `LBSTM` | Logical Block Storage Tag Mask. | Ignored if end-to-end protection is not enabled. | Storage Tag validation. |
| Identify CNS `05h` byte `08` bit `1` | `16BPISTM` | 16b Guard PI Storage Tag Mask rule. | If set, `LBSTM` shall be all ones for 16b Guard PI under the specified conditions. | 16b PI tests. |
| Identify CNS `05h` byte `08` bit `0` | `16BPISTS` | 16b Guard PI Storage Tag Support. | If clear, 16b Guard PI requires `STS=0`; if 32b/64b Guard PI is supported by any LBA format, this bit shall be set. | PI feature gating. |
| Extended LBA Format bits `08:07` | `PIF` | Protection Information Format. | `00b` 16b Guard; `01b` 32b Guard; `10b` 64b Guard; `11b` reserved. | PI format selection. |
| Extended LBA Format bits `06:00` | `STS` | Storage Tag Size. | Defines MSBs of Storage/Reference Space used as Storage Tag. Valid range depends on PI format. | Storage Tag parser. |

## I/O Command Set Specific Admin Hook

Source: NVM Command Set section 4.2.1.

| Admin command | Base opcode | NVM authority |
|---|---:|---|
| Get LBA Status | `86h` | `nvm-command-set-1.0\admin-commands\86h-get-lba-status` expands NVM-specific request fields, LBA Status Descriptor List behavior, and `ATYPE` behavior. |

The Get LBA Status command requests information about Potentially Unrecoverable LBAs. It uses Data Pointer and CDW10-CDW13. `ATYPE=10h` requests Untracked LBAs and may require significant controller scanning time. Use the expanded folder when exact CDW, descriptor, `CMPC`, or LBA Status Information log relationship is needed.

## Namespace Management Hook

NVM Command Set owns NVM-specific Namespace Management content, including NVM namespace create fields and Namespace Granularity reporting. Base Spec 2.0 CDW11.CSI `0h` creates a namespace using the NVM Command Set.

### NVM Namespace Management Create Fields

Use `admin-commands-2.0\0dh-namespace-management\payload-reference.md` for the byte-exact create buffer. NVM-specific bytes include `FLBAS`, `DPS`, `NMIC`, `ANAGRPID`, `NVMSETID`, `ENDGID`, and `LBSTM`.

## Boundary Notes

- Base owns command-set selection and the common Admin command shell.
- NVM owns logical-block command behavior, LBA format details, NVM-specific status behavior, NVM features/log pages, and NVM namespace data structures.
- ZNS is based on NVM for several commands but adds zone-specific restrictions and statuses. Use `ZNS_COMMAND_SET_INDEX.md` when CSI is `02h`.

## ZNS Modified NVM Command Redirects

When the namespace is associated with the Zoned Namespace Command Set (`CSI=02h`), read the expanded ZNS folders before making final status or restriction claims:

| NVM Opcode | Command | ZNS folder |
|---:|---|---|
| `00h` | Flush | `..\zns-command-set-1.1\modified-nvm-commands\00h-flush` |
| `01h` | Write | `..\zns-command-set-1.1\modified-nvm-commands\01h-write` |
| `02h` | Read | `..\zns-command-set-1.1\modified-nvm-commands\02h-read` |
| `04h` | Write Uncorrectable | `..\zns-command-set-1.1\modified-nvm-commands\04h-write-uncorrectable` |
| `05h` | Compare | `..\zns-command-set-1.1\modified-nvm-commands\05h-compare` |
| `08h` | Write Zeroes | `..\zns-command-set-1.1\modified-nvm-commands\08h-write-zeroes` |
| `09h` | Dataset Management | `..\zns-command-set-1.1\modified-nvm-commands\09h-dataset-management` |
| `0Ch` | Verify | `..\zns-command-set-1.1\modified-nvm-commands\0ch-verify` |
| `19h` | Copy | `..\zns-command-set-1.1\modified-nvm-commands\19h-copy` |
