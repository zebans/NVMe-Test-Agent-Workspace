# Get Features Cross-Spec Boundary

Source: NVMe Base Specification 2.0, sections 5.15 and 5.27.1.

## Base-Owned

| Area | Base ownership |
|---|---|
| Command opcode and dwords | `0Ah`, DPTR, CDW10, CDW11, CDW14. |
| `SEL` behavior | Current/default/saved/supported-capabilities selection. |
| Base feature return formats | Base-defined Feature Identifiers in section 5.27.1. |
| Supported-capabilities CQE DW0 | Figure 195. |

## External Or Shared Ownership

| Area | Boundary |
|---|---|
| I/O Command Set specific feature (`20h`) | Payload and semantics belong to the applicable I/O Command Set spec. |
| Vendor specific features (`C0h`-`FFh`) | Vendor-owned payload and UUID selection behavior. |
| Host Metadata strings | Contents are vendor/host specific even though structure is Base-defined. |
| API usage | PyNVMe call syntax belongs to API layer documentation, not this spec folder. |
