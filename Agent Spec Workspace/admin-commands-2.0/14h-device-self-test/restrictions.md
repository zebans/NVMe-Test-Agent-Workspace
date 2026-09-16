# Device Self-test Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| Reserved `STC` values are not self-test actions | `0h` and `3h`-`Dh` have no defined action. | Command field validation applies. |
| Invalid namespace ID is not accepted | `NSID` in `1h`-`FFFFFFFEh` must identify a valid namespace. | `Invalid Namespace or Format`. |
| Inactive namespace ID is not accepted | A valid but inactive namespace is not a legal target. | `Invalid Field in Command`. |
| Concurrent short/extended self-test is not accepted | Existing in-progress self-test blocks new short/extended request. | `Device Self-test in Progress`. |
| Abort self-test with no operation in progress does not modify log | `STC=Fh` with no self-test in progress completes successfully. | Device Self-test Log unchanged. |

