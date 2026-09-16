# Disconnect Selector Reference

## `RECFMT`

| Value | Meaning | Failure if unsupported |
|---:|---|---|
| `0h` | Disconnect command capsule format defined by this source. | Unsupported values return `Incompatible Format`. |

## Queue Type

| Queue | Behavior |
|---|---|
| I/O Queue | Valid queue type; command deletes the I/O Queue on which it is submitted. |
| Admin Queue | Invalid for Disconnect; abort with `Invalid Queue Type`. |

## Host Submission Rule

Host software should not submit commands to an I/O Submission Queue after submitting Disconnect to that queue; doing so results in undefined behavior.
