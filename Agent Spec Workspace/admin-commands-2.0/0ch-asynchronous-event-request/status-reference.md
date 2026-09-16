# Asynchronous Event Request Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Asynchronous Event Request Limit Exceeded` | Too many AER commands are simultaneously outstanding. | Outstanding AER count exceeded Identify Controller `AERL`. |

## Event Reporting Notes

- AER completion success means an event was reported.
- Event-specific follow-up is driven by CQE DW0 `AET`, Asynchronous Event Information, and Log Page Identifier.
- If required log page data cannot be returned because media is not ready and Get Log Page returns `Admin Command Media Not Ready`, the controller shall not post an AER CQE for that event until it can return the required log page.

