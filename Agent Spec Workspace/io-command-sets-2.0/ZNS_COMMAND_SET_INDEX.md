# Zoned Namespace Command Set 1.1 Index

Status: `COMMAND-INDEX-COMPLETE`

Primary source:

```text
..\NVMe Base Spec\2.0\NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md
```

## Identity

| Item | Value |
|---|---|
| Command set | Zoned Namespace Command Set |
| CSI | `02h` |
| Base referenced revision | Revision 1.1 |
| Local source scope | Zone model, ZNS command support, ZNS-modified NVM commands, ZNS-owned commands, ZNS Admin behavior, Changed Zone List log page, ZNS Identify structures, ZNS Namespace Management hooks. |

## Version Check

| Check | Result |
|---|---|
| Base reference | Base Spec 2.0 references `NVM Express Zoned Namespace Command Set Specification, Revision 1.1`. |
| Local file | Filename and content indicate Zoned Namespace Command Set Specification revision 1.1, 2021.06.02 ratified source. |
| Difference found | No version difference found inside the local Base 2.0 source bundle. |

## Mandatory / Optional Command Support

Source: ZNS Figure 9.

| Command | Requirement |
|---|---|
| Zone Management Send | Mandatory |
| Zone Management Receive | Mandatory |
| Zone Append | Optional |

## I/O Command Index

Source: ZNS Figure 12 and ZNS section 3.3 / 3.4.

| Opcode | Command | ZNS reference | Data direction | Authority / ZNS role |
|---:|---|---|---|---|
| `00h` | Flush | 3.3.4 | Base/NVM-defined | Base/NVM command implemented with ZNS additional status behavior. |
| `01h` | Write | 3.3.7 | NVM-defined | NVM command modified by ZNS zone rules. |
| `02h` | Read | 3.3.5 | NVM-defined | NVM command modified by ZNS zone rules. |
| `04h` | Write Uncorrectable | 3.3.8 | NVM-defined | NVM command modified by ZNS zone rules. |
| `05h` | Compare | 3.3.1 | NVM-defined | NVM command modified by ZNS zone rules. |
| `08h` | Write Zeroes | 3.3.9 | NVM-defined | NVM command modified by ZNS zone rules. |
| `09h` | Dataset Management | 3.3.3 | NVM-defined | NVM command implemented by ZNS with additional Offline-zone behavior. |
| `0Ch` | Verify | 3.3.6 | NVM-defined | NVM command modified by ZNS zone rules. |
| `0Dh` | Reservation Register | Base Specification | Base-defined | Common command implemented in ZNS context. |
| `0Eh` | Reservation Report | Base Specification | Base-defined | Common command implemented in ZNS context. |
| `11h` | Reservation Acquire | Base Specification | Base-defined | Common command implemented in ZNS context. |
| `15h` | Reservation Release | Base Specification | Base-defined | Common command implemented in ZNS context. |
| `19h` | Copy | 3.3.2 | NVM-defined | NVM command modified by ZNS source/destination zone rules. |
| `79h` | Zone Management Send | 3.4.3 | Host to controller | Defined by ZNS. |
| `7Ah` | Zone Management Receive | 3.4.2 | Controller to host | Defined by ZNS. |
| `7Dh` | Zone Append | 3.4.1 | Host to controller | Defined by ZNS. |

All ZNS commands use the Namespace Identifier field. `FFFFFFFFh` is not supported unless the opcode table footnote explicitly allows it.

## Expanded ZNS Command Folders

Detailed command-control folders live in the root-level expanded ZNS layer:

```text
..\zns-command-set-1.1
```

### ZNS-Owned Commands

| Opcode | Command | Folder | Status |
|---:|---|---|---|
| `79h` | Zone Management Send | `..\zns-command-set-1.1\commands\79h-zone-management-send` | `COMPLETE + STATUS-MATRIX-COMPLETE` |
| `7Ah` | Zone Management Receive | `..\zns-command-set-1.1\commands\7ah-zone-management-receive` | `COMPLETE + DATA-STRUCTURE-COMPLETE` |
| `7Dh` | Zone Append | `..\zns-command-set-1.1\commands\7dh-zone-append` | `COMPLETE` |

### ZNS-Modified NVM Commands

| Opcode | Command | Folder | Status |
|---:|---|---|---|
| `00h` | Flush | `..\zns-command-set-1.1\modified-nvm-commands\00h-flush` | `COMPLETE` |
| `01h` | Write | `..\zns-command-set-1.1\modified-nvm-commands\01h-write` | `COMPLETE` |
| `02h` | Read | `..\zns-command-set-1.1\modified-nvm-commands\02h-read` | `COMPLETE` |
| `04h` | Write Uncorrectable | `..\zns-command-set-1.1\modified-nvm-commands\04h-write-uncorrectable` | `COMPLETE` |
| `05h` | Compare | `..\zns-command-set-1.1\modified-nvm-commands\05h-compare` | `COMPLETE` |
| `08h` | Write Zeroes | `..\zns-command-set-1.1\modified-nvm-commands\08h-write-zeroes` | `COMPLETE` |
| `09h` | Dataset Management | `..\zns-command-set-1.1\modified-nvm-commands\09h-dataset-management` | `COMPLETE` |
| `0Ch` | Verify | `..\zns-command-set-1.1\modified-nvm-commands\0ch-verify` | `COMPLETE` |
| `19h` | Copy | `..\zns-command-set-1.1\modified-nvm-commands\19h-copy` | `COMPLETE` |

## ZNS Command-Specific Status Snapshot

Source: ZNS Figure 11 and Figures 13-21 / 30 / 40.

| Status | Meaning | Applies to |
|---:|---|---|
| `B8h` | Zone Boundary Error | Compare, Copy, Read, Verify, Write, Write Uncorrectable, Write Zeroes, Zone Append |
| `B9h` | Zone Is Full | Copy, Write, Write Uncorrectable, Write Zeroes, Zone Append |
| `BAh` | Zone Is Read Only | Copy, Write, Write Uncorrectable, Write Zeroes, Zone Append, Zone Management Send |
| `BBh` | Zone Is Offline | Compare, Copy, Dataset Management, Flush, Read, Verify, Write, Write Uncorrectable, Write Zeroes, Zone Append, Zone Management Send |
| `BCh` | Zone Invalid Write | Copy, Write, Write Uncorrectable, Write Zeroes |
| `BDh` | Too Many Active Zones | Copy, Write, Write Uncorrectable, Write Zeroes, Zone Append, Zone Management Send |
| `BEh` | Too Many Open Zones | Copy, Write, Write Uncorrectable, Write Zeroes, Zone Append, Zone Management Send |
| `BFh` | Invalid Zone State Transition | Zone Management Send |

## ZNS Admin Behavior Index

Source: ZNS section 4.1.

| Admin area | ZNS-specific hook |
|---|---|
| Asynchronous Event Request | Adds Zone Descriptor Changed event information value `EFh`; successful completion reports the NSID in CQE Dword 1. |
| Format NVM | Operates as Base and NVM Command Set, with Format Index including valid NVM User Data Format, valid NVM Extended LBA Format, and valid ZNS LBA Format Extension. |
| Get Features / Set Features | ZNS uses NVM feature behavior plus ZNS-specific behavior. Asynchronous Event Configuration CDW11 bit 27 controls Zone Descriptor Changed Notices. |
| Get Log Page | Adds Changed Zone List log page at LID `BFh`, namespace scope. |
| Identify | Adds ZNS-specific Identify Namespace and Identify Controller structures. |

## ZNS Feature / Log / Identify Field Snapshot

| Area | Field / selector | Meaning | Important rule | Affects |
|---|---|---|---|---|
| Set/Get Features `FID=0Bh` | Asynchronous Event Configuration bit `27` | Zone Descriptor Changed Notices enable. | If set, Zone Descriptor Changed event may be sent; if clear, controller shall not send it. | AER + Changed Zone List tests. |
| Get Log Page `LID=BFh` | Changed Zone List | Up to 511 changed zone identifiers. | If controller cannot list changed zones and at least one changed event exists, Number of Zone Identifiers is `FFFFh` and list is zero-filled. Read whole page with `RAE=0`. | Zone descriptor change handling. |
| Identify CNS `05h` | ZNS Identify Namespace | `ZOC`, `OZCS`, `MAR`, `MOR`, recommended limits, LBA Format Extension table. | Main source for active/open limits, read-across-zone-boundary support, variable zone capacity, zone size, and zone descriptor extension size. | ZNS command preconditions and status expectations. |
| Identify CNS `06h` | ZNS Identify Controller | `ZASL`. | If Zone Append is supported, non-zero `ZASL` gives max Zone Append transfer as `2^n` pages; `0h` means MDTS applies. | Zone Append transfer-size tests. |

## ZNS Log Page Index

Source: ZNS Figure 45.

| LID | Log Page | Scope | Reference |
|---:|---|---|---|
| `BFh` | Changed Zone List | Namespace | 4.1.4.1 |

## Identify CNS Index

Source: ZNS Figure 47.

| CNS | Meaning | Reference | CSI |
|---:|---|---|---|
| `05h` | I/O Command Set specific Identify Namespace data structure | 4.1.5.1 | `02h` |
| `06h` | I/O Command Set specific Identify Controller data structure | 4.1.5.2 | `02h` |
| `16h` | Namespace Granularity List | NVM Command Set based behavior for logical-block command sets | `00h` or `02h` context |

### ZNS Identify Namespace Field Snapshot

Source: ZNS Figures 48-49.

| Bytes / bits | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `01:00` bit `1` | `ZAE` | Zone Active Excursions. | Controller may transition active/open/closed zones to Full due to vendor-specific excursion if set. | Unexpected full-zone behavior. |
| `01:00` bit `0` | Variable Zone Capacity | Zone capacity may change without namespace format change if set. | If clear, capacity does not change without format change. | Zone capacity validation. |
| `03:02` bit `0` | Read Across Zone Boundaries | Allows read ranges crossing zone boundaries if set. | If clear, crossing read range aborts per ZNS boundary rule. | Read boundary tests. |
| `07:04` | `MAR` | Maximum Active Resources. | 0-based; `FFFFFFFFh` means no limit. | Too Many Active Zones. |
| `11:08` | `MOR` | Maximum Open Resources. | 0-based; <= `MAR`; `FFFFFFFFh` means no limit. | Too Many Open Zones. |
| `15:12` | `RRL` | Reset Recommended Limit. | Seconds before vendor-specific action for reset-recommended zones when attribute selector is `00b`; `0h` not reported. | Zone maintenance timing. |
| `19:16` | `FRL` | Finish Recommended Limit. | Seconds before vendor-specific action for finish-recommended zones when attribute selector is `00b`; `0h` not reported. | Zone maintenance timing. |
| `43:20` | `RRL1/2/3`, `FRL1/2/3` | Additional recommended limits for zone attribute selector values `01b`-`11b`. | `0h` means not reported. | Zone maintenance timing. |
| `2815:44` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `2816...3839` | LBA Format Extension entries | One extension per LBA format. | Index matches NVM LBA Format index. | Format NVM / Namespace Management. |
| LBAFE bits `63:00` | `ZSZE` | Zone Size in logical blocks. | Shall not be `0h`. | Zone layout. |
| LBAFE bits `71:64` | `ZDES` | Zone Descriptor Extension size in 64-byte units. | `0h` means Zone Descriptor Extensions are not supported. | Extended Report Zones. |

## Namespace Management Hook

ZNS uses Base Namespace Management and NVM Command Set namespace creation fields. When Base CDW11.CSI selects `02h`, use the NVM create fields in `admin-commands-2.0\0dh-namespace-management\payload-reference.md`, and interpret `FLBAS` together with the matching ZNS LBA Format Extension entry above.

## Boundary Notes

- Base owns command-set selection and common Admin command shells.
- NVM owns base behavior and fields for NVM commands that ZNS modifies.
- ZNS owns zone model, zone state, zone boundary, write pointer, active/open resource limits, zone descriptor extension, Changed Zone List behavior, ZNS-owned commands, and ZNS command-specific statuses.
- Use this file as the ZNS command-set index. Use `..\zns-command-set-1.1` only when exact command-control details are needed.
