# Device Self-test Selector Reference

## Namespace Selector

| `NSID` value | Meaning | Error condition |
|---|---|---|
| `00000000h` | Test includes controller only and no namespaces. | None for this selector value. |
| `00000001h`-`FFFFFFFEh` | Test includes the specified namespace. | Invalid namespace ID -> `Invalid Namespace or Format`; inactive namespace ID -> `Invalid Field in Command`. |
| `FFFFFFFFh` | Test includes all active namespaces accessible through the controller when the operation starts. | Not a single namespace selector. |

## Self-test Code Selector

| `CDW10.STC` value | Meaning |
|---|---|
| `0h` | Reserved. |
| `1h` | Start short device self-test operation. |
| `2h` | Start extended device self-test operation. |
| `3h`-`Dh` | Reserved. |
| `Eh` | Vendor specific. |
| `Fh` | Abort device self-test operation. |

