# Directive Send Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Number of Dwords | `CDW10.NUMD` bits 31:00 | Number of dwords to transfer, encoded as zero-based. |
| Directive Specific | `CDW11.DSPEC` bits 31:16 | Interpretation depends on Directive Type. |
| Directive Type | `CDW11.DTYPE` bits 15:08 | Selects Directive Type; list is owned by section 8.7. |
| Directive Operation | `CDW11.DOPER` bits 07:00 | Selects operation to perform; interpretation depends on Directive Type. |

## Directive Type Dispatch

| `DTYPE` | Directive type | I/O command directive | Meaning | Test/FW rule |
|---:|---|---|---|---|
| `00h` | Identify Directive | No | Determine directive support and enable/disable supported directives. | Shall be supported when Directives are supported. |
| `01h` | Streams Directive | Yes | Associate write data with stream identifiers and manage stream resources. | Optional; must be discovered through Identify Directive Return Parameters before use. |
| `02h`-`0Fh` | Reserved for I/O command directive field use | Reserved | No Base-defined meaning. | Do not invent stream-like behavior. |

## Directive Send Operations

| `DTYPE` | `DOPER` | Operation | Uses `DSPEC` | Uses `CDW12` / `CDW13` | Data transfer | Notes |
|---:|---:|---|---|---|---|---|
| `00h` | `01h` | Enable Directive | No | `CDW12` carries target `DTYPE` and `ENDIR`. | No data transfer | `CDW12.DTYPE=00h` is invalid; enabling unsupported directive is invalid. |
| `00h` | Other | Reserved | n/a | n/a | n/a | Invalid Field in Command. |
| `01h` | `01h` | Release Identifier | Yes, Stream Identifier | No | No data transfer | Releases the stream identifier for the specified namespace; `NSID=FFFFFFFFh` is invalid. |
| `01h` | `02h` | Release Resources | No | No | No data transfer | Releases all exclusive stream resources for the namespace; no-op success if none allocated. |
| `01h` | Other | Reserved | n/a | n/a | n/a | Invalid Field in Command. |
