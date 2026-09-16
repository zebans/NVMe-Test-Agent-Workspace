# SPEC Check Agent Instructions

Purpose:

This file defines how a checker agent validates the NVMe SPEC markdown layer. This layer is for documentation quality, source fidelity, completeness, and boundary validation. It is not a PyNVMe API guide and is not a test-flow design guide.

## Scope

Use this checker layer when the user asks to:

- verify whether SPEC markdown is complete;
- check whether a command folder missed fields, selectors, payloads, statuses, restrictions, or boundary notes;
- audit whether markdown matches the original spec source;
- check whether a new command/spec layer follows the established markdown structure;
- find stale, partial, legacy, or misleading SPEC markdown.

Do not use this checker layer as the default source for writing tests. Test-writing agents should read the command/reference files first and only consult this layer when completeness or source fidelity is uncertain.

## Required Read Order

For a global SPEC markdown audit:

1. `SPEC_MARKDOWN_CHECKLIST.md`
2. `SPEC_COMPLETENESS_STATUS.md`
3. `COMMAND_CONVERGENCE_AUDIT.md`
4. `SPEC_MARKDOWN_SELF_CHECK_REPORT.md`
5. Target root/index files or command folders
6. Original spec source only when a source-fidelity spot check is needed

For a single command folder audit:

1. The command folder `README.md`
2. `command-facts.md`
3. `field-reference.md`
4. `selector-reference.md`, if present
5. `payload-reference.md`, if present
6. `status-reference.md`
7. `restrictions.md`, if present
8. `cross-spec-boundary.md`
9. `COMMAND_CONTENT_AUDIT.md`
10. Original spec source section / figure when needed

## Canonical Command Folder Files

| File | Required? | Checker purpose |
|---|---|---|
| `README.md` | Yes | Confirms read path and human-facing command scope. |
| `command-facts.md` | Yes | Confirms opcode, command identity, source, data direction, queue type, and NSID scope. |
| `field-reference.md` | Yes | Confirms command dword fields, bit positions, meanings, and important rules. |
| `selector-reference.md` | When useful | Confirms selectors, actions, FID/LID/CNS/ZSA/ZRA/FCTYPE, or other routing fields. |
| `payload-reference.md` | When applicable | Confirms command data or returned data payload structures. |
| `status-reference.md` | Yes | Confirms command-specific status applicability and conditions. |
| `restrictions.md` | When applicable | Confirms invalid combinations, prerequisites, limits, and side-effect boundaries. |
| `cross-spec-boundary.md` | Yes | Confirms ownership boundaries across Base, NVM, ZNS, KV, Fabrics, MI, transports, security, and vendor docs. |
| `COMMAND_CONTENT_AUDIT.md` | Yes for audited command folders | Confirms source coverage, captured facts, known delegation, and completion state. |

## Validation Checks

Every audit should check:

| Check | What to verify |
|---|---|
| Source fidelity | Facts match the named source section, table, or figure. |
| Opcode / selector coverage | Opcode, selectors, actions, FID/LID/CNS/FCTYPE/CSI routing are not missing. |
| Field coverage | CDW bits, payload bytes, returned fields, masks, and reserved/vendor-specific handling are clear. |
| Status coverage | Command-specific status conditions are present and global status definitions are not over-applied. |
| Payload coverage | Large payloads are either byte-exact, indexed by high-value fields, or explicitly delegated. |
| Cross-spec boundary | Ownership is explicit and no layer invents behavior owned by another spec. |
| Reserved handling | Reserved fields stay reserved; do not infer behavior. |
| Vendor-specific handling | Vendor-specific areas remain boundary-only unless vendor documentation exists. |
| API/test-flow leakage | No PyNVMe calls, fixtures, pytest patterns, shell flow, or test-design logic in SPEC markdown. |
| Token-efficient routing | The file tells a future agent where to read next instead of duplicating large unrelated tables. |

## Completion Labels

Use the labels from `SPEC_COMPLETENESS_STATUS.md`. Do not invent new completion labels unless the user explicitly updates the status vocabulary.

High-value labels:

| Label | Meaning |
|---|---|
| `COMPLETE` | Relevant command-control or reference facts are captured and external ownership is explicit. |
| `BOUNDARY-COMPLETE` | The local spec only defines the boundary; detailed behavior belongs elsewhere. |
| `COMMAND-INDEX-COMPLETE` | Command-set or layer index is complete enough for routing. |
| `SOURCE-INDEX-COMPLETE` | Source sections/figures are indexed but behavior may not be expanded. |
| `PAYLOAD-INDEXED` | Payload is indexed or routed, but not fully byte-expanded. |
| `PAYLOAD-COMPLETE` | Payload fields are fully expanded or intentionally delegated. |
| `BLOCKED` | Required source is missing, unclear, external, or vendor-specific. |

## How To Use COMMAND_CONTENT_AUDIT.md

`COMMAND_CONTENT_AUDIT.md` is local maintenance evidence for the folder it lives in.

Use it to answer:

- Which source section or figure was used?
- Which fields, statuses, payloads, restrictions, or boundaries were captured?
- Which content is intentionally delegated to another spec layer?
- Is the folder marked complete, boundary-only, indexed, or blocked?

Do not use it as the primary test-writing source. If a test needs field meaning, read `field-reference.md`; if it needs expected status, read `status-reference.md`; if it needs payload layout, read `payload-reference.md`.

## Output Expectations

When reporting an audit:

- lead with missing or risky items first;
- cite file paths and line numbers when possible;
- distinguish "missing from markdown" from "not defined by the spec";
- say when a boundary is intentionally complete;
- recommend the smallest next expansion that improves precision;
- avoid writing PyNVMe API, test steps, or shell commands unless the user asks for a different layer.

## Boundary

This checker layer manages SPEC markdown quality only. It may link to `SPEC_AGENTS.md` for normal SPEC lookup behavior, but it does not replace `SPEC_AGENTS.md`, `SPEC_REFERENCE_GUIDE.md`, API agent files, or future test-flow agents.
