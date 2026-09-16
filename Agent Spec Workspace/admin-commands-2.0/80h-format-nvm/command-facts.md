# Format NVM Command Facts

Source: NVMe Base Specification 2.0, section 5.14, Figures 188-190.

## Command Identity

| Item | Value |
|---|---|
| Command | Format NVM |
| Admin opcode | `80h` |
| Data transfer | No data |
| Data pointer | Not used |
| NSID | Used |
| Primary selector | `NSID`, `CDW10.SES`, `CDW10.LBAFU:LBAFL` |

## Command Dwords

| Dword | Bits | Field | Meaning | Test/FW impact |
|---|---:|---|---|---|
| CDW10 | 13:12 | `LBAFU` | Upper two bits of User Data Format. | Ignored if Host Behavior Support `LBAFEE=0`. |
| CDW10 | 11:09 | `SES` | Secure Erase Settings. | Selects no secure erase, user data erase, or cryptographic erase. |
| CDW10 | 08 | `PIL` | Protection Information Location. | I/O Command Set specific. |
| CDW10 | 07:05 | `PI` | Protection Information. | I/O Command Set specific. |
| CDW10 | 04 | `MSET` | Metadata Settings. | I/O Command Set specific. |
| CDW10 | 03:00 | `LBAFL` | Lower four bits of User Data Format. | Combines with `LBAFU` when `LBAFEE=1`. |

## Completion

The controller posts the CQE when the media format is complete. After successful completion, the controller shall not return previous user data from affected namespaces.
