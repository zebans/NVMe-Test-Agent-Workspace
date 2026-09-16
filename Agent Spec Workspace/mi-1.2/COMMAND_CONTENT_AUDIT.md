# MI Content Audit

Audit date: 2026-06-24

Status: `FRAMEWORK-COMPLETE`

Captured:

- source filename and version signal.
- section map.
- high-value figure groups.
- Management Interface Command Set command index.
- Management Interface Command Set opcode/support table from Figure 57 through Figure 59.
- command-control fields, payload direction, and high-value command-specific checks for section 5 commands.
- Shared Figures 17-18 NVMe-MI Message Header fields, request/response and command-family selectors, command slot, MEB/CIAP, transport message-correlation boundary, and MIC parameters.
- Response Message Status values and common error hooks.
- Admin/PCIe command set boundaries.
- in-band and out-of-band ownership map.
- Admin-through-MI Figure 114 support table and Figures 115-118 wrapper/status fields in `admin-through-mi\`.
- PCIe-through-MI Figures 126-144 opcode, wrapper, field, data, status, restriction, and PCIe transport routing in `pcie-through-mi\`.

Intentionally external:

- Vendor-specific MI commands and vendor-specific statuses.
- SES diagnostic page semantics beyond MI wrapper fields.
- MCTP, SMBus/I2C, PCIe Base, IPMI FRU, and form-factor reset details where MI references another specification.
- Full byte-by-byte expansion of large returned data structures when a downstream task only needs command-control lookup; source figure anchors remain in `MI_SOURCE_INDEX.md`.

`FRAMEWORK-COMPLETE` means MI 1.2 command-control lookup, status/error lookup, source anchors, and cross-spec boundaries are captured for the spec layer. Admin-through-MI is expanded in `admin-through-mi\`; PCIe-through-MI is expanded in `pcie-through-mi\`.
