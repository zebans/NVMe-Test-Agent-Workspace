# Get Log Page Command Facts

Source: NVMe Base Specification 2.0, section 5.16, Figures 196-201.

## Command Identity

| Item | Value |
|---|---|
| Command | Get Log Page |
| Admin opcode | `02h` |
| Data transfer | Controller to host |
| Data pointer | Used; points to returned log data buffer |
| NSID | Used; interpretation depends on selected log page scope |
| Primary selector | `CDW10.LID` |

## Command Dwords

| Dword | Bits | Field | Meaning | Test/FW impact |
|---|---:|---|---|---|
| DPTR | all | Data Pointer | Start of returned data buffer. | Buffer length must match requested `NUMD + 1` dwords unless test intentionally under/over-sizes. |
| CDW10 | 31:16 | `NUMDL` | Lower 16 bits of zero-based number of dwords to return. | Combine with `NUMDU`; requested dwords = `NUMD + 1`. |
| CDW10 | 15 | `RAE` | Retain Asynchronous Event. `0` may clear related async event after successful read; `1` retains it. | Important for AER/event-clearing tests. |
| CDW10 | 14:08 | `LSP` | Log Specific Field. Meaning is defined by selected `LID`; reserved when not defined. | Persistent Event, ANA, Lockdown, Boot Partition, and telemetry use LSP-specific rules. |
| CDW10 | 07:00 | `LID` | Log Page Identifier. | Main dispatch selector. See [selector-reference.md](selector-reference.md). |
| CDW11 | 31:16 | Log Specific Identifier | Endurance Group ID, NVM Set ID, or Domain ID for selected log pages. | Invalid IDs may produce `Invalid Field in Command`. |
| CDW11 | 15:00 | `NUMDU` | Upper 16 bits of zero-based number of dwords to return. | Extended transfer count depends on Identify Controller `LPA`. |
| CDW12 | 31:00 | `LPOL` | Lower 32 bits of Log Page Offset or index. | Meaning depends on `CDW14.OT`. |
| CDW13 | 31:00 | `LPOU` | Upper 32 bits of Log Page Offset or index. | Meaning depends on `CDW14.OT`. |
| CDW14 | 31:24 | `CSI` | Command Set Identifier for command-set specific logs. | Unsupported CSI may return `I/O Command Set Not Supported`. |
| CDW14 | 23 | `OT` | Offset Type. `0` = byte offset; `1` = index offset. | `OT=1` requires index offset support for the selected LID. |
| CDW14 | 22:07 | Reserved | Reserved. | Should be zero unless a test intentionally targets invalid fields. |
| CDW14 | 06:00 | UUID Index | Selects UUID for vendor-specific log behavior when supported. | Non-zero UUID index is only valid when supported for the requested log page. |

## Offset Rules

| Case | Rule | Failure condition |
|---|---|---|
| `OT=0` byte offset | `LPOL/LPOU` is a byte offset into the log page and should be dword aligned. | Offset beyond log page size is invalid; non-dword alignment may be rejected or treated as aligned by clearing bits 1:0. |
| `OT=1` index offset | `LPOL/LPOU` is an index into a list-like log page. | Invalid if the LID does not support index offset (`IOS=0` in Supported Log Pages). |
| Extended NUMD | `NUMDU:NUMDL` form a larger transfer count when supported by Identify Controller `LPA`. | If unsupported, only the lower supported NUMD bits are valid. |
| Log Page Offset support | Controlled by Identify Controller `LPA`. | Host must not assume offset support unless `LPA` reports it. |

## NSID Scope Rule

For controller-scope or NVM-subsystem-scope log pages, an NSID other than `00000000h` or `FFFFFFFFh` should be treated as invalid by the controller. Namespace-scoped or command-set-specific logs may define additional NSID behavior in their own command set specification.
