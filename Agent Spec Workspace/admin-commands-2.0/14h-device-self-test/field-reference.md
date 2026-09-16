# Device Self-test Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `NSID` | Namespace Identifier | Selects controller-only, one namespace, or all active namespaces. | `0h`, `1h`-`FFFFFFFEh`, `FFFFFFFFh`. | Test coverage scope and namespace error cases. |
| `CDW10` bits 03:00 | `STC` | Self-test Code. | `1h` short, `2h` extended, `Eh` vendor specific, `Fh` abort. | Starts or aborts self-test. |
| `CDW10` bits 31:04 | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |
| Identify Controller | `DSTO` bit 0 | Defines whether in-progress scope is controller or NVM subsystem. | `0` = controller scope; `1` = NVM subsystem scope. | `Device Self-test in Progress` interpretation. |

