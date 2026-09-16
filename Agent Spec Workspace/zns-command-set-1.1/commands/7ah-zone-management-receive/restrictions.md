# Zone Management Receive Restrictions

Source: ZNS section 3.4.2.

## Action Restrictions

- `ZRA=00h` selects Report Zones.
- `ZRA=01h` selects Extended Report Zones.
- `ZRA=01h` requires a non-zero Zone Descriptor Extension Size for the formatted zoned namespace.
- `ZRA=02h` through `FFh` are reserved.

## Result Ordering

Report Zones and Extended Report Zones results are sorted in ascending order by `ZSLBA`.

## Partial Report

Partial Report changes the meaning of Number of Zones:

- cleared: Number of Zones means matching zones;
- set: Number of Zones means fully transferred descriptors, or fully transferred descriptor/extension pairs for Extended Report Zones.

## Data Size

If host software requests more dwords than the Zone Receive Action data structure returns, the controller returns the complete result and dwords beyond the data structure end are undefined.
