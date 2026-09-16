# Fabrics Base Agent Rules

You are reading the NVMe Base Spec 2.0 Fabrics Command Set layer.

This layer owns:

- Fabrics command identity from Base Spec 2.0 section 6.
- `OPC=7Fh` Fabrics command capsule rules from section 3.3.2.1.1 and Figure 80.
- Fabrics response capsule rules from section 3.3.2.1.2 and Figure 82.
- `FCTYPE` command type table from Figure 375.
- Fabrics command-specific status values from Figure 97.

This layer does not own:

- NVMe-MI command behavior.
- PyNVMe API calls.
- Test-flow steps or script execution order.

Important boundary:

`fabrics-base-2.0` is an independent layer, but its source is still the Base Spec 2.0 document. Treat it as "Base-owned Fabrics command facts", not as an external command-set PDF.

## Reading Rules

Start with:

```text
README.md
FABRICS_COMMAND_SET_INDEX.md
target command folder\README.md
target command folder\command-facts.md
```

Continue with `selector-reference.md`, `field-reference.md`, `payload-reference.md`, `status-reference.md`, `restrictions.md`, and `cross-spec-boundary.md` as needed.

Read `FABRICS_STATUS_REFERENCE.md` when:

- the question asks about Connect, Disconnect, authentication, or transport-specific status values;
- the command folder mentions Figure 97;
- a status value in `80h` to `BFh` is involved.

Read `BASE_TO_FABRICS_BOUNDARY.md` when:

- the question mentions command capsules, response capsules, SQ flow control, or source ownership;
- the answer must identify which source owns a requested detail.

Use this exact phrase when a detail is not defined by Base section 6 and must be read from its owning source:

```text
Delegated to the applicable owning specification.
```
