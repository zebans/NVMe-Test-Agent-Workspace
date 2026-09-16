# MCTP Control Command Reference

Status: `PAYLOAD-COMPLETE`

Source: MCTP Base DSP0236 Version 1.3.1 Tables 10-19 and 28-30.

This file expands the MCTP Control common fields and the high-priority Control commands used for endpoint setup, version discovery, message-type discovery, and endpoint discovery.

## Common Control Message Fields

| Field | Meaning | Important rule |
|---|---|---|
| `IC` | Message Integrity Check bit. | MCTP Control messages set `IC=0b`; no overall MCTP message integrity check field. |
| Message Type | MCTP Control message type. | `00h`. |
| `Rq` | Request bit. | `1b` for Request/Command and Datagram; `0b` for Response. |
| `D` | Datagram bit. | Indicates whether Instance ID tracks request/response or just identifies retransmitted message. |
| Instance ID | Request/response correlation. | Requester uses it to match response with request and distinguish retries. |
| Command Code | MCTP Control command selector. | Request command code is returned in corresponding response. |
| Completion Code | Response status. | Present only in Response messages. |
| Message Data | Command-specific request/response bytes. | Defined by command code. |

Control messages are carried in a single MCTP packet and have packet payload no larger than the baseline transmission unit size of 64 bytes.

## Completion Codes

| Value | Name | Meaning |
|---:|---|---|
| `00h` | `SUCCESS` | Request accepted and completed normally. |
| `01h` | `ERROR` | Generic failure; should not be used when a more specific result applies. |
| `02h` | `ERROR_INVALID_DATA` | Payload contained invalid data or illegal parameter value. |
| `03h` | `ERROR_INVALID_LENGTH` | Message length invalid. |
| `04h` | `ERROR_NOT_READY` | Receiver is transiently not ready. |
| `05h` | `ERROR_UNSUPPORTED_CMD` | Command field is unspecified or not supported by endpoint. |
| `80h`-`FFh` | Command-specific | Reserved for command-specific completion values. |

If completion is not `SUCCESS`, responder normally returns no additional parameter data unless the command says otherwise; requester ignores any extra data.

## Control Command Numbers

| Code | Command | Purpose | Expanded here |
|---:|---|---|---|
| `01h` | Set Endpoint ID | Assigns or changes endpoint EID. | Yes |
| `02h` | Get Endpoint ID | Returns current endpoint EID and endpoint type/status. | Yes |
| `03h` | Get Endpoint UUID | Returns endpoint UUID. | Summary |
| `04h` | Get MCTP Version Support | Returns supported MCTP/message type versions. | Yes |
| `05h` | Get Message Type Support | Returns supported message types. | Yes |
| `0Bh` | Prepare for Endpoint Discovery | Clears discovered flags where supported. | Yes |
| `0Ch` | Endpoint Discovery | Discovers undiscovered endpoints. | Yes |
| `0Dh` | Discovery Notify | Endpoint announces presence to bus owner. | Yes |
| `F0h`-`FFh` | Transport Specific | Transport-binding-specific control commands. | Boundary |

Other MCTP Control commands remain indexed in `MCTP_BASE_INDEX.md` and should be expanded when a task needs exact bytes.

## Set Endpoint ID - Command `01h`

Purpose: assign an EID to an endpoint and communicate bus owner address/EID context.

| Request byte | Field | Meaning | Important rule |
|---:|---|---|---|
| `1[7:2]` | Reserved | Reserved. | Write zero; do not infer semantics. |
| `1[1:0]` | Operation | Selects Set/Force/Reset/Discovered operation. | See operation table below. |
| `2` | Endpoint ID | EID value to assign. | `00h` and `FFh` are illegal assignment values; `ERROR_INVALID_DATA` recommended. |

| Operation | Meaning | Rule |
|---:|---|---|
| `00b` | Set EID | Conditional assignment based on bus ownership/first assignment rules. |
| `01b` | Force EID | Force assignment regardless of prior bus owner; updates tracked origin bus. |
| `10b` | Reset EID | Optional; only for endpoints supporting static EIDs. Byte 2 ignored. Unsupported returns `ERROR_INVALID_DATA`. |
| `11b` | Set Discovered Flag | Sets Discovered flag only; does not change EID. Byte 2 ignored. Invalid if binding does not support Discovered flag. |

| Response byte | Field | Meaning |
|---:|---|---|
| `1` | Completion Code | MCTP Control completion. |
| `2[7:6]` | Reserved | Reserved. |
| `2[5:4]` | EID assignment status | `00b` accepted; `01b` rejected because another bus owner assigned and assignment was not forced; `10b/11b` reserved. |
| `2[3:2]` | Reserved | Reserved. |
| `2[1:0]` | Endpoint ID allocation status | `00b` no EID pool; `01b` requires EID pool allocation; `10b` uses EID pool and already received allocation; `11b` reserved. |
| `3` | EID Setting | Accepted EID or present EID setting. |
| `4` | EID Pool Size | Dynamic EID pool size for bridge; `00h` means no dynamic EID pool. |

## Get Endpoint ID - Command `02h`

Purpose: return endpoint EID and endpoint type/status information.

| Request byte | Field | Meaning |
|---:|---|---|
| none | none | No request data. |

| Response byte | Field | Meaning | Important rule |
|---:|---|---|---|
| `1` | Completion Code | MCTP Control completion. |  |
| `2` | Endpoint ID | Present endpoint EID. | `00h` means EID not yet assigned. |
| `3[7:6]` | Reserved | Reserved. |  |
| `3[5:4]` | Endpoint Type | `00b` simple endpoint; `01b` bus owner/bridge; `10b/11b` reserved. |  |
| `3[3:2]` | Reserved | Reserved. |  |
| `3[1:0]` | Endpoint ID Type | Dynamic/static status. | See table below. |
| `4` | Medium-Specific Information | Static medium-specific capability/config info. | `00h` unless transport binding defines otherwise. |

| Endpoint ID Type | Meaning |
|---:|---|
| `00b` | Dynamic EID only. |
| `01b` | Static EID supported; present EID may or may not match static value. |
| `10b` | Static EID supported and present EID matches static EID. Optional paired status. |
| `11b` | Static EID supported and present EID does not match static EID. Optional paired status. |

## Get Endpoint UUID - Command `03h`

| Request byte | Field | Meaning |
|---:|---|---|
| none | none | No request data. |

| Response byte | Field | Meaning |
|---:|---|---|
| `1` | Completion Code | MCTP Control completion. |
| `2:17` | UUID bytes 1:16 | Endpoint UUID in RFC4122 byte order, MSB first within UUID fields. |

UUID should not change over device lifetime.

## Get MCTP Version Support - Command `04h`

Purpose: retrieve MCTP Base, MCTP Control, or message-type-specific version support.

| Request byte | Field | Meaning |
|---:|---|---|
| `1` | Message Type Number | Selects version set to return. |

| Message Type Number | Meaning |
|---:|---|
| `FFh` | Return MCTP Base specification version information. |
| `00h` | Return MCTP Control Protocol version information. |
| `7Eh`, `7Fh` | Vendor-defined behavior; support is vendor-specific. |
| Other | Return version information for the given message type. |

| Response byte | Field | Meaning |
|---:|---|---|
| `1` | Completion Code | `80h` command-specific completion means message type number not supported. |
| `2` | Version Number Entry Count | One-based count of 32-bit version entries. |
| `3:6` | Version Number Entry 1 | 32-bit version entry. |
| `7:X` | Additional version entries | Additional 32-bit entries, if any. |

Version entry format:

| Bits | Field | Meaning |
|---:|---|---|
| `31:24` | Major | BCD-encoded major version. |
| `23:16` | Minor | BCD-encoded minor version. |
| `15:8` | Update | BCD-encoded update version; `FFh` means ignored. |
| `7:0` | Alpha | ASCII alpha extension; `00h` means absent. |

Version examples from source:

| Version | Encoded value |
|---|---:|
| `1.1.0` | `F1F1F000h` |
| `3.1` | `F3F1FF00h` |
| `1.0a` | `F1F0FF61h` |
| `3.7.10a` | `F3F71061h` |
| `10.11.7` | `1011F700h` |

For DSP0236 Version 1.3.1, Base version reporting includes backward-compatible entries through 1.3.1, including `F1F3F100h` for 1.3.1.

## Get Message Type Support - Command `05h`

Purpose: discover message types supported by an endpoint.

| Request byte | Field | Meaning |
|---:|---|---|
| none | none | No request data. |

| Response byte | Field | Meaning |
|---:|---|---|
| `1` | Completion Code | MCTP Control completion. |
| `2` | MCTP Message Type Count | One-based count of message types in addition to MCTP Control. |
| `3:N` | Message Type list | One byte per supported message type. |

Response may depend on which bus the request was received over.

## Prepare for Endpoint Discovery - Command `0Bh`

Purpose: broadcast request that causes endpoints on a supported medium to set Discovered flag to undiscovered.

| Request byte | Field | Meaning |
|---:|---|---|
| none | none | No request data. |

| Response byte | Field | Meaning |
|---:|---|---|
| `1` | Completion Code | MCTP Control completion. |

Important rules:

- Typically sent by bus owner with Broadcast EID as destination.
- Does not clear existing EID assignments.
- Only bindings that use this discovery approach support it.
- If binding does not use this discovery approach, endpoint returns `ERROR_UNSUPPORTED_CMD`.

## Endpoint Discovery - Command `0Ch`

Purpose: discover endpoints whose Discovered flag is undiscovered.

| Request byte | Field | Meaning |
|---:|---|---|
| none | none | No request data. |

| Response byte | Field | Meaning |
|---:|---|---|
| `1` | Completion Code | MCTP Control completion. |

Important rules:

- Usually sent as Broadcast Request by bus owner using Broadcast EID.
- For testing, endpoints accept and handle non-broadcast Request.
- Depending on transport binding, request may be sent as datagram.
- Endpoints whose Discovered flag is discovered do not respond.

## Discovery Notify - Command `0Dh`

Purpose: endpoint announces to bus owner that it is online and may need EID assignment/update.

| Request byte | Field | Meaning |
|---:|---|---|
| none | none | No request data. |

| Response byte | Field | Meaning |
|---:|---|---|
| `1` | Completion Code | MCTP Control completion. |

Important rules:

- Used depending on physical transport binding.
- Sent from endpoint to bus owner for the bus the endpoint is on.
- SMBus/I2C binding does not use Discovery Notify for endpoint announcement because SMBus mechanisms already exist.

## Transport Specific - Commands `F0h`-`FFh`

This range is reserved for transport binding specifications. Transport-specific commands:

- are defined by the selected physical transport binding;
- are intended for setup/configuration on a given medium;
- shall only be addressed to endpoints on the same medium;
- may be blocked by a bridge from being forwarded to a different medium.

## Boundary

- This file is MCTP Control only.
- NVMe-MI command semantics belong to `..\mi-1.2`.
- PCIe VDM and SMBus/I2C physical framing belong to their transport binding folders.
