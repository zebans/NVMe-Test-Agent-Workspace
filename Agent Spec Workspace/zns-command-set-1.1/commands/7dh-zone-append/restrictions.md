# Zone Append Restrictions

Source: ZNS section 3.4.1 and ZNS command-specific status table.

## Zone Requirements

- The target zone must be Sequential Write Required.
- `ZSLBA` must be the lowest logical block of the target zone.
- The command may fail with zone-specific statuses when the target zone is Full, Read Only, Offline, or when active/open resource limits prevent the operation.

## Ordering

Write ordering for multiple outstanding Zone Append commands to the same zone is undefined and left to the controller.

## Protection Information

The host does not know the final assigned LBA when issuing the command. Therefore, LBA-based reference tag behavior is controlled by the ZNS `PIREMAP` rules in section 3.4.1.1.

## Atomicity

The NVM atomicity parameters `AWUN`, `NAWUN`, `NABSN`, `AWUPF`, `NAWUPF`, and `NABSPF` apply to Zone Append as defined in the NVM Command Set.
