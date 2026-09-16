# MCTP SMBus/I2C Transport Binding 1.1.0 Layer

Status: `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED`

This folder records the local MCTP SMBus/I2C Transport Binding Specification as an independent MCTP transport binding layer.

Primary source:

```text
..\NVMe Base Spec\2.0\MCTP\MCTP-SMBusI2C-Transport-Binding-Specification.md
```

Version signal:

```text
Document Number: DSP0237
Version: 1.1.0
```

## File Index

| File | Purpose |
|---|---|
| `MCTP_SMBUS_I2C_AGENTS.md` | Agent rules for using this transport binding layer. |
| `MCTP_SMBUS_I2C_INDEX.md` | Source and table map for token-efficient reading. |
| `MCTP_SMBUS_I2C_BEHAVIOR_REFERENCE.md` | High-value SMBus/I2C packet format, address, PEC, ARP, fairness, retry, and timing behavior. |
| `MCTP_SMBUS_I2C_PACKET_REFERENCE.md` | Expanded SMBus/I2C packet header, MCTP byte placement, PEC, and bridge behavior. |
| `MCTP_SMBUS_I2C_TIMING_ADDRESS_REFERENCE.md` | Expanded SMBus/I2C packet timing, control timing, retry values, and reserved/well-known addresses. |
| `COMMAND_CONTENT_AUDIT.md` | Current coverage and remaining expansion boundaries. |

## Scope

This layer owns MCTP over SMBus/I2C transport binding behavior:

- SMBus Block Write packet framing for MCTP.
- destination/source slave address fields.
- MCTP command code `0x0F`.
- byte count and PEC behavior.
- SMBus ARP and fixed-address considerations.
- NACK, retry, fairness arbitration, bridge buffering, and timing rules.
- anti-aliasing with IPMI/IPMB/ASF and legacy SMBus functions.

This layer does not define NVMe-MI command payload semantics.

## Complete Definition

`PAYLOAD-COMPLETE` applies to the SMBus/I2C packet, PEC, timing, retry, and reserved/well-known address references expanded in this folder.
