# Zone Management Receive Selector Reference

## Zone Receive Action (`ZRA`)

| `ZRA` | Action | Result |
|---:|---|---|
| `00h` | Report Zones | Returns the Report Zones data structure. |
| `01h` | Extended Report Zones | Returns the Extended Report Zones data structure. |
| `02h`-`FFh` | Reserved | Reserved selector; should not be assumed valid. |

Extended Report Zones is supported only if the zoned namespace is formatted with a non-zero Zone Descriptor Extension Size. Otherwise, the controller shall abort with Invalid Field in Command.

## Reporting Options

For Report Zones and Extended Report Zones:

| Value | Meaning |
|---:|---|
| `0h` | List all zones. |
| `1h` | List zones in `ZSE:Empty`. |
| `2h` | List zones in `ZSIO:Implicitly Opened`. |
| `3h` | List zones in `ZSEO:Explicitly Opened`. |
| `4h` | List zones in `ZSC:Closed`. |
| `5h` | List zones in `ZSF:Full`. |
| `6h` | List zones in `ZSRO:Read Only`. |
| `7h` | List zones in `ZSO:Offline`. |
| `8h` | Reserved. |
| `9h` | List zones with Reset Zone Recommended, Finish Zone Recommended, or Zone Finished by Controller set. |
| `10h`-`3Fh` | Reserved. |

All other values are reserved.

## Partial Report

| Partial Report | Number of Zones means |
|---:|---|
| `0` | Number of zones matching the criteria. |
| `1` | Number of zones for which complete Zone Descriptors were transferred, or complete descriptor/extension pairs for Extended Report Zones. |

## Result Ordering

Returned Zone Descriptors shall:

- include only zones whose `ZSLBA` is greater than or equal to the `ZSLBA` of the zone specified by command `SLBA`;
- match the criteria in the Zone Receive Action Specific field;
- be sorted in ascending order by each zone's `ZSLBA`.
