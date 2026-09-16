# MCTP SMBus/I2C Transport Binding 1.1.0 Index

Status: `SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED`

Primary source:

```text
..\NVMe Base Spec\2.0\MCTP\MCTP-SMBusI2C-Transport-Binding-Specification.md
```

## Source Identity

| Item | Value |
|---|---|
| Specification | MCTP SMBus/I2C Transport Binding Specification |
| Document number | `DSP0237` |
| Version | `1.1.0` |
| Local source | `MCTP-SMBusI2C-Transport-Binding-Specification.md` |

## High-Value Source Map

| Source area | Topic | Use when you need |
|---|---|---|
| Section 6 | MCTP over SMBus/I2C transport | Overall transport binding behavior. |
| Section 6.2 | Transport binding use with I2C | Supported I2C modes/addressing scope. |
| Section 6.3 / Figure 1 / Table 1 | Packet format and header fields | SMBus Block Write framing, command code, byte count, source/destination slave address, PEC. |
| Section 6.7-6.11 | Medium IDs, bus owner, address assignment | ARP/fixed address and bus owner considerations. |
| Section 6.12 | SMBus/I2C considerations | ACK/NACK and packet handling context. |
| Sections 6.13-6.17 | Fairness arbitration | Bus fairness, bridge and endpoint retry/buffering behavior, timing. |
| Section 6.18-6.20 | Packet/control timing and bus recovery | Retry counts, timeouts, clock stretching, bus recovery. |
| Section 6.21 | Protocol anti-aliasing | Differentiation from IPMI/IPMB/ASF and legacy SMBus functions. |
| Tables 5-9 | Fairness and timing tables | Exact timing values. |
| Tables 10-11 | Reserved/well-known and recommended slave address allocation | Exact address ranges and recommendations. |

## Read Next

| Question | Read |
|---|---|
| Packet framing, `0x0F`, slave address, PEC, ARP, fairness | `MCTP_SMBUS_I2C_BEHAVIOR_REFERENCE.md` |
| Exact SMBus/I2C packet header, byte placement, PEC, bridge behavior | `MCTP_SMBUS_I2C_PACKET_REFERENCE.md` |
| Packet timing, control timing, retry values, reserved/well-known slave addresses | `MCTP_SMBUS_I2C_TIMING_ADDRESS_REFERENCE.md` |
| EID/message tag/SOM/EOM behavior | `..\mctp-base-1.3.1\MCTP_BASE_BEHAVIOR_REFERENCE.md` |
| NVMe-MI command payload/status | `..\mi-1.2\README.md` |
| Source re-audit of timing/address tables | Original source Tables 5-11 |
