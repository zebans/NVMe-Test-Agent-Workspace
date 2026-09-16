# Key Value Command Set 1.0 Detail Layer

This folder contains expanded command references for Key Value Command Set-specific I/O commands.

## Source

```text
..\..\NVMe Base Spec\2.0\NVM-Express-Key-Value-Command-Set-Specification-1.0-2021.06.02-Ratified-1.md
```

## Expanded Folders

| Command | Folder | Scope |
|---|---|---|
| Store | `io-commands\01h-store` | Store KV key/value pair, `VS`, `SO`, `KL`, value payload, and store statuses. |
| Retrieve | `io-commands\02h-retrieve` | Retrieve value by key, `HBS`, `RO`, `KL`, returned value size in CQE Dword 0, and retrieve statuses. |
| List | `io-commands\06h-list` | List keys from starting key, `HBS`, returned key list structure, and list statuses. |
| Delete | `io-commands\10h-delete` | Delete key/value pair by key, `KL`, atomic delete, and delete statuses. |
| Exist | `io-commands\14h-exist` | Query whether key exists using completion status. |

## Shared KV Rules

| Rule | Meaning |
|---|---|
| CSI | Key Value Command Set uses `CSI=01h`. |
| Key size | Maximum KV key size is 16 bytes. A command with `KL > 16` is aborted with Invalid Field in Command. |
| Key fields | `CDW2/CDW3` contain key bytes `[7:0]`; `CDW14/CDW15` contain key bytes `[15:8]`. |
| Key identity | Two KV keys with different lengths are not the same key. |
| Atomic operations | Store and Delete are atomic with respect to the associated key/value pair. |
| Fused operations | The Key Value Command Set does not support fused operations. |
| Ordering | Controller does not enforce ordering between Store/Retrieve to the same key; host must enforce ordering if required. |

## Boundary

Base common I/O commands such as Flush and Reservations remain in `..\..\io-commands-2.0`. PyNVMe API syntax belongs in the API layer.
