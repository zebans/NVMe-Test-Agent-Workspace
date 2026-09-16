# MCTP SMBus/I2C Timing And Address Reference

Status: `PAYLOAD-COMPLETE`

Source: MCTP SMBus/I2C Transport Binding DSP0237 Version 1.1.0 Tables 8-10.

This file expands the high-value timing, retry, and reserved/well-known address rules for MCTP over SMBus/I2C.

## Packet Timing And Retry

Source: Table 8.

| Symbol | Name | Value | Meaning |
|---|---|---:|---|
| `PN1` | Endpoint packet-level retries | 8 | Non-bridge endpoint retries an MCTP packet after NACK up to at least this count. Also applies to bridge transmitting as endpoint. |
| `PN2` | Bridge packet-level retries | 12 | Bridge transmitting for routing retries an MCTP packet after NACK up to this count. |
| `PT1a` | Packet transaction originator duration | 250 us per byte | Overall duration from byte after slave byte through PEC is bounded by byte count times this interval. |
| `PT1b` | Originator slave address byte duration | 250 us | Time including clock stretching to transmit slave address, write bit, and ACK bits. |
| `PT1c` | Slave-induced clock stretching | 250 us per byte | MCTP receivers shall not clock-stretch overall packet beyond this per-byte amount. |
| `PT2a` | Timeout waiting bus free without STOP detection | 100 ms | Controller may assume bus free if no START/STOP observed for this interval; restarts on START. |
| `PT2b` | Timeout waiting bus free by data/clock activity | 50 us | Alternative bus-free detection using data/clock high interval and SMBus `TBUF`. |
| `PT3` | SDA Low timeout | 2 sec min, 5 sec max | Time bus owner monitors SDA low before attempting stuck-zero clearing. |

Implementation shall meet at least one of `PT2a` or `PT2b`.

## Control Message Timing

Source: Table 9.

| Symbol | Name | Min | Max | Meaning |
|---|---|---:|---:|---|
| `Treclaim` | Endpoint ID reclaim | 5 sec | none | Minimum time bus owner waits before reclaiming EID for non-responsive hot-plug endpoint. |
| `MN1` | Number of request retries | 2 | See description | Total of three tries minimum: original plus two retries. Retries limited by `MT4` max. |
| `MT1` | Request-to-response time | none | 100 ms | Responder interval from end of request reception to start of response transmission. |
| `MT2` | Timeout waiting for response | `MT1 max + 2*MT3 max` | `MT4 min` | Requester minimum wait before retrying an MCTP Control request. |
| `MT3` | Transmission delay | none | 100 ms | Time from end of transmit to beginning of receive for an MCTP Control message. |
| `MT4` | Instance ID expiration interval | 5 sec | 6 sec | Response Instance ID expires and becomes reusable; responder tracks request for this interval. |

Responses are not retried. A request retry is a complete retransmission of the MCTP Control message.

## Reserved / Well-Known Slave Addresses

Source: Table 10.

| Address / range | Meaning | Disposition |
|---|---|---|
| `00h` | I2C general call address / IPMI broadcast | Avoid |
| `01h` | START byte | Avoid |
| `02h`-`03h` | CBUS address | Avoid |
| `04h`-`05h` | Address reserved for different bus format | Avoid |
| `06h`-`07h` | Reserved for future I2C specifications | Avoid |
| `08h`-`0Fh` | I2C high-speed mode / master code range | Avoid; MCTP does not support I2C high-speed mode. |
| `10h` | SMBus host | Reserved |
| `18h`-`19h` | SMBus Alert Response address | Reserved |
| `20h`-`21h` | IPMI BMC address | Avoid if IPMI BMC may share segment. |
| `50h`-`51h` | ACCESS.bus host | Avoid. |
| `6Eh`-`6Fh` | ACCESS.bus default address | Avoid. |
| `F0h`-`F7h` | I2C 10-bit slave addressing related | Avoid; MCTP supports only 7-bit addresses on SMBus/I2C. |
| `F8h`-`FFh` | Reserved for future I2C specs | Avoid. |
| `C2h`-`C3h` | SMBus Device Default address | Reserved; used for SMBus ARP with MCTP. |

By convention, 7-bit slave address shown as two-digit hex is treated as an 8-bit value with the 7-bit address in bits `7:1` and R/W in bit `0`.

## ARP / Address Assignment Notes

| Topic | Rule |
|---|---|
| ARP-capable bus | If ARP-able devices exist, one controller must act as ARP master. |
| Bus owner needs addresses | MCTP bus owner must know physical addresses of MCTP devices to assign EIDs and route. |
| ARP master separate from bus owner | If different physical device, address assignment info must be communicated to bus owner. |
| Multiple SMBus/I2C interfaces | Interfaces should be ARP-capable or configured with non-conflicting fixed addresses; distinct UDID for ARP-able interfaces. |
| Fixed addresses | Need conflict avoidance because no effective central registry exists. |

## Boundary

- Exact recommended computer-system allocation table remains in source Table 11 unless a test needs specific address-row assertions.
- Vendor/device-specific fixed-address policy requires device/vendor documentation.
