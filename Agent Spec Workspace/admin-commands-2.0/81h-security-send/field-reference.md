# Security Send Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data Pointer | Start of host data buffer. | Transfers security protocol data to controller. | Security payload transfer. |
| `CDW10` bits 31:24 | `SECP` | Security Protocol. | Reserved value -> `Invalid Field in Command`. | Protocol selection. |
| `CDW10` bits 23:16 | `SPSP1` | Security Protocol Specific bits 15:08. | Defined by SPC-5 / selected protocol. | Protocol-specific operation. |
| `CDW10` bits 15:08 | `SPSP0` | Security Protocol Specific bits 07:00. | Defined by SPC-5 / selected protocol. | Protocol-specific operation. |
| `CDW10` bits 07:00 | `NSSF` | NVMe Security Specific Field. | Defined for `SECP=EAh`; reserved otherwise. | NVMe-specific security operation. |
| `CDW11` bits 31:00 | `TL` | Transfer Length. | Specific to Security Protocol Out with `INC_512=0h`. | Payload length. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

