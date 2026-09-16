# Namespace Management Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `NSID` | Namespace Identifier | Namespace selection. | Create: cleared to `0h`; Delete: target namespace; `FFFFFFFFh` means all namespaces. | Create/delete scope. |
| `DPTR` | Data Pointer | Start of create data buffer. | Used for Create; no data structure transferred for Delete. | Create field input. |
| `CDW10 bits 3:0` | `SEL` | Namespace Management operation. | `0h` Create, `1h` Delete, `2h`-`Fh` reserved. | Operation selection. |
| `CDW11 bits 31:24` | `CSI` | Command Set Identifier. | For Create only; reserved for other operations. | Command-set-specific namespace creation. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

## Create Data Structure Fields

| Bytes | Content | Meaning | Ownership |
|---:|---|---|---|
| `383:00` | Identify Namespace fields set by host software. | Base/common namespace create input. Reserved fields shall be cleared to `0h`. | Base plus applicable command-set rules. |
| `511:384` | I/O Command Set specific. | Command-set-specific namespace create parameters. | Applicable I/O Command Set spec. |
| `1023:512` | Reserved. | Reserved. | Base. |
| `4095:1024` | Vendor specific. | Vendor-specific create input. | Vendor. |

## Cross-Reference Fields

| Field | Where it is usually read | Why it matters |
|---|---|---|
| `TNVMCAP` / `UNVMCAP` | Identify Controller | Capacity available for namespace creation. |
| `ANAGRPID` | Create data / Identify Controller ANA fields | Invalid or unsupported ANA Group ID can fail Create. |
| `CSI` | Command-set index and Identify | Determines command-set-specific create structure ownership. |
