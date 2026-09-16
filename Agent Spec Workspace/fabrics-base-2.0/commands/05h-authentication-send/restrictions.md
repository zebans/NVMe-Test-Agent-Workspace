# Authentication Send Restrictions

Status: `COMMAND-CONTROL-COMPLETE`

- Figure 375 marks Authentication Send optional.
- Figure 375 marks Authentication Send as supported on I/O Queues.
- The data structure transferred contains security protocol specific commands, data, or parameters.
- Returned status/data for those security protocol specific commands are retrieved with Authentication Receive.
- The association between Authentication Send and later Authentication Receive is Security Protocol field dependent as defined in SPC-5.

