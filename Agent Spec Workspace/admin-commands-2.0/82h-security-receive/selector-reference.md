# Security Receive Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Security Protocol | `CDW10.SECP` bits 31:24 | Security protocol as defined in SPC-5. |
| SP Specific 1 | `CDW10.SPSP1` bits 23:16 | Bits 15:08 of Security Protocol Specific field. |
| SP Specific 0 | `CDW10.SPSP0` bits 15:08 | Bits 07:00 of Security Protocol Specific field. |
| NVMe Security Specific Field | `CDW10.NSSF` bits 07:00 | Defined for Security Protocol `EAh`; reserved for other protocols. |
| Allocation Length | `CDW11.AL` bits 31:00 | Allocation length for Security Protocol In command with `INC_512=0h` as defined in SPC-5. |

## Security Protocol Values Called Out By Base

| `SECP` | Meaning |
|---|---|
| `00h` | Security discovery; returns information about security protocols supported by the controller. Not associated with a Security Send command. |
| `EAh` | Assigned for NVMe interface use. |

## Security Protocol `EAh`

| `SPSP` value | `NSSF` meaning |
|---|---|
| `0001h` | Replay Protected Memory Block (RPMB) Target. |
| `0002h`-`FFFFh` | Reserved. |

