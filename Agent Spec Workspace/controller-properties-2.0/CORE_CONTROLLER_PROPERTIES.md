# Core Controller Properties

Status: `FIELD-COMPLETE`

Source: NVM Express Base Specification Revision 2.0, sections 3.1.3.1 through 3.1.3.7 and 3.1.3.20 through 3.1.3.21, Figures 36-49 and 61-62.

## `CAP` - Controller Capabilities (`00h`, 64 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `63:61` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `60:59` | `CRMS` | RO / implementation | Controller Ready Modes Supported. | bit 0 `CRWMS`: ready with media; bit 1 `CRIMS`: ready independent of media. |
| `58` | `NSSS` | RO / implementation | NVM Subsystem Shutdown supported. | Gates `NSSD`; if set, `CAP.CPS` is not `00b`. |
| `57` | `CMBS` | RO / implementation | Controller Memory Buffer supported. | Routes to `CMBLOC/CMBSZ` and related CMB properties. |
| `56` | `PMRS` | RO / implementation | Persistent Memory Region supported. | Routes to `PMRCAP` and related PMR properties. |
| `55:52` | `MPSMAX` | RO / implementation | Maximum host memory page size. | Maximum page size is `2^(12 + MPSMAX)` bytes; Discovery Controller reports `0h`. |
| `51:48` | `MPSMIN` | RO / implementation | Minimum host memory page size. | Minimum page size is `2^(12 + MPSMIN)` bytes; Discovery Controller reports `0h`. |
| `47:46` | `CPS` | RO / implementation | Controller power scope. | `00b` not reported; `01b` controller; `10b` NVM domain; `11b` NVM subsystem. Affects `NSSD` scope. |
| `45` | `BPS` | RO / implementation | Boot Partition Support. | Gates Boot Partition properties. |
| `44:37` | `CSS` | RO / implementation | Command Sets Supported. | bit 0 NVM; bit 6 one or more I/O Command Sets and Identify I/O Command Set; bit 7 no I/O Command Set/Admin-only; other bits reserved. |
| `36` | `NSSRS` | RO / implementation | NVM Subsystem Reset supported. | Gates `NSSR`; Discovery Controller reports `0`. |
| `35:32` | `DSTRD` | RO / implementation | Doorbell stride. | Doorbell spacing is `2^(2 + DSTRD)` bytes; NVMe-oF I/O Controller reports `0h`. |
| `31:24` | `TO` | RO / implementation | Ready timeout. | Units are 500 ms; `FFh` means 127.5 s. Used with `CC.EN`, `CSTS.RDY`, `CC.CRIME`, and `CRTO`. |
| `23:19` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `18:17` | `AMS` | RO / implementation | Arbitration mechanisms supported in addition to round robin. | bit 0 weighted round robin with urgent; bit 1 vendor-specific. Round robin is always supported. |
| `16` | `CQR` | RO / implementation | Contiguous Queues Required. | `1`: SQ/CQ memory must be physically contiguous; message-based I/O and Discovery Controllers set `1`. |
| `15:0` | `MQES` | RO / implementation | Maximum Queue Entries Supported, zero based. | Actual maximum is `MQES + 1`; minimum legal report is `1h`, meaning two entries. |

## `VS` - Version (`08h`, 32 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:16` | `MJR` | RO / implementation | Major revision number. | Revision 2.0 reports `2h`. |
| `15:8` | `MNR` | RO / implementation | Minor revision number. | Revision 2.0 reports `0h`. |
| `7:0` | `TER` | RO / implementation | Tertiary revision number for 1.2.1 and later. | Revision 2.0 reports `0h`; older version formats reserve this byte. |

## `CC` - Controller Configuration (`14h`, 32 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:25` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
| `24` | `CRIME` | RW/RO / `0` | Controller Ready Independent of Media Enable. | Writable only when `CAP.CRMS=11b`; selects independent-of-media ready behavior and timeout. |
| `23:20` | `IOCQES` | RW / `0h` | I/O Completion Queue entry size as `2^n` bytes. | Must select a size supported by the active I/O Command Set. |
| `19:16` | `IOSQES` | RW / `0h` | I/O Submission Queue entry size as `2^n` bytes. | Must select a size supported by the active I/O Command Set. |
| `15:14` | `SHN` | RW / `00b` | Shutdown notification. | `00b` none; `01b` normal; `10b` abrupt; `11b` reserved. Observe `CSTS.SHST`. |
| `13:11` | `AMS` | RW / `000b` | Selected arbitration mechanism. | `000b` round robin; `001b` weighted RR with urgent; `111b` vendor-specific; others reserved. Must be supported by `CAP.AMS`. |
| `10:7` | `MPS` | RW / `0h` | Host memory page size. | Page size is `2^(12 + MPS)` bytes and must be within `CAP.MPSMIN:MPSMAX`; change only while `CC.EN=0`. |
| `6:4` | `CSS` | RW / `000b` | I/O Command Set selected. | `000b` NVM; `110b` all supported; `111b` Admin-only; other values reserved and selections are gated by `CAP.CSS`. |
| `3:1` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
| `0` | `EN` | RW / `0` | Controller enable. | `0->1` starts initialization; wait for `CSTS.RDY=1`. `1->0` initiates Controller Reset; wait for `CSTS.RDY=0`. Configure `AQA/ASQ/ACQ` while disabled. |

## `CSTS` - Controller Status (`1Ch`, 32 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:7` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `6` | `ST` | RO / `0` | Shutdown Type. | Reports whether normal or abrupt shutdown processing applies. |
| `5` | `PP` | RO / `0` | Processing Paused. | Valid while `CC.EN=1`; host should not submit commands while paused. |
| `4` | `NSSRO` | RWC / hardware init | NVM Subsystem Reset Occurred. | Indicates an NSS reset occurred; write `1` to clear. |
| `3:2` | `SHST` | RO / `00b` | Shutdown Status. | `00b` normal operation; `01b` shutdown processing; `10b` shutdown complete; `11b` reserved. |
| `1` | `CFS` | RO / `0` | Controller Fatal Status. | `1` means a fatal controller condition; host reset/recovery is required. |
| `0` | `RDY` | RO / `0` | Controller Ready. | Tracks controller readiness after `CC.EN` transitions and selected ready mode. |

## `NSSR` - NVM Subsystem Reset (`20h`, 32 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:0` | `NSSRC` | RW / `0h` on read | NVM Subsystem Reset Control. | Write `4E564D65h` (`NVMe`) to request reset when `CAP.NSSRS=1`; other writes have no effect; reads return `0h`. |

## `NSSD` - NVM Subsystem Shutdown (`64h`, 32 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:0` | `NSSC` | RW / `0h` on read | NVM Subsystem Shutdown Control. | Write `4E726D6Ch` (`Nrml`) for normal shutdown or `41627074h` (`Abpt`) for abrupt shutdown; other writes have no effect. Scope follows `CAP.CPS`; support follows `CAP.NSSS`. |

## `CRTO` - Controller Ready Timeouts (`68h`, 32 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:16` | `CRIMT` | RO / implementation | Ready Independent of Media Timeout. | 500 ms units; `0h` when `CAP.CRMS.CRIMS=0`; should not exceed `FFh`. |
| `15:0` | `CRWMT` | RO / implementation | Ready With Media Timeout. | 500 ms units; greater than or equal to `CRIMT`. |

