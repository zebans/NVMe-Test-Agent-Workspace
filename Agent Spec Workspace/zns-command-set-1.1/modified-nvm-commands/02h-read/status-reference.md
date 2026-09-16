# ZNS-Modified Read Status Reference

Additional ZNS statuses from ZNS Figure 17:

| Value | Status | Meaning |
|---:|---|---|
| `B8h` | Zone Boundary Error | Command specifies logical blocks in more than one zone. |
| `BBh` | Zone Is Offline | Accessed zone is `ZSO:Offline`. |

Base Read statuses remain owned by the NVM Command Set.
