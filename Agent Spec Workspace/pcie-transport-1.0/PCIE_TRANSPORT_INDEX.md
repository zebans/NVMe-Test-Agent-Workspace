# PCIe Transport Index

Status: `COMPLETE`

Primary source:

```text
..\NVMe Base Spec\2.0\NVMe-over-PCIe-Transport-Specification-1_0-2021.06.02-Ratified-1.md
```

## Section Map

| Topic | Section |
|---|---|
| Overview | 1.1 |
| Scope and precedence | 1.2 |
| Conventions | 1.3 |
| Definitions | 1.4 |
| References | 1.5 |
| Transport overview | 2 |
| Transport binding | 3 |
| Setup and initialization | 3.1 |
| PCI device requirements | 3.1.1 |
| Transport specific controller properties | 3.1.2 |
| SQ Tail Doorbell | 3.1.2.1, Figure 5 |
| CQ Head Doorbell | 3.1.2.2, Figure 6 |
| Queue model instantiation | 3.2 |
| Resets | 3.3 |
| Data transfer model | 3.4 |
| Interrupts | 3.5 |
| Power management | 3.6 |
| Error handling model | 3.7 |
| Transport specific content | 3.8 |
| Host considerations | Annex A |

## High-Value Figures

| Figure | Topic |
|---|---|
| Figure 3 | PCI Express Registers |
| Figure 4 | PCI Express Specific Controller Property Definitions |
| Figure 5 | SQyTDBL - Submission Queue y Tail Doorbell |
| Figure 6 | CQyHDBL - Completion Queue y Head Doorbell |
| Figure 7 | Create I/O Completion Queue CDW11 Interrupt Vector definition |
| Figure 8 | Command Processing |
| Figure 9 | Pin Based, Single MSI, and Multiple MSI Behavior |
| Figure 10 | PCI Express Type 0/1 Common Configuration Space |
| Figures 11-29 | PCI Header fields |
| Figures 30-33 | PCI Power Management Capability |
| Figures 34-41 | MSI Capability |
| Figures 42-46 | MSI-X Capability |
| Figures 47-57 | PCI Express Capability |
| Figures 58-67 | Advanced Error Reporting Capability |

## Key Facts

- PCIe transport uses memory mapped I/O for data transfer and register access.
- Controller Properties are memory mapped registers located in the address range specified by `MLBAR` / `MUBAR` (`BAR0` / `BAR1`).
- NVMe PCIe controller registers start at the offset defined by Figure 4.
- Host shall not issue locked accesses to registers.
- Host shall access registers in their native width or aligned 32-bit accesses.
- Accesses targeting any portion of two or more registers are not supported.
- Reserved registers and reserved bits are read-only and return `0h` when read.
- MSI-X is the recommended interrupt mechanism.
