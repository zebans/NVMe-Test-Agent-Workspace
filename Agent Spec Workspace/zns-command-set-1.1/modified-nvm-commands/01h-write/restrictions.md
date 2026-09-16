# ZNS-Modified Write Restrictions

- Command range shall not violate ZNS zone boundary requirements.
- Target zone state can cause Full, Read Only, or Offline status.
- Writes to Sequential Write Required zones must respect the write pointer.
- Active/open zone resource limits may abort the command with ZNS-specific status.
