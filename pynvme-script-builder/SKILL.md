---
name: pynvme-script-builder
description: Orchestrate NVMe test sources, normalized flows, or Engineer-adopted TEST_REVIEWER AI-TF handoffs through test-flow conversion, persisted SPEC reasoning, mandatory delivery review, PyNVMe3 API mapping, and pytest generation. Use when the user asks to build a PyNVMe3 script or continue an adopted reviewer proposal while applying local test-flow-converter, SPEC_AGENTS.md, TEST_REVIEWER_AGENT.md, API_AGENTS.md, PyNVMe3/AGENTS.md, and Enginner_AGENTS.md guidance.
---

# PyNVMe Script Builder

Use this skill to run the layered pipeline from source test material to a
PyNVMe3 pytest validation script.

This skill coordinates existing guidance. It does not replace:

- `test-flow-converter` for source-to-flow normalization.
- `SPEC_AGENTS.md` for NVMe specification facts.
- `TEST_REVIEWER_AGENT.md` for test-flow delivery review.
- `API_AGENTS.md` for PyNVMe3 API mapping.
- `PyNVMe3/AGENTS.md` for hard pytest generation rules.
- `Enginner_AGENTS.md` for local script-writing style.

## Required Reading

1. Read the `test-flow-converter` skill before converting any CSV, shell, IOL,
   or text source into a standard test flow.
2. Before the test-flow review gate, locate only the required review guidance
   from paths supplied by the user or by searching the current workspace:
   - `SPEC_AGENTS.md`
   - `TEST_REVIEWER_AGENT.md`
3. Read only the needed SPEC references for the current task.
4. When invoked from a Reviewer adoption control, read and validate the
   `pynvme-script-builder:handoff` payload before regenerating any flow.
5. Only after the current formal-flow review decision is `Deliverable`, locate and read the
   downstream implementation guidance:
   - `API_AGENTS.md`
   - `PyNVMe3/AGENTS.md` or another project-level `AGENTS.md`
   - `Enginner_AGENTS.md`

Do not rely on hard-coded absolute paths. When multiple matching AGENTS exist,
prefer the one nearest to the source file or ask the user to disambiguate if the
choice changes behavior.

## Pipeline

1. Source intake
   - Identify the source file or inline test description.
   - If the user provides an existing standardized test-flow artifact folder or
     file, treat `manifest.yaml` as the required authoritative input for the
     flow. Use `flow.md` only as human-readable traceability, not as the source
     for script decisions.
   - Do not generate a PyNVMe3 script from a standardized test-flow artifact set
     unless `manifest.yaml` is present and readable. If only `flow.md` is
     provided, stop and ask for the matching `manifest.yaml` instead of
     re-interpreting Markdown prose.
   - Preserve original path, row numbers, line numbers, labels, and parameter
     names.
   - Decide the output artifact directory. Default to
     `<source_stem>_test_flow` beside the source file unless the user specifies
     a path.

2. Test-flow conversion
   - Use `test-flow-converter`.
   - Produce the standard artifacts:
     - `flow.md`
     - `manifest.yaml`
     - `coverage-matrix.md`
     - `test-template.md`
     - `index.md`
   - Preserve source command names and parameters.
   - Flag ambiguities instead of silently resolving them.
   - After conversion, all SPEC review, API mapping, and script generation must
     read the normalized flow from `manifest.yaml`. Cross-check with `flow.md`
     and `coverage-matrix.md` only to preserve traceability and catch conversion
     gaps.

3. SPEC evidence
   - Read `SPEC_AGENTS.md`.
   - Use the smallest relevant local spec reference files.
   - Run its Test-Flow Evidence Report Mode against the authoritative
     `manifest.yaml` and original source.
   - Generate or update
     `<source_stem>_spec_reasoning_map.html` in the test-flow artifact folder.
     Do not create versioned or timestamped variants for the same flow.
   - Collect implementation-neutral command facts, fields/selectors, expected
     behavior, restrictions, completion/status facts, source anchors, and
     evidence-backed source-to-SPEC inferences needed by the test reviewer.
   - Require every grouped behavior to preserve its manifest step IDs and source
     references. Require a compact SPEC Index at the bottom of every visible
     behavior node; use `Direct SPEC Reference: None` for test-platform behavior
     with no SPEC ownership.
   - Read and validate the embedded `spec-reasoning-map-data` JSON. Require
     `report_contract=spec_reasoning_map_v1`, matching visible behavior nodes,
     and explicit separation of SPEC facts from Agent inferences.
   - If the report or metadata is missing, malformed, or does not cover every
     manifest behavior, repair it before starting the test-flow review gate.
   - Keep spec review implementation-neutral.

4. Test-flow review gate
   - Read `TEST_REVIEWER_AGENT.md`.
   - Give the reviewer the source, `manifest.yaml`, `flow.md`,
     `coverage-matrix.md`, and `<source_stem>_spec_reasoning_map.html`, including
     its embedded evidence metadata.
   - Treat SPEC_AGENT inferences as advisory evidence, not as owner-approved
     flow decisions. The reviewer alone determines whether an unresolved
     inference is a blocker and whether the formal flow is deliverable.
   - Generate `<source_stem>_test_review_report.html` in the artifact folder.
   - Read the report's embedded review metadata. Require
     `report_contract=test_reviewer_compact_v1` and validate that visible
     findings and AI-TF steps match the metadata.
   - If the decision is `Not Deliverable` and there is no validated
     Engineer-adopted handoff, stop this run. Do not read
     `API_AGENTS.md`, `PyNVMe3/AGENTS.md`, or `Enginner_AGENTS.md`; do not
     generate a script. Report the blocking finding IDs and required owner
     confirmations to the user.
   - Do not create an automatic confirmation loop. A later user request may
     provide a new flow or ask `test-flow-converter` to reference the report and
     create a new formal flow.

5. Engineer-adopted AI-TF handoff
   - Enter this branch only when the runtime supplies a
     `pynvme-script-builder:handoff` payload. A report that merely contains an
     unchecked or ready-state button is not an adoption decision.
   - Require all of the following:
     - `target=pynvme-script-builder`;
     - `source_review_decision=not_deliverable`;
     - adopted flow `adoption_status=engineer_adopted`;
     - adopted flow `handoff_status=handed_off`;
     - source report, reviewed source, SPEC reasoning-map reference, blocking
       finding IDs, handoff timestamp, and one or more unique `AI-TF-##` steps;
     - every AI-TF step has an action, evidence type, and any available SPEC
       Basis.
   - Preserve the original `Not Deliverable` decision and blocker history. The
     handoff adopts a proposal for regeneration; it does not retroactively make
     the reviewed source flow deliverable.
   - Do not read API or Engineer guidance in this branch yet.
   - Give `test-flow-converter` the original source, original formal artifacts,
     review report, SPEC reasoning map, required decisions, and adopted AI-TF
     steps. Generate a new formal artifact set under the next available
     `<artifact_folder>/revisions/rev-###/` directory; do not overwrite the
     reviewed revision.
   - Require every regenerated manifest step derived from the proposal to keep
     traceability to its `AI-TF-##`, addressed `TF-###` findings, source
     behavior, and review report.
   - Run SPEC Evidence and TEST_REVIEWER again against the regenerated
     `manifest.yaml`. Generate the revision's SPEC reasoning map and compact
     review report in the same revision directory.
   - If the regenerated flow is still `Not Deliverable`, stop and report the
     new blocker IDs. Never chain another adoption automatically.
   - Continue to API mapping only when the regenerated formal flow is
     `Deliverable`.

6. API mapping
   - Read `API_AGENTS.md`.
   - Map each flow action to PyNVMe3 fixtures, objects, methods, buffers,
     completion handling, result extraction, and cleanup.
   - Before mapping source parameters into PyNVMe3 call arguments, confirm the
     command's specification-owned fields and selectors from `SPEC_AGENTS.md`
     and the relevant SPEC reference files. A source parameter that is not a
     SPEC-defined field for that command must remain a source/tool-level
     abstraction until an explicit source-backed translation rule is available.
   - Do not directly map tool-level parameters such as CSV runner names,
     aliases, or legacy client-script arguments into NVMe command fields or
     PyNVMe3 API arguments merely because the names look related. First record
     the SPEC field boundary, then let `API_AGENTS.md` map the validated SPEC
     intent into PyNVMe3 syntax.
   - When a source parameter is not a SPEC field but has an approved,
     source-backed translation rule, map it through API semantics. Example: CSV `TXLEN` for
     Firmware Image Download is a tool-level transfer length and must be
     translated to one or more API `fw_download(buf, offset_bytes, size_bytes)`
     calls, not treated as an NVMe command field.
   - API mapping owns translating an approved normalized flow plus SPEC facts
     into script assertions, log checks, and implementation calls.
   - Do not invent API calls. Verify uncertain API syntax from the local
     PyNVMe3 project files.

7. Script generation
   - Read `PyNVMe3/AGENTS.md` for hard pytest rules.
   - Read `Enginner_AGENTS.md` for final script style.
   - Generate a fixture-driven PyNVMe3 pytest script with visible test flow,
     `logging.info()` progress, explicit assertions, and cleanup.
   - Generate only from a `Deliverable` flow. Do not use script comments to
     carry unresolved test-purpose, expected-result, parameter, or source/SPEC
     conflict decisions.
   - Add concise flow trace comments before each major implementation block
     using only this single-line format:
     `# Flow Step[index]: <short action or purpose>`.
   - Use the `index` from the reviewed `manifest.yaml` step ID. For grouped or
     parameterized cases, use the parent flow step ID and keep the comment
     short, e.g. `# Flow Step[3]: Run Firmware Commit CA=1 cases`.
   - Do not expand flow trace comments into multi-line `Flow/Source/Intent`
     blocks unless the user explicitly asks.
   - Keep other comments concise, such as reviewed flow version and report path
     when useful.
   - Keep destructive or state-changing behavior exactly aligned with the flow
     and user request.

8. Validation
   - Run static checks such as `python -m py_compile` for generated Python.
   - Do not run pytest or commands that can affect a DUT, firmware, namespaces,
     power state, or persistent device state unless the user explicitly asks.

## Output Rules

Create or update this artifact set unless the user requests a smaller inline
answer:

```text
<source_stem>_test_flow/
  flow.md
  manifest.yaml
  coverage-matrix.md
  test-template.md
  index.md
```

The SPEC agent and test reviewer create these reports before API mapping:

```text
<source_stem>_test_flow/
  <source_stem>_spec_reasoning_map.html
  <source_stem>_test_review_report.html
```

The SPEC reasoning map is required even when the reviewer later returns
`Not Deliverable`; it is the persisted evidence input for that decision.

If its decision is `Not Deliverable`, the report is the only review artifact
needed for the current run. Do not create a script or a separate proposed-flow
artifact. A later validated Engineer-adopted handoff creates a new revision:

```text
<source_stem>_test_flow/
  revisions/
    rev-001/
      flow.md
      manifest.yaml
      coverage-matrix.md
      test-template.md
      index.md
      <source_stem>_spec_reasoning_map.html
      <source_stem>_test_review_report.html
```

Do not treat the revision as script-ready until its own review metadata says
`Deliverable`.

Write the generated pytest script beside the artifact folder by default:

```text
test_<source_stem>_engineer.py
```

If the user provides an output path, use that path exactly.

## Authority Order

When guidance conflicts, apply this order:

1. Current user request and confirmed test-flow decisions.
2. Reviewed `Deliverable` manifest and its source traceability.
3. `SPEC_AGENTS.md` for expected NVMe behavior.
4. `API_AGENTS.md` and local PyNVMe3 source for implementation calls.
5. `PyNVMe3/AGENTS.md` for hard pytest rules.
6. `Enginner_AGENTS.md` for final code style.

## Final Response

Report:

- generated artifact folder
- SPEC reasoning map path
- test-review report path and delivery decision
- blocking finding IDs and required confirmations when not deliverable
- adopted AI-TF handoff validation and regenerated revision path when used
- generated script path and static checks only when deliverable
- whether pytest or DUT-affecting commands were intentionally not run
