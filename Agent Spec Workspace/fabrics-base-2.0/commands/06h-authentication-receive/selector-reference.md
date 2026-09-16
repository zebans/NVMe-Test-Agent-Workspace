# Authentication Receive Selector Reference

| Selector | Meaning | Owner |
|---|---|---|
| `SECP` | Security Protocol. | SPC-5. |
| `SPSP0` | Bits `07:00` of Security Protocol Specific field. | SPC-5. |
| `SPSP1` | Bits `15:08` of Security Protocol Specific field. | SPC-5. |
| `AL` | Allocation Length. | Security-protocol-specific as defined in SPC-5 where `INC_512` is cleared. |

If a reserved `SECP` value is specified, the controller aborts the command with `Invalid Parameter` indicated.

## Pairing Rule

Authentication Receive gets status/data for one or more previous Authentication Send commands. The association is Security Protocol dependent, not globally defined by Base Fabrics.
