# Capacity Management Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| Create capacity fields only apply to create operations | `Capacity Upper/Lower` are used for Create Endurance Group and Create NVM Set. | Reserved-field validation for other operations. |
| NVM Set operations require NVM Set support | If controller does not support NVM Sets, create/delete NVM Set is not supported. | Command failure per common/field validation. |
| Unknown non-zero capacity entity is invalid | Element Identifier must correspond to relevant existing entity when required. | `Invalid Field in Command`. |
| Delete operations are destructive | Delete Endurance Group deletes contained namespaces/NVM Sets; Delete NVM Set deletes namespaces in that NVM Set. | Test flow must treat as destructive behavior. |

