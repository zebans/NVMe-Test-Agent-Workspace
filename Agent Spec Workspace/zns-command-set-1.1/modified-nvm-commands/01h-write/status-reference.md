# ZNS-Modified Write Status Reference

Additional ZNS statuses from ZNS Figure 19:

| Value | Status | Meaning |
|---:|---|---|
| `B8h` | Zone Boundary Error | Command specifies logical blocks in more than one zone. |
| `B9h` | Zone Is Full | Accessed zone is `ZSF:Full`. |
| `BAh` | Zone Is Read Only | Accessed zone is `ZSRO:Read Only`. |
| `BBh` | Zone Is Offline | Accessed zone is `ZSO:Offline`. |
| `BCh` | Zone Invalid Write | Write was not at the write pointer. |
| `BDh` | Too Many Active Zones | Controller does not allow additional active zones. |
| `BEh` | Too Many Open Zones | Controller does not allow additional open zones. |

Base Write statuses remain owned by the NVM Command Set.
