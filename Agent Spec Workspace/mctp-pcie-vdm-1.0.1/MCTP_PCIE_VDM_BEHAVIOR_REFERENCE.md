# MCTP PCIe VDM Behavior Reference

Status: `BEHAVIOR-INDEXED`

This file captures the high-value behavior for MCTP over PCIe VDM.

## Layer Position

```text
NVMe-MI payload, if present
  inside MCTP message
    inside MCTP packet
      inside PCIe Type 1 Vendor Defined Message with data
```

## Encapsulation Facts

| Field / concept | Rule |
|---|---|
| PCIe message type | MCTP over PCIe uses PCIe Type 1 VDMs with data. |
| MCTP VDM code | MCTP messages use the MCTP VDM code value `0000b`. |
| Message Code | Set to `0111_1111b` for Type 1 VDM. |
| Vendor ID | DMTF VDM Vendor ID is `0x1AB4` (`6836`). |
| Traffic Class | Set to `000b` for MCTP over PCIe VDM. |
| TLP Digest (`TD`) | Set to `0b` for MCTP over PCIe VDM. |
| Error Present (`EP`) | Set to `0b` for MCTP over PCIe VDM. |
| Address Type (`AT`) | Set to `00b` for PCIe versions where present. |
| Pad bytes | `0x00` pad bytes may be used to dword-align the PCIe VDM data. |

Use the original source Table 1 when exact bit positions or PCIe-version-specific fields are needed.

## Routing Rules

| Topic | Rule |
|---|---|
| PCIe physical routing | Uses PCIe routing rules; this is not the same as MCTP logical bridging. |
| Non-bus-owner endpoint messages | Messages between endpoints that are not the bus owner are routed to or through the PCIe bus owner as an MCTP bridge. |
| PCIe to other buses | MCTP messages spanning PCIe and other buses go through the PCIe bus owner. |
| Bus owner access | PCIe VDM bus owner functionality is accessible through Route-to-Root Complex addressing. |

## Discovery Behavior

| Discovery item | High-value rule |
|---|---|
| Discovery Notify | Sent by PCIe endpoint to PCIe bus owner when the endpoint needs ID update/discovery handling. |
| Discovery Notify destination | Destination EID is Null Destination EID. |
| Discovery Notify source | Source EID is Null Source EID before assignment, otherwise assigned EID. |
| Prepare for Endpoint Discovery | Causes recipients to set their PCIe endpoint discovered flag to undiscovered. |
| Endpoint Discovery | Undiscovered MCTP-capable endpoints respond. |
| Set Endpoint ID | Bus owner assigns EID after discovering endpoint. |
| Full discovery | Uses broadcast Prepare for Endpoint Discovery, then repeated Endpoint Discovery and Set Endpoint ID until no undiscovered responses remain. |
| Partial discovery | May avoid clearing all discovered flags; uses targeted or periodic discovery around Discovery Notify. |

## Reset / Power / Availability

| Condition | Behavior impact |
|---|---|
| PCIe fabric not configured/enumerated | MCTP over PCIe VDM communication may be unavailable. |
| Function Level Reset or fundamental reset | May reset the MCTP PCIe endpoint and require reinitialization. |
| PCIe link states | MCTP communication is possible only when link state allows VDM communication. |
| Host power management | May make PCIe VDM communication unavailable or cause MCTP state loss. |

## Boundary

| Not owned here | Owner |
|---|---|
| MCTP EID and message-tag semantics | `..\mctp-base-1.3.1` |
| NVMe-MI commands and response status | `..\mi-1.2` |
| NVMe Admin/I/O queues, doorbells, SQ/CQ | Base / PCIe transport / command folders |
| SMBus/I2C packet format and PEC | `..\mctp-smbus-i2c-1.1.0` |
