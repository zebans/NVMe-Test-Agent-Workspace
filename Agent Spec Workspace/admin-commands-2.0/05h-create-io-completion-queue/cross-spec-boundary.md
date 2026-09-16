# Create I/O Completion Queue Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Create I/O Completion Queue command semantics.
- `PRP1`, `CDW10.QSIZE`, `CDW10.QID`, `CDW11.IV`, `CDW11.IEN`, and `CDW11.PC` meanings.
- Queue memory validity rules that are stated by the Base Spec.
- Command-specific status meanings for this command.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Concrete host memory allocation APIs.
- Test flow setup/teardown scripts.
- Transport-specific interrupt vector definitions beyond the Base Spec boundary note.
