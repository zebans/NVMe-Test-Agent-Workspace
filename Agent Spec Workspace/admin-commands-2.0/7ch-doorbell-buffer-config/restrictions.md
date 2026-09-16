# Doorbell Buffer Config Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| `PRP1` page aligned | Shadow Doorbell buffer base shall be memory page aligned. | `Invalid Field in Command` if address invalid. |
| `PRP2` page aligned | EventIdx buffer base shall be memory page aligned. | `Invalid Field in Command` if address invalid. |
| Buffer size must cover queue range | Layout covers SQ/CQ entries through `y=max(NSQA,NCQA)`. | Host buffer must be sized consistently with queue configuration. |

