# NVM Get LBA Status Field Reference

Source: NVM Command Set 1.0 section 4.2.1, Figures 107-112.

## Command Fields

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `NSID` | Namespace Identifier | Namespace to examine. | `FFFFFFFFh` is not supported by the Base opcode boundary for Get LBA Status. | Namespace scope. |
| `DPTR` bits `127:00` | Data Pointer | Start of controller-to-host data buffer. | Uses Common Command Format data pointer rules. | Returned LBA Status Descriptor List location. |
| `CDW10` bits `31:00` | `SLBA[31:00]` | Low dword of Starting LBA. | Combined with `CDW11`. | Start of examined LBA range. |
| `CDW11` bits `31:00` | `SLBA[63:32]` | High dword of Starting LBA. | Combined with `CDW10`. | Start of examined LBA range. |
| `CDW12` bits `31:00` | `MNDW` | Maximum Number of Dwords to return. | Zero-based value. Actual returned amount is indicated by `NLSD`. | Buffer sizing and partial result behavior. |
| `CDW13` bits `31:24` | `ATYPE` | Action Type. | `10h` scan and return Untracked plus Tracked LBAs; `11h` return Tracked LBAs; all others reserved. | Report mechanism and delay expectation. |
| `CDW13` bits `23:16` | Reserved | No NVM-defined meaning. | Host should clear. | Invalid-field testing. |
| `CDW13` bits `15:00` | `RL` | Range Length. | Number of contiguous LBAs beginning at `SLBA`; `0h` means through `NSZE - 1`. | Examined range length. |
| Other command-specific fields | Reserved | No NVM-defined meaning. | Host should clear. | Invalid-field testing. |

## Returned Descriptor List Fields

| Offset | Field | Meaning | Important values / rules | Affects |
|---:|---|---|---|---|
| `03:00` | `NLSD` | Number of LBA Status Descriptor entries returned. | `0h` is valid and means no entries returned. | Parser loop bound. |
| `04` | `CMPC` | Completion Condition. | `0h` no indication; `1h` completed due to `MNDW` transfer limit; `2h` completed because action covered the requested range. | Whether host should continue querying same range. |
| `07:05` | Reserved | No NVM-defined meaning. | Reserved in returned structure. | Parser should ignore. |
| `23:08` onward | LBA Status Descriptor Entries | 16-byte entries, if present. | Entry count is `NLSD`. | Potentially unrecoverable LBA range list. |

## LBA Status Descriptor Entry

| Offset within entry | Field | Meaning | Important values / rules | Affects |
|---:|---|---|---|---|
| `07:00` | `DSLBA` | Descriptor Starting LBA. | First entry starts at the lowest LBA >= command `SLBA` that matches `ATYPE`; later entries are ordered after previous `DSLBA + NLB`. | Recovery target range. |
| `11:08` | `NLB` | Number of Logical Blocks. | Zero-based value; controller should return the largest aggregated possible value. | Range length for recovery/read-risk handling. |
| `12` | Reserved | No NVM-defined meaning. | Reserved. | Parser should ignore. |
| `13` bit `1` | Write Uncorrectable indication | Set means the range describes LBAs written with Write Uncorrectable. | Clear means it may or may not describe Write Uncorrectable LBAs. | Distinguishes explicit Write Uncorrectable surface. |
| `13` bit `0` | Unrecovered read risk | Set means Copy, Read, Verify, or Compare to each reported LBA may complete with Unrecovered Read Error. | Clear means controller has not detected that each LBA may cause that completion. | Expected read/verify/compare failure risk. |
| `13` bits `7:2` | Reserved | No NVM-defined meaning. | Reserved. | Parser should ignore. |
| `15:14` | Reserved | No NVM-defined meaning. | Reserved. | Parser should ignore. |
