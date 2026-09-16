# MCTP Common Header Reference

Status: `PAYLOAD-COMPLETE`

Source: MCTP Base DSP0236 Version 1.3.1 Table 1.

This file expands the common MCTP packet/message fields that appear before message-type-specific payload interpretation.

## MCTP Packet / Message Layout

| Field | Size | Meaning | Important rule | Affects |
|---|---:|---|---|---|
| Medium-specific header | Transport-defined | Physical addressing and framing. | Defined by transport binding, such as SMBus/I2C or PCIe VDM. | Where the MCTP packet is carried. |
| Medium-specific trailer | Transport-defined | Extra per-packet integrity or trailer fields. | Defined by transport binding. | CRC/checksum/PEC-like transport validation. |
| MCTP transport header | 32 bits | Common packet header with version, EIDs, assembly flags, sequence, and tag. | Present in every MCTP packet. Field placement may vary by transport binding. | Packet routing and message reassembly. |
| Message body | Variable | Payload of the MCTP message. | May span multiple MCTP packets. | Carries MCTP Control, NVMe-MI, vendor-defined, or other message types. |
| Message integrity check | Message-type-specific | Optional integrity check over message body. | If present, carried in the last bytes of the message body. | End-to-end message body integrity. |

## MCTP Transport Header Fields

| Field | Size | Meaning | Important rule | Affects |
|---|---:|---|---|---|
| `RSVD` | 4 bits | Reserved for MCTP Base. | Write as zero unless spec says otherwise; ignore on receive where required by implementation rules. | Future expansion. |
| `Hdr Version` | 4 bits | Header version / transport binding format identifier. | Value is defined by the transport binding. | Binding-specific packet parsing. |
| Destination EID | 8 bits | Logical endpoint to receive packet. | `00h` and `FFh` have special meanings. | Routing target. |
| Source EID | 8 bits | Logical endpoint that originated packet. | `00h` is Null Source EID. | Message identity and response routing. |
| `SOM` | 1 bit | Start of Message. | `1b` when this packet is the first packet of a message. | Message reassembly. |
| `EOM` | 1 bit | End of Message. | `1b` when this packet is the last packet of a message. | Message reassembly. |
| Packet Sequence | 2 bits | Packet sequence number. | For multi-packet messages, increments modulo 4 after the `SOM` packet. | Missing-packet detection and reassembly. |
| `TO` | 1 bit | Tag Owner. | `1b` means source originated the message tag. | Request/response tag ownership. |
| Message Tag | 3 bits | Transport-level message correlation tag. | Combined with Source EID and `TO` to identify a unique MCTP message. | Concurrent/interleaved message tracking. |

## First Message Body Byte

The first byte of the MCTP message body in the first packet contains:

| Bits | Field | Meaning | Important rule |
|---:|---|---|---|
| `7` | `IC` | MCTP message integrity check bit. | `0b` means no MCTP message integrity check; `1b` means present. |
| `6:0` | Message Type | Identifies the protocol carried by the message body. | MCTP Control is `00h`; other message types are owned by their specs or vendor definitions. |

## Message-Type-Specific Body

| Field | Size | Meaning | Owner |
|---|---:|---|---|
| Message header | 0 to M bytes | Additional header for the selected message type. | Message type specification. |
| Message data | 0 to N bytes | Data associated with the selected message type. | Message type specification. |
| MCTP packet payload | Transport-limited | Portion of message body carried in one packet. | MCTP Base + transport binding transmission unit rules. |

## Special EIDs

| EID | Meaning | Rule |
|---:|---|---|
| `00h` | Null EID | Used for null destination/source cases before assignment or physical-address-only flows. Bridging restrictions apply. |
| `01h`-`07h` | Reserved | Do not infer semantics. |
| `FFh` | Broadcast EID | Bus-local broadcast; bridge forwarding restrictions apply. |

## Request / Response Tag Pattern

| Message class | Destination EID | `TO` | `Rq` | `D` | Meaning |
|---|---:|---:|---:|---:|---|
| Command / Request | Target EID | `1b` | `1b` | `0b` | Response expected and tracked by Instance ID. |
| Response | Target EID | `0b` | `0b` | `0b` | Response to a request. |
| Broadcast Request | Broadcast EID | `1b` | `1b` | `0b` | Responses expected and tracked by Instance ID. |
| Datagram | Target EID | `1b` | `1b` | `1b` | Unacknowledged; responses are not expected. |
| Broadcast Datagram | Broadcast EID | `1b` | `1b` | `1b` | Broadcast unacknowledged control command. |

MCTP Control messages with unexpected or incorrect flag bit values are silently discarded by the receiver.

## Boundary

- Transport-specific byte placement belongs to the binding layer.
- NVMe-MI command payload semantics belong to `..\mi-1.2`.
- Vendor-defined message body semantics require vendor documentation.
