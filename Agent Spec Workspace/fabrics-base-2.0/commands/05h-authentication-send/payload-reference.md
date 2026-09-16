# Authentication Send Payload Reference

Authentication Send transfers security protocol specific commands, data, or parameters from host to controller.

| Payload area | Meaning | Owner |
|---|---|---|
| Data referenced by `SGL1` | Security protocol specific command/data/parameters. | SPC-5 / selected security protocol. |
| Length described by `TL` | Security-protocol-specific transfer length. | SPC-5. |

## Boundary

This folder does not define the internal security protocol payload. Use the selected SPC-5 security protocol definition for payload layout and command-specific meaning.
