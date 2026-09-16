# ZNS-Modified Compare Selector Reference

| Condition | Meaning | Expected status direction |
|---|---|---|
| LBA range crosses zone boundary | Compare range spans more than one zone. | `Zone Boundary Error` (`B8h`). |
| Target zone is Full | Accessed zone is `ZSF:Full`. | `Zone Is Full` (`B9h`). |
| Target zone is Read Only | Accessed zone is `ZSRO:Read Only`. | `Zone Is Read Only` (`BAh`). |
| Target zone is Offline | Accessed zone is `ZSO:Offline`. | `Zone Is Offline` (`BBh`). |
| Zone invalid write condition applies | ZNS write-pointer-related invalid condition. | `Zone Invalid Write` (`BCh`). |
| Insufficient active resources | Controller cannot allow additional active zones. | `Too Many Active Zones` (`BDh`). |
| Insufficient open resources | Controller cannot allow additional open zones. | `Too Many Open Zones` (`BEh`). |
