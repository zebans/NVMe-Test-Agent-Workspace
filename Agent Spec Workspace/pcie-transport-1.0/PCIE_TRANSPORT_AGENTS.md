# PCIe Transport Agent Rules

You are reading the NVMe over PCIe Transport Specification Revision 1.0 layer.

This layer owns PCIe transport facts only. It does not own Admin/I/O command semantics, I/O command-set behavior, Fabrics command identity, NVMe-MI behavior, or PyNVMe API calls.

Read in this order:

```text
README.md
PCIE_TRANSPORT_INDEX.md
PCIE_TRANSPORT_BEHAVIOR_REFERENCE.md
PCIE_REGISTER_FIELD_REFERENCE.md
original source section only when PCIe-owned wording must be quoted or re-audited
```

Use this layer for:

- PCIe controller register access through BAR0/BAR1.
- SQ/CQ doorbell offset formulas.
- PCI header / capability / extended capability source anchors.
- NVMe-specific PCI header / capability / extended capability field rules.
- MSI, MSI-X, pin-based interrupt behavior.
- PCIe transport queue instantiation details.
- PCIe reset, power, host-flow, and error handling model.

Do not write test-flow steps or implementation APIs here.

When a question says PCIe Configuration Read/Write, PCIe I/O Read/Write, or PCIe Memory Read/Write **through NVMe-MI**, route first to `..\mi-1.2\pcie-through-mi\README.md`. This PCIe transport layer interprets the selected target register, capability, BAR, or controller behavior; it does not own the MI command wrapper, opcode, `CTLID`, `LENGTH`, `OFFSET`, or MI status.
