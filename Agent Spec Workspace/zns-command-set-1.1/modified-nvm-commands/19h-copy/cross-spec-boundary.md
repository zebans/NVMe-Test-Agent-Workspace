# ZNS-Modified Copy Cross-Spec Boundary

NVM owns:

- base Copy command fields;
- Source Range Entry structure;
- base copy semantics and completion.

ZNS owns:

- zone boundary constraints for source and destination ranges;
- destination write pointer constraint;
- source/destination zone-state status additions.

API usage and test-flow design are outside this file.
