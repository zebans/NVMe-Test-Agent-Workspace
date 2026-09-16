# Get LBA Status Field Reference

| Field surface | Base meaning | Detailed owner |
|---|---|---|
| Admin opcode | `86h` identifies Get LBA Status. | Base Spec opcode table |
| Data buffer | Controller-to-host transfer. | Applicable NVM/ZNS Command Set |
| `NSID` | Used; `FFFFFFFFh` is not supported. | Base opcode note plus command-set definition |
| Capability | Identify Controller Get LBA Status capability bit indicates support. | Base Identify Controller data structure |
| Command-specific fields | Not expanded in Base Spec 2.0 Admin command sections. | Applicable NVM/ZNS Command Set |

## NVM Command Set Detail Routing

| Surface | NVM owner | Lookup note |
|---|---|---|
| Command purpose | NVM Command Set section 5.8 and 4.2.1 | Identify Potentially Unrecoverable LBAs in a requested range. |
| Request fields | NVM Command Set section 4.2.1 | Uses Data Pointer and CDW10-CDW13; Base does not define these dwords. |
| Returned descriptors | NVM Command Set LBA Status Descriptor List | May return zero or more LBA Status Descriptors per LBA Range Descriptor reported by the LBA Status Information log. |
| `ATYPE` behavior | NVM Command Set section 4.2.1 | `ATYPE=10h` requests Untracked LBAs and may require significant controller scanning time. |
| Related log page | NVM Command Set LID `0Eh` LBA Status Information | Host usually reads this log before issuing targeted Get LBA Status commands. |
