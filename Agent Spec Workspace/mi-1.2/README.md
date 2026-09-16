# NVMe Management Interface 1.2 Layer

Status: `FRAMEWORK-COMPLETE`

This folder records the local NVM Express Management Interface Revision 1.2 source as an independent MI layer.

Primary source:

```text
..\..\NVMe Base Spec\2.0\NVMe\NVM-Express-Management-Interface-1.2-2021.06.02-Ratified.md
```

Version signal:

```text
NVM Express Management Interface Revision 1.2
June 2, 2021
```

## File Index

| File | Purpose |
|---|---|
| `MI_AGENTS.md` | Agent rules for using this MI layer. |
| `MI_SOURCE_INDEX.md` | Section and figure map for token-efficient reading. |
| `MI_COMMAND_SET_INDEX.md` | Management Interface Command Set command index. |
| `MI_COMMAND_REFERENCE.md` | Opcode, support, field, payload, and command-control reference. |
| `MI_MESSAGE_HEADER_REFERENCE.md` | Shared four-byte MI header, request/response type, `NMIMT`, `CSI`, `CIAP`, `MEB`, message-correlation boundary, and MIC reference. |
| `MI_STATUS_AND_ERROR_REFERENCE.md` | Response Message Status and common error mapping reference. |
| `MI_INBAND_OUTOFBAND_BOUNDARY.md` | Out-of-band and in-band tunneling boundary map. |
| `admin-through-mi\README.md` | Out-of-band NVMe Admin Command Set through MI command support, wrapper fields, status boundary, and Base Admin routing. |
| `pcie-through-mi\README.md` | Out-of-band PCIe Command Set through MI opcode, wrapper, field, status, restriction, and PCIe transport routing. |
| `COMMAND_CONTENT_AUDIT.md` | Coverage status and remaining expansion boundaries. |

## Scope

This layer owns NVMe-MI behavior:

- NVMe-MI messages and message transport.
- out-of-band message servicing.
- in-band tunneling via NVMe-MI Send and NVMe-MI Receive.
- Management Interface Command Set.
- NVMe Admin Command Set tunneling through MI.
- optional PCIe Command Set through MI.
- management architecture, VPD, reset, security, and enclosure-related structures.

Base Spec 2.0 Admin commands `NVMe-MI Send` and `NVMe-MI Receive` are only the Base-side tunnel commands. Use this layer for the actual MI command/message behavior.

## Completion Definition

`FRAMEWORK-COMPLETE` means this folder captures MI source anchors, message boundaries, native MI command-control lookup, status/error lookup, and in-band/out-of-band ownership. `admin-through-mi\` is `FIELD-COMPLETE + ROUTING-COMPLETE` for NVMe Admin commands through the out-of-band MI mechanism. `pcie-through-mi\` is `FIELD-COMPLETE + ROUTING-COMPLETE` for MI section 7 PCIe Configuration, I/O, and Memory Read/Write commands.
