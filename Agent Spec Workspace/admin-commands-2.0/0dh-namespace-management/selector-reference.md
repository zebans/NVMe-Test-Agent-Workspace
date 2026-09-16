# Namespace Management Selector Reference

## `CDW10.SEL`

| `SEL` | Operation | Meaning |
|---:|---|---|
| `0h` | Create | Create a namespace using the create data buffer and `CDW11.CSI`. |
| `1h` | Delete | Delete the namespace specified by `NSID`, or all namespaces with `NSID=FFFFFFFFh`. |
| `2h`-`Fh` | Reserved | Reserved selector values. |

## `CDW11.CSI`

| Operation | `CSI` meaning |
|---|---|
| Create | Selects the I/O Command Set of the namespace being created. |
| Delete | Reserved; should be cleared. |

## `NSID`

| Operation | `NSID` rule |
|---|---|
| Create | Reserved and cleared to `0h`. |
| Delete single namespace | Identifies the namespace to delete. |
| Delete all namespaces | `FFFFFFFFh` deletes all namespaces and succeeds if there are zero valid namespaces. |

## Test-Relevant Selector Boundaries

| Case | Expected direction |
|---|---|
| Reserved `SEL` | Invalid field style failure. |
| Create with unsupported `CSI` | `I/O Command Set Not Supported`. |
| Create with invalid I/O command-set association | `Invalid I/O Command Set`. |
| Delete with `NSID=FFFFFFFFh` | All namespaces deletion path; success is possible even when no valid namespaces exist. |
