# PCIe-Through-MI Command Format Reference

Status: `FIELD-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 7, Figures 126-130.

Shared header source: MI sections 3.1 and 3.1.1, Figures 17-18. Read `..\MI_MESSAGE_HEADER_REFERENCE.md` for the complete bit definitions and MCTP correlation boundary.

## Complete OOB PCIe Command Request Layout

| Bytes | Field / selector | Required value or source | Purpose |
|---:|---|---|---|
| `00` | `IC` + MCTP `MT` | `84h` for OOB NVMe-MI | `IC=1b`; MCTP Message Type is `04h`, NVMe-MI. |
| `01` | `ROR` + `NMIMT` + `CSI` | `20h` for Request/PCIe/Slot 0; `21h` for Slot 1 | `ROR=0b`; `NMIMT=4h` selects PCIe Command; `CSI` selects Command Slot. |
| `02` | `CIAP` + `MEB` | Normally `00h`; capability/use dependent | Auto-pause and Management Endpoint Buffer controls. |
| `03` | Reserved | `00h` | Reserved header byte. |
| `04` | `OPC` | `00h`-`05h` from Figure 128 | Selects Configuration, Memory, or I/O Read/Write operation. |
| `05` | Reserved | `00h` | Reserved command byte. |
| `07:06` | `CTLID` | Target controller identifier | Selects the NVMe Controller whose PCIe address spaces are accessed. |
| `11:08` | `NMD0` | Command-specific | Carries `LENGTH`; I/O/Memory commands also carry BAR selector. |
| `15:12` | `NMD1` | Command-specific | Carries Configuration/I/O offset or low 32 bits of Memory offset. |
| `19:16` | `NMD2` | Command-specific or reserved | Carries high 32 bits of Memory offset; reserved for Configuration/I/O. |
| `N-1:20` | `REQD` | Write commands only | Write data, with length rounded up to a dword. |
| `N+3:N` | `MIC` | CRC-32C | Required for OOB NVMe-MI because `IC=1b`. |

MCTP Destination/Source EID, `SOM/EOM`, packet sequence, `TO`, and Message Tag surround this NVMe-MI message at the MCTP transport layer. They are not bytes in the NVMe-MI PCIe Command layout above.

## Request Message

| Bytes | Field | Meaning | Important rule |
|---:|---|---|---|
| `03:00` | `NMH` | NVMe-MI Message Header. | `NMIMT` is `4h`, PCIe Command. Header details remain in MI section 3.1. |
| `04` | `OPC` | PCIe Command opcode. | Use Figure 128 / `MI_PCIE_THROUGH_COMMAND_TABLE.md`. |
| `05` | Reserved | Reserved request byte. | Reserved fields are cleared and reserved/unimplemented values in defined fields result in `04h Invalid Parameter`. |
| `07:06` | `CTLID` | Controller Identifier of the target NVMe Controller. | An unimplemented Controller ID makes the request not well formed. |
| `11:08` | `NMD0` | PCIe Request Dword 0. | Command-specific; normally carries `LENGTH` and, for I/O/Memory commands, `BAR`. |
| `15:12` | `NMD1` | PCIe Request Dword 1. | Command-specific; carries the 12-bit, 32-bit, or low 32 bits of `OFFSET`. |
| `19:16` | `NMD2` | PCIe Request Dword 2. | Reserved for Configuration and I/O commands; high 32 bits of `OFFSET` for Memory commands. |
| `N-1:20` | `REQD` | Optional Request Data. | Present for Write commands; its size is determined by `LENGTH`, rounded up to a dword. |
| `N+3:N` | `MIC` | Message Integrity Check. | Defined by MI section 3.1. |

## Response Message

| Bytes | Field | Meaning | Important rule |
|---:|---|---|---|
| `03:00` | `NMH` | NVMe-MI Message Header. | The response `NMIMT` remains PCIe Command. |
| `04` | `STATUS` | MI Response Message Status for the PCIe Command. | Use `status-and-restrictions-reference.md` and `..\MI_STATUS_AND_ERROR_REFERENCE.md`. |
| `07:05` | Reserved | Reserved response bytes. | No command-specific completion dwords are defined here. |
| `N-1:08` | `RESPD` | Optional Response Data. | Returned by successful Read commands; size is `LENGTH` rounded up to a dword. |
| `N+3:N` | `MIC` | Message Integrity Check. | Defined by MI section 3.1. |

For the common successful OOB response header, byte `00` is `84h`; byte `01` is `A0h` for Slot 0 or `A1h` for Slot 1 because `ROR=1b`, `NMIMT=4h`, and `CSI` identifies the associated request slot.

This is the PCIe Command response layout used for command completion. When `STATUS` identifies an Error Response or More Processing Required Response, the response body follows the status-specific format in MI section 4.1.2. In particular, `04h Invalid Parameter` returns the PEL structure instead of normal Read Response Data.

## Data Placement

| Command kind | Request Data | Response Data |
|---|---|---|
| Configuration / I/O / Memory Read | None | Read bytes begin at response byte `08`; response length is `LENGTH` rounded up to a dword. |
| Configuration / I/O / Memory Write | Write bytes begin at request byte `20`; request length is `LENGTH` rounded up to a dword. | None on success. |

If a Read `LENGTH` is not a multiple of four, padding bytes in the final response dword are cleared to `0h`. If a Write `LENGTH` is not a multiple of four, padding bytes in Request Data are discarded.
