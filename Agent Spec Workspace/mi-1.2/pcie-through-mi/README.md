# PCIe Command Set Through MI

Status: `FIELD-COMPLETE + ROUTING-COMPLETE`

This folder captures NVM Express Management Interface Revision 1.2 section 7, the PCIe Command Set through the out-of-band mechanism.

Primary source:

```text
..\..\..\NVMe Base Spec\2.0\NVMe\NVM-Express-Management-Interface-1.2-2021.06.02-Ratified.md
```

## File Index

| File | Purpose |
|---|---|
| `MI_PCIE_THROUGH_AGENTS.md` | Agent rules and token-efficient reading order. |
| `SECTION_7_SOURCE_MAP.md` | Complete Section 7 subsection/figure coverage and authoritative original-source route. |
| `MI_PCIE_THROUGH_COMMAND_TABLE.md` | Figure 128 opcode and O/M/P support table. |
| `command-format-reference.md` | Figures 126-130 common request and response wrapper. |
| `field-reference.md` | Figures 131-144 command-specific `LENGTH`, `BAR`, `OFFSET`, and data rules. |
| `status-and-restrictions-reference.md` | Status, PEL, range, access, state, and host-interference rules. |
| `cross-spec-boundary.md` | Ownership links among NVMe-MI, PCIe transport, MCTP, and Lockdown. |
| `COMMAND_CONTENT_AUDIT.md` | Coverage status and intentional external boundaries. |

## Scope

This folder owns:

- PCIe Command Set message identity using `NMIMT=4h`.
- Out-of-band support and opcode definitions for PCIe Configuration, I/O, and Memory Read/Write.
- Common PCIe-through-MI request and response bytes.
- Command-specific `CTLID`, `NMD0`, `NMD1`, `NMD2`, `LENGTH`, `BAR`, and `OFFSET` meanings.
- Request Data, Response Data, dword padding, range checks, and MI Response Message Status behavior.
- Routing from a selected BAR or configuration-space offset to the PCIe transport register reference.

This folder does not own:

- Normal host NVMe Admin or I/O queue processing.
- PCIe TLP encoding, link training, electrical behavior, or the full PCI Express Base Specification.
- MCTP, SMBus/I2C, or PCIe VDM packet framing.
- Host and Management Controller coordination policy.
- PyNVMe API usage, pytest code, or test-flow design.

## Fast Routing

| Question | Read |
|---|---|
| Which PCIe-through-MI opcode is used? | `MI_PCIE_THROUGH_COMMAND_TABLE.md` |
| What are the complete Section 7 source and figure anchors? | `SECTION_7_SOURCE_MAP.md` |
| What are the MI header, request type, command selector, slot, or message-ID equivalents? | `..\MI_MESSAGE_HEADER_REFERENCE.md` |
| Where are `OPC`, `CTLID`, `NMD0-2`, Request Data, and Response Data? | `command-format-reference.md` |
| What do `LENGTH`, `BAR`, or `OFFSET` mean for one command? | `field-reference.md` |
| Which error/status applies? | `status-and-restrictions-reference.md` |
| What does the selected PCIe register or BAR contain? | `cross-spec-boundary.md`, then `..\..\pcie-transport-1.0\PCIE_REGISTER_FIELD_REFERENCE.md` |
| What does a Base Controller Property at the selected BAR offset mean? | `..\..\controller-properties-2.0\CONTROLLER_PROPERTY_INDEX.md`, then its routed field reference. |
