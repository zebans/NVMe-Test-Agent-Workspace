# NVMe RDMA Transport 1.0 Layer

Status: `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE`

This folder records the local RDMA Transport Specification source as an independent spec layer.

Primary source:

```text
..\NVMe Base Spec\2.0\NVM-Express-RDMA-Transport-Specification-2021.06.02-Ratified-1.md
```

Version signal:

```text
NVM Express RDMA Transport Specification, Revision 1.0
May 18th, 2021
```

## File Index

| File | Purpose |
|---|---|
| `RDMA_TRANSPORT_INDEX.md` | Section and figure map for token-efficient reading. |
| `RDMA_TRANSPORT_AGENTS.md` | Agent rules for using this transport layer. |
| `COMMAND_CONTENT_AUDIT.md` | Current coverage and remaining expansion boundaries. |

## Scope

This transport specification maps NVMe Base Specification extensions to the RDMA transport. It owns RDMA-specific setup, queue instantiation, data transfer, keep alive, error handling, and transport-specific content.

Use this layer when the question is about RDMA transport behavior rather than Base Fabrics command identity.

