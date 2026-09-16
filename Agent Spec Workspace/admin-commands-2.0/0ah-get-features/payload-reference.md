# Get Features Payload Reference

Source: NVMe Base Specification 2.0, sections 5.15 and 5.27.1.

| Return form | Meaning | Examples |
|---|---|---|
| CQE Dword 0 only | Feature returns attributes in completion. | Volatile Write Cache, Number of Queues, Keep Alive Timer, Reservation Persistence. |
| CQE Dword 0 plus data buffer | Feature returns a scalar plus structured data. | Autonomous Power State Transition, Predictable Latency Mode Config. |
| Data buffer | Feature returns structured data. | Host Behavior Support, Timestamp, Host Identifier, Host Metadata. |
| Supported Capabilities CQE Dword 0 | `SEL=011b` returns capability bits, not normal feature value. | Any supported feature. |

## Supported Capabilities Return

| CQE DW0 bit | Field | Meaning |
|---:|---|---|
| `2` | Changeable | Feature values are changeable if set. |
| `1` | NS Specific | Feature is namespace specific if set. |
| `0` | Saveable | Feature values are saveable if set. |

## Feature Payload Index

Use [selector-reference.md](selector-reference.md) for the `FID` table and [field-reference.md](field-reference.md) for common returned fields. For byte-level parsing of Timestamp, Host Behavior Support, Host Metadata, and Host Identifier buffers, use the Set Features [payload-reference.md](../09h-set-features/payload-reference.md); those data structures are shared or paired with Get Features.

## High-Value Returned Data Buffer Layouts

| FID | Returned payload | Where to decode | Notes |
|---:|---|---|---|
| `0Eh` | Timestamp Get data structure | [../09h-set-features/payload-reference.md](../09h-set-features/payload-reference.md) | Get adds Origin and Synch fields at bytes `06`/`07`; see below. |
| `16h` | Host Behavior Support data structure | [../09h-set-features/payload-reference.md](../09h-set-features/payload-reference.md) | Same byte layout as Set. |
| `7Dh` / `7Eh` / `7Fh` | Host Metadata data structure | [../09h-set-features/payload-reference.md](../09h-set-features/payload-reference.md) | Get CDW11 bit `0` (`GDHM`) may generate default vendor strings before return. |
| `81h` | Host Identifier data structure | [../09h-set-features/payload-reference.md](../09h-set-features/payload-reference.md) | Size is selected by `EXHID` / transport requirements. |

### FID `0Eh` - Timestamp Get Data Structure Delta

Source: Figure 340.

| Bytes / bits | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `05:00` | Timestamp | Controller timestamp value. | Meaning depends on Origin. If Origin `000b`, milliseconds since last Controller Level Reset. If Origin `001b`, host-set value plus elapsed milliseconds, modulo `2^48` if needed. | Timestamp validation. |
| byte `06` bits `03:01` | Origin | How Timestamp was initialized. | `000b` Controller Level Timestamp Reset; `001b` Set Features; `010b`-`111b` reserved. | Interpreting timestamp value. |
| byte `06` bit `00` | Synch | Continuous counting indicator. | `0` counted continuously; `1` may have stopped counting during vendor-specific intervals. | Time accuracy expectations. |
| `07:04` and byte `07` | Reserved | Reserved. | Do not assign meaning. | Reserved-field validation. |

For Host Metadata Get, CDW11 bit `0` is `GDHM`: if set, the controller generates default vendor-specific strings for supported element types before returning the Host Metadata data structure.
