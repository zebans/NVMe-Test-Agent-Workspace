# MCTP SMBus/I2C Behavior Reference

Status: `BEHAVIOR-INDEXED`

This file captures the high-value behavior for MCTP over SMBus/I2C.

## Layer Position

```text
NVMe-MI payload, if present
  inside MCTP message
    inside MCTP packet
      inside SMBus Block Write transaction over SMBus/I2C
```

## Packet Framing

| Field / concept | Rule |
|---|---|
| Transaction type | MCTP over SMBus/I2C uses SMBus Block Write transactions. |
| Destination Slave Address | SMBus destination slave address for the local link. |
| R/W bit | Set to write (`0b`) for MCTP messages. |
| Command Code | All MCTP over SMBus messages use command code `0x0F`. |
| Byte Count | Counts bytes after Byte Count up to but not including PEC. |
| Source Slave Address | MCTP-specific source slave address field in the SMBus data bytes. |
| MCTP transport header | Follows SMBus-specific header fields and carries common MCTP fields. |
| PEC | Packet Error Code byte; all MCTP transactions include PEC. |

## PEC And Bridge Behavior

| Topic | Rule |
|---|---|
| PEC presence | Every MCTP over SMBus/I2C transaction includes a PEC byte. |
| PEC checking | Destination checks PEC. |
| Bridge forwarding | Bridge leaves MCTP payload fields intact as appropriate but updates local SMBus addressing. |
| PEC recalculation | Bridge recalculates PEC when source/destination slave address changes. |
| Bad PEC | A bridge drops a received packet if the PEC is incorrect. |

## Address And Discovery Context

| Topic | Rule |
|---|---|
| Slave address | Each device has a slave address used as transaction target. |
| ARP-capable | Device supports SMBus ARP-based dynamic slave address assignment. |
| Fixed and discoverable | Device has fixed address but supports discovery commands. |
| Fixed-not-discoverable | Device has fixed address and limited discovery capability. |
| Non-ARP-capable | Device does not support ARP commands; address is fixed/configured. |
| Bus owner / ARP master | If ARP-able devices exist, one controller assigns slave addresses and bus owner needs address information for MCTP EID work. |

## NACK, Retry, Fairness, And Timing

| Topic | High-value behavior |
|---|---|
| Slave address NACK | Indicates physical absence of the target interface in SMBus/I2C semantics. |
| Packet-level retry | Non-bridge endpoints retry packet transactions according to binding timing/retry rules. |
| Bridge buffering | Bridges need input buffer space; if insufficient, the bridge may NACK/drop according to rules. |
| Fairness arbitration | MCTP adds fairness behavior so one port does not monopolize the bus. |
| Clock stretching / bus free | Binding defines SMBus/I2C timing constraints and recovery-related behavior. |
| Exact values | Use source Tables 5-9 for timing constants and retry values. |

## Anti-Aliasing

| Conflict area | MCTP distinction |
|---|---|
| IPMI over SMBus / IPMB | MCTP uses source slave address conventions and header/version fields to distinguish traffic. |
| ASF / legacy SMBus | MCTP uses command code `0x0F`; legacy functions using the same command code need careful separation. |
| Legacy SMBus functions | A device may use separate slave addresses or protocol discrimination to avoid aliasing. |

## Boundary

| Not owned here | Owner |
|---|---|
| MCTP EID and message-tag semantics | `..\mctp-base-1.3.1` |
| NVMe-MI commands and response status | `..\mi-1.2` |
| PCIe VDM encapsulation and routing | `..\mctp-pcie-vdm-1.0.1` |
| Exact vendor/device SMBus behavior | Vendor documentation |
