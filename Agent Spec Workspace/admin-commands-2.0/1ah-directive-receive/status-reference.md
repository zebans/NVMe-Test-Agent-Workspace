# Directive Receive Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Invalid Field in Command` | `DTYPE` is not supported, disabled, or reserved; `DOPER` is reserved for selected `DTYPE`; Identify Return Parameters uses `NSID=FFFFFFFFh`; other section 8.7 selector constraints are violated. | Selector or operation is invalid before directive-specific data is returned. |
| `Stream Resource Allocation Failed` (`7Fh`) | Streams Allocate Resources cannot allocate exclusive namespace resources and no NVM subsystem stream resources are available. | Streams-specific resource failure from section 8.7.3. |
| `Namespace is Write Protected` | Command is prohibited while the namespace is write protected. | Directive operation is blocked by namespace write protection. |

Status values outside this table may still come from common Admin completion behavior, transport failure, or vendor-specific behavior.
