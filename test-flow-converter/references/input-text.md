# Plain Text Test Description Input

Use this reference for prose, copied requirements, screenshot text converted to
text, issue descriptions, and numbered test steps.

## Detection

Treat input as plain text when it is not shell, IOL, or CSV and includes:

- Numbered steps or bullet lists.
- Natural-language setup and expected behavior.
- Copied text from screenshots, documents, tickets, or specifications.
- Mixed prose and command snippets without a formal file format.

If the original source is an image, PDF, DOCX, spreadsheet, or another
non-text-readable file, convert it with `markitdown` first and use the converted
Markdown as the extraction source.

## Extraction

Read the text in this order:

1. Title, heading, filename, or first sentence for purpose.
2. Setup/preconditions, DUT assumptions, tools, test data, and safety notes.
3. Numbered or ordered steps.
4. Command snippets, parameter assignments, enum values, register names, and
   expected outputs.
5. Verification language such as "check", "verify", "should", "must",
   "expected", "pass", "fail", and "not applicable".
6. Cleanup, reset, teardown, restore, or final-state language.

Preserve source wording where it carries technical meaning, especially command
names, bit names, register names, parameter names, field names, opcode/FID/LID
values, row identifiers, and quoted values.

## Step Normalization

- Convert each numbered source step into one generated step by default.
- Split one source step into multiple generated steps only when it contains
  multiple independent commands or checks that need separate verification.
- Combine tiny source fragments only when they are clearly one command with its
  expected result.
- Add `Source step: <identifier>` or equivalent traceability to every generated
  step.

## Inference Rules

Infer only what is strongly supported:

- A title can come from the heading or filename.
- Common verify can be generalized when the source repeatedly says every
  command must check completion/status.
- A read-only test does not require cleanup unless the source says state is
  changed.
- A state-changing test requires cleanup, rollback, or an explicit "leave as
  is" final state.

Flag, rather than hide, inferred domain assumptions such as enum restrictions,
unit conversions, command ordering, or safety gates.

## Ambiguity And Unsupported Logic

Flag these conditions:

- A step says to "check" something without saying what value is expected.
- Required setup is implied by domain knowledge but not present in the source.
- A destructive or persistent change lacks safety and cleanup guidance.
- The text references a screenshot/table/attachment that is not available.
- The text says "same as above" but the referenced step is unclear.
- Timing terms such as "wait enough" or "long time" have no concrete value.

Ask for clarification only when ambiguity blocks required fields. Otherwise
include the ambiguity in the flow and validation notes.
