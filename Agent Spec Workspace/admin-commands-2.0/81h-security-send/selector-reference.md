# Security Send Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Security Protocol | `CDW10.SECP` bits 31:24 | Security protocol as defined in SPC-5. |
| SP Specific 1 | `CDW10.SPSP1` bits 23:16 | Bits 15:08 of Security Protocol Specific field. |
| SP Specific 0 | `CDW10.SPSP0` bits 15:08 | Bits 07:00 of Security Protocol Specific field. |
| NVMe Security Specific Field | `CDW10.NSSF` bits 07:00 | Defined for Security Protocol `EAh`; reserved for other protocols. |
| Transfer Length | `CDW11.TL` bits 31:00 | Length for Security Protocol Out command with `INC_512=0h` as defined in SPC-5. |

## Security Protocol `EAh`

| `SPSP` value | `NSSF` meaning |
|---|---|
| `0001h` | Replay Protected Memory Block (RPMB) Target. |
| `0002h`-`FFFFh` | Reserved. |

