# Directive Receive Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Number of Dwords | `CDW10.NUMD` bits 31:00 | Number of dwords to transfer, encoded as zero-based. |
| Directive Specific | `CDW11.DSPEC` bits 31:16 | Interpretation depends on Directive Type. |
| Directive Type | `CDW11.DTYPE` bits 15:08 | Selects Directive Type; list is owned by section 8.7. |
| Directive Operation | `CDW11.DOPER` bits 07:00 | Selects operation to perform; interpretation depends on Directive Type. |

## Directive Type Dispatch

| `DTYPE` | Directive type | I/O command directive | Meaning | Test/FW rule |
|---:|---|---|---|---|
| `00h` | Identify Directive | No | Reports supported directive types and enabled directive types. | Shall be supported when Directives are supported. |
| `01h` | Streams Directive | Yes | Reports stream capabilities, open streams, and resource allocation result. | Optional; discover through Identify Directive before use. |
| `02h`-`0Fh` | Reserved for I/O command directive field use | Reserved | No Base-defined meaning. | Do not invent directive behavior. |

## Directive Receive Operations

| `DTYPE` | `DOPER` | Operation | Uses `DSPEC` | Uses `CDW12` / `CDW13` | Data transfer | Notes |
|---:|---:|---|---|---|---|---|
| `00h` | `01h` | Return Parameters | No | No | Controller to host | Returns supported and enabled directive bit vectors; `NSID=FFFFFFFFh` is invalid. |
| `00h` | Other | Reserved | n/a | n/a | n/a | Invalid Field in Command. |
| `01h` | `01h` | Return Parameters | No | No | Controller to host | Returns Streams capability and namespace/host stream resource fields. |
| `01h` | `02h` | Get Status | No | No | Controller to host | Returns open stream count and stream identifier list. |
| `01h` | `03h` | Allocate Resources | No | `CDW12.NSR` requests namespace streams. | CQE Dword 0 returns allocation; no data buffer | Allocated value may be less than or equal to requested. |
| `01h` | Other | Reserved | n/a | n/a | n/a | Invalid Field in Command. |
