# Authentication Send Cross-Spec Boundary

## Owned By Fabrics Base / This Folder

| Area | Covered here |
|---|---|
| Capsule fields | `OPC`, `FCTYPE`, `SGL1`, `SPSP0`, `SPSP1`, `SECP`, `TL`. |
| Queue support | Optional command, supported on I/O Queues. |
| Send/Receive pairing boundary | Authentication Receive retrieves status/data results. |
| Base-visible status | Reserved `SECP` invalid parameter rule and Authentication Required exclusion. |

## Delegated Outside This Folder

| Area | Owner |
|---|---|
| Security protocol payload semantics | SPC-5 / selected security protocol. |
| Authentication transport details | Applicable NVMe Transport binding. |
| Transport-specific status `B0h`-`BFh` | Applicable NVMe Transport binding. |
| PyNVMe API call syntax | API layer such as `API_AGENTS.md`. |
