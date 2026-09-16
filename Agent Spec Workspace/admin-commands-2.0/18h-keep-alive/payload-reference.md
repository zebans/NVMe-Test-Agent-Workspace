# Keep Alive Payload / Timer Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | None | Keep Alive has no data transfer. |
| Completion | CQE on Admin Completion Queue | Posted when Keep Alive command completes. |
| Timer state | Controller/host Keep Alive Timer | Restarted according to section 3.9 and section 5.18 rules. |

## Timer Restart Rules

| Condition | Rule |
|---|---|
| Keep Alive Timeout enabled on Admin Queue | Timer is restarted when Keep Alive command is processed. |
| `TBKAS=0` | Timer is restricted to Keep Alive command based restart. |
| `TBKAS=1` and Admin/I/O command processed during interval | Timer is restarted at the end of the Keep Alive Timeout. |
| Timer disabled | Keep Alive Timeout shall not occur. |

