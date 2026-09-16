# Admin-Through-MI Content Audit

Audit date: 2026-07-29

Status: `FIELD-COMPLETE + ROUTING-COMPLETE`

Captured:

- MI 1.2 section 6 scope and mechanism boundary.
- Figure 114 Admin command O/M/P support table.
- Links from every Figure 114 Admin opcode/range to the canonical `admin-commands-2.0` folder.
- Figures 115-118 request/response field layout.
- Section 6.1 request/response data rules.
- Section 6.2 status boundary between MI response status and NVMe Admin completion status.
- Figures 121-125 high-value support overlays for log pages, sanitize/format, and feature support.
- Cross-spec ownership rules for MI wrapper, Base Admin command semantics, MCTP/transport, and vendor-specific behavior.

Source-quality note:

- The local converted MI markdown has extraction damage in Figure 114. The table preserves Figure 114 support intent and normalizes opcode values against the Base Admin opcode table.

Intentionally external:

- Full Base Admin command CDW and payload semantics; route to `..\..\admin-commands-2.0`.
- Exact log page and feature payload meanings; route through the linked Get Log Page, Get Features, or Set Features folders.
- Vendor-specific Admin command behavior.
- MCTP, SMBus/I2C, and PCIe VDM transport packet fields.

Complete definition:

`FIELD-COMPLETE + ROUTING-COMPLETE` means this folder can answer Admin-through-MI support, wrapper-field, data-slicing, and status-boundary questions without reopening the original MI source. It should route command-body questions to the linked Admin command folder.
