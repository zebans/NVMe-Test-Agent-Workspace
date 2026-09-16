# Zone Management Receive Payload Reference

Source: ZNS section 3.4.2.2, Figures 35-37.

## Report Zones Data Structure

| Bytes | Field | Meaning |
|---:|---|---|
| `07:00` | Number of Zones | Count meaning depends on Partial Report. |
| `63:08` | Reserved | Reserved. |
| `127:64` | Zone Descriptor 0, if any | First returned Zone Descriptor. |
| `191:128` | Zone Descriptor 1, if any | Second returned Zone Descriptor. |
| `((n+1)*64)+63 : (n+1)*64` | Zone Descriptor n, if any | Nth returned Zone Descriptor. |

## Extended Report Zones Data Structure

The Extended Report Zones structure contains:

- Number of Zones;
- reserved bytes;
- Zone Descriptor and Zone Descriptor Extension pairs.

`ZDES` corresponds to the formatted Zone Descriptor Extension Size in bytes, equal to the field value multiplied by 64.

## Number of Zones Meaning

| Partial Report | Report Zones | Extended Report Zones |
|---:|---|---|
| `0` | Number of zones matching the criteria. | Number of zones matching the criteria. |
| `1` | Number of zones for which complete Zone Descriptors were transferred. | Number of zones for which complete Zone Descriptors and complete Zone Descriptor Extensions were transferred. |

## Zone State Values

| Value | State |
|---:|---|
| `1h` | Empty |
| `2h` | Implicitly Opened |
| `3h` | Explicitly Opened |
| `4h` | Closed |
| `Dh` | Read Only |
| `Eh` | Full |
| `Fh` | Offline |

Other values shown as reserved in the source remain reserved.

## Zone Descriptor High-Value Fields

| Field | Why tests and FW care |
|---|---|
| `ZT` | Confirms Sequential Write Required zone behavior. |
| `ZS` | Determines valid ZNS command behavior and expected status values. |
| `ZA` | Exposes Zone Descriptor Extension Valid and recommendation attributes. |
| `ZCAP` | Defines writable user-data capacity for the zone. |
| `ZSLBA` | Identifies the zone and sorts report entries. |
| `WP` | Drives write pointer validation for write-like commands. |
