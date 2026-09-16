# Reservation Report Field Reference

## Command Fields

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data pointer | Points to returned Reservation Status data buffer. | Controller-to-host transfer. | Payload placement and transfer validation. |
| `CDW10` | `NUMD` | Zero-based dword count. | Short count truncates; long count returns complete structure only. | Transfer length tests. |
| `CDW11 bit 0` | `EDS` | Extended Data Structure selector. | Must match Host Identifier format. | Payload shape and `Host Identifier Inconsistent Format`. |
| Other command bits | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

## Returned Fields

| Field | Meaning | Important values / rules | Affects |
|---|---|---|---|
| `GEN` | Reservation generation counter. | Increments on successful registration / clear / preempt changes and wraps at 32 bits. | Change detection across reservation operations. |
| `RTYPE` | Current reservation type. | `0` means no reservation; non-zero values follow reservation type encoding. | Access-right behavior. |
| `REGCTL` | Registered controller count. | Number of registered-controller structures returned. | Payload parser length and registration checks. |
| `PTPLS` | Persist Through Power Loss state. | `0` no persist; `1` persist. | Power-cycle behavior. |
| `CNTLID` | Controller identifier. | Identifies each registered controller entry. | Multi-controller tests. |
| `RCSTS bit 0` | Reservation holder association. | Set when controller is associated with the host that holds the reservation. | Holder detection. |
| `HOSTID` | Host Identifier. | 64-bit or 128-bit depending on Host Identifier format and `EDS`. | Host ownership checks. |
| `RKEY` | Reservation key. | Registered key associated with the controller/host entry. | Key validation and debug. |

## Cross-Command Fields

| Field | Defined / reused by | Why it matters here |
|---|---|---|
| `RTYPE` | Reservation Acquire / Release reservation type encoding. | Reservation Report returns the active reservation type using the same logical values. |
| `RKEY` | Reservation Register / Acquire / Release. | Reservation Report exposes registered keys for validation. |
| Host Identifier | Host Identifier feature. | Determines whether normal or extended report format is valid. |
