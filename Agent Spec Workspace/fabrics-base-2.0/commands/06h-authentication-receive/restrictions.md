# Authentication Receive Restrictions

Status: `COMMAND-CONTROL-COMPLETE`

- Figure 375 marks Authentication Receive optional.
- Figure 375 marks Authentication Receive as supported on I/O Queues.
- Authentication Receive transfers status and data results of one or more Authentication Send commands.
- The association with previous Authentication Send commands depends on `SECP`.
- Returned data format depends on `SECP`.
- Authentication Receive data shall not be retained if communication is lost or a Controller Level Reset occurs.

