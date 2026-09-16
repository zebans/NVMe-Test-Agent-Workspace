# Sanitize Payload Reference

Source: NVMe Base Specification 2.0, section 5.24.

Sanitize has no data buffer payload. All command parameters are in `CDW10` and `CDW11`.

## Related Runtime Payloads

| Need | Use |
|---|---|
| Sanitize progress | Get Log Page `LID=81h` Sanitize Status. |
| Sanitize operation completion/failure state | Sanitize Status log and asynchronous event behavior. |
| Supported sanitize operation types | Identify Controller `SANICAP`. |
| No-deallocate behavior | Identify Controller `SANICAP.NDI/NODMMAS` and Set Features Sanitize Config `NODRM`. |
