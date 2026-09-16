# MCTP Base Behavior Reference

Status: `BEHAVIOR-INDEXED`

This file captures high-value MCTP Base behavior for token-efficient lookup. Use the source tables when byte-exact control command payloads are required.

## Layer Position

```text
NVMe-MI message body
  inside MCTP message
    split into one or more MCTP packets
      carried by a transport binding such as SMBus/I2C or PCIe VDM
```

## Core Concepts

| Concept | Meaning | Why it matters |
|---|---|---|
| Endpoint | Terminus for MCTP communication. | A physical device may expose one or more MCTP endpoints. |
| `EID` | Logical Endpoint ID. | Routes MCTP packets independently from medium-specific addresses. |
| Bus owner | Entity that manages EID assignment and often physical address resolution on a bus. | Required for dynamic EID assignment and routing. |
| Bridge | MCTP device that forwards packets between buses or ports. | Owns routing table behavior and EID pool handling. |
| Message Type | Identifies the protocol carried by MCTP message body. | MCTP Control is one type; NVMe-MI uses its own carried message semantics. |

## Packet And Message Fields

| Field | Meaning | Important rule |
|---|---|---|
| `Hdr Version` | MCTP transport header format/version. | Transport binding also defines medium-specific use. |
| Destination EID | Logical target endpoint. | `00h` is Null Destination EID; `FFh` is broadcast on a given bus. |
| Source EID | Logical origin endpoint. | `00h` is Null Source EID. |
| `SOM` | Start of Message. | Set on first packet of a multi-packet or single-packet message. |
| `EOM` | End of Message. | Set on last packet of a multi-packet or single-packet message. |
| Packet Sequence | Packet order within a message. | Increments modulo 4 for multi-packet messages. |
| `TO` | Tag Owner. | Helps distinguish request/response tag ownership. |
| Message Tag | Message correlation tag. | Combined with Source EID and `TO` to track a message. |
| Message Type | Protocol carried in the message body. | MCTP Control uses `00h`; other specs own other message types. |
| Message Integrity Check | Optional message-level integrity field. | If present, carried in the last packet. |

## Special EIDs

| EID | Meaning | Boundary |
|---:|---|---|
| `00h` | Null EID. | Used before assignment or for physical-addressed control flows; bridging restrictions apply. |
| `01h`-`07h` | Reserved. | Do not infer endpoint meaning. |
| `FFh` | Broadcast EID. | Broadcast is bus-local; bridge forwarding restrictions apply. |

## Message Assembly

| Rule | Meaning |
|---|---|
| Same message identity | Packets in one message share Source EID, `TO`, and Message Tag. |
| First and last packet | `SOM` and `EOM` identify message boundaries. |
| Fragmented messages | Packet sequence supports reassembly. |
| Transmission unit | All packets in a message use compatible transmission unit sizing; last packet may be shorter. |

## Control Protocol

| Field | Meaning |
|---|---|
| Message Type | `00h` for MCTP Control. |
| Instance ID | Correlates request and response. |
| Command Code | Selects the MCTP Control command. |
| Completion Code | Present in responses; reports control command completion status. |
| `Rq` bit | Request vs response indication for control messages. |

## Routing And Discovery

| Topic | High-value behavior |
|---|---|
| EID assignment | Bus owner assigns dynamic EIDs using Set Endpoint ID. |
| Static EIDs | Allowed by spec constraints, but still interact with bus owner behavior. |
| EID reassignment | Reassigned EIDs require care because a logical EID may later refer to another endpoint. |
| EID pools | Bridges may receive EID pools for downstream assignment. |
| Routing tables | Bus owners/bridges maintain logical EID routing information. |
| Endpoint discovery | Transport bindings decide how discovery messages are used on the medium. |
| Transport Specific command | MCTP Base provides a dispatch mechanism; transport binding owns the transport-specific body. |

## What This File Does Not Own

| Topic | Owner |
|---|---|
| NVMe-MI command payload, MI opcode, MI response status | `..\mi-1.2` |
| SMBus/I2C Block Write format, PEC, slave address, ARP, NACK/retry timing | `..\mctp-smbus-i2c-1.1.0` |
| PCIe VDM fields, PCIe requester/routing, PCIe endpoint discovery timing | `..\mctp-pcie-vdm-1.0.1` |
| Vendor-defined message body semantics | Vendor documentation |
