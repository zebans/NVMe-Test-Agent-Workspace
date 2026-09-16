# Authentication Receive Payload Reference

Authentication Receive transfers security protocol status/data from controller to host.

| Payload area | Meaning | Owner |
|---|---|---|
| Data referenced by `SGL1` | Security protocol result/status/data. | SPC-5 / selected security protocol. |
| Length described by `AL` | Security-protocol-specific allocation length. | SPC-5. |

## Retention Rule

Authentication Receive data shall not be retained if communication is lost or if a Controller Level Reset occurs.

## Boundary

This folder does not define the internal returned security protocol payload. Use the selected SPC-5 security protocol definition for returned data layout and command-specific meaning.
