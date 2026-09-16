# ZNS-Modified Write Uncorrectable Selector Reference

| Condition | Meaning | Expected status direction |
|---|---|---|
| LBA range crosses zone boundary | Range spans more than one zone. | `Zone Boundary Error` (`B8h`). |
| Target zone is Full | Accessed zone is `ZSF:Full`. | `Zone Is Full` (`B9h`). |
| Target zone is Read Only | Accessed zone is `ZSRO:Read Only`. | `Zone Is Read Only` (`BAh`). |
| Target zone is Offline | Accessed zone is `ZSO:Offline`. | `Zone Is Offline` (`BBh`). |
| Operation not at write pointer | Write-pointer validity fails. | `Zone Invalid Write` (`BCh`). |
| Insufficient active resources | Controller cannot allow additional active zones. | `Too Many Active Zones` (`BDh`). |
| Insufficient open resources | Controller cannot allow additional open zones. | `Too Many Open Zones` (`BEh`). |
