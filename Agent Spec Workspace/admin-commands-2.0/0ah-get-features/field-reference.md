# Get Features Field Reference

Source: NVMe Base Specification 2.0, section 5.15, Figures 191-195, and feature return definitions in section 5.27.1.

## Command-Level Fields

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| CDW10 bits `10:08` | `SEL` | Selects current/default/saved/supported-capabilities return. | `011b` changes CQE DW0 meaning to capability bits. | Query type. |
| CDW10 bits `07:00` | `FID` | Feature Identifier. | Dispatches returned value format. | All Get Features behavior. |
| CDW11 | Feature-specific | Extra selector for some features. | Example: Host Metadata `GDHM`; interrupt vector selection. | Feature-specific query. |
| CDW14 bits `06:00` | UUID Index | Vendor-specific UUID selection. | Only valid when supported. | Vendor feature query. |

## Supported Capabilities CQE DW0 (`SEL=011b`)

| Bit | Field | Meaning | Test/FW use |
|---:|---|---|---|
| `2` | Changeable | Feature values are changeable. | Gate Set Features positive/negative tests. |
| `1` | NS Specific | Feature settings apply to individual namespaces. | Decide NSID usage. |
| `0` | Saveable | Feature values are saveable. | Decide whether `SV=1` is legal. |

## Common Returned Fields

| FID | Returned field | Meaning | Affects |
|---|---|---|---|
| `02h` Power Management | Power state | Current/default/saved power state. | Power management validation. |
| `06h` Volatile Write Cache | `WCE` | Write cache enabled/disabled. | Cache/Flush tests. |
| `07h` Number of Queues | `NCQA`, `NSQA` | Allocated I/O CQ/SQ counts, 0-based. | Queue setup. |
| `0Bh` Asynchronous Event Configuration | Event mask | Enabled async event notices. | AER tests. |
| `0Ch` APST | `APSTE` plus APST table | APST enable and transition entries. | Power management tests. |
| `0Dh` Host Memory Buffer | Attributes data structure | HMB state and memory attributes. | HMB tests. |
| `10h` HCTM | `TMT1`, `TMT2` | Thermal management thresholds. | Thermal management. |
| `16h` Host Behavior Support | `ACRE`, `ETDAS`, `LBAFEE` | Host-supported behavior flags. | Command retry, telemetry, command-set behavior. |
| `19h` I/O Command Set Profile | `IOCSCI` | Current I/O Command Set Combination Index. | Command-set switching validation. |
| `81h` Host Identifier | Host Identifier | 64-bit or 128-bit host identity. | Reservation and Fabrics host association. |
| `82h` Reservation Notification Mask | `RESPRE`, `RESREL`, `REGPRE` | Reservation notification mask bits. | Reservation notification tests. |
| `83h` Reservation Persistence | `PTPL` | Persist Through Power Loss state. | Reservation persistence tests. |
| `84h` Namespace Write Protection | Write Protection State | Current namespace write-protect state. | Write-protect validation. |

## Saved Value Fallback

If `SEL=010b` requests the saved value and the feature is not saveable or has no saved value, the controller behaves as if `SEL=001b` default value was requested.
