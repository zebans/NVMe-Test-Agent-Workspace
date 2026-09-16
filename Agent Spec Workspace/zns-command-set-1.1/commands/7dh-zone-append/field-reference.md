# Zone Append Field Reference

Source: ZNS Figures 22-29.

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `MPTR` | Metadata Pointer | Metadata buffer, if applicable. | Base common command format. | Metadata transfer. |
| `DPTR` | Data Pointer | Host-to-controller data buffer. | Base common command format. | Data transfer. |
| `CDW2-3 bits 47:0` | `LBST` / `ILBRT` portion | Storage/reference tag fields with `CDW14`. | Ignored if namespace is not formatted for end-to-end PI. | PI behavior. |
| `CDW10-11` | `ZSLBA` | Lowest LBA of target zone. | Identifies zone, not final write LBA. | Target zone selection. |
| `CDW12 bit 31` | `LR` | Limited Retry. | NVM-owned. | Retry behavior. |
| `CDW12 bit 30` | `FUA` | Force Unit Access. | NVM-owned. | Persistence behavior. |
| `CDW12 bits 29:26` | `PRINFO` | Protection Information field. | NVM-owned baseline. | PI checks. |
| `CDW12 bit 25` | `PIREMAP` | Protection Information Remap. | ZNS-specific remap behavior. | Reference tag handling. |
| `CDW12 bit 24` | `STC` | Storage Tag Check. | NVM-owned. | PI checks. |
| `CDW12 bits 23:20` | `DTYPE` | Directive Type. | NVM-owned. | Directive behavior. |
| `CDW12 bits 15:0` | `NLB` | Number of logical blocks, zero-based. | Range shall not cross zone boundary. | Transfer length / status. |
| `CDW13 bits 31:16` | `DSPEC` | Directive Specific. | NVM-owned. | Directive behavior. |
| `CDW14` | `LBST` / `ILBRT` portion | Storage/reference tag fields with `CDW2-3`. | Ignored if no end-to-end PI format is used. | PI behavior. |
| `CDW15 bits 31:16` | `LBATM` | Logical Block Application Tag Mask. | NVM-owned. | PI behavior. |
| `CDW15 bits 15:0` | `LBAT` | Logical Block Application Tag. | NVM-owned. | PI behavior. |

## Completion Fields

| CQE location | Field | Meaning | Affects |
|---|---|---|---|
| Dword 0 | `ALBA[31:00]` | Lower 32 bits of assigned lowest LBA. | Host learns actual write location. |
| Dword 1 | `ALBA[63:32]` | Upper 32 bits of assigned lowest LBA. | Host learns actual write location. |
