# NVM Get LBA Status Restrictions

## Condition To Rule Matrix

| Condition | Rule / expected behavior |
|---|---|
| `ATYPE=10h` | Controller returns Untracked and Tracked LBAs in range and may incur significant delay due to scanning. |
| `ATYPE=11h` | Controller returns Tracked LBAs in range and does not perform a foreground scan for Untracked LBAs. |
| `ATYPE` other than `10h` or `11h` | Reserved; do not assign behavior. |
| `RL=0h` | Range begins at `SLBA` and ends at `NSZE - 1`. |
| Successfully rewritten LBAs existed in the requested range before command processing | Controller removes them from relevant internal structures before reporting unless they were newly detected again before command processing. |
| `MNDW` limit stops transfer | Returned `CMPC=1h`; more descriptor entries may remain in the specified range. |
| Action covers requested range | Returned `CMPC=2h`; no more descriptor entries remain in the specified range. |
| Descriptor list returns `NLSD=0h` | Valid successful returned data structure with no descriptor entries. |

## Host Sequencing Boundaries

| Related step | Rule |
|---|---|
| Before targeted Get LBA Status | Host normally reads LBA Status Information log page `LID=0Eh` to get namespace/range/action hints. |
| Alert clearing | Reading `LID=0Eh` with `RAE=0` clears an outstanding LBA Status Information Alert and restarts the report interval. |
| Recovery | Host decides when to recover/rewrite LBAs relative to reading and clearing the log page. |
| Re-check | Host may issue Get LBA Status again after recovery to confirm rewritten LBAs are no longer tracked. |

## Do Not Infer

| Surface | Reason |
|---|---|
| Vendor-specific media recovery policy | Not defined by NVM command fields. |
| Whether every reported LBA will definitely fail a read | Descriptor status bit 0 says "may result" in Unrecovered Read Error. |
| ZNS-specific zone-state behavior | Not defined by this NVM command folder; route to ZNS layer if CSI is `02h`. |
