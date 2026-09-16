# ZNS Command-Control Model

Status: `COMPLETE`

This file records ZNS model facts that affect command-control behavior across multiple ZNS commands.

Primary source:

```text
..\NVMe Base Spec\2.0\NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md
```

## Source Anchors

| Area | Source |
|---|---|
| Zone Descriptor | Figure 37 |
| I/O Command Set Specific Identify Namespace data | Figure 48 |
| LBA Format Extension | Figure 49 |
| Zone Descriptor Extension | Section 5.3 |
| Reset Zone Recommended | Section 5.4 |
| Finish Zone Recommended | Section 5.5 |
| Zone Active Excursions | Section 5.6 |

## Zone Descriptor Fields

Source: Figure 37.

| Bytes | Field | Command-control relevance |
|---|---|---|
| `00` | Zone Type (`ZT`) | `2h` means Sequential Write Required. Other values are reserved. |
| `01` | Zone State (`ZS`) | Drives valid/invalid command behavior and ZNS status values. |
| `02` | Zone Attributes (`ZA`) | Includes Zone Descriptor Extension Valid, Reset Zone Recommended, Finish Zone Recommended, and Zone Finished by Controller. |
| `03` | Zone Attributes Information (`ZAI`) | Selects Reset/Finish recommended time-limit fields. |
| `07:04` | Reserved | Reserved. |
| `15:08` | Zone Capacity (`ZCAP`) | Maximum logical blocks available for user data when the zone is Empty. |
| `23:16` | Zone Start Logical Block Address (`ZSLBA`) | Lowest LBA of the zone. |
| `31:24` | Write Pointer (`WP`) | LBA where the next write operation for the zone should be issued. |
| `63:32` | Reserved | Reserved. |

## Zone State Values

| Value | State |
|---:|---|
| `0h` | Reserved |
| `1h` | Empty |
| `2h` | Implicitly Opened |
| `3h` | Explicitly Opened |
| `4h` | Closed |
| `5h`-`Ch` | Reserved |
| `Dh` | Read Only |
| `Eh` | Full |
| `Fh` | Offline |

## Identify Namespace Fields That Affect Commands

Source: Figure 48.

| Field | Bytes | Meaning |
|---|---|---|
| Zone Operation Characteristics (`ZOC`) | `01:00` | Includes Zone Active Excursions and Variable Zone Capacity bits. |
| Optional Zoned Command Support (`OZCS`) | `03:02` | Bit 0 is Read Across Zone Boundaries support. |
| Maximum Active Resources (`MAR`) | `07:04` | Maximum concurrently active zones. `FFFFFFFFh` means no limit. 0-based value. |
| Maximum Open Resources (`MOR`) | `11:08` | Maximum concurrently open zones. `FFFFFFFFh` means no limit. 0-based value. |
| Reset Recommended Limit fields (`RRL`, `RRL1`, `RRL2`, `RRL3`) | `15:12`, `23:20`, `27:24`, `31:28` | Used by Zone Attributes Information `RZRTL`. |
| Finish Recommended Limit fields (`FRL`, `FRL1`, `FRL2`, `FRL3`) | `19:16`, `35:32`, `39:36`, `43:40` | Used by Zone Attributes Information `FZRTL`. |
| LBA Format Extension entries (`LBAFE0`-`LBAFE63`) | `2815:2816` onward | Each references Figure 49. |
| Vendor Specific | `4095:3840` | Vendor specific. |

## LBA Format Extension Fields

Source: Figure 49.

| Bits | Field | Meaning |
|---:|---|---|
| `127:72` | Reserved | Reserved. |
| `71:64` | Zone Descriptor Extension Size (`ZDES`) | Size in 64-byte units. `0h` means Zone Descriptor Extensions are not supported. |
| `63:00` | Zone Size (`ZSZE`) | Zone size in logical blocks; shall not be cleared to `0h`. |

Commands such as Format NVM and Namespace Management that use an index to refer to an NVM LBA Format data structure use the same index to refer to the LBA Format Extension data structure.

## Read Across Zone Boundaries

If `OZCS` bit 0 is set, User Data Read Access Commands may read across zone boundaries.

If `OZCS` bit 0 is cleared, a command that performs a read operation and specifies an LBA range containing logical blocks in more than one zone is aborted as defined by the ZNS source.

## Active And Open Resources

`MAR` and `MOR` define limits for active and open zones. Commands that would exceed those limits may complete with ZNS command-specific status values:

| Status | Meaning |
|---:|---|
| `BDh` | Too Many Active Zones |
| `BEh` | Too Many Open Zones |

When a command is aborted due to insufficient active/open resources, no zone state transition occurs where the command-specific source says so.

## Zone Descriptor Extension

Source: section 5.3.

Zone Descriptor Extension lets host software associate a small amount of data with a zone. It is accessed by Zone Management Receive with Extended Report Zones. A Zone Descriptor Extension is associated with a zone when that zone transitions from Empty to Closed by Zone Management Send with Set Zone Descriptor Extension.

The association remains until:

- the zone transitions to Empty or Offline; and
- Zone Descriptor Extension Valid is cleared.

## Recommended Attributes

Reset Zone Recommended and Finish Zone Recommended are advisory attributes. The controller may set them and generate a Zone Descriptor Changed event. Host action is optional according to the ZNS source, but these attributes affect what a test may choose to observe or validate.

## Zone Active Excursions

Source: section 5.6.

If Zone Active Excursions are supported, a controller may transition a zone in Implicitly Opened, Explicitly Opened, or Closed state to Full due to a vendor specific excursion event. This behavior is orthogonal to Finish Zone Recommended.

## Boundary

This model file supports command-control lookup. It does not define PyNVMe API usage or test-flow sequence.
