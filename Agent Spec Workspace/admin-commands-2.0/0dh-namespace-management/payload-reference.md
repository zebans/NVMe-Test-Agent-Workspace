# Namespace Management Payload Reference

## Create Input Payload

Namespace Create uses a 4096-byte host-to-controller data buffer.

| Bytes | Region | Meaning |
|---:|---|---|
| `383:00` | Host-set Identify Namespace fields | Namespace attributes supplied by host software. |
| `511:384` | I/O Command Set specific | Namespace create fields owned by the selected command set. |
| `1023:512` | Reserved | Reserved and cleared. |
| `4095:1024` | Vendor specific | Vendor-specific input. |

If PRPs are used, the data buffer shall not be a PRP List and may not cross more than one page boundary.

## Delete Payload

No data structure is transferred for Delete.

## Completion Payload

| Operation | CQE Dword 0 |
|---|---|
| Create | Contains the created `NSID`. |
| Delete | No command-specific completion payload captured here. |

## Important Boundary

The bytes used for I/O Command Set-specific namespace creation are not defined by Base. Use the selected command-set rows below before reopening the original source.

## Base Create Command Fields

| Location | Field | Meaning | Important rule | Affects |
|---|---|---|---|---|
| `DPTR` | Data Pointer | Start of the 4096-byte create data buffer. | If using PRPs, this shall not point to a PRP List and the buffer may not cross more than one page boundary. | Buffer placement validation. |
| `CDW10 bits 03:00` | `SEL` | Namespace Management operation. | `0h` Create; `1h` Delete; `2h`-`Fh` reserved. | Operation selection. |
| `CDW11 bits 31:24` | `CSI` | Command Set Identifier for Create. | `0h` NVM; `1h` KV; `2h` ZNS. Reserved for non-Create operations. | Command-set-specific bytes `511:384`. |

## NVM Command Set Create Fields (`CSI=00h`)

Source: NVM Command Set Figure 105.

| Bytes | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `07:00` | `NSZE` | Namespace Size. | Host-specified. | Namespace capacity. |
| `15:08` | `NCAP` | Namespace Capacity. | Host-specified; interacts with Namespace Granularity. | Thin provisioning/capacity. |
| `25:16` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| `26` | `FLBAS` | Formatted LBA Size. | Selects an LBA format from Identify Namespace. | Format and LBA size. |
| `28:27` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| `29` | `DPS` | End-to-end Data Protection Type Settings. | Host-specified protection information setting. | Protection information. |
| `30` | `NMIC` | Namespace Multi-path I/O and Sharing Capabilities. | Host-specified. | Sharing / multipath behavior. |
| `91:31` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| `95:92` | `ANAGRPID` | ANA Group Identifier. | `0h` lets controller determine if supported; ignored if associated feature not supported. | ANA placement. |
| `99:96` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| `101:100` | `NVMSETID` | NVM Set Identifier. | `0h` lets controller determine if supported; ignored if not supported. | NVM Set placement. |
| `103:102` | `ENDGID` | Endurance Group Identifier. | `0h` lets controller determine if supported; ignored if not supported. | Endurance group placement. |
| `383:104` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| `391:384` | `LBSTM` | Logical Block Storage Tag Mask. | NVM command-set-specific create field. | Protection information / storage tag tests. |
| `511:392` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |

## Key Value Command Set Create Fields (`CSI=01h`)

Source: KV Command Set Figure 38.

| Bytes | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `07:00` | `NSZE` | Namespace Size in bytes for KV keys and values. | Host-specified. | KV namespace capacity. |
| `29:08` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| `30` | `NMIC` | Namespace Multi-path I/O and Sharing Capabilities. | Host-specified. | Sharing / multipath behavior. |
| `91:31` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| `95:92` | `ANAGRPID` | ANA Group Identifier. | `0h` lets controller determine if supported; ignored if not supported. | ANA placement. |
| `99:96` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| `101:100` | `NVMSETID` | NVM Set Identifier. | `0h` lets controller determine if supported; ignored if not supported. | NVM Set placement. |
| `103:102` | `ENDGID` | Endurance Group Identifier. | `0h` lets controller determine if supported; ignored if not supported. | Endurance group placement. |
| `511:104` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |

## Zoned Namespace Command Set Create Fields (`CSI=02h`)

ZNS section 4.1.5 states that Namespace Management operates as defined in the NVM Command Set Specification. For ZNS namespace creation, use the NVM Command Set create fields above, and interpret LBA format selection together with the ZNS LBA Format Extension table in `ZNS_COMMAND_SET_INDEX.md`.
