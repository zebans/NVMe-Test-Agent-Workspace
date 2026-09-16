# MCTP To NVMe-MI Boundary

Status: `BOUNDARY-COMPLETE`

This file prevents mixing NVMe-MI command semantics with MCTP transport-substrate behavior.

## Correct Layering

```text
NVMe-MI command / response payload
  carried as an MCTP message body
    identified by an MCTP Message Type
      framed by MCTP packet fields
        transported by SMBus/I2C or PCIe VDM binding
```

## Ownership Table

| Question | Owner |
|---|---|
| What NVMe-MI command is being sent? | `..\mi-1.2` |
| What does an NVMe-MI response status mean? | `..\mi-1.2\MI_STATUS_AND_ERROR_REFERENCE.md` |
| What endpoint EID is used? | `mctp-base-1.3.1` |
| How is a message fragmented/reassembled? | `mctp-base-1.3.1` |
| How does EID assignment or discovery work? | `mctp-base-1.3.1` plus relevant transport binding. |
| How is the packet carried on SMBus/I2C? | `..\mctp-smbus-i2c-1.1.0` |
| How is the packet carried on PCIe VDM? | `..\mctp-pcie-vdm-1.0.1` |
| What does an NVMe Admin/I/O queue command do? | Base/NVM/ZNS/KV command folders, not MCTP. |

## Common Confusion

General NVMe over PCIe and NVMe-MI over MCTP over PCIe VDM can both use PCIe as the physical fabric, but they are different protocol paths:

| Path | Uses NVMe queues? | Uses MCTP? | Uses PCIe VDM? |
|---|---:|---:|---:|
| NVMe over PCIe Admin/I/O | Yes | No | No |
| NVMe-MI over MCTP over PCIe VDM | No | Yes | Yes |
| NVMe-MI over MCTP over SMBus/I2C | No | Yes | No |

## Boundary Rules

- Do not treat PCIe VDM as an NVMe Submission Queue mechanism.
- Do not treat MCTP Control commands as NVMe-MI commands.
- Do not derive NVMe-MI command payload fields from MCTP packet fields.
- Do not derive SMBus/I2C PEC, slave address, or PCIe VDM field rules from the MCTP Base source.
- Do not invent vendor-defined message body semantics.
