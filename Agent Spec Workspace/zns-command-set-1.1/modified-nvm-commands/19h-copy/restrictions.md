# ZNS-Modified Copy Restrictions

| Condition | Expected status / rule |
|---|---|
| Source Range Entry spans more than one zone | `Zone Boundary Error` (`B8h`). |
| Destination LBA range spans more than one zone | `Zone Boundary Error` (`B8h`). |
| Destination zone is `ZSF:Full` | `Zone Is Full` (`B9h`). |
| Destination zone is `ZSRO:Read Only` | `Zone Is Read Only` (`BAh`). |
| Source or destination zone is `ZSO:Offline` | `Zone Is Offline` (`BBh`). |
| Destination write is not at the zone write pointer | `Zone Invalid Write` (`BCh`). |
| Destination transition/resource usage exceeds active resource limit | `Too Many Active Zones` (`BDh`). |
| Destination transition/resource usage exceeds open resource limit | `Too Many Open Zones` (`BEh`). |
