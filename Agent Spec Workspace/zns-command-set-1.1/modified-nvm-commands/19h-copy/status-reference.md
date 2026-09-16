# ZNS-Modified Copy Status Reference

Additional ZNS statuses from ZNS Figure 14:

| Value | Status | Meaning |
|---:|---|---|
| `B8h` | Zone Boundary Error | A Source Range Entry contains logical blocks in more than one zone, or the destination LBA range contains logical blocks in more than one zone. |
| `B9h` | Zone Is Full | Destination zone is `ZSF:Full`. |
| `BAh` | Zone Is Read Only | Destination zone is `ZSRO:Read Only`. |
| `BBh` | Zone Is Offline | Source range zone or destination range zone is `ZSO:Offline`. |
| `BCh` | Zone Invalid Write | Destination write was not at the write pointer. |
| `BDh` | Too Many Active Zones | Controller does not allow additional active zones. |
| `BEh` | Too Many Open Zones | Controller does not allow additional open zones. |

Base Copy statuses remain owned by the NVM Command Set.
