# Namespace Management Restrictions

## Create

| Restriction | Meaning |
|---|---|
| Create does not attach | The namespace exists after Create but is not attached to a controller. |
| `NSID` cleared | Create reserves `NSID`; host clears it to `0h`. |
| Data buffer PRP rule | If PRPs are used, the create data buffer shall not be a PRP List and may not cross more than one page boundary. |
| Command-set-specific bytes | Some create fields are owned by the selected I/O Command Set. |

## Delete

| Restriction / behavior | Meaning |
|---|---|
| Detach side effect | Delete detaches the namespace from all controllers. |
| Detach recommendation | Host software is recommended to detach all controllers before deleting a namespace. |
| Attribute notice | Delete may issue a Namespace Attribute Notice to another controller with notices enabled. |
| `NSID=FFFFFFFFh` | Delete all namespaces; success is possible if there are zero valid namespaces. |

## Support Coupling

If Namespace Management is supported, Namespace Attachment shall also be supported.
