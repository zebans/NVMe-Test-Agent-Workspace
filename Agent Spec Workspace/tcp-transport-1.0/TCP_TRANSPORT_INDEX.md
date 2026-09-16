# TCP Transport Index

Status: `SOURCE-INDEX-COMPLETE`

Primary source:

```text
..\NVMe Base Spec\2.0\NVM-Express-TCP-Transport-Specification-2021.06.02-Ratified-1.md
```

## Source Map

| Topic | Source section / figure |
|---|---|
| Overview | Section 1.1 |
| Scope and precedence | Section 1.2 |
| Definitions | Section 1.4 |
| References | Section 1.5 |
| Acronyms | Section 1.6 |
| Transport overview | Section 2 |
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
| Figure 2 | NVMe/TCP Acronym Descriptions |
| Figure 3 | NVMe/TCP PDU Structure |
| Figure 4 | NVMe/TCP PDU Header |
| Figure 5 | Multiple NVMe/TCP PDUs in a Single TCP/IP Packet |
| Figure 6 | NVMe/TCP PDU Spanning across TCP/IP Packets |
| Figure 7 | NVMe/TCP Queue Establishment Sequence |
| Figure 8 | Example of 64B PDU DATA Alignment in H2CData PDU |
| Figure 9 | Example of 64B PDU DATA Alignment in C2HData PDU |
| Figure 10 | NVMe/TCP PDU Types |
| Figure 11 | NVMe/TCP Capsule Size |
| Figure 12 | Host to Controller NVMe/TCP PDU Digests |
| Figure 13 | Controller to Host NVMe/TCP PDU Digests |
| Figure 14 | Command Data Buffer Transport SGL Data Block Descriptor |
| Figure 15 | Controller to Host Data Transfer Example |
| Figure 16 | Host to Controller Data Transfer Example |
| Figure 17 | Transport Specific Address Subtype Definition for NVMe/TCP Transport |
| Figure 18 | `{TLS PSK, TLS Identity, Hash}` Tuple Derivation |
| Figure 19 | PDU Common Header |
| Figure 20 | Initialize Connection Request PDU |
| Figure 21 | Initialize Connection Response PDU |
| Figure 22 | Host to Controller Terminate Connection Request PDU |
| Figure 23 | Controller to Host Terminate Connection Request PDU |
| Figure 24 | Command Capsule PDU |
| Figure 25 | Response Capsule PDU |
| Figure 26 | Host to Controller Data Transfer PDU |
| Figure 27 | Controller to Host Data Transfer PDU |
| Figure 28 | Ready to Transfer PDU |

## Boundary

Use `fabrics-base-2.0` for Base-owned `OPC=7Fh` and `FCTYPE` command identity.

Use this layer for TCP-specific transport mapping, PDU formats, and transport-specific content.

