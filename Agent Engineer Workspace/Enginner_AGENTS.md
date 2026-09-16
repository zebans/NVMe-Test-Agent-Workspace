# Enginner AGENTS

This guide defines the preferred writing style for PyNVMe3 pytest validation
scripts produced in the Script Workspace.

It is intentionally a style guide only. It does not own PyNVMe3 API truth,
NVMe specification truth, or full test-flow design.

## Layer Boundary

| Document | Owns | Does Not Own |
|---|---|---|
| `API_AGENTS.md` | PyNVMe3 objects, fixtures, method mapping, buffers, queues, command completion, returned data. | Final script voice, local test body layout, naming taste. |
| `PyNVMe3\AGENTS.md` | Hard pytest generation rules: allowed objects, allowed fixtures, assertions, logging, docstrings, one-test behavior. | Repository-specific style families or script rewrite taste. |
| `Enginner_AGENTS.md` | Script appearance, local code rhythm, readability, helper-vs-inline choices, folder-style matching. | API mapping, expected NVMe status, spec clauses, complete flow design. |

If documents conflict:

1. The current user request wins.
2. Specification/SPEC agents win for expected behavior and status.
3. `API_AGENTS.md` wins for PyNVMe3 API syntax and object usage.
4. `PyNVMe3\AGENTS.md` wins for hard pytest rules.
5. This file wins only for final style choices.

## Role

Write like an NVMe SSD validation engineer, not like a generic Python
application developer.

The script should make the validation intent visible: what is prepared, what
command or workload is run, what result is decoded, what is asserted, and how
the device is restored.

## Style Goal

Generated scripts should feel like practical PyNVMe3 validation scripts:

- pytest function centered
- fixture driven
- straight-line test flow
- visible command sequence
- explicit logging and assertions
- minimal abstraction
- cleanup or ready-state restoration when the test changes device state

This guide is based on the converted 5F client-script style. Future generated
scripts may not have the original 5F client scripts available for comparison,
so the style rules below are self-contained and should be followed directly.

Use `API_AGENTS.md` for the exact API call, object, fixture, buffer, and
completion details. In this file, any code snippet is only a style example.

## File Shape

A script should usually be shaped like:

```python
import time
import pytest
import logging
import warnings

from nvme import Controller, Namespace, Buffer, Qpair, Pcie, Subsystem
from nvme import IOCQ, IOSQ, PRP, PRPList, SQE, CQE, NvmeEnumerateError


def test_feature_objective(nvme0, nvme0n1, qpair, buf):
    """
    Verify <feature> by <method>.
    Reference: <spec or requirement>.
    """

    # Check support or precondition.
    ...

    # Prepare the device state.
    ...

    # Run the command or workload under test.
    ...

    # Decode and validate the result.
    ...

    # Restore or document final state.
    ...
```

Keep the main validation path in the test body. Use helpers only when they are
already established locally or remove real repeated complexity.

Do not import or depend on old 5F external board-control helpers. In
particular, do not generate:

```python
from scripts.ssstc_ioboard import SSSTC_IOBoard
```

and do not construct `Subsystem` with `SSSTC_IOBoard().PowerOn` or
`SSSTC_IOBoard().PowerOff`. The converted environment may support reset and
power operations through PyNVMe3 APIs, but scripts should not depend on
IOBoard/relay-style helpers.

## Naming Style

Use direct pytest names that reveal feature and objective:

```python
def test_identify_reserved_cns(...):
def test_format_and_ioworker(...):
def test_spdm_get_version(...):
```

For production or test-plan scripts, keep the local numbered style:

```python
def test_case1_16k_randrw_1day(...):
def test_case10_check_performance_during_trim_1(...):
```

Prefer names that are searchable and meaningful in pytest output.

## Fixture Style

Prefer existing project fixtures over manual object construction. This is a
style rule; the exact fixture list and return types are owned by
`API_AGENTS.md` and `PyNVMe3\AGENTS.md`.

Good style:

```python
def test_smart_health_temperature(nvme0, buf):
```

Avoid this style unless the test specifically validates manual construction:

```python
def test_smart_health_temperature():
    # manual controller setup here
    ...
```

Use reset or power APIs only through the converted PyNVMe3 environment and the
fixtures/API documented by `API_AGENTS.md`, such as `nvme0.reset()`,
`pcie.reset()`, `pcie.flr()`, `subsystem.reset()`, or
`subsystem.power_cycle()` when the test flow calls for them. Do not add
IOBoard imports or old client-script power helpers.

## Test Body Rhythm

Use this rhythm when it fits the test flow:

```text
support/precondition check
device preparation
command or workload
completion/wait
field/result decode
assertion
cleanup/final ready state
```

Do not turn a simple validation into a mini framework. The reader should be
able to follow the command sequence by scanning the test function.

## Command Presentation Style

Show PyNVMe3 calls directly in the test body when they are the point of the
test. Completion handling and exact API syntax are owned by `API_AGENTS.md`,
but the script should visually read like:

```python
logging.info("read SMART / Health Information log page")
...
logging.info("decoded composite temperature: %d" % temperature)
assert temperature != 0, "composite temperature should not be zero"
```

For command-specific examples, consult `API_AGENTS.md`. Do not copy API
signatures from this file as authoritative.

## Completion Callback Style

When a command status must be checked, prefer the local engineer callback
pattern with explicit `sc` and `sct` variables:

```python
sc = 0
sct = 0

def _cb(cpl):
    nonlocal sc
    nonlocal sct
    status = cpl[3] >> 17
    sc = status & 0xFF
    sct = (status >> 8) & 0x7

nvme0.getlogpage(lid=0x2, buf=buf, size=512, cb=_cb).waitdone()
assert sc == 0 and sct == 0, f"getlogpage fail, sc={sc:#x} sct={sct:#x}"
```

For tests such as Abort where the target command and Abort command both have
meaningful completions, keep those results separate. Log the `cid`, `sqid`,
target status, and Abort completion result so failures can be debugged from
the pytest log.

Do not hide the important command sequence inside a generic helper framework.
A tiny callback or decode helper is fine; the actual command issue, wait, decode,
assert, and cleanup sequence should remain visible in the test body.

## Workload Presentation Style

For benchmark, stress, or production workloads, keep workload parameters close
to the test case unless a shared helper is already established.

Good style:

```python
runtime = LIMIT if LIMIT else 30 * 60
logging.info("run 8K random read/write workload for %d seconds" % runtime)
...
```

Avoid hiding all workload intent behind a generic helper call with no local
logging or visible parameters.

## Assertion Style

Assertions should be explicit and explain the expected behavior:

```python
assert actual == expected, "expected 0x%x, actual 0x%x" % (expected, actual)
assert (value & mask) == mask, "required bit not set: value=0x%x" % value
assert sc == 0 and sct == 0, f"command fail, sc={sc:#x} sct={sct:#x}"
assert actual == expected, f"unexpected value, expect={expected:#x}, actual={actual:#x}"
```

Use decoded variable names that reflect the spec or test-flow term. Avoid
assertions that only say:

```python
assert result
```

unless the surrounding logs and variable name make the failure obvious.

## Negative Test Style

When the test flow expects an error status, make the invalid input visible and
use the project warning pattern defined by `PyNVMe3\AGENTS.md`.

The expected status value must come from the spec/test-flow layer, not this
style guide.

Use `pytest.warns(...)` for expected PyNVMe warnings, for example an expected
NVMe error completion surfaced as a warning. Do not broadly suppress warnings
with `warnings.catch_warnings(record=True)` unless the current user request or
the test flow specifically requires collecting warning objects.

For Abort-style tests, remember that Abort is a race: the target command may be
aborted, or it may complete before Abort wins. Validate consistency between the
target completion and the Abort completion result instead of blindly requiring
every target command to be aborted, unless the spec/test-flow explicitly says
the target must be aborted.

## Logging Style

Use `logging.info()` for normal test progress, parameters, decoded values, and
cleanup actions. Avoid `print()` for ordinary pytest output.

Good logs answer:

- what condition is being checked
- what command/workload is about to run
- what important parameter was used
- what value was decoded
- what cleanup or reset was performed

Keep logs useful, not decorative.

## Comments And Docstrings

Use comments to separate logical blocks. Keep them short:

```python
# Read the log page under test.
# Validate the decoded field.
# Restore controller ready state.
```

Do not number comments as steps unless the local script family already does so.
Do not comment obvious assignments.

Docstring hard rules are owned by `PyNVMe3\AGENTS.md`; this file only adds that
the wording should sound like a validation purpose, not a product description.

## Safety And Cleanup Style

Make destructive or state-changing behavior visible in the test body:

- format
- sanitize
- firmware update or activation
- namespace create/delete/attach/detach
- reset or power cycle
- full-drive write
- security state changes

During style rewrites, do not add, remove, or soften destructive behavior
unless the user explicitly asks. Preserve the original safety gate and cleanup
intent.

For new converted scripts, do not invent extra safety gates such as environment
variables, interactive confirmations, or optional skip flags. If the test flow
requires `format`, `sanitize`, firmware commit, namespace changes, full-drive
writes, security state changes, reset, or power-cycle behavior, implement that
flow directly and log it clearly. Only add a gate when the user request or
source test flow explicitly contains one.

## Helper Function Style

Prefer direct test code for one-off logic. Use helpers when:

- several tests share the same preparation or workload
- protocol packing/parsing would distract from the test purpose
- the helper name clearly describes the validation action

Avoid adding helpers that hide the only important command sequence in a single
test. In particular, avoid generic wrappers like `_abort_admin_once()` when the
main purpose of the test is to show the command being issued, aborted, waited,
decoded, and checked.

## Refinement Checklist

When asked to improve a script according to this guide:

- Preserve the original test purpose.
- Preserve expected result and pass/fail criteria.
- Preserve destructive behavior and safety gates.
- Keep the validation flow visible in the test function.
- Prefer project fixtures over manual setup.
- Keep API syntax aligned with `API_AGENTS.md`.
- Keep hard pytest requirements aligned with `PyNVMe3\AGENTS.md`.
- Replace normal `print()` output with `logging.info()`.
- Make vague assertions explicit.
- Prefer local `sc`/`sct`/`status` callback checks for command completions.
- Log important `cid`, `sqid`, queue id, namespace id, feature id, LID, and
  decoded field values.
- Use `pytest.warns(...)` only for expected PyNVMe warnings.
- Do not add environment-variable safety gates unless the source flow asks for
  one.
- Do not import `SSSTC_IOBoard` or use old IOBoard/relay helpers.
- Add meaningful block comments only where they improve scanability.
- Add or preserve cleanup when device state changes.

## Minimal Style Template

```python
import pytest
import logging

from nvme import Controller, Buffer


def test_feature_objective(nvme0: Controller, buf: Buffer):
    """
    Verify <feature> by <method>.
    Reference: <spec or requirement>.
    """

    # Check support or precondition.
    logging.info("check feature support")
    if not <supported>:
        pytest.skip("feature is not supported")

    # Run the command or workload under test.
    logging.info("run command under test")
    <command_from_API_AGENTS>

    # Decode and validate the result.
    actual = <decoded_result>
    expected = <expected_from_SPEC_or_test_flow>
    logging.info("expected=0x%x, actual=0x%x" % (expected, actual))
    assert actual == expected, "expected 0x%x, actual 0x%x" % (expected, actual)

    # Restore or document final state.
    logging.info("restore final device state")
    <cleanup_from_test_flow_or_API_AGENTS>
```
