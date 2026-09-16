# Format NVM Selector Reference

Source: NVMe Base Specification 2.0, section 5.14, Figure 189.

## Secure Erase Settings

| SES | Meaning | Test/FW impact |
|---|---|---|
| `000b` | No secure erase operation requested. | Format behavior without secure erase. |
| `001b` | User Data Erase. | User data erase behavior and scope use secure erase FNA rule. |
| `010b` | Cryptographic Erase. | Crypto erase behavior and scope use secure erase FNA rule. |
| `011b`-`111b` | Reserved. | Invalid field / invalid format testing. |

## Scope Selectors

| Selector | Meaning | Affects |
|---|---|---|
| `NSID` allocated namespace | Format target namespace unless FNA escalates scope. | Single namespace vs subsystem-wide destructive behavior. |
| `NSID=FFFFFFFFh` | Broadcast namespace selector. | May target all namespaces in relevant scope or be disallowed by FNA bit 3. |
| Identify Controller `FNA` bit 0 | Format applies to all namespaces behavior. | Used when `SES=000b`. |
| Identify Controller `FNA` bit 1 | Secure erase applies to all namespaces behavior. | Used when `SES!=000b`. |
| Identify Controller `FNA` bit 3 | Whether `NSID=FFFFFFFFh` is supported for Format NVM. | If disallowed and used, abort with Invalid Field in Command. |

## User Data Format Selector

| Field | Meaning | Dependency |
|---|---|---|
| `LBAFL` | Lower four bits of User Data Format. | Always part of format selection. |
| `LBAFU` | Upper two bits of User Data Format. | Valid only when Host Behavior Support `LBAFEE=1`; ignored when `LBAFEE=0`. |
