# Controller Property Cross-Spec Boundary

Status: `ROUTING-COMPLETE`

## Ownership Matrix

| Question | Owning layer | Route |
|---|---|---|
| What property exists at an offset, how wide is it, and what do its bits mean? | NVMe Base 2.0 section 3.1.3 | `CONTROLLER_PROPERTY_INDEX.md`, then the matching field-reference file in this folder. |
| How does an NVMe-oF host read or write a property? | Fabrics Base Property Get / Property Set | `..\fabrics-base-2.0\commands\04h-property-get\README.md` or `..\fabrics-base-2.0\commands\00h-property-set\README.md`. |
| How is a Controller Property exposed over NVMe over PCIe? | NVMe over PCIe transport | `..\pcie-transport-1.0\PCIE_TRANSPORT_BEHAVIOR_REFERENCE.md`. |
| How does out-of-band MI issue a PCIe Memory Read/Write to a BAR offset? | NVMe-MI section 7 PCIe Command Set | `..\mi-1.2\pcie-through-mi\README.md`, then `field-reference.md`. |
| What is at PCI configuration-space offsets such as BAR0/BAR1, MSI-X, PCIe Capability, or AER? | NVMe over PCIe transport and PCI Express | `..\pcie-transport-1.0\PCIE_REGISTER_AND_CAPABILITY_INDEX.md`. These are not Base Controller Properties. |
| What is at `1000h` and above? | Applicable transport or vendor | PCIe doorbells begin at `1000h`; `1300h+` is vendor-specific according to Figure 35 and needs vendor documentation. |

## Access Path Comparison

| Path | Selector used to reach the property | Property meaning comes from |
|---|---|---|
| Message-based Fabrics | Property Get/Set `ATTRIB` + `OFST`; Set also carries `VALUE`. | This folder. |
| NVMe over PCIe host access | BAR0/BAR1 mapping plus the Controller Property byte offset. | This folder; PCIe layer owns alignment, ordering, and register-access mechanics. |
| Out-of-band PCIe-through-MI | MI PCIe Memory Read/Write selects controller, BAR, offset, length, and data. | This folder when the target offset is a Base property; MI owns wrapper/status/range checks. |

## Boundary Rules

- Do not infer support from property existence alone. Use the Figure 35 applicability column and capability bits such as `CAP.CMBS`, `CAP.PMRS`, `CAP.BPS`, `CAP.NSSRS`, and `CAP.NSSS`.
- Do not use the PCIe transport register index as a substitute for Base field meanings.
- An MI transport or wrapper error is not the same as a Controller Property value or an NVMe completion status.
- Vendor-specific property values and meanings are intentionally unresolved without vendor documentation.
- No Controller Property in Base 2.0 reports whether the physical SSD connector supports hot-plug. Hot-plug capability is owned by the platform/PCIe slot, firmware, and PCIe mechanisms rather than this property map.

