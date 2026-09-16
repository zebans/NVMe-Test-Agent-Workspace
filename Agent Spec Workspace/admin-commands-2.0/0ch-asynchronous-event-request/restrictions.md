# Asynchronous Event Request Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| Outstanding AER limit | Identify Controller `AERL` limits simultaneous AER commands. | `Asynchronous Event Request Limit Exceeded`. |
| No command timeout | AER is expected to remain outstanding until an event is available. | Do not treat normal wait as timeout. |
| Event type masking | Once an event type is reported, subsequent events of that type are masked until cleared. | Read associated log page to clear unless otherwise stated. |
| Reset behavior | Outstanding AER commands during controller reset are aborted and should not return CQEs. | Reset flow should not expect normal AER completion. |

