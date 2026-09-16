# ZNS-Modified Write Selector Reference

These are not new command selectors. They are ZNS conditions derived from the base Write command range and the target zone.

| Condition | Meaning | Expected status direction |
|---|---|---|
| LBA range crosses zone boundary | Write range spans more than one zone. | `Zone Boundary Error` (`B8h`). |
| Target zone is Full | Accessed zone is `ZSF:Full`. | `Zone Is Full` (`B9h`). |
| Target zone is Read Only | Accessed zone is `ZSRO:Read Only`. | `Zone Is Read Only` (`BAh`). |
| Target zone is Offline | Accessed zone is `ZSO:Offline`. | `Zone Is Offline` (`BBh`). |
| Write not at write pointer | Sequential Write Required write is not at `WP`. | `Zone Invalid Write` (`BCh`). |
| Insufficient active resources | Controller cannot allow additional active zones. | `Too Many Active Zones` (`BDh`). |
| Insufficient open resources | Controller cannot allow additional open zones. | `Too Many Open Zones` (`BEh`). |
