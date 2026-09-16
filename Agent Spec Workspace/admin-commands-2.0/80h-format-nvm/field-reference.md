# Format NVM Field Reference

Source: NVMe Base Specification 2.0, section 5.14, Figure 189.

## CDW10

| Bits | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `13:12` | `LBAFU` | Upper two bits of User Data Format. | Ignored when `LBAFEE=0`; combines with `LBAFL` when `LBAFEE=1`. | Extended LBA format selection. |
| `11:09` | `SES` | Secure Erase Settings. | `000b` none; `001b` User Data Erase; `010b` Cryptographic Erase; others reserved. | Secure erase behavior and FNA scope bit selection. |
| `08` | `PIL` | Protection Information Location. | I/O Command Set specific. | PI layout after format. |
| `07:05` | `PI` | Protection Information. | I/O Command Set specific. | PI enable/type after format. |
| `04` | `MSET` | Metadata Settings. | I/O Command Set specific. | Metadata transfer mode after format. |
| `03:00` | `LBAFL` | Lower four bits of User Data Format. | Combines with `LBAFU`. | LBA format selection. |

## Identify Dependencies

| Identify field | Meaning | Affects |
|---|---|---|
| `FNA` bit 0 | Format applies to all namespaces behavior. | Scope for non-secure erase format. |
| `FNA` bit 1 | Secure erase applies to all namespaces behavior. | Scope for `SES=001b/010b`. |
| `FNA` bit 3 | `NSID=FFFFFFFFh` Format NVM support. | Broadcast namespace selector validity. |
| Host Behavior Support `LBAFEE` | LBA Format Extension Enable. | Whether `LBAFU` participates in User Data Format. |
| Identify Namespace LBAF / extended format data | Available user data formats. | Whether selected format is valid. |
