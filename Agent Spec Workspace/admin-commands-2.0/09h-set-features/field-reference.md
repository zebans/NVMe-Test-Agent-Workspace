# Set Features Field Reference

Source: NVMe Base Specification 2.0, section 5.27.1, Figures 317-369.

This file expands high-value feature fields for test and firmware lookup. It does not reproduce every byte of large feature payloads.

## Command-Level Fields

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| CDW10 bit `31` | `SV` | Save requested value across power states/resets. | Requires feature to be saveable. | Persistence tests and `Feature Identifier Not Saveable`. |
| CDW10 bits `07:00` | `FID` | Feature Identifier. | Dispatches to feature-specific fields. | All Set Features behavior. |
| CDW14 bits `06:00` | UUID Index | Vendor-specific UUID selection. | Only valid when supported. | Vendor feature tests. |

## Common Feature Fields

| FID | Field | Meaning | Important bits | Affects |
|---|---|---|---|---|
| `01h` Arbitration | `AB`, `LPW`, `MPW`, `HPW` | Arbitration Burst and low/medium/high priority weights. | CDW11. | SQ scheduling behavior. |
| `02h` Power Management | `PS`, `WH` | Requested power state and workload hint. | CDW11; Get returns selected power state. | Power-state tests. |
| `04h` Temperature Threshold | `THSEL`, `TMPSEL`, `TMPTH` | Threshold type, temperature sensor selector, threshold in Kelvin. | `TMPSEL=Fh` valid for Set as all implemented sensors; reserved for Get. | Thermal threshold tests. |
| `06h` Volatile Write Cache | `WCE` | Enable/disable volatile write cache. | bit0. | Flush/cache behavior. |
| `07h` Number of Queues | `NCQR`, `NSQR` | Requested I/O CQ/SQ counts, 0-based. | `FFFFh` should be invalid; only during initialization before I/O queues. | Queue allocation tests. |
| `08h` Interrupt Coalescing | `TIME`, `THR` | Aggregation time and threshold. | `TIME` is in 100 us units; `THR` is 0-based. | Interrupt behavior. |
| `09h` Interrupt Vector Configuration | `CD`, `IV` | Coalescing disable and interrupt vector. | Vector must be valid and associated with an I/O CQ. | MSI/MSI-X interrupt tests. |
| `0Bh` Asynchronous Event Configuration | Event mask bits | Enables/disables AER notices. | Bits include SMART warnings, namespace attribute, firmware activation, telemetry, ANA, predictable latency, endurance group, discovery, ZNS notices. | AER tests. |
| `0Ch` APST | `APSTE`, APST entries | Enable APST and define per-power-state idle transition entries. | Data structure has 32 64-bit entries. | Power management tests. |
| `0Dh` Host Memory Buffer | `EHM`, `MR`, descriptor list fields | Enable/disable HMB and describe host memory regions. | Enabling while already enabled is command sequence error. | HMB setup/teardown. |
| `0Eh` Timestamp | Timestamp data | Sets controller timestamp. | Data buffer feature. | Timestamp tests. |
| `0Fh` Keep Alive Timer | `KATO` | Keep Alive Timeout. | CDW11. | Fabrics/keep-alive behavior. |
| `10h` HCTM | `TMT1`, `TMT2` | Thermal management temperature thresholds. | CDW11. | Thermal management tests. |
| `11h` NOPSC | `NOPPME` | Non-operational power state permissive mode. | CDW11 bit0. | Background operations in non-operational power states. |
| `12h` Read Recovery Level Config | NVM Set ID, RRL | NVM Set target and read recovery level. | CDW11/CDW12. | Read recovery tuning. |
| `13h` Predictable Latency Mode Config | NVM Set ID, enable, thresholds | Configures predictable latency mode. | Requires supported NVM Set behavior. | Predictable latency tests. |
| `14h` Predictable Latency Mode Window | NVM Set ID, Window Select | Selects DTWIN or NDWIN. | Invalid if predictable latency mode not enabled. | Latency window transitions. |
| `16h` Host Behavior Support | `ACRE`, `ETDAS`, `LBAFEE` | Enables host-supported behaviors. | `ACRE` enables Command Interrupted/retry behavior; `ETDAS` enables telemetry area 4 support; `LBAFEE` is command-set specific. | Status retry and telemetry behavior. |
| `17h` Sanitize Config | `NODRM` | No-Deallocate Response Mode. | Interacts with Identify Controller `SANICAP.NDI` and Sanitize `NDAS`. | Sanitize behavior. |
| `18h` Endurance Group Event Configuration | ENDGID, critical warning mask | Configures endurance group event generation. | Invalid ENDGID or reserved warning bits abort. | Endurance group AER/log tests. |
| `19h` I/O Command Set Profile | `IOCSCI` | I/O Command Set Combination Index. | Rejected if unsupported/zero combination. | Command-set switching. |
| `1Ah` Spinup Control | Enable | Enables spinup control for rotational media endurance groups. | Invalid if no rotational media endurance groups. | Rotational media tests. |
| `7Dh`/`7Eh`/`7Fh` Host Metadata | `GDHM`, `EA`, metadata descriptors | Get can generate defaults; Set adds/replaces/deletes metadata elements. | Enhanced Controller Metadata differs from Controller/Namespace Metadata actions. | Metadata management. |
| `80h` Software Progress Marker | `PBSLC` | Pre-boot software load count. | Does not wrap from 255 to 0. | Boot progress diagnostics. |
| `81h` Host Identifier | `EXHID`, Host Identifier | Selects 64-bit vs 128-bit Host ID and provides ID data. | Fabrics uses non-zero 128-bit Host ID set by Connect. | Reservation and host association. |
| `82h` Reservation Notification Mask | `RESPRE`, `RESREL`, `REGPRE` | Masks reservation notification types. | Namespace-specific; `NSID=FFFFFFFFh` behavior differs for Set/Get. | Reservation notification tests. |
| `83h` Reservation Persistence | `PTPL` | Persist Through Power Loss. | Namespace-specific; also modifiable via Reservation Register. | Reservation persistence. |
| `84h` Namespace Write Protection | Write Protection State | No WP, WP, WP until power cycle, permanent WP. | Some transitions are not changeable. | Namespace write-protect tests. |

## High-Risk Feature Rules

| Feature | Rule | Expected impact |
|---|---|---|
| Number of Queues | Set only during initialization before I/O queues are created. | Later Set Features may return Command Sequence Error. |
| Host Memory Buffer | Enabling HMB while already enabled aborts with Command Sequence Error. | HMB lifecycle tests must disable before re-enable. |
| Host Behavior Support | Not saveable; default all zeros. | Do not expect persistence. |
| Reservation Notification Mask | Get with `NSID=FFFFFFFFh` should be invalid. | Reservation feature tests. |
| Reservation Persistence | Get with `NSID=FFFFFFFFh` should be invalid. | PTPL tests. |
| Namespace Write Protection | Write Protect Until Power Cycle and Permanent Write Protect restrict later changes. | `Feature Not Changeable`. |
