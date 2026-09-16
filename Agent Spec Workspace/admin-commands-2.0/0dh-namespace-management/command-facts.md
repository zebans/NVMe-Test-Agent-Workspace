# Namespace Management Command Facts

Source: NVMe Base Spec 2.0 section 5.23, Figures 297-302.

| Item | Value |
|---|---|
| Command | Namespace Management |
| Opcode | `0Dh` |
| Command set | Admin |
| Data transfer | Host to controller |
| Namespace | `NSID` used |
| Main selector | `CDW10.SEL` |
| Create command-set selector | `CDW11.CSI` |

## Required Command Behavior

| Operation | Required behavior |
|---|---|
| Create | Creates a namespace. The namespace is not attached to any controller by this command. |
| Delete | Deletes a namespace. Delete detaches the namespace from all controllers as a side effect. |
| Namespace Management support | If Namespace Management is supported, Namespace Attachment shall also be supported. |
| Completion | Posts a CQE to the Admin Completion Queue. For Create, CQE Dword 0 contains the created `NSID`. |

## High-Signal Side Effects

| Condition | Effect |
|---|---|
| Create succeeds | New namespace exists but is not attached. |
| Delete succeeds | Namespace is detached from all controllers and deleted. |
| Namespace attached to another controller with Namespace Attribute Notices enabled | Delete may issue a Namespace Attribute Notice. |
| `NSID=FFFFFFFFh` with Delete | Deletes all namespaces and succeeds if there are zero valid namespaces. |
