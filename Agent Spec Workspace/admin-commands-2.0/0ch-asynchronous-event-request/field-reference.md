# Asynchronous Event Request Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| Command-specific fields | Reserved | AER command has no command-specific input fields. | Host should clear. | Reserved-field validation. |
| CQE DW0 bits 23:16 | Log Page Identifier | Associated log page for the event. | Read the associated log page to clear the event unless otherwise specified. | Event clearing and follow-up Get Log Page. |
| CQE DW0 bits 15:08 | Asynchronous Event Information | Event-specific value. | Meaning depends on `AET`. | Event interpretation. |
| CQE DW0 bits 02:00 | Asynchronous Event Type | Event category. | Error, SMART/Health, Notice, Immediate, I/O Command specific, Vendor specific. | Which event information table applies. |
| Identify Controller | `AERL` | Outstanding AER command limit. | Too many outstanding AER commands returns `Asynchronous Event Request Limit Exceeded`. | AER queue depth tests. |

