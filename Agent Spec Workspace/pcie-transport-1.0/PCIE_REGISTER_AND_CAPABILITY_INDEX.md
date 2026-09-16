# PCIe Register and Capability Index

Status: `COMPLETE`

Source: NVMe over PCIe Transport Specification Revision 1.0.

## PCI Express Register Groups

| Register group | Source |
|---|---|
| PCI Header | Figure 3, Figures 10-29 |
| PCI Power Management Capability | Figure 3, Figures 30-33 |
| Message Signaled Interrupt Capability | Figure 3, Figures 34-41 |
| MSI-X Capability | Figure 3, Figures 42-46 |
| PCI Express Capability | Figure 3, Figures 47-57 |
| Advanced Error Reporting Capability | Figure 3, Figures 58-67 |

## NVMe PCIe Controller Properties

The Base-owned Controller Property meanings and fields are indexed in `..\controller-properties-2.0\README.md`. This PCIe transport layer owns how those properties are mapped and accessed, plus the transport-specific doorbells below.

| Symbol | Source | Purpose |
|---|---|---|
| `SQyTDBL` | Section 3.1.2.1, Figure 5 | Submission Queue y Tail Doorbell. |
| `CQyHDBL` | Section 3.1.2.2, Figure 6 | Completion Queue y Head Doorbell. |

Doorbell offset formulas:

```text
SQyTDBL = 1000h + ((2y) * (4 << CAP.DSTRD))
CQyHDBL = 1000h + ((2y + 1) * (4 << CAP.DSTRD))
```

## Queue and Interrupt Hooks

| Topic | Source |
|---|---|
| Interrupt Vector field in Create I/O Completion Queue CDW11 | Figure 7 |
| Command processing flow | Figure 8 |
| Pin-based / single MSI / multiple MSI behavior | Figure 9 |
| MSI-X behavior | Section 3.5 |
| Interrupt coalescing feature relationship | Section 3.5 |

## PCIe External Source Boundaries

| Area | Owning source |
|---|---|
| PCI Express register reset behavior | PCI Express Base Specification |
| Conventional Reset / Function Level Reset mechanics | PCI Express Base Specification |
| PCI/PCIe capability field definitions duplicated in section 3.8 | PCI / PCI Express specifications are normative; this layer records NVMe controller additional requirements. |

## Detailed References

| Need | Read |
|---|---|
| NVMe-specific register and capability field rules | `PCIE_REGISTER_FIELD_REFERENCE.md` |
| Doorbell, queue, reset, interrupt, power, error, and host-flow behavior | `PCIE_TRANSPORT_BEHAVIOR_REFERENCE.md` |
