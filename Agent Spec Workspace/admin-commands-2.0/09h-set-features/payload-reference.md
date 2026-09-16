# Set Features Payload Reference

Source: NVMe Base Specification 2.0, section 5.27.1.

| FID | Input location | Main figure(s) | Notes |
|---|---|---|---|
| `01h` Arbitration | CDW11 | Figure 317 | No data buffer. |
| `02h` Power Management | CDW11 | Figure 318 | Get completion uses Figure 319. |
| `04h` Temperature Threshold | CDW11 | Figure 320 | Sensor/threshold selector plus temperature. |
| `06h` Volatile Write Cache | CDW11 | Figure 321 | `WCE` enable bit. |
| `07h` Number of Queues | CDW11 | Figures 322-323 | Set request in CDW11; allocated values returned in CQE DW0. |
| `08h` Interrupt Coalescing | CDW11 | Figure 324 | Aggregation time/threshold. |
| `09h` Interrupt Vector Configuration | CDW11 | Figure 325 | Interrupt vector and coalescing disable. |
| `0Bh` Asynchronous Event Configuration | CDW11 | Figure 326 | Event enable mask. |
| `0Ch` Autonomous Power State Transition | CDW11 + data buffer | Figures 327-329 | 256-byte APST table. |
| `0Dh` Host Memory Buffer | CDW11-CDW15 | Figures 330-338 | Set uses command fields and descriptor list; Get returns attributes data structure. |
| `0Eh` Timestamp | data buffer | Figures 339-340 | Set and Get use different timestamp data structures. |
| `0Fh` Keep Alive Timer | CDW11 | Figure 341 | Keep alive timeout value. |
| `10h` Host Controlled Thermal Management | CDW11 | Figure 342 | TMT1/TMT2 thresholds. |
| `11h` Non-Operational Power State Config | CDW11 | Figure 343 | `NOPPME`. |
| `12h` Read Recovery Level Config | CDW11-CDW12 | Figures 344-345 | NVM Set plus read recovery level. |
| `13h` Predictable Latency Mode Config | CDW11-CDW12 + data buffer | Figures 346-348 | NVM Set, enable, threshold config. |
| `14h` Predictable Latency Mode Window | CDW11-CDW12 | Figures 349-350 | NVM Set plus window select. |
| `16h` Host Behavior Support | data buffer | Figure 351 | 512-byte host behavior support structure. |
| `17h` Sanitize Config | CDW11 | Figure 352 | `NODRM`. |
| `18h` Endurance Group Event Configuration | CDW11 | Figure 353 | ENDGID and warning mask. |
| `19h` I/O Command Set Profile | CDW11 | Figures 354-355 | Set combination index; Get returns selected index. |
| `1Ah` Spinup Control | CDW11 | Figures 356-357 | Spinup control enable. |
| `7Dh`/`7Eh`/`7Fh` Host Metadata | CDW11 + data buffer | Figures 358-363 | Host metadata action and descriptor structure. |
| `80h` Software Progress Marker | CDW11 | Figure 364 | Pre-boot software load count. |
| `81h` Host Identifier | CDW11 + data buffer | Figures 365-366 | 64-bit or 128-bit Host ID. |
| `82h` Reservation Notification Mask | CDW11 | Figure 367 | Reservation notification mask bits. |
| `83h` Reservation Persistence | CDW11 | Figure 368 | PTPL bit. |
| `84h` Namespace Write Protection Config | CDW11 | Figure 369 | Write protection state. |

## Data Buffer Rule

If the selected feature does not use a data structure, `DPTR` is not used. If a feature uses a data structure, validate buffer size and ownership against the feature-specific section before generating a test.

## High-Value Data Buffer Layouts

Use this section when a test or FW question needs exact bytes in Set Features data buffers. Features not listed here either use CDW fields or are routed to their command-set/vendor owner.

### FID `0Eh` - Timestamp Set Data Structure

Source: Figure 339.

| Bytes | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `05:00` | Timestamp | Milliseconds elapsed since midnight, 01-Jan-1970 UTC. | Host-provided timestamp value. | Timestamp feature tests and persistent event timestamp-change records. |
| `07:06` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |

### FID `16h` - Host Behavior Support Data Structure

Source: Figure 351 plus NVM Command Set Figure 86 for command-set-specific byte `02`.

| Bytes | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `00` | `ACRE` | Advanced Command Retry Enable. | `1h` enables `Command Interrupted` status and non-zero Command Retry Delay behavior; `0h` disables both. Other values reserved. | Retry/status behavior. |
| `01` | `ETDAS` | Extended Telemetry Data Area 4 Supported. | `1h` says host supports telemetry data area 4; `0h` says it does not. Other values reserved. | Telemetry Host/Controller-Initiated logs. |
| `02` | `LBAFEE` | LBA Format Extension Enable. | I/O Command Set-specific. For NVM, enables extended LBA formats when controller supports ELBAS; for other command sets, use the owning command-set spec. Other values reserved. | NVM extended LBA formats, protection information formats, Namespace Management/Format NVM. |
| `511:03` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |

### FID `7Dh` / `7Eh` / `7Fh` - Host Metadata Data Structure

Sources: Figures 359-363.

| Bytes / bits | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| CDW11 bits `14:13` | `EA` | Element Action for Set Features. | `00b` Add/Replace; `01b` Delete Entry Multiple; `10b` Add Entry Multiple; `11b` reserved. `EA=00b` is invalid for Enhanced Controller Metadata. `EA=10b` is valid only for Enhanced Controller Metadata. | Metadata update semantics and invalid-field tests. |
| data byte `00` | Number of Metadata Element Descriptors | Count of descriptors in the 4 KiB Host Metadata data structure. | `0h` means no descriptors. | Parser loop bound. |
| data byte `01` | Reserved | Reserved. | Clear to `0h`. | Reserved-field validation. |
| descriptor bits `04:00` | `ET` | Element Type. | `00h` reserved; `01h`-`17h` spec-defined; `18h`-`1Fh` vendor-specific. | Metadata element dispatch. |
| descriptor bits `11:08` | `ER` | Element Revision. | Clear to `0h` unless otherwise specified. | Descriptor versioning. |
| descriptor bits `31:16` | `ELEN` | Element Value length in bytes. | Shall be `0h` when deleting (`EA=01b`); should be non-zero when adding/updating (`EA=00b`). | Descriptor length parsing and invalid-field tests. |
| descriptor bits `31+(ELEN*8):32` | `EVAL` | Element Value. | String/content interpretation is vendor or element-type specific. | Metadata value validation. |

Controller Metadata and Namespace Metadata may contain at most one descriptor per Element Type. Enhanced Controller Metadata may contain more than one descriptor per Element Type. The full Host Metadata data structure is 4 KiB.

### FID `81h` - Host Identifier Data Structure

Sources: Figures 365-366.

| Bytes / bits | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| CDW11 bit `00` | `EXHID` | Enable Extended Host Identifier. | `0` selects 64-bit Host Identifier; `1` selects 128-bit Host Identifier. Fabrics implementations use non-zero 128-bit Host Identifier. | Reservation ownership, Host Identifier format, Fabrics boundary. |
| data bytes `07:00` | `HOSTID` | 64-bit Host Identifier when `EXHID=0`. | `0h` means not associated with any other controller in the NVM subsystem. | Reservation and multi-controller association. |
| data bytes `15:00` | `HOSTID` | 128-bit Host Identifier when `EXHID=1`. | Used by Fabrics; size mismatch across controllers may cause `Host Identifier Inconsistent Format`. | Reservation and Fabrics host association. |
