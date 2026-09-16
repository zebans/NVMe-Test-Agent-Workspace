# MCTP Base 1.3.1 Index

Status: `SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED`

Primary source:

```text
..\NVMe Base Spec\2.0\MCTP\MCTP-Base-Specification.md
```

## Source Identity

| Item | Value |
|---|---|
| Specification | Management Component Transport Protocol Base Specification |
| Document identifier | `DSP0236` |
| Version | `1.3.1` |
| Local source | `MCTP-Base-Specification.md` |

## High-Value Source Map

| Source area | Topic | Use when you need |
|---|---|---|
| Section 8 | MCTP base protocol | Packet/message fields, transmission unit size, message assembly, EID assignment, EID reassignment. |
| Section 9 | Routing and bridging | EID resolution, routing tables, bridge behavior, cross-bus routing. |
| Section 11 | MCTP Control Protocol common fields | Message type `00h`, control command code, instance ID, request/response bits, completion code. |
| Section 12 | MCTP Control command specifications | Set/Get Endpoint ID, Get UUID, version support, message type support, routing, discovery, transport-specific commands. |
| Table 1 | MCTP base protocol common fields | `Hdr Version`, Destination EID, Source EID, `SOM`, `EOM`, packet sequence, `TO`, message tag, message body. |
| Table 2 | Special Endpoint IDs | Null and broadcast EID behavior. |
| Table 3 | MCTP Message Types | Message Type routing. |
| Table 10 | MCTP control message fields | Control command common format. |
| Table 11 | `TO`, `Rq`, and `D` bit usage | Request/response/datagram tag behavior. |
| Table 12 | MCTP control command numbers | Control command opcode index. |
| Table 13 | MCTP control completion codes | Control response status surface. |
| Tables 14-39 | Individual Control commands | Byte-level request/response fields when needed. |

## MCTP Control Command Index

| Command | Purpose |
|---|---|
| Set Endpoint ID | Assigns or changes an endpoint EID. |
| Get Endpoint ID | Returns present EID and endpoint type/status information. |
| Get Endpoint UUID | Returns endpoint UUID for identity correlation. |
| Get MCTP Version Support | Reports supported MCTP control/message type versions. |
| Get Message Type Support | Reports supported MCTP message types. |
| Get Vendor Defined Message Support | Reports vendor-defined messaging support. |
| Resolve Endpoint ID | Resolves EID to medium-specific physical address. |
| Allocate Endpoint IDs | Allocates EID pools to bridges/endpoints. |
| Routing Information Update | Updates bridge routing information. |
| Get Routing Table Entries | Returns routing table entries. |
| Prepare for Endpoint Discovery | Prepares endpoints for discovery on supported media. |
| Endpoint Discovery | Discovers endpoints that need EID assignment. |
| Discovery Notify | Endpoint informs bus owner that discovery/EID work is needed. |
| Transport Specific | Dispatches additional transport-binding-specific control functions. |

## Read Next

| Question | Read |
|---|---|
| EID, message tag, SOM/EOM, packet sequence, message type | `MCTP_BASE_BEHAVIOR_REFERENCE.md` |
| Common MCTP packet/message header fields | `MCTP_COMMON_HEADER_REFERENCE.md` |
| Set/Get Endpoint ID, version support, message type support, endpoint discovery, Discovery Notify | `MCTP_CONTROL_COMMAND_REFERENCE.md` |
| NVMe-MI over MCTP layering | `MCTP_TO_NVME_MI_BOUNDARY.md` |
| SMBus/I2C byte framing, PEC, slave address, ARP, NACK/retry | `..\mctp-smbus-i2c-1.1.0\README.md` |
| PCIe VDM encapsulation, VDM fields, PCIe discovery/routing | `..\mctp-pcie-vdm-1.0.1\README.md` |
| Less common exact Control command byte fields | Original source Section 12 / Tables 14-39 |
