# MI Command Set Index

Status: `FRAMEWORK-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 5 and Figure 57.

## Command Families

| Family | Source | Notes |
|---|---|---|
| Management Interface Command Set | Section 5, Figure 57 | Native NVMe-MI management commands. |
| NVM Express Admin Command Set through MI | Section 6, Figures 114-125 | Admin commands through the out-of-band MI mechanism. Detailed support/format/status routing is in `admin-through-mi\README.md`. |
| PCIe Command Set | Section 7, Figures 126-144 | Optional out-of-band PCIe command set. Detailed opcode/format/field/status routing is in `pcie-through-mi\README.md`. |

## Management Interface Command Set

| Opcode | Command | Source section | Key figures | Detailed reference |
|---|---|---|---|---|
| `00h` | Read NVMe-MI Data Structure | 5.7 | Figures 90-101 | `MI_COMMAND_REFERENCE.md` |
| `01h` | NVM Subsystem Health Status Poll | 5.6 | Figures 88-89 | `MI_COMMAND_REFERENCE.md` |
| `02h` | Controller Health Status Poll | 5.3 | Figures 76-81 | `MI_COMMAND_REFERENCE.md` |
| `03h` | Configuration Set | 5.2 | Figures 69-75 | `MI_COMMAND_REFERENCE.md` |
| `04h` | Configuration Get | 5.1 | Figures 62-68 | `MI_COMMAND_REFERENCE.md` |
| `05h` | VPD Read | 5.12 | Figures 108-110 | `MI_COMMAND_REFERENCE.md` |
| `06h` | VPD Write | 5.13 | Figures 111-113 | `MI_COMMAND_REFERENCE.md` |
| `07h` | Reset | 5.8 | Figure 102 | `MI_COMMAND_REFERENCE.md` |
| `08h` | SES Receive | 5.9 | Figures 103-105 | `MI_COMMAND_REFERENCE.md` |
| `09h` | SES Send | 5.10 | Figure 106 | `MI_COMMAND_REFERENCE.md` |
| `0Ah` | Management Endpoint Buffer Read | 5.4 | Figures 82-84 | `MI_COMMAND_REFERENCE.md` |
| `0Bh` | Management Endpoint Buffer Write | 5.5 | Figures 85-87 | `MI_COMMAND_REFERENCE.md` |
| `0Ch` | Shutdown | 5.11 | Figure 107 | `MI_COMMAND_REFERENCE.md` |
| `0Dh`-`BFh` | Reserved | Figure 57 | n/a | `MI_COMMAND_REFERENCE.md` |
| `C0h`-`FFh` | Vendor Specific | Figure 57 | Vendor-defined | Vendor documentation required. |

## Support Tables

| Support context | Source |
|---|---|
| Out-of-band mechanism support | Figure 58 |
| In-band tunneling support | Figure 59 |

## Admin Command Set Through MI

| Need | Read |
|---|---|
| Which Admin commands are Mandatory, Optional, or Prohibited over OOB MI? | `admin-through-mi\MI_ADMIN_THROUGH_COMMAND_TABLE.md` |
| Admin-through-MI request/response bytes and fields | `admin-through-mi\command-format-reference.md` and `admin-through-mi\field-reference.md` |
| Get Log Page, Get/Set Features, sanitize, or Format NVM support overlays | `admin-through-mi\support-overlays-reference.md` |
| MI wrapper status versus tunneled Admin completion status | `admin-through-mi\status-boundary-reference.md` |
| Base Admin command CDW/payload/status semantics | Linked `..\admin-commands-2.0\<opcode-folder>\` from `MI_ADMIN_THROUGH_COMMAND_TABLE.md` |

## PCIe Command Set Through MI

| Need | Read |
|---|---|
| PCIe Configuration, I/O, or Memory command opcode and optional support | `pcie-through-mi\MI_PCIE_THROUGH_COMMAND_TABLE.md` |
| Common PCIe-through-MI request and response bytes | `pcie-through-mi\command-format-reference.md` |
| Shared MI header, request type, command selector, slot, message identity, and MIC | `MI_MESSAGE_HEADER_REFERENCE.md` |
| Complete Section 7 source and Figure 126-144 coverage | `pcie-through-mi\SECTION_7_SOURCE_MAP.md` |
| `LENGTH`, BAR selector, 12-bit/32-bit/64-bit `OFFSET`, and data behavior | `pcie-through-mi\field-reference.md` |
| PEL, range checks, Access Denied, PCIe Inaccessible, and operational restrictions | `pcie-through-mi\status-and-restrictions-reference.md` |
| Selected PCIe register, capability, or BAR meaning | `pcie-through-mi\cross-spec-boundary.md`, then `..\pcie-transport-1.0\` |

## Detailed References

| Need | Read |
|---|---|
| Opcode, command support, fields, payload direction, and command checks | `MI_COMMAND_REFERENCE.md` |
| Response Message Status and common error mapping | `MI_STATUS_AND_ERROR_REFERENCE.md` |
| In-band vs out-of-band ownership | `MI_INBAND_OUTOFBAND_BOUNDARY.md` |
| NVM Express Admin Command Set through MI | `admin-through-mi\README.md` |
| PCIe Command Set through MI | `pcie-through-mi\README.md` |
