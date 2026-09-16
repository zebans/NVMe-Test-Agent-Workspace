# Virtualization Management Restrictions

| Restriction | Meaning | Violation / outcome |
|---|---|---|
| Resource range must exist | Requested VQ/VI resources must exist. | `Invalid Resource Identifier`. |
| Resource type must be supported | VQ/VI private or unsupported resource requests are invalid. | `Invalid Resource Identifier`. |
| Resources must be available | `NR` cannot exceed remaining available flexible resources. | `Invalid Resource Identifier`. |
| Secondary Assign requires Offline state | Assigning resources to a secondary controller requires appropriate state. | `Invalid Secondary Controller State`. |
| Secondary Online requires proper configuration and enabled primary controller | Otherwise online action is invalid. | `Invalid Secondary Controller State`. |

