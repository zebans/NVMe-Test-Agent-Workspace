# NVMe Admin Command Set Through MI

Status: `FIELD-COMPLETE + ROUTING-COMPLETE`

This folder captures NVM Express Management Interface Revision 1.2 section 6, the NVM Express Admin Command Set through the out-of-band mechanism.

Primary source:

```text
..\..\NVMe Base Spec\2.0\NVMe\NVM-Express-Management-Interface-1.2-2021.06.02-Ratified.md
```

## File Index

| File | Purpose |
|---|---|
| `MI_ADMIN_THROUGH_AGENTS.md` | Agent rules for Admin-through-MI lookup. |
| `MI_ADMIN_THROUGH_COMMAND_TABLE.md` | Figure 114 command support table with links to Base Admin command folders. |
| `command-format-reference.md` | Figures 115-118 request/response message format. |
| `field-reference.md` | Byte and field meanings for Admin-through-MI request/response. |
| `support-overlays-reference.md` | Figures 121-125 log page, feature, sanitize/format support overlays. |
| `status-boundary-reference.md` | Section 6.2 status boundary between MI response status and NVMe Admin completion status. |
| `cross-spec-boundary.md` | Ownership boundary between MI wrapper, Base Admin command semantics, transport, and vendor areas. |
| `COMMAND_CONTENT_AUDIT.md` | Coverage status and remaining boundaries. |

## Scope

This folder owns:

- Out-of-band support requirements for NVMe Admin commands through a Management Endpoint.
- Admin-through-MI request and response wrapper fields.
- Status ownership rules for malformed MI request messages versus completed NVMe Admin commands.
- Routing from MI Figure 114 rows to the canonical Base Admin command folders.
- Get Log Page, Get/Set Features, and sanitize/format support overlays specific to Management Endpoints.

This folder does not own:

- In-band Admin Submission Queue command execution.
- Base Admin command field semantics beyond wrapper mapping.
- PyNVMe API usage or pytest test flow.
- MCTP, SMBus/I2C, or PCIe VDM packet framing.
