# ZNS-Modified Read Selector Reference

| Condition | Meaning | Expected status direction |
|---|---|---|
| LBA range crosses zone boundary | Read range spans more than one zone. | `Zone Boundary Error` (`B8h`). |
| Accessed zone is Offline | Target zone is `ZSO:Offline`. | `Zone Is Offline` (`BBh`). |
