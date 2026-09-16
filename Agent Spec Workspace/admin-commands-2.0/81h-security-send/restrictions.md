# Security Send Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| `SECP` reserved values are invalid | Security Protocol is selected by `SECP`. | `Invalid Field in Command`. |
| `NSSF` is only defined for `SECP=EAh` | For all other Security Protocols, `NSSF` is reserved. | Reserved-field validation applies. |
| Protocol details are outside Base | Payload format and Send/Receive pairing are SPC-5 / protocol-defined. | Use protocol spec for detailed payload validation. |

