# MI Status And Error Reference

Status: `COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 4.1.2 and Figure 26 through Figure 29.

## Response Message Status Values

| Value | Name | Meaning | Response format |
|---|---|---|---|
| `00h` | Success | Command completed successfully. | Success response, command-specific body. |
| `01h` | More Processing Required | Command is still in progress; a later response contains the result. Shall not be sent more than once per command except retransmission due to Replay Control Primitive. | More Processing Required response. |
| `02h` | Internal Error | Request could not be processed due to vendor-specific internal error. | Generic Error Response. |
| `03h` | Invalid Command Opcode | Opcode is reserved, invalid, or optional but not implemented. | Generic Error Response. |
| `04h` | Invalid Parameter | Defined field has invalid, reserved, or unimplemented value. | Invalid Parameter Error Response with PEL. |
| `05h` | Invalid Command Size | Message Body size differs from expected for a reason other than too much or too little Request Data. | Generic Error Response. |
| `06h` | Invalid Command Input Data Size | Command requires Request Data and contains too much or too little Request Data. | Generic Error Response. |
| `07h` | Access Denied | Request was blocked by vendor-specific protection or Command and Feature Lockdown. | Generic Error Response. |
| `08h`-`1Fh` | Reserved | Reserved. | n/a |
| `20h` | VPD Updates Exceeded | VPD was updated more times than allowed. | Generic Error Response. |
| `21h` | PCIe Inaccessible | PCIe functionality is unavailable. | Generic Error Response. |
| `22h` | Management Endpoint Buffer Cleared Due to Sanitize | Read attempted data in Management Endpoint Buffer that was zeroed due to sanitize. | Generic Error Response. |
| `23h` | Enclosure Services Failure | Enclosure Services Process failed in an unknown manner. | Generic Error Response. |
| `24h` | Enclosure Services Transfer Failure | Communication with Enclosure Services Process failed. | Generic Error Response. |
| `25h` | Enclosure Failure | Unrecoverable enclosure failure detected. | Generic Error Response. |
| `26h` | Enclosure Services Transfer Refused | NVM Subsystem or Enclosure Services Process indicated error or invalid format. | Generic Error Response. |
| `27h` | Unsupported Enclosure Function | SES Send attempted to a simple Subenclosure. | Generic Error Response. |
| `28h` | Enclosure Services Unavailable | Enclosure service encountered an error but may become available again. | Generic Error Response. |
| `29h` | Enclosure Degraded | Noncritical enclosure failure detected. | Generic Error Response. |
| `2Ah` | Sanitize In Progress | Requested command is prohibited during sanitize. | Generic Error Response. |
| `2Bh`-`DFh` | Reserved | Reserved. | n/a |
| `E0h`-`FFh` | Vendor Specific | Vendor-defined status. | Vendor-defined. |

## Error Response Rules

| Rule | Source |
|---|---|
| If multiple errors are present, the Responder may choose which error status to report. | 4.1.2 |
| Generic Error Response is used when no additional information beyond status is provided. | 4.1.2.1 / Figure 27 |
| Invalid Parameter Error Response is used when `STATUS=04h`; it includes PEL to identify the invalid field. | 4.1.2.2 / Figure 28 / Figure 29 |
| Invalid opcodes include reserved opcodes and optional opcodes that are not implemented. | Figure 26 |
| Request Messages with reserved or unimplemented values in defined fields shall complete with Invalid Parameter. | Figure 26 |
| Request Data size mismatch maps to Invalid Command Input Data Size rather than Invalid Command Size. | Figure 26 and Figure 56 |

## Common Command-Specific Error Hooks

| Command area | Error hook |
|---|---|
| Configuration Get/Set | Reserved Configuration Identifier returns `04h Invalid Parameter`; PEL identifies Configuration Identifier. |
| SMBus/I2C Frequency Set | Unsupported frequency or non-SMBus port returns `04h Invalid Parameter`; PEL identifies frequency or Port Identifier. |
| MCTP Transmission Unit Size Set | Unsupported size or invalid Port Identifier returns `04h Invalid Parameter`; changing while requests are outstanding is undefined. |
| Controller Health Status Poll | `MAXRENT` value representing 256 entries is invalid. |
| Management Endpoint Buffer Read/Write | Invalid offset/range/length returns `04h`; sanitized-cleared data returns `22h`. |
| SES Receive/Send | Invalid page code or invalid command field returns `04h`; enclosure-service failures use status `23h`-`29h`. |
| VPD Write | Exceeded write-cycle/update limit returns `20h`. |
| Sanitize interaction | Prohibited commands during sanitize return `2Ah`; Management Endpoint Buffer data cleared by sanitize returns `22h`. |
