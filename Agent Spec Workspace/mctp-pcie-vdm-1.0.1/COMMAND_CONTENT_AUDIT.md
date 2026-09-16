# MCTP PCIe VDM Content Audit

Status: `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED`

## Source

```text
..\NVMe Base Spec\2.0\MCTP\MCTP-PCIe-VDM-Transport-Binding-Specification.md
```

## Captured

| Area | Evidence |
|---|---|
| Source identity | `DSP0238`, Version `1.0.1`. |
| Source index | PCIe VDM source sections, figures, and timing table are indexed. |
| Behavior reference | Encapsulation, fixed field values, routing, discovery, reset/power availability, and boundary facts are summarized. |
| Packet/timing expansion | `MCTP_PCIE_VDM_PACKET_REFERENCE.md` expands Table 1 packet fields, supported routing values, and Table 4 timing requirements. |
| Boundary | NVMe-MI, MCTP Base, NVMe queue path, PCIe transport, and SMBus/I2C ownership are separated. |

## Not Expanded

| Area | Reason |
|---|---|
| PCIe Base Specification behavior | Outside this transport binding layer. |

## Token-Efficient Use

Use `MCTP_PCIE_VDM_PACKET_REFERENCE.md` before opening the full source for packet fields or timing constants. Open the full source only for source re-audit.
