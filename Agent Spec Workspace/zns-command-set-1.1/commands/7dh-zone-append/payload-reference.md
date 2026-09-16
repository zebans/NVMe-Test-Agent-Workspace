# Zone Append Payload Reference

## Data and Metadata Transfer

| Pointer | Payload | Direction |
|---|---|---|
| `DPTR` | User data buffer for the append. | Host to controller. |
| `MPTR` | Metadata buffer, if applicable. | Host to controller. |

## Controller-Assigned LBA

The controller assigns the actual logical blocks within the selected zone. On success, the lowest assigned LBA is returned as `ALBA` in the completion queue entry.

If the command does not complete successfully, `ALBA` contents are undefined.

## `PIREMAP` Behavior

Because the actual LBA is not known to the host until completion, LBA-based reference tags need ZNS-specific handling.

| `PIREMAP` | Behavior |
|---:|---|
| `0` | Controller writes the Reference Tag to media according to the NVM Command Set without modification. |
| `1` | Controller writes calculated Logical Block Reference Tags. |

When `PIREMAP=1`:

```text
Media Reference Tag[0] = ILBRT + (ALBA - ZSLBA)
Media Reference Tag[n+1] = Media Reference Tag[n] + 1
```

The controller writes all other protection information received from the host without modification.
