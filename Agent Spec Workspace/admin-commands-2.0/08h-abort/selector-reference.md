# Abort Selector Reference

| Selector | Location | Meaning | Important rule |
|---|---|---|---|
| Submission Queue Identifier | `CDW10.SQID` bits 15:00 | Submission Queue associated with the target command. | Selects where the target command was submitted. |
| Command Identifier | `CDW10.CID` bits 31:16 | Command Identifier of the target command. | Matches `CDW0.CID` of the command being aborted. |
| Abort Command Limit | Identify Controller `ACL` | Maximum concurrently outstanding Abort commands. | Excess Abort commands may complete with `Abort Command Limit Exceeded`. |

