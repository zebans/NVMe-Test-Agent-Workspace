# PCIe Transport Content Audit

Audit date: 2026-06-24

Status: `COMPLETE`

Captured:

- source filename and version signal.
- section map.
- high-value figure map.
- PCI register / capability group index.
- doorbell formula source anchors.
- queue/interrupt source anchors.
- PCIe external source ownership boundary.
- doorbell, queue, reset, interrupt, power, error, and host-flow behavior reference.
- NVMe-specific PCI Header, PCI capability, PCIe capability, MSI/MSI-X, and AER field-rule reference.

Intentionally external:

- PCI Express Base Specification mechanics for link behavior, capability traversal, detailed reset semantics, MSI/MSI-X table protocol, AER protocol, and electrical/protocol requirements.
- Vendor-specific BAR/register behavior.

`COMPLETE` means the NVMe-over-PCIe Transport 1.0 material needed for spec-layer lookup is captured and the remaining PCIe-owned details are explicitly bounded to the PCI Express Base Specification.
