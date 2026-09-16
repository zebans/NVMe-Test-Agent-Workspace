# Security Receive Payload Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | Security protocol status/data | Returned from controller to host. |
| Completion | CQE on Admin Completion Queue | Reports Security Receive command status. |

## Security Protocol `00h`

Security Receive with `SECP=00h` returns information about security protocols supported by the controller. It is used in security discovery and is not associated with a Security Send command.

## Retention Rule

Security Receive data may not be retained if communication is lost between controller and host, or if a Controller Level Reset occurs.

