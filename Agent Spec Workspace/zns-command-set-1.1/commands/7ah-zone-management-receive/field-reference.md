# Zone Management Receive Field Reference

Source: ZNS Figures 31-34 and Figure 37.

Naming note: ZNS 1.1 Figure 33 names CDW12 **Number of Dwords** but does not assign the acronym `NUMD`. This folder uses `NUMD` only as a local lookup alias.

## Command Fields

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data pointer | Controller-to-host result buffer. | Holds Report Zones or Extended Report Zones data. | Payload placement and transfer length. |
| `CDW10-11` | `SLBA` | LBA in the lowest numbered zone that the action operates on. | Results include zones with `ZSLBA` greater than or equal to this zone's `ZSLBA`. | Report start point. |
| `CDW12` | `NUMD` | Number of dwords to return, zero-based. | Controls transfer size. | Partial buffer / truncation behavior. |
| `CDW13 bit 16` | Partial Report | Changes meaning of Number of Zones. | `0` matching zones; `1` fully transferred entries. | Report count interpretation. |
| `CDW13 bits 15:8` | Zone Receive Action Specific Field | Reporting Options for Report Zones / Extended Report Zones. | Filters by zone state or advisory attributes. | Which zones appear in report. |
| `CDW13 bits 7:0` | `ZRA` | Zone Receive Action. | Report Zones or Extended Report Zones. | Payload structure. |

## Zone Descriptor Fields

| Bytes | Field | Meaning | Important values / rules | Affects |
|---:|---|---|---|---|
| `00` | Zone Type (`ZT`) | Zone type. | `2h` means Sequential Write Required; other values reserved. | Determines write model. |
| `01` | Zone State (`ZS`) | Current zone state. | Empty, Implicitly Opened, Explicitly Opened, Closed, Read Only, Full, Offline. | Valid command behavior and status. |
| `02` | Zone Attributes (`ZA`) | Zone advisory/extension attributes. | Includes `ZDEV`, `RZR`, `FZR`, `ZFC`. | Extension and advisory handling. |
| `03` | Zone Attributes Information (`ZAI`) | Attribute information. | Includes `RZRTL` and `FZRTL`. | Advisory timing interpretation. |
| `07:04` | Reserved | Reserved. | No command-specific meaning. | Ignore unless validating reserved bytes. |
| `15:08` | Zone Capacity (`ZCAP`) | Maximum logical blocks available for user data when Empty. | May be less than zone size. | Write-range capacity checks. |
| `23:16` | Zone Start Logical Block Address (`ZSLBA`) | Lowest LBA for the zone. | Sort key for returned descriptors. | Zone addressing. |
| `31:24` | Write Pointer (`WP`) | LBA where next write operation should be issued. | Important for Sequential Write Required zones. | Write / append validation. |
| `63:32` | Reserved | Reserved. | No command-specific meaning. | Ignore unless validating reserved bytes. |
