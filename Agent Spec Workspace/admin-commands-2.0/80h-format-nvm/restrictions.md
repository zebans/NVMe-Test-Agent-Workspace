# Format NVM Restrictions

Source: NVMe Base Specification 2.0, section 5.14.

## Destructive Scope

| Case | Affected scope |
|---|---|
| Relevant FNA bit cleared, `NSID=FFFFFFFFh` | All namespaces attached to the controller; other namespaces are not affected. |
| Relevant FNA bit cleared, allocated namespace ID | Specified namespace only. |
| Relevant FNA bit set, allocated namespace ID or `FFFFFFFFh` | All allocated namespaces in the NVM subsystem. |

Use FNA bit 1 for secure erase scope and FNA bit 0 for format without secure erase.

## Required Cautions

| Restriction | Expected impact |
|---|---|
| Previous user data shall not be returned after successful completion. | Destructive data expectation. |
| `NSID=FFFFFFFFh` may be disallowed by FNA bit 3. | Invalid Field in Command. |
| Active I/O commands for affected namespaces may conflict. | Command Sequence Error or Format in Progress behavior. |
| Format in progress may abort I/O to affected namespaces. | Format in Progress. |
| Write-protected namespace state may prohibit Format NVM. | Namespace is Write Protected. |
| Security/access state may prohibit Format NVM. | Access Denied or Operation Denied. |
| Domain division may prevent formatting requested namespace set. | Asymmetric Access Inaccessible or Persistent Loss. |
| Command-set-specific LBA format / PI / metadata choices must be valid. | Invalid Format or Invalid Namespace or Format. |
