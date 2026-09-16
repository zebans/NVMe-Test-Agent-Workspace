# Directive Receive Payload Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | Directive-dependent data | Transferred from controller to host. |
| Completion | CQE on Admin Completion Queue | Reports command status. |

## Transfer Length Behavior

| `NUMD` relationship to returned data structure | Transfer behavior |
|---|---|
| Less than returned data structure size | Only the specified portion is transferred. |
| Greater than returned data structure size | Entire data structure is transferred and no additional data is transferred. |

The returned data structure is dependent on Directive Type. Section 8.7 owns the detailed payload format for each directive.

## Operation Payload Map

| `DTYPE` | `DOPER` | Returned payload / completion surface | High-value fields |
|---:|---:|---|---|
| `00h` | `01h` | Identify Directive Return Parameters data structure. | Directives Supported bit vector; Directives Enabled bit vector. |
| `01h` | `01h` | Streams Return Parameters data structure. | `MSL`, `NSSA`, `NSSO`, `NSSC`, `SWS`, `SGS`, `NSA`, `NSO`. |
| `01h` | `02h` | Streams Get Status data structure. | Open Stream Count, ordered Stream Identifier list. |
| `01h` | `03h` | No data buffer; CQE Dword 0 returns allocation. | CQE Dword 0 `NSA` reports Namespace Streams Allocated. |
