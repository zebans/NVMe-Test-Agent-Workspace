# SPEC Markdown Checklist

This checklist validates whether the `NVMe Spec` markdown layer is reliable for future Codex Agents.
Use it to check:
- Source fidelity and completeness of extracted SPEC markdown.
- Agent lookup routing across root indexes, command folders, MCTP layers, and cross-spec boundaries.
- Separation between SPEC facts, test-flow design, and PyNVMe API mapping.

This checklist belongs to the SPEC layer. It does not replace PyNVMe API checks, test-flow checks, or source-fidelity spot checks.

## Pass/Fail Review Template

Use this template for each review run.

```text
Date:
Reviewer / Agent:
Scope:
Command(s):

Result:
- PASS:
- FAIL:
- BLOCKED:

Evidence:
- Files read:
- Source sections / figures checked:
- Issues found:

Notes:
```

## 1. File Structure Checklist

- [ ] `SPEC_AGENTS.md` exists at the `NVMe Spec` root.
- [ ] `SPEC_REFERENCE_GUIDE.md` exists at the `NVMe Spec` root.
- [ ] `Base_Spec_2_0_Index.md` exists at the `NVMe Spec` root.
- [ ] `Admin_Command_Spec_Table.md` exists at the `NVMe Spec` root.
- [ ] `IO_Command_Spec_Table.md` exists at the `NVMe Spec` root.
- [ ] `Status_Code_Reference.md` exists at the `NVMe Spec` root.
- [ ] `Command_Status_Matrix.md` exists at the `NVMe Spec` root.
- [ ] `admin-commands-2.0\` exists.
- [ ] `io-commands-2.0\` exists.
- [ ] Each command folder has at least `README.md` and a canonical facts/reference entry file.
- [ ] Expanded command folders include only files that match real command complexity.

Expected evidence:

```text
List root files.
List command folders.
List missing README.md or canonical entry files, if any.
```

## 2. Source Fidelity Checklist

- [ ] The primary source is always:

```text
NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

- [ ] Each root table states its source section or figure.
- [ ] Command facts cite section and figure numbers when available.
- [ ] Opcode, command name, queue type, data transfer direction, and NSID usage match the Base Spec source.
- [ ] Reserved values are not invented.
- [ ] Optional behavior is marked as optional or conditional, not mandatory.
- [ ] Missing facts are not filled from memory.
- [ ] If the local extracted markdown is incomplete, the answer uses:

```text
Not explicitly found in the local NVMe Base Specification 2.0 source.
```

Expected evidence:

```text
Source file checked:
Section / figure:
Markdown file checked:
Field or fact compared:
PASS / FAIL:
```

## 2A. Spec Content Completeness Checklist

This section checks whether the extracted markdown is complete enough for reliable command lookup.

- Markdown must map back to the Base Spec source.
- Missing fields, selectors, payload structures, restrictions, or status rules must be recorded explicitly.

For each audited command, compare the command markdown against the full local Base Spec section, not only against root tables.

- [ ] The command's source section was opened from the local Base Spec source.
- [ ] Every command-specific figure/table in that section was identified.
- [ ] Every command-specific field was classified as used, reserved, ignored, selector, data pointer, or command-specific payload.
- [ ] Every selector/action value defined in the section was captured or explicitly marked as not yet extracted.
- [ ] Every input data structure defined in the section was captured or explicitly marked as not yet extracted.
- [ ] Every output data structure defined in the section was captured or explicitly marked as not yet extracted.
- [ ] Every normative behavior statement using terms such as shall, shall not, may, should, required, optional, abort, fail, complete, return, or support was reviewed.
- [ ] Every command-specific completion rule was captured or explicitly marked as not yet extracted.
- [ ] Every command-specific status code mention was captured or explicitly marked as not yet extracted.
- [ ] Every namespace, controller, queue, sanitize, format, reservation, capability, or feature dependency was captured or explicitly marked as not yet extracted.
- [ ] Every cross-reference to another section, figure, feature, data structure, or external specification was captured or explicitly marked as not yet extracted.
- [ ] Every delegated behavior is marked as delegated instead of filled in from memory.
- [ ] Every missing but relevant rule is recorded in an audit note.

Completeness status must use one of these labels:

| Label | Meaning |
|---|---|
| `COMPLETE` | The command section was fully audited against the Base Spec source and no known relevant rule is missing from markdown. |
| `PARTIAL` | The markdown has useful facts, but some fields, structures, statuses, or rules still need extraction. |
| `SKELETON` | The folder is only a reference anchor with `README.md` and a minimal canonical entry file; it is not content-complete. |
| `BLOCKED` | The local source is unclear, corrupted, missing, or requires another specification. |

Expected evidence:

```text
Command:
Base Spec section:
Figures / tables reviewed:
Normative statements reviewed:
Fields reviewed:
Data structures reviewed:
Status rules reviewed:
Cross-spec references reviewed:
Completeness label:
Missing rules:
Required markdown updates:
```

## 3. Command Folder Checklist

For each command folder:

- [ ] `README.md` identifies command name, opcode, section, table/figure, queue type, data transfer direction, and NSID rule.
- [ ] `command-facts.md` exists for expanded command folders and provides opcode, command dwords, command-control rules, and reading guidance.
- [ ] `command-facts.md` does not contain concrete PyNVMe API calls.
- [ ] `command-facts.md` does not prescribe a full test sequence.
- [ ] `command-facts.md` clearly marks delegated behavior or points to `cross-spec-boundary.md`.
- [ ] If the command uses selectors, the folder either has `selector-reference.md` or clearly says selector details are not yet expanded.
- [ ] If the command uses input/output payloads, the folder either has `payload-reference.md` or clearly says payload details are not yet expanded.
- [ ] If the command has payload fields/bits/enum values useful to tests or firmware interpretation, the folder either has `field-reference.md` or clearly says field lookup is not yet expanded.
- [ ] If the command has nontrivial status behavior, the folder either has `status-reference.md` or clearly says status details are not yet expanded.

Expanded command folders may include:

```text
command-facts.md
selector-reference.md
field-reference.md
payload-reference.md
status-reference.md
restrictions.md
cross-spec-boundary.md
COMMAND_CONTENT_AUDIT.md
```

Do not require every command to have every file.

## 4. Status And Completion Checklist

- [ ] Global status definitions live in `Status_Code_Reference.md`.
- [ ] Command-specific status references live in the command folder or `Command_Status_Matrix.md`.
- [ ] The command folder does not duplicate the entire global status table unless there is a clear reason.
- [ ] Generic status, command-specific status, media/data integrity status, and path related status are not mixed together without SCT context.
- [ ] Completion behavior is stated separately from command operation behavior.
- [ ] Status applicability is marked as explicit, inferred from global status, or not found.

Expected evidence:

```text
Status Code Type:
Status Code:
Source figure / section:
Command-specific applicability:
```

## 5. Cross-Spec Boundary Checklist

- [ ] Base Spec-owned behavior is separated from I/O Command Set-specific behavior.
- [ ] NVM, ZNS, KV, Fabrics, MI, and vendor-specific details are not invented inside Base Spec-only files.
- [ ] Command-set-specific CNS/LID/FID/opcode behavior is marked as delegated.
- [ ] Vendor-specific opcode ranges identify the range only, unless a vendor document is added.
- [ ] If a future test needs delegated details, the markdown says which external spec layer is required.

Expected wording:

```text
Delegated to the applicable I/O Command Set specification.
Delegated to vendor-specific documentation.
Not explicitly found in the local NVMe Base Specification 2.0 source.
```

## 6. Token-Efficient Reading Checklist

Default read path:

```text
SPEC_AGENTS.md
Base_Spec_2_0_Index.md
Admin_Command_Spec_Table.md or IO_Command_Spec_Table.md
target command folder/README.md
target command folder/command-facts.md or equivalent canonical entry file
```

- [ ] The agent does not open the full Base Spec source by default.
- [ ] The agent reads `README.md` and `command-facts.md` before specialized command files for expanded folders.
- [ ] The agent reads only the specialized file that matches the missing detail.
- [ ] The agent opens the full Base Spec source only when extracted markdown is missing, inconsistent, incomplete, or the user explicitly requests original-source verification.
- [ ] When the full source is opened, only the relevant section or figure is used when possible.
- [ ] The agent reports which markdown files were read when asked.

Concrete conditions for reading beyond `command-facts.md`:

- [ ] Exact CDW, NSID, Data Pointer, or reserved-field rules are needed.
- [ ] Behavior changes by selector, action, FID, LID, CNS, DTYPE, DOPER, reservation action/type, or another command-specific value.
- [ ] Input or output data structure layout is needed.
- [ ] A payload field, bit, byte offset, enum, or capability meaning is needed.
- [ ] Exact completion behavior or status-code applicability is needed.
- [ ] State, sanitize, format, destructive, namespace, media, queue, ordering, or capability restrictions are needed.
- [ ] Behavior may be delegated to another NVMe spec or vendor document.
- [ ] `command-facts.md` explicitly says another file should be checked.

## 7. API Layer Boundary Checklist

- [ ] SPEC markdown does not include PyNVMe fixture names as required usage.
- [ ] SPEC markdown does not include concrete Python calls such as `nvme0.identify(...)`, `nvme0n1.write(...)`, or pytest assertions.
- [ ] SPEC markdown does not decide which PyNVMe API should implement a behavior.
- [ ] SPEC markdown may hand off to the API layer for later implementation mapping.
- [ ] A missing or changing API-layer entry point does not fail SPEC-layer completion.
- [ ] Do not record a concrete API-layer path until that layer has a stable canonical entry point.

- [ ] If an answer needs implementation mapping, the spec layer stops at spec facts and hands off to the API layer.

Allowed boundary statement:

```text
This is a spec-layer fact. Concrete PyNVMe3 API mapping belongs to the API layer.
```

## 8. Test Flow Input Boundary Checklist

- [ ] SPEC markdown may provide facts that a future test-flow layer can use.
- [ ] SPEC markdown may identify preconditions stated by the Base Spec.
- [ ] SPEC markdown may identify expected behavior and completion/status facts.
- [ ] SPEC markdown must not prescribe complete testcase order.
- [ ] SPEC markdown must not prescribe setup/cleanup sequence unless the Base Spec explicitly defines ordering.
- [ ] SPEC markdown must not decide DUT-specific policy.
- [ ] SPEC markdown must not decide script style, command line, fixture usage, or retry strategy.

Allowed output to test-flow layer:

```text
Spec precondition:
Spec action meaning:
Expected spec behavior:
Completion/status facts:
Delegated or missing details:
```

Not allowed in SPEC markdown:

```text
Use this fixture.
Run this pytest.
Call this API.
Wait 10 seconds.
Retry three times.
```

## 9. Sample Validation Prompts

Use these prompts to test whether the markdown and agent behavior are correct.

### Prompt A: Identify Selector

```text
Read NVMe Spec/SPEC_AGENTS.md and answer Identify CNS=01h as spec facts.
Read only the needed markdown first; do not open the full Base Spec unless the extracted markdown is insufficient.
Tell me which md files you read and why.
```

Expected behavior:

- Reads root agent/index/table files.
- Reads `admin-commands-2.0\06h-identify\command-facts.md`, `selector-reference.md`, `payload-reference.md`, and `field-reference.md`.
- Reads only the specialized reference file needed for the question after the command entry point.
- Does not use PyNVMe API calls.

### Prompt B: Flush NSID

```text
Using the SPEC markdown, check whether Flush supports NSID FFFFFFFFh.
If the markdown is not enough, say which Base Spec source section must be checked.
```

Expected behavior:

- Reads I/O command table and the Flush folder's canonical entry file, such as `command-facts.md` if expanded.
- Does not open full Base Spec unless verification is requested.
- States the conditional nature of `FFFFFFFFh` support.

### Prompt C: Format NVM Boundary

```text
Using the SPEC markdown, explain Format NVM destructive/restriction behavior.
Keep the answer in the SPEC layer and do not produce API calls or a test procedure.
```

Expected behavior:

- Uses Admin command table and Format NVM folder.
- Marks restrictions and destructive implications as spec facts only when sourced.
- Does not produce a test procedure.
- Does not pick PyNVMe APIs.

### Prompt D: Missing Fact Handling

```text
If a command canonical entry file does not contain the needed fact, what should the SPEC agent read next?
```

Expected behavior:

- Explains concrete expansion conditions.
- Reads only the matching specialized file first.
- Uses the full Base Spec only when extracted markdown is missing, inconsistent, incomplete, or original-source verification is requested.

### Prompt E: API Boundary

```text
Using SPEC markdown, answer Identify CNS=01h expected behavior without PyNVMe API calls.
If API mapping is needed, point to the API layer instead.
```

Expected behavior:

- Answers only spec facts.
- Hands implementation mapping off to the API layer without requiring a concrete API-layer path.
- Does not include concrete PyNVMe calls.

## 10. Review Report Template

```text
# SPEC Markdown Review Report

Date:
Reviewer:
Scope:

## Summary

PASS / FAIL / BLOCKED:

## Files Checked

- 

## Source Fidelity

- PASS:
- FAIL:
- Evidence:

## Command Folder Quality

- PASS:
- FAIL:
- Evidence:

## Status / Completion

- PASS:
- FAIL:
- Evidence:

## Cross-Spec Boundary

- PASS:
- FAIL:
- Evidence:

## Token-Efficient Reading

- PASS:
- FAIL:
- Evidence:

## API / Test Flow Boundary

- PASS:
- FAIL:
- Evidence:

## Required Fixes

1.
2.
3.

## Notes
```
