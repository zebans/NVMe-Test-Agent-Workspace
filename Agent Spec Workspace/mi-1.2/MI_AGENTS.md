# MI Agent Rules

You are reading the NVM Express Management Interface Revision 1.2 layer.

This layer owns MI specification facts only. Do not write PyNVMe API calls, pytest fixtures, shell commands, or complete test flows.

Read in this order:

```text
README.md
MI_SOURCE_INDEX.md
MI_COMMAND_SET_INDEX.md
MI_MESSAGE_HEADER_REFERENCE.md when header bytes, request type, NMIMT, CSI, CIAP, MEB, message identity, or MIC is needed
MI_COMMAND_REFERENCE.md
admin-through-mi\README.md when the question involves NVM Express Admin commands through MI
admin-through-mi\MI_ADMIN_THROUGH_COMMAND_TABLE.md when the question asks which Admin commands are supported/prohibited over OOB MI
admin-through-mi\command-format-reference.md when Admin-through-MI request/response wrapper bytes are needed
admin-through-mi\status-boundary-reference.md when status ownership is ambiguous
pcie-through-mi\README.md when the question involves PCIe Configuration, I/O, or Memory access through MI
pcie-through-mi\SECTION_7_SOURCE_MAP.md when every Section 7 source/figure dependency or exact original-source route is needed
pcie-through-mi\MI_PCIE_THROUGH_COMMAND_TABLE.md for PCIe-through-MI opcode and optional-support lookup
pcie-through-mi\command-format-reference.md for the common PCIe Command request/response wrapper
pcie-through-mi\field-reference.md for LENGTH, BAR, OFFSET, Request Data, and Response Data rules
pcie-through-mi\status-and-restrictions-reference.md for PEL, range checks, Access Denied, or PCIe Inaccessible
MI_STATUS_AND_ERROR_REFERENCE.md
MI_INBAND_OUTOFBAND_BOUNDARY.md
original source section only when exact wording or delegated external-spec wording must be re-audited
```

Use this layer when a question involves:

- NVMe-MI message fields.
- MI Message Header, request/response selector, command-family selector, Command Slot Identifier, or transport message-correlation boundary.
- out-of-band SMBus/I2C or MCTP transport.
- in-band tunneling through NVMe-MI Send / Receive.
- Management Interface Command Set commands.
- MI command opcode/support, command-control fields, payload direction, and response status.
- NVMe Admin commands through MI.
- PCIe commands through MI.
- management endpoint behavior, VPD, enclosure, reset, or security.

Use `admin-through-mi\` for out-of-band Admin-through-MI support, wrapper fields, and status boundary. Use Base Spec 2.0 admin command folders for Base-side `NVMe-MI Send` / `NVMe-MI Receive` opcode boundary and for the tunneled Admin command's own CDW, payload, and status semantics.

Use `pcie-through-mi\` for the out-of-band PCIe Command Set wrapper, opcode, `CTLID`, `LENGTH`, BAR, `OFFSET`, data, status, and restriction rules. Route from that folder to `pcie-transport-1.0` only when the selected PCIe register, capability, BAR content, controller property, or transport behavior must be interpreted.
