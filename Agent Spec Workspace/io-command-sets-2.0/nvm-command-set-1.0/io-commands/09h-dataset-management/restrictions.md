# NVM Dataset Management Restrictions

| Condition | Rule / expected behavior |
|---|---|
| `DMRL`, `DMRSL`, `DMSL` all non-zero and ONCS bit 2 set | Controller should process only logical blocks satisfying all three limits and skip those that do not. |
| `DMRL`, `DMRSL`, `DMSL` all non-zero and ONCS bit 2 clear | If any logical block violates one or more limits, abort with Command Size Limit Exceeded. |
| `DMRL`, `DMRSL`, `DMSL` all zero and ONCS bit 2 set | Dataset Management supported with no reported processing limits. |
| `DMRL`, `DMRSL`, `DMSL` all zero and ONCS bit 2 clear | Dataset Management not supported. |
| Controller processes attributes/context attributes | Controller may still choose to take no action. |
| Range extends beyond namespace | Controller can abort if it detects the error, even if that range is otherwise not processed due to limits. |
| Namespace uses ZNS (`CSI=02h`) | Apply ZNS overlay for Offline zone condition. |

Reserved command-specific fields have no NVM-defined meaning and should be cleared.
