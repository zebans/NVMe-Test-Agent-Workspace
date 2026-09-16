# Namespace Attachment Selector Reference

## `CDW10.SEL`

| `SEL` | Operation | Meaning |
|---:|---|---|
| `0h` | Controller Attach | Attach controllers listed in the Controller List to the namespace. |
| `1h` | Controller Detach | Detach controllers listed in the Controller List from the namespace. |
| `2h`-`Fh` | Reserved | Reserved selector values. |

## Operation-Specific Expectations

| Operation | Common failure direction |
|---|---|
| Attach controller already attached | `Namespace Already Attached`. |
| Attach private namespace already attached to one controller | `Namespace Is Private`. |
| Attach exceeds `MAXDNA` or `MAXCNA` | `Namespace Attachment Limit Exceeded`. |
| Attach to controller without command-set support | `I/O Command Set Not Supported`. |
| Attach to controller with command set supported but disabled by profile | `I/O Command Set Not Enabled`. |
| Detach controller not attached | `Namespace Not Attached`. |

## Controller List Scope

The command applies to the controllers listed in the 4096-byte Controller List. The Admin controller is not a valid attachment target.
