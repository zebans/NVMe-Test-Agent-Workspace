# Reservation Report Payload Reference

## Figure 404 - Reservation Status Data Structure

| Bytes | Field | Meaning | Important detail | Affects |
|---:|---|---|---|---|
| `03:00` | `GEN` | Generation counter. | 32-bit wrapping counter. Rolls from `FFFFFFFFh` to `0`. | Detecting reservation-state changes. |
| `04` | `RTYPE` | Current reservation type. | `0` means no reservation; non-zero values use the reservation type encoding. | Reservation holder / registrant access behavior. |
| `06:05` | `REGCTL` | Number of registered controller structures. | Counts controllers associated with registrant hosts. | Payload parsing length and registered-controller table. |
| `07` | Reserved | Reserved. | No command-specific meaning. | Ignore unless validating reserved bytes. |
| `09:08` | `PTPLS` | Persist Through Power Loss state. | `0` reservations/registrants released on power-on; `1` persist across power loss. | Power-cycle reservation behavior. |
| Following bytes | Registered Controller Data Structures | Per-controller reservation registration information. | Structure layout depends on Host Identifier format / `EDS`. | Host/controller ownership checks. |

## `GEN` Increment Rules

`GEN` increments when any of these complete successfully:

- Reservation Register command.
- Reservation Release command with `RRELA=Clear`.
- Reservation Acquire command with `RACQA=Preempt`.
- Reservation Acquire command with `RACQA=Preempt and Abort`.

## Figure 405 - Extended Reservation Status Data Structure

| Bytes | Field / region | Meaning |
|---:|---|---|
| `23:00` | Reservation Status fields | Same logical fields as Figure 404. |
| `63:24` | Reserved | Reserved region before extended registered-controller entries. |
| `64+` | Registered Controller Extended Data Structures | Per-controller entries for extended Host Identifier reporting. |

## Registered Controller Structures

| Structure | Used when | Entry size | Entry start |
|---|---|---:|---|
| Figure 406 Registered Controller Data Structure | 64-bit Host Identifier reporting / `EDS=0` | 24 bytes | `24 + 24*n` |
| Figure 407 Registered Controller Extended Data Structure | 128-bit Host Identifier reporting / `EDS=1` | 64 bytes | `64 + 64*n` |

### Figure 406 - Registered Controller Data Structure

| Entry bytes | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `01:00` | `CNTLID` | Controller ID of the controller whose status is reported. | Dynamic controller not associated with a host reports `FFFFh`. | Multi-controller mapping. |
| `02` | `RCSTS` | Reservation status of this controller. | bit0 set means this controller is associated with a host that holds the reservation; bits7:1 reserved. | Holder detection. |
| `07:03` | Reserved | Reserved. | No command-specific meaning. | Reserved-field validation. |
| `15:08` | `HOSTID` | 64-bit Host Identifier. | Used with normal report format. | Host ownership checks. |
| `23:16` | `RKEY` | Reservation key for this controller's associated host. | Compare with expected registered key. | Key validation. |

### Figure 407 - Registered Controller Extended Data Structure

| Entry bytes | Field | Meaning | Important rule | Affects |
|---:|---|---|---|---|
| `01:00` | `CNTLID` | Controller ID. | Same definition as Figure 406. | Multi-controller mapping. |
| `02` | `RCSTS` | Reservation status. | Same definition as Figure 406. | Holder detection. |
| `07:03` | Reserved | Reserved. | No command-specific meaning. | Reserved-field validation. |
| `15:08` | `RKEY` | Reservation key. | In extended structure, `RKEY` precedes `HOSTID`. | Key validation. |
| `31:16` | `HOSTID` | 128-bit Host Identifier. | Used with extended report format. | Host ownership checks. |
| `63:32` | Reserved | Reserved. | No command-specific meaning. | Reserved-field validation. |

## `RCSTS`

| Bit | Meaning | Affects |
|---:|---|---|
| `0` | Indicates the controller is associated with a host that holds the reservation. | Identifying the reservation holder among registered controllers. |
