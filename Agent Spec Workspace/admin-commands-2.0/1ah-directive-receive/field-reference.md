# Directive Receive Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `NSID` | Namespace Identifier | Namespace scope for directive operation. | `FFFFFFFFh` support depends on Directive Operation. | Scope of directive behavior. |
| `DPTR` | Data Pointer | Start of controller-to-host data buffer. | Buffer format depends on `DTYPE`/`DOPER`. | Directive payload return. |
| `CDW10` bits 31:00 | `NUMD` | Number of dwords to transfer. | Zero-based. | Transfer length and truncation behavior. |
| `CDW11` bits 31:16 | `DSPEC` | Directive Specific. | Directive Type dependent. | Directive-specific selector. |
| `CDW11` bits 15:08 | `DTYPE` | Directive Type. | Defined in section 8.7. | Directive family selection. |
| `CDW11` bits 07:00 | `DOPER` | Directive Operation. | Directive Type dependent. | Directive action selection. |
| `CDW12`, `CDW13` | Type/operation-specific | May be used based on `DTYPE` and `DOPER`. | Section 8.7 owns interpretation. | Directive-specific behavior. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

