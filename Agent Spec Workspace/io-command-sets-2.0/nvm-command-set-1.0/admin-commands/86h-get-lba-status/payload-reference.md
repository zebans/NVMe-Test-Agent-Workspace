# NVM Get LBA Status Payload Reference

The command returns an LBA Status Descriptor List in the controller-to-host data buffer.

## Returned Data Structure

| Offset | Field | Meaning | Important values |
|---:|---|---|---|
| `03:00` | `NLSD` | Number of LBA Status Descriptor entries returned. | `0h` is valid. |
| `04` | `CMPC` | Completion Condition. | `0h`, `1h`, `2h`; all others reserved. |
| `07:05` | Reserved | Reserved bytes. | Ignore for parsing. |
| `23:08` | Descriptor Entry 0 | First 16-byte LBA Status Descriptor Entry, if present. | Present when `NLSD >= 1`. |
| `39:24` | Descriptor Entry 1 | Second descriptor entry, if present. | Present when `NLSD >= 2`. |
| `(N*16+23):(N*16+8)` | Descriptor Entry N | N+1th descriptor entry. | Present according to `NLSD`. |

## Completion Condition (`CMPC`)

| `CMPC` | Meaning | Host implication |
|---:|---|---|
| `0h` | No indication of completion condition. | Do not infer whether more entries exist from `CMPC`. |
| `1h` | Command completed due to transferring amount of data specified by `MNDW`. | There may be more LBA Status Descriptor Entries in the specified range. |
| `2h` | Command completed because the action was performed over the requested range. | There are no more LBA Status Descriptor Entries to transfer in the specified range. |
| Other | Reserved. | Do not assign meaning. |

## Descriptor Entry

| Offset within entry | Field | Meaning | Important bits |
|---:|---|---|---|
| `07:00` | `DSLBA` | First LBA of this descriptor's range. | First entry is the lowest matching LBA greater than or equal to command `SLBA`. |
| `11:08` | `NLB` | Number of contiguous logical blocks in this descriptor. | Zero-based; controller should aggregate as much as possible. |
| `12` | Reserved | Reserved. | Ignore for parsing. |
| `13` | Status | Additional status about this LBA range. | bit1 Write Uncorrectable indication; bit0 Unrecovered Read Error risk. |
| `15:14` | Reserved | Reserved. | Ignore for parsing. |

## Status Byte Bits

| Bit | Meaning when set | Meaning when clear | Test/FW use |
|---:|---|---|---|
| `1` | This range describes LBAs written with Write Uncorrectable. | Range may or may not describe Write Uncorrectable LBAs. | Helps identify explicit Write Uncorrectable source. |
| `0` | Copy, Read, Verify, or Compare to each reported LBA may complete with Unrecovered Read Error. | Controller has not detected that each reported LBA may produce that completion. | Drives recovery and negative read/verify checks. |

## Ordering Rule

For the first descriptor, `DSLBA` is the lowest numbered LBA greater than or equal to command `SLBA` that matches the selected `ATYPE`.

For subsequent descriptors, `DSLBA` is the lowest numbered matching LBA greater than the previous descriptor's `DSLBA + NLB`.
