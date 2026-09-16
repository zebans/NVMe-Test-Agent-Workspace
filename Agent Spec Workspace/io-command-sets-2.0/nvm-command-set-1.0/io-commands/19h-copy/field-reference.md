# NVM Copy Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data Pointer | Host data buffer containing Source Range Entries. | Descriptor format selected by `CDW12`. | Source payload. |
| `CDW2:3` bits `47:00` | `LBST` / `ILBRT` portion | PI tag fields for write portion. | Ignored if namespace is not formatted for PI. | Destination PI behavior. |
| `CDW10:11` | `SDLBA` | Starting Destination LBA. | 64-bit destination start. | Destination range. |
| `CDW12` bit `31` | `LR` | Limited Retry for write portion. | Set: limited retry; clear: all available recovery means. | Write effort. |
| `CDW12` bit `30` | `FUA` | Force Unit Access for write portion. | Set: write destination data/metadata to non-volatile media before completion. | Persistence behavior. |
| `CDW12` bits `29:26` | `PRINFOW` | PI action/check for write portion. | Defined by NVM Figure 9. | Destination PI behavior. |
| `CDW12` bit `24` | `STCW` | Storage Tag Check for write portion. | Checks Storage Tag for write portion. | Destination PI behavior. |
| `CDW12` bits `23:20` | `DTYPE` | Directive Type for write portion. | Base Directives model. | Directive behavior. |
| `CDW12` bits `15:12` | `PRINFOR` | PI action/check for read portion. | Applies to Source Range Entries. | Source PI behavior. |
| `CDW12` bits `11:08` | Descriptor Format | Source Range Entry format. | `0h` format 0; `1h` format 1; others reserved. | Payload layout. |
| `CDW12` bits `07:00` | `NR` | Number of Source Range Entries. | Zero-based. | Source entry count. |
| `CDW13` bits `31:16` | `DSPEC` | Directive Specific. | Interpreted with `DTYPE`. | Directive behavior. |
| `CDW14` | PI tag continuation | Additional `LBST` / `ILBRT` bits for write portion. | Ignored if namespace is not formatted for PI. | Destination PI behavior. |
| `CDW15` bits `31:16` | `LBATM` | Application Tag Mask for write portion. | Ignored if namespace is not formatted for PI. | Destination PI behavior. |
| `CDW15` bits `15:00` | `LBAT` | Application Tag for write portion. | Ignored if namespace is not formatted for PI. | Destination PI behavior. |
