# Security Send Payload Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | Security protocol data | Security protocol specific commands and data/parameters transferred to controller. |
| Completion | CQE on Admin Completion Queue | Reports Security Send command status. |

## Association With Security Receive

The relationship between a Security Send command and a later Security Receive command is Security Protocol dependent and defined in SPC-5.

