# Key Value Command Set 1.0 Index

Status: `COMMAND-INDEX-COMPLETE`

Primary source:

```text
..\NVMe Base Spec\2.0\NVM-Express-Key-Value-Command-Set-Specification-1.0-2021.06.02-Ratified-1.md
```

## Identity

| Item | Value |
|---|---|
| Command set | Key Value Command Set |
| CSI | `01h` |
| Base referenced revision | Revision 1.0 |
| Local source scope | Key/value command model, KV I/O commands, KV feature `20h`, KV Identify structures, KV Namespace Management hooks, KV command-specific status values. |

## Version Check

| Check | Result |
|---|---|
| Base reference | Base Spec 2.0 references `NVM Express Key Value Command Set Specification, Revision 1.0`. |
| Local file | Filename and content indicate Key Value Command Set Specification 1.0, 2021.06.02 ratified source. |
| Difference found | No version difference found inside the local Base 2.0 source bundle. |

## Mandatory Command Support

Source: KV Figure 2.

| Command | Requirement |
|---|---|
| Store | Mandatory |
| Retrieve | Mandatory |
| Delete | Mandatory |
| Exist | Mandatory |
| List | Mandatory |

## I/O Command Index

Source: KV Figure 5.

| Opcode | Command | Reference | Data direction | NSID rule |
|---:|---|---|---|---|
| Base-defined | Flush | Base Specification | Base-defined | Uses NSID in KV context. |
| Base-defined | Reservation Register | Base Specification | Base-defined | Uses NSID in KV context. |
| Base-defined | Reservation Report | Base Specification | Base-defined | Uses NSID in KV context. |
| Base-defined | Reservation Acquire | Base Specification | Base-defined | Uses NSID in KV context. |
| Base-defined | Reservation Release | Base Specification | Base-defined | Uses NSID in KV context. |
| `01h` | Store | `key-value-command-set-1.0\io-commands\01h-store` | Host to controller | Uses NSID. |
| `02h` | Retrieve | `key-value-command-set-1.0\io-commands\02h-retrieve` | Controller to host | Uses NSID. |
| `06h` | List | `key-value-command-set-1.0\io-commands\06h-list` | Controller to host | Uses NSID. |
| `10h` | Delete | `key-value-command-set-1.0\io-commands\10h-delete` | No data transfer | Uses NSID. |
| `14h` | Exist | `key-value-command-set-1.0\io-commands\14h-exist` | No data transfer | Uses NSID. |

All KV commands use the Namespace Identifier field. `FFFFFFFFh` is not supported unless a figure footnote explicitly allows it.

## Expanded KV Command Folders

| Command | Folder | Use when you need |
|---|---|---|
| Store | `key-value-command-set-1.0\io-commands\01h-store` | `VS`, `SO`, `KL`, key bytes, value payload, create-only/update-only status. |
| Retrieve | `key-value-command-set-1.0\io-commands\02h-retrieve` | `HBS`, `RO`, `KL`, returned value size in CQE Dword 0, partial retrieval. |
| List | `key-value-command-set-1.0\io-commands\06h-list` | `HBS`, starting key, returned key list structure, ordering/stability boundary. |
| Delete | `key-value-command-set-1.0\io-commands\10h-delete` | `KL`, key bytes, atomic delete, `EDNEK` interaction. |
| Exist | `key-value-command-set-1.0\io-commands\14h-exist` | Success-as-exists and `KV Key Does Not Exist` absence semantics. |

## KV Command Model Snapshot

| Topic | KV source fact |
|---|---|
| Store | Stores a key/value pair to the namespace. Store is atomic for the associated key/value pair. |
| Retrieve | Retrieves a value for the specified key. If the buffer is too small, the host should issue a later Retrieve with enough buffer. |
| Delete | Deletes the specified key/value pair. Delete is atomic for the associated key/value pair. |
| Exist | Returns whether the specified key exists. Successful status means the key exists; KV Key Does Not Exist indicates absence. |
| List | Returns a list of KV keys; ordering is not specified, but stable conditions are described by the source. |
| Ordering | The controller is not responsible for ordering checks between Retrieve and Store for the same key. |

## KV Command-Specific Status Snapshot

Source: KV command status table near the command model and individual command figures.

| Status | Meaning | Commands |
|---:|---|---|
| `81h` | Capacity Exceeded | Store |
| `82h` | Namespace Not Ready | Delete, Exist, Retrieve, Store |
| `83h` | Reservation Conflict | Delete, Store, Retrieve |
| `84h` | Format In Progress | Delete, Exist, List, Retrieve, Store |
| `85h` | Invalid Value Size | Store |
| `86h` | Invalid Key Size | List, Retrieve, Store |
| `87h` | KV Key Does Not Exist | Delete, Exist, Retrieve, Store |
| `88h` | Unrecovered Error | Retrieve |
| `89h` | Key Exists | Store |

## Feature Index

Source: KV Figure 33.

| FID | Feature | Persistent | Memory Buffer | Notes |
|---:|---|---|---|---|
| `20h` | Key Value Configuration | Yes | No | Command Set Specific feature. Logged in Persistent Event Log. |

The Key Value Configuration feature controls KV Command Set behavior. It is namespace-scoped. Set Features uses CDW11 attributes; Get Features returns attributes in CQE Dword 0.

### KV Feature `20h` Field Snapshot

Source: KV Figure 34.

| Bits | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `31:01` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| `00` | `EDNEK` | Error on Delete of Non-Existent KV Key. | If set, Delete of a non-existent key aborts with `KV Key Does Not Exist`; if clear, Delete completes as if the key existed and was deleted. | Delete negative tests and idempotent delete behavior. |

## Log Page Index

The Key Value Command Set source states that it does not define additional Key Value specific mandatory, optional, or prohibited log page support beyond the Base Specification.

## Identify CNS Index

Source: KV Figure 35.

| CNS | Meaning | Reference | CSI |
|---:|---|---|---|
| `05h` | I/O Command Set specific Identify Namespace data structure for specified NSID and CSI | 4.1.5.1 | `01h` |
| `06h` | I/O Command Set Specific Controller data structure | 4.1.5.2 | `01h` |

KV notes that it does not have a CNS `06h` controller data structure; the controller returns a zero-filled data structure.

### KV Identify Namespace Field Snapshot

Source: KV Figures 36-37.

| Bytes | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `07:00` | `NSZE` | Namespace size in bytes for KV keys and values. | Undefined before namespace is formatted. | Capacity tests. |
| `15:08` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `23:16` | `NUSE` | Bytes currently allocated for KV keys and values. | <= `NSZE`; cleared to `0h` when ANA Inaccessible or Persistent Loss applies under ANA reporting. | Utilization and ANA behavior. |
| `24` | `NSFEAT` | Namespace features. | bit3 controls NGUID/EUI64 reuse semantics; bits7:4 and 2:0 reserved. | Namespace identity reuse. |
| `25` | `NKVF` | Number of KV formats. | 0-based; max supported indication is 16; formats beyond value are invalid. | KV format parser. |
| `26` | `NMIC` | Namespace sharing capabilities. | Same role as Base Identify Namespace. | Multipath/sharing. |
| `27` | `RESCAP` | Reservation capabilities. | Base semantics. | Reservation support. |
| `28` | `FPI` | Format Progress Indicator. | Base semantics. | Format progress. |
| `35:32` | `NOVG` | Namespace Optimal Value Granularity in bytes. | `0h` means not reported. | Store value sizing for performance. |
| `39:36` | `ANAGRPID` | ANA Group Identifier. | Base semantics. | ANA grouping. |
| `43` | `NSATTR` | Namespace Attributes. | Base semantics. | Namespace attributes. |
| `45:44` | `NVMSETID` | NVM Set Identifier. | Base semantics. | NVM Set grouping. |
| `47:46` | `ENDGID` | Endurance Group Identifier. | Base semantics. | Endurance grouping. |
| `63:48` | `NGUID` | Namespace Globally Unique Identifier. | Base semantics. | Namespace identity. |
| `71:64` | `EUI64` | IEEE Extended Unique Identifier. | Base semantics. | Namespace identity. |
| `87:72` ... `327:312` | `KVF0` ... `KVF15` | KV Format entries. | Valid entries depend on `NKVF`; valid but unavailable format may set KV Key Max and KV Value Max to `0000h`. | KV format selection. |
| `3839:328` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `4095:3840` | Vendor Specific | Vendor-owned. | Requires vendor documentation. | Vendor-specific behavior. |

### KV Format Entry

| Bytes | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `01:00` | KV Key Max Length | Maximum key length in bytes. | Version 1.0 commands support max 16 bytes. | Key length validation. |
| `02` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `03` bits `1:0` | `RP` | Relative Performance. | `00b` best, `01b` better, `10b` good, `11b` degraded. | Format choice/performance. |
| `07:04` | KV Value Max Length | Maximum value length in bytes. | Defines maximum KV value size. | Store/Retrieve sizing. |
| `11:08` | Max Num Keys | Maximum number of keys. | `0h` means no maximum indicated. | Capacity/key-count tests. |
| `15:12` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |

## Namespace Management Hook

Source: KV section 5.1 and Figure 38.

Namespace Management operates as defined in Base Spec 2.0. For create operation with CSI `01h`, the host software specified fields are defined by KV Figure 38. Reserved fields should be cleared. After successful create, the namespace is formatted with the specified attributes.

Use `admin-commands-2.0\0dh-namespace-management\payload-reference.md` for the byte-exact KV create buffer. High-value fields are `NSZE`, `NMIC`, `ANAGRPID`, `NVMSETID`, and `ENDGID`; bytes `511:104` are reserved for KV create.

## Boundary Notes

- Base owns command-set selection, namespace creation command shell, and common Admin command behavior.
- KV owns key/value semantics, KV command fields, KV status values, KV Identify Namespace structure, and KV Namespace Management create fields.
- Expanded per-command folders split Delete, List, Retrieve, Exist, and Store because their CDW usage and command-specific statuses differ.
