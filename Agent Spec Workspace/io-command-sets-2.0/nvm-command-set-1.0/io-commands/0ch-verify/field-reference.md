# NVM Verify Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW2:3` bits `47:00` | `ELBST` / `EILBRT` portion | Expected storage/reference tag for PI. | Ignored if namespace is not formatted for PI. | PI checking. |
| `CDW10:11` | `SLBA` | Starting LBA. | 64-bit value; CDW10 low, CDW11 high. | Target range. |
| `CDW12` bit `31` | `LR` | Limited Retry. | Same effect as in Read. | Error recovery effort. |
| `CDW12` bit `30` | `FUA` | Force Unit Access. | Flush volatile cache for range before verifying committed media. | Cache/media source behavior. |
| `CDW12` bits `29:26` | `PRINFO` | Protection Information action/check. | `PRACT` shall be cleared; `PRCHK` selects checks. | PI behavior. |
| `CDW12` bit `24` | `STC` | Storage Tag Check. | Checks Storage Tag as part of Verify. | PI validation. |
| `CDW12` bits `15:00` | `NLB` | Number of logical blocks. | Zero-based. | Verify range size. |
| `CDW14` | PI tag continuation | Additional `ELBST` / `EILBRT` bits. | Ignored if namespace is not formatted for PI. | PI checking. |
| `CDW15` bits `31:16` | `ELBATM` | Expected Application Tag Mask. | Ignored if namespace is not formatted for PI. | PI Application Tag check. |
| `CDW15` bits `15:00` | `ELBAT` | Expected Application Tag. | Ignored if namespace is not formatted for PI. | PI Application Tag value. |
