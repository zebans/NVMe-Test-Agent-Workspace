# Set Features Selector Reference

Source: NVMe Base Specification 2.0, section 5.27, Figure 316.

## Feature Identifier Table

| FID | Feature | Source | Uses memory buffer | Test/FW use |
|---|---|---|---|---|
| `01h` | Arbitration | 5.27.1.1 | No | Command arbitration burst/weight settings. |
| `02h` | Power Management | 5.27.1.2 | No | Power state selection and workload hint. |
| `04h` | Temperature Threshold | 5.27.1.3 | No | Thermal warning/critical threshold programming. |
| `06h` | Volatile Write Cache | 5.27.1.4 | No | Enable/disable volatile write cache. |
| `07h` | Number of Queues | 5.27.1.5 | No | Request I/O SQ/CQ allocation during initialization. |
| `08h` | Interrupt Coalescing | 5.27.1.6 | No | Interrupt aggregation time/threshold. |
| `09h` | Interrupt Vector Configuration | 5.27.1.7 | No | Per-vector coalescing disable. |
| `0Bh` | Asynchronous Event Configuration | 5.27.1.8 | No | Enable/disable AER notices. |
| `0Ch` | Autonomous Power State Transition | 5.27.1.9 | Yes | APST enable and transition table. |
| `0Dh` | Host Memory Buffer | 5.27.1.10 | Set: command fields; Get: data buffer | HMB enable/disable and descriptor list. |
| `0Eh` | Timestamp | 5.27.1.11 | Yes | Set controller timestamp. |
| `0Fh` | Keep Alive Timer | 5.27.1.12 | No | Keep-alive timeout. |
| `10h` | Host Controlled Thermal Management | 5.27.1.13 | No | Thermal management thresholds. |
| `11h` | Non-Operational Power State Config | 5.27.1.14 | No | Non-operational power state behavior. |
| `12h` | Read Recovery Level Config | 5.27.1.15 | No | Read recovery level per NVM Set. |
| `13h` | Predictable Latency Mode Config | 5.27.1.16 | Yes | Predictable latency enable and threshold config. |
| `14h` | Predictable Latency Mode Window | 5.27.1.17 | No | DTWIN/NDWIN selection. |
| `16h` | Host Behavior Support | 5.27.1.18 | Yes | Enables controller behavior requiring host support. |
| `17h` | Sanitize Config | 5.27.1.19 | No | No-deallocate response behavior. |
| `18h` | Endurance Group Event Configuration | 5.27.1.20 | No | Endurance group event reporting. |
| `19h` | I/O Command Set Profile | 5.27.1.21 | No | Select I/O Command Set Combination. |
| `1Ah` | Spinup Control | 5.27.1.22 | No | Rotational media spinup method. |
| `20h` | I/O Command Set specific feature | I/O command set spec | Spec-defined | External command-set feature. |
| `7Dh` | Enhanced Controller Metadata | 5.27.1.23.1 | Yes | Host metadata with enhanced controller metadata rules. |
| `7Eh` | Controller Metadata | 5.27.1.23.2 | Yes | Host platform metadata. |
| `7Fh` | Namespace Metadata | 5.27.1.23.3 | Yes | Namespace metadata. |
| `80h` | Software Progress Marker | 5.27.1.24 | No | Pre-boot/OS progress marker. |
| `81h` | Host Identifier | 5.27.1.25 | Yes | Host identity for subsystem/reservations. |
| `82h` | Reservation Notification Mask | 5.27.1.26 | No | Mask reservation notifications. |
| `83h` | Reservation Persistence | 5.27.1.27 | No | PTPL state. |
| `84h` | Namespace Write Protection Config | 5.27.1.28 | No | Namespace write protection state. |
| `C0h`-`FFh` | Vendor specific | Vendor definition | Vendor-defined | Vendor-owned behavior. |

## Selector Notes

| Selector | Meaning | Boundary |
|---|---|---|
| `FID` | Selects the feature. | Base owns listed Base features; `20h` and vendor range are external. |
| `SV` | Requests saved value persistence. | Valid only for saveable features. |
| NSID | Selects namespace scope for namespace-specific features. | Non-namespace-specific feature access can return `Feature Not Namespace Specific`. |
| UUID Index | Vendor-specific UUID selection. | Only valid when UUID selection is supported for the selected vendor feature. |
