# MCTP PCIe VDM Transport Binding 1.0.1 Index

Status: `SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED`

Primary source:

```text
..\NVMe Base Spec\2.0\MCTP\MCTP-PCIe-VDM-Transport-Binding-Specification.md
```

## Source Identity

| Item | Value |
|---|---|
| Specification | MCTP PCIe VDM Transport Binding Specification |
| Document number | `DSP0238` |
| Version | `1.0.1` |
| Local source | `MCTP-PCIe-VDM-Transport-Binding-Specification.md` |

## High-Value Source Map

| Source area | Topic | Use when you need |
|---|---|---|
| Section 6 | MCTP over PCI Express VDM Transport | Overall transport binding behavior. |
| Section 6.2 | Packet format / medium-specific fields | PCIe VDM field values and MCTP placement. |
| Section 6.3 | Physical address format | MCTP Control messages requiring medium-specific physical addresses. |
| Section 6.4 | Message routing | Route-to-root, peer routing limits, cross-bus routing through bus owner. |
| Section 6.6 | PCIe bus address assignment | PCIe address assignment dependency. |
| Section 6.7 | Reset and power management considerations | Conditions that may make MCTP PCIe VDM unavailable or require reinitialization. |
| Section 6.8 | Discovery Notify use | Endpoint announcement to PCIe bus owner. |
| Section 6.9 | PCIe endpoint discovery | Full and partial endpoint discovery/enumeration. |
| Section 6.10 | Timing requirements | MCTP control timing over PCIe VDM. |
| Figure 1 / Table 1 | MCTP over PCIe packet format and medium-specific fields | Exact VDM field lookup. |
| Figures 2-3 | Full and partial discovery flows | Discovery sequence lookup. |
| Table 4 | Timing specifications | Timing constants and retry windows. |

## Read Next

| Question | Read |
|---|---|
| PCIe VDM fixed field meanings | `MCTP_PCIE_VDM_BEHAVIOR_REFERENCE.md` |
| PCIe VDM packet fields, routing values, timing constants | `MCTP_PCIE_VDM_PACKET_REFERENCE.md` |
| EID/message tag/SOM/EOM behavior | `..\mctp-base-1.3.1\MCTP_BASE_BEHAVIOR_REFERENCE.md` |
| NVMe-MI command payload/status | `..\mi-1.2\README.md` |
| Source re-audit of VDM table bytes or timing values | Original source Table 1 or Table 4 |
