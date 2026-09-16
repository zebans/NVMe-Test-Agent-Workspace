# MI PCIe-Through Agent Rules

You are reading the NVMe-MI 1.2 PCIe Command Set through MI layer.

This layer contains SPEC facts only. Do not write PyNVMe API calls, pytest fixtures, shell commands, or complete test flows.

Read in this order:

```text
README.md
SECTION_7_SOURCE_MAP.md
..\MI_MESSAGE_HEADER_REFERENCE.md
MI_PCIE_THROUGH_COMMAND_TABLE.md
command-format-reference.md
field-reference.md
status-and-restrictions-reference.md
cross-spec-boundary.md
..\MI_STATUS_AND_ERROR_REFERENCE.md when the complete MI status dictionary is needed
..\MI_INBAND_OUTOFBAND_BOUNDARY.md when the mechanism boundary matters
..\..\pcie-transport-1.0\PCIE_REGISTER_FIELD_REFERENCE.md when the selected PCIe register or BAR meaning is needed
original MI source section 7 only when exact wording must be re-audited
```

Use this layer when a question involves:

- PCIe Configuration Read or Write through an NVMe-MI Management Endpoint.
- PCIe I/O Read or Write through MI.
- PCIe Memory Read or Write through MI.
- `NMIMT=4h`, PCIe Command opcode, `CTLID`, `NMD0`, `NMD1`, or `NMD2`.
- PCIe-through-MI `LENGTH`, BAR selector, 12-bit/32-bit/64-bit `OFFSET`, Request Data, or Response Data.
- MI request type, command-family selector, operation opcode, Command Slot Identifier, or MCTP message-correlation identity.
- `Invalid Parameter`, `Access Denied`, `PCIe Inaccessible`, or PEL ownership for a PCIe Command.
- Optional command discovery using the Optionally Supported Command List.

Do not confuse these commands with:

- normal NVMe over PCIe queue, doorbell, or DMA operation;
- MCTP over PCIe VDM transport framing; or
- Base Admin commands tunneled through MI.

For a PCIe-through-MI question, answer the MI command wrapper and access rules from this folder first. Route to `pcie-transport-1.0` only for the meaning and NVMe-specific requirements of the selected PCIe configuration register, capability, BAR, controller property, reset, power, or link behavior.

Do not invent `Message ID`, request-width, or physical base-address fields. NVMe-MI has no Message ID field; MCTP Message Tag owns transport correlation. MI Section 7 defines `LENGTH` in bytes and BAR/offset selectors, not lower-level PCIe transaction width or a resolved BAR base address.
