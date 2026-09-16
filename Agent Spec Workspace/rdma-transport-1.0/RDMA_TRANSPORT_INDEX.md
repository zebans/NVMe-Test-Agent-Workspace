# RDMA Transport Index

Status: `SOURCE-INDEX-COMPLETE`

Primary source:

```text
..\NVMe Base Spec\2.0\NVM-Express-RDMA-Transport-Specification-2021.06.02-Ratified-1.md
```

## Source Map

| Topic | Source section / figure |
|---|---|
| Overview | Section 1.1 |
| Scope and precedence | Section 1.2 |
| Definitions | Section 1.4 |
| References | Section 1.5 |
| Transport overview | Section 2 |
| RDMA command list | Section 2.1 |
| Setup and initialization | Section 3.1 |
| Queue model instantiation | Section 3.2 |
| Data transfer model | Section 3.3 |
| Keep alive model | Section 3.4 |
| Error handling model | Section 3.5 |
| Transport specific content | Section 3.6 |

## Figure Map

| Figure | Topic |
|---|---|
| Figure 1 | NVMe Family of Specifications |
| Figure 2 | RDMA Transport Protocol Layers |
| Figure 3 | Transport Specific Address Subtype Definition for RDMA Transport |
| Figure 4 | RDMA Transport Discovery Log Page Entry Usage by `RDMA_CMS` |
| Figure 5 | `RDMA_CM_REQUEST` Private Data Format |
| Figure 6 | `RDMA_CM_ACCEPT` Private Data Format |
| Figure 7 | `RDMA_CM_REJECT` Private Data Format |
| Figure 8 | Command Sequence Using RDMA Operations |
| Figure 9 | RDMA Capsule Size and SGL Mapping |
| Figure 10 | SGL Sub Types Specific to RDMA |
| Figure 11 | RDMA Transport Errors |

## Boundary

Use `fabrics-base-2.0` for Base-owned `OPC=7Fh` and `FCTYPE` command identity.

Use this layer for RDMA-specific transport mapping and transport-specific content.

