# Keep Alive Selector Reference

| Selector / capability | Location | Meaning |
|---|---|---|
| Keep Alive Timer granularity | Identify Controller `KAS` | Granularity of the Keep Alive Timer. |
| Traffic Based Keep Alive Support | Identify Controller `TBKAS` | Whether Admin/I/O traffic may restart the Keep Alive Timer. |
| Keep Alive Timeout | Keep Alive Timer Feature `KATO` / Fabrics Connect `KATO` | Timeout value that enables/disables and configures the timer. |

## Timer Modes

| Mode | Condition | Timer restart behavior |
|---|---|---|
| Keep Alive command based | `TBKAS=0` | Timer restarts only when Keep Alive command is processed. |
| Traffic based | `TBKAS=1` | Timer may restart when Admin or I/O command is processed during the interval. |

