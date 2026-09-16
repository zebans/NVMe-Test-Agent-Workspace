# Security Receive Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data Pointer | Start of host data buffer. | Receives security protocol status/data from controller. | Security payload return. |
| `CDW10` bits 31:24 | `SECP` | Security Protocol. | Unsupported value -> `Invalid Field in Command`. | Protocol selection. |
| `CDW10` bits 23:16 | `SPSP1` | Security Protocol Specific bits 15:08. | Defined by SPC-5 / selected protocol. | Protocol-specific operation. |
| `CDW10` bits 15:08 | `SPSP0` | Security Protocol Specific bits 07:00. | Defined by SPC-5 / selected protocol. | Protocol-specific operation. |
| `CDW10` bits 07:00 | `NSSF` | NVMe Security Specific Field. | Defined for `SECP=EAh`; reserved otherwise. | NVMe-specific security operation. |
| `CDW11` bits 31:00 | `AL` | Allocation Length. | Specific to Security Protocol In with `INC_512=0h`. | Returned payload length. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

