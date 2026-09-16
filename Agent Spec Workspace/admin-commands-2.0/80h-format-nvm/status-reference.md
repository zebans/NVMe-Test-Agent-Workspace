# Format NVM Status Reference

Source: NVMe Base Specification 2.0, section 5.14, Figure 190, and global command-specific status table.

## Command Specific Status Values

| SCT | SC | Name | Meaning | Typical trigger |
|---|---|---|---|---|
| Command Specific | `0Ah` | Invalid Format | Selected format is invalid or unavailable. | Invalid User Data Format, insufficient metadata resources for PI, selected format unavailable, invalid security state. |

## Common Status Conditions

| Status | Typical trigger |
|---|---|
| Invalid Field in Command | Invalid `NSID=FFFFFFFFh` usage, reserved `SES`, reserved fields, invalid selector. |
| Invalid Namespace or Format | Command-set-specific format invalid, especially when `LBAFEE=0` and extended formats are requested. |
| Command Sequence Error | Format conflicts with command sequencing or active affected namespace command processing. |
| Format in Progress | I/O commands to affected namespace while format is in progress. |
| Operation Denied | Access-right/security state denies operation. |
| Namespace is Write Protected | Namespace write protection prohibits the command. |
| Access Denied | Security specification denies access to namespace/user data operation. |
| Asymmetric Access Inaccessible / Persistent Loss | Domain/subsystem division prevents requested format scope. |
