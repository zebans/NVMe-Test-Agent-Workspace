# Sanitize Field Reference

Source: NVMe Base Specification 2.0, section 5.24, Figures 303-304.

Naming note: Figure 303 names bit 9 **No-Deallocate After Sanitize** but does not assign the acronym `NDAS`. This folder uses `NDAS` only as a local lookup alias.

## CDW10

| Bits | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `09` | `NDAS` | No-Deallocate After Sanitize. | If set and Identify `SANICAP.NDI=0`, controller shall not deallocate user data as a result of successful sanitize. If inhibited, controller should deallocate. | Post-sanitize media/deallocation behavior. |
| `08` | `OIPBP` | Overwrite Invert Pattern Between Passes. | Used only when `SANACT=011b` Overwrite. | Overwrite data pattern. |
| `07:04` | `OWPASS` | Overwrite Pass Count. | `0h` means 16 overwrite passes; ignored unless Overwrite. | Overwrite duration and pattern passes. |
| `03` | `AUSE` | Allow Unrestricted Sanitize Exit. | Set = unrestricted completion mode; clear = restricted completion mode; ignored for Exit Failure Mode. | Failure recovery rules. |
| `02:00` | `SANACT` | Sanitize Action. | `001b` Exit Failure Mode; `010b` Block Erase; `011b` Overwrite; `100b` Crypto Erase. | Operation selection. |

## CDW11

| Bits | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `31:00` | `OVRPAT` | Overwrite Pattern. | Ignored unless `SANACT=011b`. | Data pattern used for Overwrite sanitize. |

## Identify / Feature Dependencies

| Source field | Meaning | Affects |
|---|---|---|
| Identify Controller `SANICAP` | Supported sanitize operation types and no-deallocate behavior. | Whether Block Erase, Overwrite, Crypto Erase, and `NDAS` are valid/effective. |
| Set Features Sanitize Config `NODRM` | No-Deallocate Response Mode. | Whether inhibited no-deallocate is warning-style or error-style behavior. |
| Get Log Page `LID=81h` Sanitize Status | Operation progress/final state. | Polling and pass/fail determination. |
