# MCTP SMBus/I2C Packet Reference

Status: `PAYLOAD-COMPLETE`

Source: MCTP SMBus/I2C Transport Binding DSP0237 Version 1.1.0 Figure 1 and Table 1.

This file expands the SMBus/I2C packet header used to carry MCTP packets.

## Packet Position

```text
SMBus Block Write transaction
  Destination Slave Address
  Command Code = 0Fh
  Byte Count
  SMBus Source Slave Address
  MCTP transport header
  MCTP message payload
  PEC
```

## SMBus Block Write Header

| Byte | Field | Bits | Meaning | Important rule |
|---:|---|---:|---|---|
| `1` | Destination Slave Address | `7:1` | SMBus destination slave address for local link. | Target device for the local SMBus/I2C segment. |
| `1` | `Wr` | `0` | SMBus R/W bit. | Shall be `0b`; all MCTP messages use SMBus write transactions. |
| `2` | Command Code | `7:0` | SMBus command code. | All MCTP over SMBus messages use `0Fh`. |
| `3` | Byte Count | `7:0` | Count of bytes following Byte Count up to, but not including, PEC. | If MCTP packet payload starting at byte 9 is 64 bytes, Byte Count is 69. |

## SMBus-Specific Data Bytes And MCTP Header

| Byte | Field | Bits | Meaning | Important rule |
|---:|---|---:|---|---|
| `4` | Source Slave Address | `7:1` | SMBus source slave address for local link. | Changed by bridges when forwarding across SMBus/I2C ports. |
| `4` | Source bit | `0` | Protocol discrimination bit. | Shall be `1b`; helps distinguish MCTP from IPMI over SMBus/IPMB. |
| `5` | MCTP reserved | `7:4` | Reserved by MCTP Base. | Reserved; no semantics. |
| `5` | Header Version | `3:0` | MCTP header version. | Set to `0001b` for conformant devices for this binding. Other values reserved. |
| `6` | Destination EID | `7:0` | MCTP destination endpoint ID. | Defined by MCTP Base. |
| `7` | Source EID | `7:0` | MCTP source endpoint ID. | Defined by MCTP Base. |
| `8` | `SOM` | `7` | Start of Message. | Defined by MCTP Base. |
| `8` | `EOM` | `6` | End of Message. | Defined by MCTP Base. |
| `8` | Packet Sequence | `5:4` | Packet sequence number. | Defined by MCTP Base. |
| `8` | `TO` | `3` | Tag Owner. | Defined by MCTP Base. |
| `8` | Message Tag | `2:0` | Message tag. | Defined by MCTP Base. |
| `9` | `IC` | `7` | Integrity Check bit. | Defined by MCTP Base. |
| `9` | Message Type | `6:0` | MCTP message type. | Defined by MCTP Base; MCTP Control is `00h`. |
| `10:N-1` | Message header/data | variable | Message-type-specific payload. | Owner is selected by Message Type. |
| `N` | PEC | `7:0` | Packet Error Code. | All MCTP transactions include PEC; source transmits and destination checks. |

## Byte Count Example

| MCTP packet payload length from byte 9 | Bytes counted after Byte Count before PEC | Byte Count |
|---:|---:|---:|
| 64 bytes | 5 bytes of bytes 4-8 plus 64 bytes payload | 69 |

## Bridge Behavior

| Action | Rule |
|---|---|
| Forward within SMBus/I2C | Bridge updates destination slave address and source slave address for the target bus/link. |
| Preserve MCTP content | Packet header, message header, and data fields remain unchanged except local physical addressing. |
| Recalculate PEC | Bridge recalculates PEC when source/destination slave address changes. |
| Bridge between media | Physical addressing/header/integrity information changes to match target medium. |

## PEC Rules

| Rule | Meaning |
|---|---|
| PEC is mandatory | Every MCTP over SMBus/I2C transaction includes PEC. |
| Source transmits PEC | Source device generates and transmits PEC. |
| Destination checks PEC | Receiver checks PEC. |
| Bridge drops bad PEC | Bridge drops a received packet if the PEC is incorrect. |

## Boundary

- MCTP EID, `SOM`, `EOM`, sequence, `TO`, message tag, `IC`, and Message Type are defined by MCTP Base.
- SMBus/I2C binding defines byte placement, `0Fh` command code, source/destination slave address, and PEC.
- NVMe-MI payload semantics belong to `..\mi-1.2`.
