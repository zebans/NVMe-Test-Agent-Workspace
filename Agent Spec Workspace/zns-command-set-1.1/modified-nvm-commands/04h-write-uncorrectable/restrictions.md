# ZNS-Modified Write Uncorrectable Restrictions

| Condition | Expected status / rule |
|---|---|
| Write Uncorrectable range spans more than one zone | `Zone Boundary Error` (`B8h`). |
| Target zone is `ZSF:Full` | `Zone Is Full` (`B9h`). |
| Target zone is `ZSRO:Read Only` | `Zone Is Read Only` (`BAh`). |
| Target zone is `ZSO:Offline` | `Zone Is Offline` (`BBh`). |
| Operation is not valid at the zone write pointer | `Zone Invalid Write` (`BCh`). |
| Command would require another active zone resource and none is available | `Too Many Active Zones` (`BDh`). |
| Command would require another open zone resource and none is available | `Too Many Open Zones` (`BEh`). |
