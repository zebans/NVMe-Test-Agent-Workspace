# NVMe-MI Message Header Reference

Status: `FIELD-COMPLETE + BOUNDARY-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 sections 3.1 and 3.1.1, Figures 17-18, plus section 4.1 message taxonomy and request/response rules.

This file owns the common four-byte NVMe-MI Message Header. Command-specific bytes begin after this header and remain in the applicable native MI, Admin-through-MI, or PCIe-through-MI reference.

## Four-Byte Header

| Byte | Bits | Field | Meaning | Out-of-band PCIe Command request value |
|---:|---:|---|---|---|
| `00` | `7` | `IC` | MCTP Integrity Check bit. All OOB NVMe-MI messages use a 32-bit CRC and set this bit to `1b`; in-band messages clear it to `0b`. | `1b` |
| `00` | `6:0` | `MT` | MCTP Message Type. Every NVMe-MI message uses `04h`. | `04h` |
| `01` | `7` | `ROR` | Request or Response. `0b` is Request; `1b` is Response. | `0b` |
| `01` | `6:3` | `NMIMT` | Selects the NVMe-MI message/command family. | `4h`, PCIe Command |
| `01` | `2:1` | Reserved | Reserved. | `00b` |
| `01` | `0` | `CSI` | Command Slot Identifier for OOB messages. Selects Command Slot 0 or 1 and is copied into the associated response. Reserved in-band. | `0b` or `1b` |
| `02` | `7:2` | Reserved | Reserved. | `000000b` |
| `02` | `1` | `CIAP` | Command Initiated Auto Pause. If supported and set, pause the Management Endpoint when the command enters Process state. OOB Command Messages only. | Normally `0b`; use `1b` only when supported and intended. |
| `02` | `0` | `MEB` | Management Endpoint Buffer selection. `0b` means Message Data is inline; `1b` redirects Message Data to the MEB. | Use `1b` only if this exact command is listed in the MEB Supported Command List. |
| `03` | `7:0` | Reserved | Reserved. | `00h` |

## NMIMT Command Selector

`NMIMT` selects the body format; it is the command-family selector, not the individual command opcode.

| `NMIMT` | Message/body type | Main owner |
|---:|---|---|
| `0h` | Control Primitive | MI section 4.2.1 |
| `1h` | Native NVMe-MI Command | MI section 5 |
| `2h` | NVMe Admin Command through MI | MI section 6 / `admin-through-mi\` |
| `3h` | Reserved | n/a |
| `4h` | PCIe Command through MI | MI section 7 / `pcie-through-mi\` |
| `5h`-`Fh` | Reserved | n/a |

After `NMIMT` selects a command family, the command body's byte `04 OPC` selects the individual operation. For PCIe Commands, use Figure 128 and `pcie-through-mi\MI_PCIE_THROUGH_COMMAND_TABLE.md`.

## Request Type And Correlation Identity

| Requested concept | Actual NVMe-MI / MCTP field | Rule |
|---|---|---|
| Request type | `ROR=0b` plus `NMIMT` | `ROR` identifies Request versus Response; `NMIMT` identifies Control, native MI, Admin, or PCIe body format. |
| Command selector | `NMIMT` | Selects the command family. |
| Operation code | `OPC` at command-body byte `04` | Selects the command within the chosen family. |
| Command slot | `CSI` | Selects OOB Command Slot 0 or 1; it is not an operation selector. |
| MI Message ID | No such field exists in the four-byte NVMe-MI header. | Do not invent a Message ID field. |
| Transport request/response correlation | MCTP Source EID + `TO` + Message Tag | Owned by MCTP Base; read `..\mctp-base-1.3.1\MCTP_COMMON_HEADER_REFERENCE.md`. |
| MCTP Control request correlation | Instance ID | Applies to MCTP Control messages, not as a generic NVMe-MI PCIe Command field. |

`CSI` and MCTP Message Tag solve different problems: `CSI` identifies the Management Endpoint command-servicing slot, while Message Tag correlates transport messages.

## Concrete OOB PCIe Header Values

For a PCIe Command request carried out-of-band with inline Message Data and no auto-pause:

| Byte | Slot 0 | Slot 1 | Derivation |
|---:|---:|---:|---|
| `00` | `84h` | `84h` | `IC=1b`, `MT=04h` |
| `01` | `20h` | `21h` | `ROR=0b`, `NMIMT=4h`, reserved `00b`, `CSI=0b/1b` |
| `02` | `00h` | `00h` | `CIAP=0b`, `MEB=0b` |
| `03` | `00h` | `00h` | Reserved |

The corresponding response uses `ROR=1b`, retains `NMIMT=4h`, and identifies the associated request slot with the same `CSI`; byte `01` is therefore `A0h` for Slot 0 or `A1h` for Slot 1. Response-reserved fields are cleared.

## Message Integrity Check

When `IC=1b`, the message ends with a four-byte MIC containing CRC-32C (Castagnoli):

| Parameter | Value |
|---|---:|
| Width | `32` |
| Polynomial | `1EDC6F41h` |
| Initial value | `FFFFFFFFh` |
| Reflect input / output | `True` / `True` |
| XOR output | `FFFFFFFFh` |
| Check value | `E3069283h` |

The MIC is computed across the NVMe-MI Message Body as defined by MI section 3.1.1.1. MCTP packetization, EIDs, `SOM/EOM`, packet sequence, `TO`, and Message Tag remain outside this four-byte header.

