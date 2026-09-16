# NVM Get LBA Status Selector Reference

## Action Type (`ATYPE`)

| `ATYPE` | Action | Returned LBA classes | Controller behavior | Test/FW interpretation |
|---:|---|---|---|---|
| `10h` | Perform scan and return Untracked LBAs and Tracked LBAs in range. | Untracked + Tracked | Controller scans internal LBA-related data structures. Significant delay may occur. Successfully rewritten LBAs are removed from relevant internal structures before reporting, unless newly detected again. | Use when host wants the controller to actively discover affected LBAs for the range. |
| `11h` | Return Tracked LBAs in range. | Tracked only | No foreground scan for Untracked LBAs. Successfully rewritten LBAs are removed from relevant internal structures before reporting, unless newly detected again. | Use when host wants known tracked results without scan latency. |
| Other | Reserved | None defined | Reserved selector value. | Invalid-field negative test candidate. |

## Range Selector

| Field | Meaning | Rule |
|---|---|---|
| `SLBA` | First LBA in range. | `CDW10` contains bits `31:00`; `CDW11` contains bits `63:32`. |
| `RL` | Range Length. | `0h` means from `SLBA` through `NSZE - 1`; otherwise the contiguous range length is encoded by the field. |
| `MNDW` | Maximum dwords returned. | If the returned descriptor list hits `MNDW`, `CMPC=1h` indicates there may be more descriptor entries in the specified range. |

## Log Page To Command Selector Path

| LBA Status Information log field | How it feeds Get LBA Status |
|---|---|
| `NEID` | Use as Get LBA Status `NSID`. |
| `RATYPE` | Use as Get LBA Status `ATYPE`. |
| LBA Range Descriptor `RSLBA` | Use as Get LBA Status `SLBA`. |
| LBA Range Descriptor `RNLB` | Use as Get LBA Status range length input. |
| `NLRD=FFFFFFFFh` | No range descriptors are present and host should examine all LBAs in the namespace. |
