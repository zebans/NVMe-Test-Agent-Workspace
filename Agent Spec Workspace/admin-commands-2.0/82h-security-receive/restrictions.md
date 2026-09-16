# Security Receive Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| `SECP` unsupported values are invalid | Security Protocol is selected by `SECP`. | `Invalid Field in Command`. |
| `NSSF` is only defined for `SECP=EAh` | For all other Security Protocols, `NSSF` is reserved. | Reserved-field validation applies. |
| Protocol details are outside Base | Payload format and Send/Receive pairing are SPC-5 / protocol-defined. | Use protocol spec for detailed payload validation. |
| Returned data may not be retained across loss/reset | Communication loss or Controller Level Reset may discard receive data. | Host should not assume persistence. |

