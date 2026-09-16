# NVM Write Zeroes Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW2:3` bits `47:00` | `LBST` / `ILBRT` portion | Storage/reference tag input for PI. | Ignored if namespace is not formatted for PI. | PI generation/check. |
| `CDW10:11` | `SLBA` | Starting LBA. | 64-bit value; CDW10 low, CDW11 high. | Target range. |
| `CDW12` bit `31` | `LR` | Limited Retry. | Set: limited retry; clear: all available recovery means. | Error recovery effort. |
| `CDW12` bit `30` | `FUA` | Force Unit Access. | Set: write data/metadata to non-volatile media before completion. | Persistence behavior. |
| `CDW12` bits `29:26` | `PRINFO` | Protection Information action/check. | `PRCHK` shall be `000b`. | PI behavior and invalid PI status. |
| `CDW12` bit `25` | `DEAC` | Deallocate request. | Set: host requests deallocation of specified logical blocks. | Deallocation behavior. |
| `CDW12` bit `24` | `STC` | Storage Tag Check. | Shall be cleared. | PI restriction. |
| `CDW12` bits `15:00` | `NLB` | Number of logical blocks. | Zero-based. | Zeroed range size. |
| `CDW14` | PI tag continuation | Additional `LBST` / `ILBRT` bits. | Ignored if namespace is not formatted for PI. | PI behavior. |
| `CDW15` bits `31:16` | `LBATM` | Application Tag Mask. | Ignored if namespace is not formatted for PI. | PI Application Tag behavior. |
| `CDW15` bits `15:00` | `LBAT` | Application Tag. | Ignored if namespace is not formatted for PI. | PI Application Tag value. |
