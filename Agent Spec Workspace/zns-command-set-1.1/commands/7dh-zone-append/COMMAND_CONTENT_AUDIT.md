# Zone Append Content Audit

Status: `COMPLETE`

Audited source:

- ZNS 1.1 section 3.4.1.
- Figures 22-30.
- ZNS Figure 12 opcode table.

Covered:

- command identity;
- data transfer direction;
- field map;
- operation semantics;
- PI remap behavior;
- completion ALBA behavior;
- command-specific status values;
- Base/NVM/ZNS ownership boundary.

Delegated / outside this command folder:

- full NVM end-to-end protection model;
- shared ZNS model details are centralized in `..\..\zns-model.md`;
- API/test-flow mapping.
