# Directive Send Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| `NSID=FFFFFFFFh` is conditional | Support depends on Directive Operation. | Use section 8.7 operation rule. |
| `CDW12/CDW13` are conditional | They may be used based on `DTYPE`/`DOPER`. | Section 8.7 owns interpretation. |
| Payload is directive-dependent | Base defines command shell, not every directive payload. | Read directive-specific reference before payload validation. |

