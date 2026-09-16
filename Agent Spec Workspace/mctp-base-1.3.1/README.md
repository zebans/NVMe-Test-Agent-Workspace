# MCTP Base 1.3.1 Layer

Status: `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED`

This folder records the local Management Component Transport Protocol Base Specification as an independent transport substrate layer.

Primary source:

```text
..\NVMe Base Spec\2.0\MCTP\MCTP-Base-Specification.md
```

Version signal:

```text
Document Identifier: DSP0236
Version: 1.3.1
```

## File Index

| File | Purpose |
|---|---|
| `MCTP_BASE_AGENTS.md` | Agent rules for using this MCTP Base layer. |
| `MCTP_BASE_INDEX.md` | Section, figure, and table map for token-efficient reading. |
| `MCTP_BASE_BEHAVIOR_REFERENCE.md` | High-value MCTP packet, message, EID, tag, routing, discovery, and control-command behavior. |
| `MCTP_COMMON_HEADER_REFERENCE.md` | Expanded MCTP common packet/message header fields from Table 1. |
| `MCTP_CONTROL_COMMAND_REFERENCE.md` | Expanded high-priority MCTP Control common fields, completion codes, and setup/discovery command payloads. |
| `MCTP_TO_NVME_MI_BOUNDARY.md` | Boundary between NVMe-MI content and MCTP transport substrate behavior. |
| `COMMAND_CONTENT_AUDIT.md` | Current coverage and remaining expansion boundaries. |

## Scope

This layer owns MCTP common behavior:

- MCTP endpoints and Endpoint IDs (`EID`).
- MCTP packets and messages.
- packet assembly with `SOM`, `EOM`, packet sequence, `TO`, and message tag.
- MCTP message type routing.
- MCTP Control Protocol command list and common completion codes.
- EID assignment, EID pools, discovery, routing tables, and bridge behavior.

This layer does not own NVMe-MI command payload semantics. If the message body is NVMe-MI, use `..\mi-1.2\README.md` for MI command/status/payload behavior and this folder only for MCTP transport framing and routing.

## Complete Definition

`PAYLOAD-COMPLETE` applies to the common MCTP header and high-priority MCTP Control commands expanded in this folder. Less common Control commands remain indexed and should be expanded on demand.
