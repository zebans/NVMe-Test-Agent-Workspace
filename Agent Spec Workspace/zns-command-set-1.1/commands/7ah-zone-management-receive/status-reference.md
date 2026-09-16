# Zone Management Receive Status Reference

## Completion

When the command is completed, the controller posts a CQE to the associated I/O Completion Queue indicating command status.

The command returns its result through the data buffer described by `DPTR`.

## Command-Specific Status

The source section does not define a separate Zone Management Receive command-specific status table.

## Other Status Sources

| Status | When it applies |
|---|---|
| Invalid Field in Command | Extended Report Zones requested while the zoned namespace is not formatted with a non-zero Zone Descriptor Extension Size. |
| Invalid Field in Command | Reserved `ZRA` value. |
| Invalid Field in Command | Reserved Zone Receive Action Specific Field value. |

## Data Size Rule

If host software requests more dwords than the selected Zone Receive Action data structure returns, the controller returns the complete result and dwords beyond the data structure end are undefined.
