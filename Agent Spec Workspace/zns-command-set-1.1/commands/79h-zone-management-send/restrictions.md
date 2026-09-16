# Zone Management Send Restrictions

Source: ZNS section 3.4.3.

## Select All

If Select All is set, `SLBA` is ignored and the action applies to all zones that match the action's state criteria.

Set Zone Descriptor Extension shall be aborted with Invalid Field in Command if Select All is set.

## SLBA

If Select All is cleared, `SLBA` must specify the starting logical block for a zone in the specified zoned namespace. Otherwise, the controller shall abort with Invalid Field in Command.

## Resource Limits

If there are insufficient available Active Resources or Open Resources, the command is aborted as defined in the ZNS resource model and no zone state transition occurs.

## Write Protection

If the zoned namespace containing the specified zone is write protected as described in the Base Specification Namespace Write Protection section, the controller shall abort with Namespace is Write Protected.

## Outstanding Commands

If the controller has multiple outstanding Zone Management Send commands that specify one or more of the same zones, results are undefined.

## Shared Zoned Namespace

For a shared zoned namespace, host coordination for Zone Management Send commands is outside the scope of the ZNS specification.
