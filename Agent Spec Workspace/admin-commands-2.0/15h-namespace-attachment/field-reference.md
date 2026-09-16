# Namespace Attachment Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `NSID` | Namespace Identifier | Namespace to attach or detach. | Shall identify the namespace for the operation. | Attachment target. |
| `DPTR` | Data Pointer | Start of 4096-byte Controller List. | If PRPs are used, buffer shall not be a PRP List and may not cross more than one page boundary. | Controller list input. |
| `CDW10 bits 3:0` | `SEL` | Namespace Attachment operation. | `0h` Attach, `1h` Detach, `2h`-`Fh` reserved. | Operation selection. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

## Controller List Fields

| Region | Field | Meaning | Affects |
|---|---|---|---|
| Controller List header / count | Number of controller identifiers. | Determines how many controller entries are processed. | Controller-list validation. |
| Controller Identifier entries | Controller IDs to attach/detach. | Each entry identifies a target controller. | Attach/detach operation and first-failure reporting. |

## Cross-Reference Fields

| Field | Where it is usually read | Why it matters |
|---|---|---|
| `MAXDNA` | Identify Controller | Maximum Domain Namespace Attachments. |
| `MAXCNA` | Identify Controller | Maximum I/O Controller Namespace Attachments. |
| `NMIC` | Identify Namespace | Namespace sharing/private capability. |
| I/O Command Set support | Identify / command-set profile | Required for attaching namespace to a controller. |
