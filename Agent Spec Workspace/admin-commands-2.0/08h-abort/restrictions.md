# Abort Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| Abort is best effort | Completion success does not guarantee target abort. | Check Abort CQE DW0 bit 0. |
| Concurrent Abort limit | Identify Controller `ACL` limits outstanding Abort commands. | `Abort Command Limit Exceeded`. |
| Target completion ordering | Aborted target completion comes before Abort completion. | Completion ordering is part of expected behavior. |

