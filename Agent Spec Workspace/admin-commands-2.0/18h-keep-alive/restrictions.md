# Keep Alive Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| No command-specific fields | Keep Alive command input fields are reserved. | Reserved-field validation applies. |
| Feature support depends on Identify / transport | `KAS` and transport binding determine support/requirements. | Unsupported or invalid timeout behavior belongs to feature/transport validation. |
| Timer mode depends on `TBKAS` | Traffic based restart is only available when supported. | Otherwise use command-based Keep Alive behavior. |

