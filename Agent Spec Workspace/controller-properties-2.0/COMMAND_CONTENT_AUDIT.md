# Controller Property Content Audit

Status: `COMPLETE`

Audit target: NVM Express Base Specification Revision 2.0 section 3.1.3, Figure 35, and Figures 36-69.

## Coverage

| Requirement | Result | Evidence |
|---|---|---|
| Every Figure 35 named property is indexed | PASS | `CONTROLLER_PROPERTY_INDEX.md` covers `CAP` through `PMRMSCU`. |
| Offset, size, and controller-type applicability are searchable | PASS | `CONTROLLER_PROPERTY_INDEX.md`. |
| Every defined Figure 36-69 field has a bit range and meaning | PASS | Three field-reference files. |
| Capability and selector values that affect command/test behavior are retained | PASS | Core, queue/interrupt, and memory-region tables include values and effects. |
| Reserved and vendor-specific ownership is explicit | PASS | Index and `cross-spec-boundary.md`. |
| Message-based, memory-based, Fabrics, PCIe, and MI ownership is separated | PASS | `cross-spec-boundary.md`. |
| Figure 35 `Fh` versus property-specific `10h` discrepancy is preserved and resolved | PASS | `CONTROLLER_PROPERTY_INDEX.md` source-discrepancy note. |
| PyNVMe API or test-flow instructions are absent | PASS | This layer is implementation-neutral. |

## Intentional Boundaries

- Transport-specific properties from `1000h` are expanded by their transport owner, not by Base property files.
- Vendor-specific space from `1300h` requires vendor documentation.
- PCI configuration space and PCIe Extended Capabilities are owned by the PCIe transport/PCI Express layers.
- This audit proves markdown coverage and routing. Original source remains authoritative for legal or certification-grade interpretation.

