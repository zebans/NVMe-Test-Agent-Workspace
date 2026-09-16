# ZNS-Modified Flush Field Reference

ZNS does not redefine base Flush command fields. Use the NVM Command Set reference for byte-exact Flush fields.

| ZNS-relevant value | Meaning | Why it matters |
|---|---|---|
| Specified zone state | Whether the relevant zone is Offline. | Drives the ZNS-added `Zone Is Offline` status. |
