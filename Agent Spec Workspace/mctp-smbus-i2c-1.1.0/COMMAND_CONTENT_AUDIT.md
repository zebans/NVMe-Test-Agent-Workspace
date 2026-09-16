# MCTP SMBus/I2C Content Audit

Status: `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED`

## Source

```text
..\NVMe Base Spec\2.0\MCTP\MCTP-SMBusI2C-Transport-Binding-Specification.md
```

## Captured

| Area | Evidence |
|---|---|
| Source identity | `DSP0237`, Version `1.1.0`. |
| Source index | SMBus/I2C source sections, figures, and timing/address tables are indexed. |
| Behavior reference | Block Write framing, `0x0F`, slave addresses, byte count, PEC, ARP/fixed address, NACK/retry/fairness/timing, anti-aliasing are summarized. |
| Packet expansion | `MCTP_SMBUS_I2C_PACKET_REFERENCE.md` expands packet byte placement, PEC, and bridge behavior. |
| Timing/address expansion | `MCTP_SMBUS_I2C_TIMING_ADDRESS_REFERENCE.md` expands Table 8 packet timing, Table 9 control timing, retry values, and Table 10 reserved/well-known addresses. |
| Boundary | NVMe-MI, MCTP Base, PCIe VDM, and vendor/device ownership are separated. |

## Not Expanded

| Area | Reason |
|---|---|
| Full recommended computer-system slave address allocation table | Source Table 11 remains exact authority unless needed by a test. |
| Device-specific SMBus behavior | Vendor documentation required. |

## Token-Efficient Use

Use `MCTP_SMBUS_I2C_PACKET_REFERENCE.md` and `MCTP_SMBUS_I2C_TIMING_ADDRESS_REFERENCE.md` before opening the full source for packet, PEC, timing, retry, or reserved address questions. Open the full source only for Table 11 details or source re-audit.
