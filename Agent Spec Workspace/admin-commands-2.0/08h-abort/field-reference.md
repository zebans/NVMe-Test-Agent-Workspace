# Abort Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW10` bits 31:16 | `CID` | Target command identifier. | Same value as target command `CDW0.CID`. | Which command may be aborted. |
| `CDW10` bits 15:00 | `SQID` | Target Submission Queue Identifier. | Queue where target command is associated. | Which queue is searched for the target command. |
| Abort CQE DW0 bit 0 | Abort result | Whether the target command was aborted. | `0` = target command aborted; `1` = target command was not aborted. | Pass/fail interpretation for abort result. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

