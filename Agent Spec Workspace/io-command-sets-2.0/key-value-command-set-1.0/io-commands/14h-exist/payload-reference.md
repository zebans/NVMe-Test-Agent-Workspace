# KV Exist Payload Reference

Exist has no command data payload and no returned data payload.

The existence result is encoded in completion status:

| Completion status | Meaning |
|---|---|
| Success `00h` | Key exists. |
| `87h` KV Key Does Not Exist | Key does not exist. |
