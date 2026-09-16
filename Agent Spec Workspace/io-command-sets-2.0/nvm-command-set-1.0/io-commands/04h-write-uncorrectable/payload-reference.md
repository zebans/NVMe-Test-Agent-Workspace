# NVM Write Uncorrectable Payload Reference

Write Uncorrectable has no command data payload.

| Result surface | Meaning |
|---|---|
| Later reads of marked LBAs | Fail with Unrecovered Read Error. |
| Later write to marked LBAs | Clears invalid logical block status. |
| Get LBA Status | May report LBAs written by Write Uncorrectable through descriptor status bit 1. |
