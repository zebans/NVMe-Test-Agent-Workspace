# Capacity Management Payload / Effect Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | None | Capacity Management has no data transfer. |
| Completion | CQE on Admin Completion Queue | Reports command status. |

## Operation Effects

| Operation | Effect |
|---|---|
| Select Capacity Configuration with non-zero Element Identifier | Creates Endurance Groups and NVM Sets from the selected Capacity Configuration Descriptor when Media Unit Status Selected Configuration is `0h`. |
| Select Capacity Configuration with Element Identifier `0h` | Clears configuration: deletes namespaces, NVM Sets if any, Endurance Groups, then clears Selected Configuration to `0h`. |
| Create Endurance Group | Creates an Endurance Group with capacity from `Capacity Upper:Capacity Lower`. |
| Delete Endurance Group | Deletes the Endurance Group and all namespaces/NVM Sets it contains. |
| Create NVM Set | Creates an NVM Set in the specified or controller-selected Endurance Group. |
| Delete NVM Set | Deletes the NVM Set and all namespaces in the NVM Set. |

