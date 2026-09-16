# NVMe over PCIe Transport 1.0 Layer

Status: `COMPLETE`

This folder records the local NVMe over PCIe Transport Specification source as an independent transport layer.

Primary source:

```text
..\NVMe Base Spec\2.0\NVMe-over-PCIe-Transport-Specification-1_0-2021.06.02-Ratified-1.md
```

Version signal:

```text
NVMe over PCIe Transport Specification, Revision 1.0
May 18th, 2021
```

## File Index

| File | Purpose |
|---|---|
| `PCIE_TRANSPORT_AGENTS.md` | Agent rules for using this PCIe transport layer. |
| `PCIE_TRANSPORT_INDEX.md` | Section and figure map for token-efficient reading. |
| `PCIE_REGISTER_AND_CAPABILITY_INDEX.md` | PCI header, PCI capabilities, PCIe capabilities, AER, BAR, MSI/MSI-X, and doorbell index. |
| `PCIE_TRANSPORT_BEHAVIOR_REFERENCE.md` | Doorbell, queue, reset, interrupt, power, error, and host-flow behavior reference. |
| `PCIE_REGISTER_FIELD_REFERENCE.md` | PCI Header, capability, MSI/MSI-X, PCIe Capability, and AER field-rule reference. |
| `COMMAND_CONTENT_AUDIT.md` | Coverage status and remaining expansion boundaries. |

Base-owned Controller Property fields are intentionally not duplicated here. Read `..\controller-properties-2.0\README.md` for property offsets and bit meanings, then return here for PCIe mapping and access rules.

## Scope

This layer owns PCIe-specific transport behavior:

- PCIe register and capability requirements for NVMe controllers.
- BAR0/BAR1 memory-mapped controller register access.
- Doorbell offset formulas and SQ/CQ doorbell behavior.
- PCIe queue instantiation details such as Interrupt Vector.
- PCIe resets, command processing, interrupts, power management, and error handling.
- PCIe configuration space and capability layouts as referenced by this transport specification.

Use Base Spec 2.0 for NVMe command semantics. Use this layer when the question is specifically about PCIe transport behavior.

For PCIe Configuration, I/O, or Memory Read/Write encapsulated as out-of-band NVMe-MI commands, start from `..\mi-1.2\pcie-through-mi\README.md`. Return here only to interpret the selected PCIe register, capability, BAR, controller property, or transport behavior.

## Complete Definition

`COMPLETE` means this folder captures the NVMe-over-PCIe transport lookup path, source anchors, controller-property doorbell rules, queue/interrupt/reset/power/error behavior, host-flow considerations, and NVMe-specific PCI/PCIe register requirements. It does not replace the PCI Express Base Specification for PCIe-owned protocol, electrical, link, reset, and capability mechanics.
