# Directive Send Status Reference

| Status | Applies when | Test/FW interpretation |
|---|---|---|
| `Invalid Field in Command` | `DTYPE` is not supported, disabled, or reserved; `DOPER` is reserved for the selected `DTYPE`; Identify Enable Directive targets `DTYPE=00h`; Enable Directive requests an unsupported directive; operation uses an invalid `NSID` such as `FFFFFFFFh` where section 8.7 prohibits it. | Selector or operation is invalid before directive-specific work proceeds. |
| `Stream Resource Allocation Failed` (`7Fh`) | Streams Allocate Resources cannot allocate exclusive namespace resources and no NVM subsystem stream resources are available. | Streams-specific resource failure from section 8.7.3. |
| `Namespace is Write Protected` | Namespace write-protection state prohibits a directive operation that would modify namespace-related directive state. | Treat as namespace protection, not selector decode failure. |

Status values outside this table may still come from common Admin completion behavior, transport failure, or vendor-specific behavior.
