# ZNS-Modified Copy Selector Reference

These are ZNS conditions derived from the base Copy command's source ranges and destination range.

| Condition | Applies to | Expected status direction |
|---|---|---|
| Source Range Entry crosses zone boundary | Source | `Zone Boundary Error` (`B8h`). |
| Destination LBA range crosses zone boundary | Destination | `Zone Boundary Error` (`B8h`). |
| Destination zone is Full | Destination | `Zone Is Full` (`B9h`). |
| Destination zone is Read Only | Destination | `Zone Is Read Only` (`BAh`). |
| Source zone is Offline | Source | `Zone Is Offline` (`BBh`). |
| Destination zone is Offline | Destination | `Zone Is Offline` (`BBh`). |
| Destination write not at write pointer | Destination | `Zone Invalid Write` (`BCh`). |
| Insufficient active resources | Destination / resource model | `Too Many Active Zones` (`BDh`). |
| Insufficient open resources | Destination / resource model | `Too Many Open Zones` (`BEh`). |
