# MI Command Reference

Status: `COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 5, Figure 57, Figure 58, and Figure 59.

This file is the command-control reference for the Management Interface Command Set. Use it before opening the full MI source when a test needs MI opcode, command direction, support requirements, fields, payload rules, or high-value error conditions.

## Opcode Table

| Opcode | Command | Source section | OOB support | In-band mapping | Data direction |
|---|---|---|---|---|---|
| `00h` | Read NVMe-MI Data Structure | 5.7 | Storage Device: Mandatory; Enclosure: Mandatory | NVMe-MI Receive | Response Data |
| `01h` | NVM Subsystem Health Status Poll | 5.6 | Storage Device: Mandatory; Enclosure: Optional | NVMe-MI Receive | Response Data |
| `02h` | Controller Health Status Poll | 5.3 | Storage Device: Mandatory; Enclosure: Optional | NVMe-MI Receive | Response Data |
| `03h` | Configuration Set | 5.2 | Storage Device: Mandatory; Enclosure: Mandatory | NVMe-MI Send | No Request Data |
| `04h` | Configuration Get | 5.1 | Storage Device: Mandatory; Enclosure: Mandatory | NVMe-MI Receive | Response Data through `NMRESP` or no Response Data |
| `05h` | VPD Read | 5.12 | Storage Device: Mandatory; Enclosure: Optional | NVMe-MI Receive | Response Data |
| `06h` | VPD Write | 5.13 | Storage Device: Optional; Enclosure: Optional | NVMe-MI Send | Request Data |
| `07h` | Reset | 5.8 | Storage Device: Optional; Enclosure: Optional | NVMe-MI Send | No data |
| `08h` | SES Receive | 5.9 | Storage Device: Prohibited; Enclosure: Mandatory | NVMe-MI Receive for enclosure; prohibited for storage device | Response Data |
| `09h` | SES Send | 5.10 | Storage Device: Prohibited; Enclosure: Mandatory | NVMe-MI Send for enclosure; prohibited for storage device | Request Data |
| `0Ah` | Management Endpoint Buffer Read | 5.4 | Storage Device: Optional; Enclosure: Mandatory | Prohibited | Response Data |
| `0Bh` | Management Endpoint Buffer Write | 5.5 | Storage Device: Optional; Enclosure: Mandatory | Prohibited | Request Data |
| `0Ch` | Shutdown | 5.11 | Storage Device: Optional; Enclosure: Optional | NVMe-MI Send | No data |
| `0Dh`-`BFh` | Reserved | Figure 57 | Prohibited | Prohibited | n/a |
| `C0h`-`FFh` | Vendor specific | Figure 57 | Optional | Optional | Vendor-defined |

OOB support comes from Figure 58. In-band mapping comes from Figure 59. In-band support differs by device type; always verify storage-device vs enclosure support before writing a test.

## Common Request And Response Shape

| Field | Source | Rule |
|---|---|---|
| `OPC` | Figure 56 | Byte 04 of the NVMe-MI Command Request Message selects the MI command. |
| `NMD0` | Figure 56 | Bytes 11:08, command-specific dword 0. |
| `NMD1` | Figure 56 | Bytes 15:12, command-specific dword 1. |
| `REQD` | Figure 56 | Optional Request Data. If its size does not match the command's data-length rule, return `06h Invalid Command Input Data Size`. |
| `STATUS` | Figure 61 | Byte 04 of the Command Response Message. Values are in `MI_STATUS_AND_ERROR_REFERENCE.md`. |
| `NMRESP` | Figure 61 | Bytes 07:05, command-specific response. |
| `RESPD` | Figure 61 | Optional Response Data. |

## Command Details

| Command | Key fields | Payload / response | Required checks |
|---|---|---|---|
| Configuration Get | `NMD0[7:0]` Configuration Identifier; identifier-specific bits in `NMD0[31:8]`; `NMD1` identifier-specific | SMBus/I2C Frequency and MCTP Transmission Unit Size return values in `NMRESP`; Health Status Change returns success with reserved `NMRESP` and no Response Data | Reserved Configuration Identifier causes `Invalid Parameter`; Health Status Change should not be used with Configuration Get but still completes successfully. |
| Configuration Set | `NMD0[7:0]` Configuration Identifier; identifier-specific bits in `NMD0[31:8]`; `NMD1` identifier-specific | No Request Data; `NMRESP` identifier-specific | Reserved Configuration Identifier causes `Invalid Parameter`; unsupported SMBus/I2C frequency or invalid port returns `Invalid Parameter`; changing MCTP Transmission Unit Size while commands are outstanding is undefined. |
| Controller Health Status Poll | `NMD0` has `ALL`, controller-type include bits, `MAXRENT`, `SCTLID`; `NMD1` has `CCF` and health-change selectors | `NMRESP.RENT` reports number of Controller Health Data Structures; Response Data contains CHDS entries | `MAXRENT` is zero-based; specifying 256 entries is invalid. OOB and in-band mechanisms keep independent health data and changed flags. |
| Management Endpoint Buffer Read | `NMD0.DOFST`; `NMD1.DLEN` | Returns bytes from Management Endpoint Buffer; reserved `NMRESP` | `DOFST >= buffer size` invalid; `DOFST + DLEN` beyond buffer invalid; `DLEN` beyond max Response Data invalid; zero-length read succeeds; sanitized-zeroed buffer returns status `22h`. |
| Management Endpoint Buffer Write | `NMD0.DOFST`; `NMD1.DLEN` | Request Data writes bytes into Management Endpoint Buffer; no Response Data; reserved `NMRESP` | Same offset/range checks as read; `DLEN` beyond max Response Data invalid per source wording; zero-length write succeeds and transfers no data. |
| NVM Subsystem Health Status Poll | `NMD1` controls clear/report behavior for NVM Subsystem health status | Response Data is NVM Subsystem Health Data Structure | OOB and in-band mechanisms operate independently and maintain independent health structures. |
| Read NVMe-MI Data Structure | `NMD0.DTYP`; `NMD0`/`NMD1` selectors depend on selected data type | Returns selected MI data structure: NVM Subsystem Information, Port Information, Controller Information, optionally supported commands, or Management Endpoint Buffer command support list | Invalid/reserved DTYP or invalid selector causes `Invalid Parameter`; Management Endpoint Buffer command support list depends on non-zero buffer size. |
| Reset | `NMD0` Reset Type | No Success Response for successful NVM Subsystem Reset; other reset behavior follows section 8.3 | Reset type support depends on device features; NVM Subsystem Reset may interfere with host software. |
| SES Receive | `NMD0.PCODE`; `NMD1` length/allocation fields | Returns SES status diagnostic page in Response Data or Management Endpoint Buffer | Invalid page code or invalid field returns `Invalid Parameter`; OOB support requires MEB support and adequate MEB size for maximum SES status diagnostic page. |
| SES Send | `NMD1.PCODE` and data length | Sends SES control diagnostic page from Request Data or Management Endpoint Buffer | Invalid page code or invalid field returns `Invalid Parameter`; `DLEN=0` with no data is valid. |
| Shutdown | `NMD0` Shutdown Type | Initiates Normal or Abrupt NVM Subsystem Shutdown | Mandatory OOB only if NVM Subsystem Shutdown feature is supported. Completion requires controllers to report shutdown status. |
| VPD Read | `NMD0` offset; `NMD1` length | Returns VPD contents in Response Data | Zero-length read succeeds; invalid offset/length returns `Invalid Parameter`. |
| VPD Write | `NMD0` offset; `NMD1` length | Writes Request Data to VPD | Zero-length write succeeds; invalid offset/length returns `Invalid Parameter`; exceeding update limit returns `20h VPD Updates Exceeded`. |
| Vendor Specific | Vendor-defined | Vendor-defined | Vendor documentation is required. |

## Configuration Identifier Map

| Identifier | Name | OOB | In-band | Notes |
|---|---|---|---|---|
| `00h` | Reserved | Prohibited | Prohibited | Invalid for Configuration Get/Set. |
| `01h` | SMBus/I2C Frequency | Mandatory | Prohibited | Get returns current frequency; Set updates selected SMBus/I2C port. |
| `02h` | Health Status Change | Mandatory | Mandatory | Set clears selected Composite Controller Status bits; Get succeeds but should not be used. |
| `03h` | MCTP Transmission Unit Size | Mandatory | Prohibited | Get/Set selected port MCTP transmission unit size. |
| `04h`-`BFh` | Reserved | Prohibited | Prohibited | Invalid. |
| `C0h`-`FFh` | Vendor Specific | Optional | Optional | Vendor-defined. |

## Management Endpoint Buffer Rules

The Management Endpoint Buffer is optional, per Management Endpoint, and not shared across endpoints. If supported, the endpoint shall support Management Endpoint Buffer Read and Write. Commands that use the MEB bit shall be listed in the Management Endpoint Buffer Command Support List returned by Read NVMe-MI Data Structure.

When the MEB bit redirects Request Data or Response Data, data starts at offset zero in the buffer. Buffer contents are cleared to `0h` on Management Endpoint reset. If response data updates the buffer, buffer bytes not updated are cleared to `0h`. Concurrent operations using the buffer are not guaranteed to be atomic. Sanitize may clear buffer contents; later access to that zeroed data returns status `22h`.
