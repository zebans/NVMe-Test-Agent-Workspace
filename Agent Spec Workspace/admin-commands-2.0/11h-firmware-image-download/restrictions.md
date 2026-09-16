# Firmware Image Download Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| `NUMD` and `OFST` should meet `FWUG` | Transfer size and offset follow firmware update granularity. | `Invalid Field in Command` or download failure. |
| Ranges should not overlap | Host should avoid overlapping dword ranges. | `Overlapping Range`. |
| Firmware Commit required after download | Download does not activate or commit the image. | Image remains pending until Firmware Commit. |
| Boot Partition portions shall be ordered | Boot Partition update sequence is stricter than firmware image pieces. | Sequence may fail or produce invalid update behavior. |
| Reset before Firmware Commit completion discards downloaded portions | Downloaded image portions are not retained through that reset condition. | Host must redownload after reset. |

