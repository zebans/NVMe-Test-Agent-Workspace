# Connect Selector Reference

## `RECFMT`

| Value | Meaning | Failure if unsupported |
|---:|---|---|
| `0h` | Connect command capsule format defined by this source. | Unsupported values return `Incompatible Format`. |

## `QID`

| `QID` | Meaning |
|---:|---|
| `0h` | Admin Queue Connect. |
| `1` to `65,534` | I/O Queue Connect. |

If the host sends Connect for a Queue ID that has already been created, `Command Sequence Error` is returned.

## `SQSIZE`

| Case | Expected status direction |
|---|---|
| `SQSIZE=0h` | `Connect Invalid Parameters`. |
| Larger than supported | `Connect Invalid Parameters`. |

## `CATTR`

| Bits | Meaning | Notes |
|---:|---|---|
| `7:4` | Reserved | Host should clear. |
| `3` | Host supports deleting individual I/O Queues. | Connect attribute. |
| `2` | Request SQ flow control disabled. | Disabled only if response `SQHD=FFFFh`. |
| `1:0` | Priority class for I/O Queues. | Cleared to `00b` for Admin Queue. |

Priority classes:

| `CATTR[1:0]` | Priority |
|---|---|
| `00b` | Urgent |
| `01b` | High |
| `10b` | Medium |
| `11b` | Low |

## `CNTLID`

| Controller model / case | Required value / behavior |
|---|---|
| Dynamic controller model Admin Queue Connect | `CNTLID` shall be `FFFFh`; otherwise `Connect Invalid Parameters`. |
| Static controller model Admin Queue Connect | `CNTLID=FFFFh` returns `Connect Invalid Parameters`. |
| Static controller model request any Controller ID | `CNTLID=FFFEh`. |

## `KATO`

`KATO` is Keep Alive Timeout for Admin Queue Connect. It is reserved for I/O Queue Connect.
