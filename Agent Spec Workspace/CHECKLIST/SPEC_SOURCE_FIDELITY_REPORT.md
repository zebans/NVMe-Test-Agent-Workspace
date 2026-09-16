# SPEC Source Fidelity Report

Date: 2026-09-14

Purpose: record direct comparison of curated command references against the local Base 2.0 source bundle and original PDFs. This report covers source ownership and high-signal command facts; it does not treat structural readiness as proof of semantic fidelity.

## Result

| Check | Scope | Result |
|---|---:|---|
| Command owner, section, and opcode consistency | 70 `command-facts.md` files | PASS after correction |
| Explicit source section / figure existence | 206 source declarations | PASS |
| Root Admin opcode table vs Base Figure 138 | All standard Admin rows | PASS |
| Root common I/O opcode table vs Base Figure 390 | All common I/O rows | PASS |
| Global status dictionary vs Base Figures 92-99 | SCT and SC tables | PASS |
| Command status code/name lookup against Base plus owner source | All explicit command status rows | PASS |
| Field-token existence scan | 72 `field-reference.md` files | PASS with documented local aliases |
| Structural/readiness checker | 702 Markdown files | PASS, 0 errors / 0 warnings |

## Corrected Defects

| File | Defect | Correction |
|---|---|---|
| `..\admin-commands-2.0\00h-delete-io-submission-queue\command-facts.md` | Source incorrectly named section 5.1, which is Abort. | Corrected to section 5.7. |
| Same file | Initial correction included Figures 163-164, which belong to Delete I/O Completion Queue. | Narrowed to Figures 165-166. |

## PDF Checks

The original PDFs were used where converted Markdown formatting could hide or merge table structure:

- Base Figure 94 confirmed that the reserved Generic Status range printed by revision 2.0 is `90h` to `BFh`; the apparent gap after `89h` is present in the source and was not silently rewritten.
- NVM Figure 18 confirmed NVM opcode, transfer direction, and reference-section routing, including Compare section 3.2.1 and the remaining NVM command rows.
- Key Value sections 3.2.4 and 3.2.5 confirmed the Exist and Store command headings and field ownership.
- ZNS sections 3.3.8, 3.3.9, and 3.4.1 confirmed Write Uncorrectable, Write Zeroes, and Zone Append routing and status ownership.

## Converted-Source Handling

The NVM, Key Value, and ZNS Markdown conversions sometimes omit a parent command heading number while retaining the command heading, child completion section, opcode table, and figures. The source-fidelity checker accepts the combination of those anchors rather than reporting the conversion artifact as a SPEC defect.

The following searchable abbreviations are local aliases because the cited figure spells out the field name without assigning that acronym:

| Local alias | Exact source field name | Source |
|---|---|---|
| `AET` | Asynchronous Event Type | Base Figure 143 |
| `NDAS` | No-Deallocate After Sanitize | Base Figure 303 |
| `NUMD` in Zone Management Receive | Number of Dwords | ZNS Figure 33 |

`ATYPE` in the Base Get LBA Status boundary is not a Base-owned field. It is correctly routed to NVM Command Set section 4.2.1.

## Boundary Of This Pass

This pass proves that command source anchors, opcode routing, explicit status names/codes, and searchable field identities are backed by the named local source. Automated checks cannot prove every prose condition, state transition, byte offset, or reserved-bit rule. Those require per-command manual source review and should continue to be represented by each command folder's `COMMAND_CONTENT_AUDIT.md`.
