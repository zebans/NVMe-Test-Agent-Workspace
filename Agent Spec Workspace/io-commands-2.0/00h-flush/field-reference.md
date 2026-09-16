# Flush Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `NSID` | Namespace Identifier | Namespace(s) whose volatile data/metadata should be flushed. | `FFFFFFFFh` behavior depends on `VWC[2:1]`. | Flush scope and invalid namespace behavior. |
| Identify Controller | `VWC[2:1]` | Flush all-namespace behavior. | `11b` supports all attached namespaces; `10b` rejects `FFFFFFFFh`; `00b` not indicated. | `NSID=FFFFFFFFh` tests. |
| Command-specific fields | Reserved | No command-specific fields. | Host should clear. | Reserved-field validation. |

