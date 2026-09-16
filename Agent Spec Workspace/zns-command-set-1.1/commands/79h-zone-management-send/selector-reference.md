# Zone Management Send Selector Reference

## Zone Send Action (`ZSA`)

| `ZSA` | Action | Reference |
|---:|---|---|
| `00h` | Reserved | Invalid / reserved selector. |
| `01h` | Close Zone | Close open zones or no-op on Closed. |
| `02h` | Finish Zone | Finish Empty, Opened, or Closed zones. |
| `03h` | Open Zone | Explicitly open Empty, Implicitly Opened, or Closed zones. |
| `04h` | Reset Zone | Reset Opened, Closed, or Full zones to Empty. |
| `05h` | Offline Zone | Move Read Only zones to Offline. |
| `06h`-`0Fh` | Reserved | Invalid / reserved selector. |
| `10h` | Set Zone Descriptor Extension | Attach extension data to an Empty zone and transition it to Closed. |
| `11h`-`FFh` | Reserved | Invalid / reserved selector. |

## Select All

| Select All | Meaning | Important rule |
|---:|---|---|
| `0` | `SLBA` identifies one target zone. | `SLBA` must be the zone's lowest LBA. |
| `1` | Action applies to all zones matching the action criteria. | `SLBA` is ignored. Invalid for Set Zone Descriptor Extension. |

## Action / State Matrix

| Action | Valid transition / no-op | Invalid state transition |
|---|---|---|
| Close Zone | Implicitly Opened or Explicitly Opened -> Closed; Closed -> no change. Select All closes all Implicitly/Explicitly Opened zones. | Empty, Full, Read Only, Offline. |
| Finish Zone | Empty, Implicitly Opened, Explicitly Opened, or Closed -> Full; Full -> no change. Select All finishes Implicitly Opened, Explicitly Opened, and Closed zones. | Read Only, Offline. |
| Open Zone | Empty, Implicitly Opened, or Closed -> Explicitly Opened; Explicitly Opened -> no change. Select All opens Closed zones. | Full, Read Only, Offline. |
| Reset Zone | Implicitly Opened, Explicitly Opened, Closed, or Full -> Empty; Empty -> no change. Select All resets Implicitly Opened, Explicitly Opened, Closed, and Full zones. | Read Only, Offline. |
| Offline Zone | Read Only -> Offline; Offline -> no change. Select All offlines Read Only zones. | Empty, Implicitly Opened, Explicitly Opened, Closed, Full. |
| Set Zone Descriptor Extension | Empty -> Closed and descriptor extension data is set. | Any state other than Empty; Select All set. |

## Resource-Limit Rule

If there are insufficient available Active Resources or Open Resources, the command is aborted as defined by the ZNS resource model and no zone state transition occurs.
