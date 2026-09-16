# ZNS-Modified Write Zeroes Status Reference

Additional ZNS statuses from ZNS Figure 21:

| Value | Status | Meaning |
|---:|---|---|
| `B8h` | Zone Boundary Error | Command specifies logical blocks in more than one zone. |
| `B9h` | Zone Is Full | Accessed zone is `ZSF:Full`. |
| `BAh` | Zone Is Read Only | Accessed zone is `ZSRO:Read Only`. |
| `BBh` | Zone Is Offline | Accessed zone is `ZSO:Offline`. |
| `BCh` | Zone Invalid Write | Operation was not valid at the write pointer. |
| `BDh` | Too Many Active Zones | Controller does not allow additional active zones. |
| `BEh` | Too Many Open Zones | Controller does not allow additional open zones. |

Base Write Zeroes statuses remain owned by the NVM Command Set.
