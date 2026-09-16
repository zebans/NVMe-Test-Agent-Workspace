# PCIe-Through-MI Content Audit

Audit date: 2026-07-31

Status: `FIELD-COMPLETE + ROUTING-COMPLETE`

Captured:

- MI 1.2 section 7 scope, `NMIMT=4h`, and out-of-band-only boundary.
- Shared MI Figures 17-18 four-byte header, request/response, command-family selector, CSI, CIAP, MEB, message-ID boundary, and CRC-32C route.
- Complete Section 7 subsection/Figure 126-144 source map with Figure 122 correction.
- Figures 126-130 common request/response byte layout.
- Figure 128 opcode and Storage Device / Enclosure O/M/P support table.
- Figures 131-144 command-specific `LENGTH`, BAR selector, and 12-bit/32-bit/64-bit `OFFSET` fields.
- Configuration, I/O, and Memory Read/Write Request Data and Response Data behavior.
- Dword rounding, read-zero-padding, and write-padding-discard rules.
- Invalid opcode, parameter, command size, input data size, Access Denied, and PCIe Inaccessible status routing.
- PEL ownership for `CTLID`, BAR, `OFFSET`, and reserved fields.
- Figure 98-99 optional command support-discovery route.
- Section 8.1 reset, SR-IOV VF, power-state, link-state, and ASPM behavior.
- Cross-links to PCIe transport registers/capabilities, MCTP transport, and Base Lockdown.
- Explicit access-tuple boundary: `LENGTH` is byte count; no independent transaction-width or resolved physical base-address field exists.

Source-quality note:

- The local converted Markdown has damaged visual layouts for Figures 126, 129, and some surrounding page artwork. Figures 127 and 130 provide the normative byte descriptions used by this layer. Figures 131-144 provide readable bit descriptions for all six command-specific dwords.

Intentionally external:

- Full PCI Express Base Specification protocol and electrical behavior.
- Vendor-specific BAR contents, blocked address ranges, and protection policies.
- Management Controller and host coordination implementation.
- MCTP / SMBus-I2C / PCIe VDM packet framing.
- PyNVMe API calls and test-flow design.

Complete definition:

`FIELD-COMPLETE + ROUTING-COMPLETE` means this folder can answer PCIe-through-MI command identity, wrapper-byte, command-field, data-direction, range, status, and ownership questions without reopening MI section 7. Questions about the selected PCIe register or address-space contents route to the PCIe transport layer or vendor documentation.
