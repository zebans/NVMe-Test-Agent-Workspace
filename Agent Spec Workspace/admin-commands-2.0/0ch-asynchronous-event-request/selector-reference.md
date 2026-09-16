# Asynchronous Event Request Selector Reference

Naming note: Base Spec 2.0 Figure 143 names the field **Asynchronous Event Type** but does not assign the acronym `AET`. This folder uses `AET` only as a local lookup alias.

| Returned selector | Location | Meaning |
|---|---|---|
| Log Page Identifier | CQE DW0 bits 23:16 | Log page associated with the asynchronous event. |
| Asynchronous Event Information | CQE DW0 bits 15:08 | More specific information for the event type. |
| Asynchronous Event Type (`AET`) | CQE DW0 bits 02:00 | Event type category. |

## Event Type Values

| `AET` value | Event type | Event information table |
|---|---|---|
| `000b` | Error status | Figure 144; see [payload-reference.md](payload-reference.md) |
| `001b` | SMART / Health status | Figure 145; see [payload-reference.md](payload-reference.md) |
| `010b` | Notice | Figure 146; see [payload-reference.md](payload-reference.md) |
| `011b` | Immediate | Figure 148; see [payload-reference.md](payload-reference.md) |
| `100b`-`101b` | Reserved | Reserved |
| `110b` | I/O Command specific status | Figure 147; see [payload-reference.md](payload-reference.md) |
| `111b` | Vendor specific | Vendor specific |
