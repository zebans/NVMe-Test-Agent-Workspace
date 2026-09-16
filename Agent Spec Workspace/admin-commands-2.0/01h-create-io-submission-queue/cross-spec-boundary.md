# Create I/O Submission Queue Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Create I/O Submission Queue command semantics.
- `PRP1`, `CDW10.QSIZE`, `CDW10.QID`, `CDW11.CQID`, `CDW11.QPRIO`, `CDW11.PC`, and `CDW12.NVMSETID` meanings.
- Queue memory validity rules that are stated by the Base Spec.
- SQ-to-CQ binding rules.
- Command-specific status meanings for this command.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Concrete host memory allocation APIs.
- Test flow setup/teardown scripts beyond spec-required preconditions.
- Arbitration policy implementation details beyond field meaning.
- Namespace/NVM Set inventory tables outside the field-level rule.
