# NVM Compare Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `MPTR` | Metadata Pointer | Metadata pointer if applicable. | Metadata is compared excluding PI. | Metadata comparison. |
| `DPTR` | Data Pointer | Host comparison data buffer. | PRP or SGL according to command format. | Compare data source. |
| `CDW2:3` bits `47:00` | `ELBST` / `EILBRT` portion | Expected storage/reference tag for PI. | Ignored if namespace is not formatted for PI. | PI checking. |
| `CDW10:11` | `SLBA` | Starting LBA. | 64-bit value; CDW10 low, CDW11 high. | Target range. |
| `CDW12` bit `31` | `LR` | Limited Retry. | Set: limited retry; clear: all available recovery means. | Error recovery effort. |
| `CDW12` bit `30` | `FUA` | Force Unit Access. | Set: commit then read from non-volatile media for compare. | Cache behavior. |
| `CDW12` bits `29:26` | `PRINFO` | Protection Information action/check. | `PRACT` shall be cleared; `PRCHK` non-zero performs checks. | PI behavior. |
| `CDW12` bit `24` | `STC` | Storage Tag Check. | Checks Storage Tag as part of PI processing. | PI validation. |
| `CDW12` bits `15:00` | `NLB` | Number of logical blocks. | Zero-based. | Compare range size. |
| `CDW14` | PI tag continuation | Additional `ELBST` / `EILBRT` bits. | Ignored if namespace is not formatted for PI. | PI checking. |
| `CDW15` bits `31:16` | `ELBATM` | Expected Application Tag Mask. | Ignored if namespace is not formatted for PI. | PI Application Tag check. |
| `CDW15` bits `15:00` | `ELBAT` | Expected Application Tag. | Ignored if namespace is not formatted for PI. | PI Application Tag value. |
