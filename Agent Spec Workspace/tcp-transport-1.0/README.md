# NVMe TCP Transport 1.0 Layer

Status: `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE`

This folder records the local TCP Transport Specification source as an independent spec layer.

Primary source:

```text
..\NVMe Base Spec\2.0\NVM-Express-TCP-Transport-Specification-2021.06.02-Ratified-1.md
```

Version signal:

```text
NVM Express TCP Transport Specification, Revision 1.0
May 18th, 2021
```

## File Index

| File | Purpose |
|---|---|
| `TCP_TRANSPORT_INDEX.md` | Section and figure map for token-efficient reading. |
| `TCP_TRANSPORT_AGENTS.md` | Agent rules for using this transport layer. |
| `COMMAND_CONTENT_AUDIT.md` | Current coverage and remaining expansion boundaries. |

## Scope

This transport specification maps NVMe Base Specification extensions to the TCP transport. It owns TCP-specific setup, queue establishment, data transfer, keep alive, error handling, transport-specific content, PDU formats, and TCP-specific security material.

Use this layer when the question is about TCP transport behavior rather than Base Fabrics command identity.

