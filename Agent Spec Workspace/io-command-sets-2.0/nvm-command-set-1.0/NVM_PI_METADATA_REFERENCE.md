# NVM Protection Information And Metadata Reference

Status: `COMPLETE`

Source:

```text
..\..\NVMe Base Spec\2.0\NVM-Express-NVM-Command-Set-Specification-2021.06.02-Ratified-1.md
```

Primary source sections / figures:

| Source | Scope |
|---|---|
| NVM section 5.2 | End-to-end data protection and metadata handling. |
| Figure 9 | Protection Information action and check bits. |
| Figure 10 | Storage Tag Check definition. |
| Figures 114-118 | 16b, 32b, and 64b Guard PI formats. |
| Figures 122-125 | Storage Tag / Reference Tag split and command dword routing. |
| Figures 126-135 | Write, Read, Compare, Copy PI processing examples and rules. |
| Figures 148-149 | Metadata contiguous with LBA data vs separate metadata buffer. |

## Purpose

This file is the shared NVM lookup for Protection Information and metadata semantics. Use it when a question touches:

| Topic | Examples |
|---|---|
| PI command fields | `PRINFO`, `PRACT`, `PRCHK`, `STC`, `LBAT`, `LBATM`, `LBST`, `ILBRT`, `ELBAT`, `ELBATM`, `ELBST`, `EILBRT`. |
| Identify / format fields | `MC`, `DPC`, `DPS`, LBA Format metadata size, Extended LBA Format `PIF`, `STS`, `LBSTM`. |
| Metadata placement | Extended logical block metadata vs separate metadata buffer / metadata SGL. |
| PI failure status | Guard, Application Tag, Reference Tag, Storage Tag, Invalid Protection Information. |

Command-specific dword locations remain in each command folder's `field-reference.md`. This file explains the shared meaning behind those fields.

## Read Path

| Need | Read |
|---|---|
| Namespace supports PI / metadata | `..\NVM_COMMAND_SET_INDEX.md` Identify snapshots, plus Identify command payload reference in Base. |
| Exact command field bits | The target command folder's `field-reference.md`. |
| Shared PI / metadata behavior | This file. |
| Command-specific status applicability | The target command folder's `status-reference.md`. |
| Global status code meaning | `..\..\Status_Code_Reference.md`. |
| ZNS Zone Append PI remap behavior | `..\..\zns-command-set-1.1\commands\7dh-zone-append`. |

## Capability And Format Fields

| Field | Owner / source structure | Meaning | Important rule | Affects |
|---|---|---|---|---|
| `MC` | Identify Namespace | Metadata capabilities. | Indicates whether metadata may be transferred as part of an extended logical block, as a separate buffer, or both. | How command data and metadata buffers are built. |
| `DPC` | Identify Namespace | End-to-end data protection capabilities. | Reports supported PI types and whether PI may be placed as first or last bytes of metadata. | Which `DPS` formats are valid. |
| `DPS` | Identify Namespace / Format NVM | Selected PI settings for the namespace. | Selects PI type and PI location for the formatted namespace. | Whether NVM I/O commands interpret PRINFO and PI fields. |
| LBA Format `MS` | Identify Namespace LBA Format | Metadata size in bytes. | PI is possible only when metadata size is large enough to contain the selected PI format. | Metadata transfer size and PI placement. |
| LBA Format `LBADS` | Identify Namespace LBA Format | Logical block data size. | 32b and 64b Guard formats require an LBA data size of at least 4 KiB. | Valid PI format selection. |
| Extended LBA Format `PIF` | NVM Identify CNS `05h` | Protection Information Format. | `00b` 16b Guard, `01b` 32b Guard, `10b` 64b Guard, `11b` reserved. | PI byte layout and tag widths. |
| Extended LBA Format `STS` | NVM Identify CNS `05h` | Storage Tag Size. | Defines how many most-significant bits of the Storage/Reference Space are Storage Tag. | Storage Tag vs Reference Tag parsing. |
| `LBSTM` | NVM Identify CNS `05h` | Logical Block Storage Tag Mask. | Used for Storage Tag checks when Storage Tag is defined and checked. | Masked Storage Tag comparisons. |
| Host Behavior Support `LBAFEE` | Feature `16h` byte `02` | Extended LBA Format Enable. | Affects whether extended LBA format reporting / selection is active. | `PIF`, `STS`, and extended LBA format interpretation. |

## Metadata Placement

| Placement | Meaning | Command data implication |
|---|---|---|
| Extended logical block | Metadata is contiguous with each logical block's data. | Data buffer includes user data plus metadata bytes per logical block. |
| Separate metadata buffer | Metadata is transferred through Metadata Pointer or metadata SGL. | Data buffer carries user data; metadata buffer carries metadata bytes. |

Important rules:

- If metadata size equals PI size, the metadata is only PI.
- If metadata size is larger than PI size, the remaining metadata bytes are non-PI metadata.
- If `PRACT` causes the controller to generate or strip PI, non-PI metadata bytes may still be transferred when metadata size is larger than PI size.
- Metadata placement is a namespace format/capability question first, then a command-buffer construction question.

## Protection Information Command Bits

| Field | Meaning | Important rule | Affects |
|---|---|---|---|
| `PRACT` | Protection Information Action. | Changes whether PI is transferred by the host or generated/removed by the controller, depending on command direction. | PI buffer content and transfer size. |
| `PRCHK[2]` | Guard Check. | When enabled, controller compares PI Guard to the calculated guard value. | Guard Check Error. |
| `PRCHK[1]` | Application Tag Check. | When enabled, controller compares Application Tag using `LBAT`/`ELBAT` and mask fields. | Application Tag Check Error. |
| `PRCHK[0]` | Reference Tag Check. | When enabled, controller compares Reference Tag according to PI type and reference-tag rules. | Reference Tag Check Error or Invalid Protection Information. |
| `STC` | Storage Tag Check. | Applies only when a Storage Tag field is defined by `STS`; otherwise ignored. | Storage Tag Check Error. |

## PI Format Summary

| PI format | Guard | Application Tag | Storage/Reference Space | `STS` range | High-value rules |
|---|---|---|---|---|---|
| 16b Guard | 16-bit CRC | 16 bits | 32 bits | `0`-`32` | `STS=0` means no Storage Tag; `STS=32` means no Reference Tag. |
| 32b Guard | 32-bit CRC | 16 bits | 64 bits | `16`-`64` | Requires LBA data size at least 4 KiB; Storage Tag is always present because minimum `STS` is 16. |
| 64b Guard | 64-bit CRC | 16 bits | 48 bits | `0`-`48` | Requires LBA data size at least 4 KiB; `STS=0` means no Storage Tag; `STS=48` means no Reference Tag. |

Reserved `PIF` values and out-of-range `STS` values have no defined NVM semantics.

## Storage Tag And Reference Tag Split

| Concept | Rule |
|---|---|
| Storage Tag | The most-significant `STS` bits of the Storage/Reference Space. |
| Logical Block Reference Tag | The remaining least-significant bits of the Storage/Reference Space. |
| No Storage Tag | Occurs when `STS=0` for 16b Guard or 64b Guard formats. |
| No Reference Tag | Occurs when `STS` consumes the full Storage/Reference Space. |
| `LBSTM` | Masks Storage Tag comparison when Storage Tag Check is performed. |

If there is no Storage Tag, `STC` does not create a Storage Tag comparison. If there is no Reference Tag, Reference Tag checking does not have a Reference Tag field to compare.

## Command Field Routing

| Command family | PI field names | Meaning |
|---|---|---|
| Write-like path | `LBST`, `ILBRT`, `LBAT`, `LBATM` | Expected / inserted Storage Tag, initial Logical Block Reference Tag, Application Tag, Application Tag Mask. |
| Read-like path | `ELBST`, `EILBRT`, `ELBAT`, `ELBATM` | Expected Storage Tag, expected initial Logical Block Reference Tag, expected Application Tag, expected Application Tag Mask. |
| Compare | Uses read-like expected fields plus compare data/metadata payload. | Comparison excludes PI bytes; PI checking follows NVM Compare rules. |
| Verify | Uses read-like PI check fields without transferring user data. | Verification may surface read-like media/data integrity errors. |
| Copy | Uses read-side `PRINFOR` and write-side `PRINFOW` controls. | Read portion and write portion each have their own PI action/check rules. |
| Write Zeroes | Uses write-like PI fields. | Command-specific restrictions still come from the Write Zeroes folder. |

The command dword packing for `LBST`/`ELBST` and `ILBRT`/`EILBRT` depends on PI format and `STS`. Unused command dword bits are ignored by the controller.

## PRACT Behavior By Command

| Command | `PRACT=0` | `PRACT=1` | Notes |
|---|---|---|---|
| Write | Host transfers PI with metadata; controller may check enabled PI fields. | Controller generates PI from command fields and user data. | If metadata size is larger than PI size, host still transfers non-PI metadata bytes. |
| Read | Controller transfers PI to host with metadata; controller may check enabled PI fields. | Controller checks PI as applicable, then removes PI from the returned metadata. | If metadata size is larger than PI size, non-PI metadata may still be returned. |
| Compare | Host supplies compare data and metadata; PI is processed according to Compare rules. | Command-specific restrictions apply; use Compare folder before claiming validity. | Compare compares data and non-PI metadata while PI has separate check semantics. |
| Verify | No user-data transfer; PI checks follow read-like rules. | Command-specific restrictions apply; use Verify folder before claiming validity. | Verify is useful for integrity/status lookup without data transfer. |
| Copy | Read and write portions are controlled separately by `PRINFOR` and `PRINFOW`. | Invalid read/write `PRACT` combinations are command-specific Copy errors. | Use Copy folder for source-range descriptor details. |

## Check Behavior And Status Mapping

| Check | Compared value | Status surface |
|---|---|---|
| Guard Check | PI Guard vs controller-calculated guard value. | Guard Check Error. |
| Application Tag Check | PI Application Tag vs `LBAT` / `ELBAT`, using `LBATM` / `ELBATM`. | Application Tag Check Error. |
| Storage Tag Check | PI Storage Tag vs `LBST` / `ELBST`, using `LBSTM`. | Storage Tag Check Error. |
| Reference Tag Check | PI Reference Tag vs command-derived reference tag. | Reference Tag Check Error or Invalid Protection Information, depending on the violation. |
| Invalid PI format / invalid PI command use | Command PI fields inconsistent with namespace PI format or command rules. | Invalid Protection Information or Invalid Field in Command, depending on the command rule. |

Use `Status_Code_Reference.md` for the global status code definitions. Use the command folder's `status-reference.md` for whether a status is listed for that command.

## Reference Tag Rules

| PI type | Reference Tag rule |
|---|---|
| Type 1 | Reference Tag is tied to the logical block reference. NVM uses `ILBRT` / `EILBRT`; host initialization must align with the command's starting LBA rule. |
| Type 2 | Reference Tag is compared to the command-derived reference tag. |
| Type 3 | Reference Tag checking should not be performed; commands may ignore `ILBRT` / `EILBRT` for Reference Tag purposes. |

When the Reference Tag field is all ones, the spec defines cases where Reference Tag checking is disabled. When the Application Tag field is all ones, Application Tag checking may also be disabled. For byte-exact all-ones width, use the selected PI format's field width.

## Ignore / Disable Conditions

| Condition | Result |
|---|---|
| Namespace is not formatted with PI | PI-specific checks and fields are not meaningful unless a command-specific rule says the command is invalid. |
| `PRCHK` bit is clear | That PI check is not requested. |
| `STC` set but no Storage Tag is defined | Storage Tag comparison is not performed. |
| Reserved PI values | No defined NVM behavior; do not infer semantics. |
| Vendor-specific metadata | Vendor documentation is required. |

## Boundaries

- This file does not define PyNVMe calls, pytest behavior, fixtures, or test flow steps.
- This file does not replace per-command field/status files. It supplies shared PI and metadata semantics.
- ZNS Zone Append has additional `PIREMAP` behavior; use the ZNS Zone Append folder for that overlay.
- Exact CRC polynomial/test-vector implementation belongs to the NVM source figures when byte-perfect CRC generation is needed. This markdown captures routing, field meaning, and status behavior.
