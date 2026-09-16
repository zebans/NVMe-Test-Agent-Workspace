# NVM Get LBA Status Cross-Spec Boundary

## This Folder Owns

- NVM Command Set 1.0 Get LBA Status command fields.
- `ATYPE` meanings for `10h` and `11h`.
- Returned LBA Status Descriptor List layout.
- Descriptor entry status bits.
- NVM LBA Status Information log page relationship.

## This Folder Does Not Own

- Base Admin opcode table identity beyond routing from opcode `86h`.
- PyNVMe API call syntax.
- Test-flow command sequencing policy.
- ZNS-specific zone state, write pointer, or zone boundary behavior.
- Vendor-specific media recovery details.

## Read Across Layers

| Question | Read |
|---|---|
| Is Admin opcode `86h` valid and what is its Base boundary? | `..\..\..\..\admin-commands-2.0\86h-get-lba-status` |
| What are `SLBA`, `MNDW`, `ATYPE`, `RL`? | This folder. |
| How do I parse returned descriptor entries? | [payload-reference.md](payload-reference.md) |
| How do I know which range/action to query first? | NVM LBA Status Information log page `LID=0Eh`; summarized in [selector-reference.md](selector-reference.md). |
| What if the namespace uses ZNS (`CSI=02h`)? | `..\..\..\..\zns-command-set-1.1` for ZNS-specific behavior. |
| How do I call this through PyNVMe? | API layer, not SPEC layer. |
