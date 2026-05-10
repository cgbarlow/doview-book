---
source_pdf: docs/pdf/b22tool.pdf
pair: b22
kind: tool
---

# DoView Tool B22 — Representing Citizen-Experience Maps As DoView Strategy Diagrams Explainer

> **Pair:** [Question](b22question.md) · Tool (this page)

Citizen-experience maps can be used to specifying citizen outcomes. You can represent them as a DoView strategy diagram. 'A' below is a DoView citizens-experience map for making it easier for all citizens to interact with government in a digital world. 'B' is a citizen-experience map for an example of where government wants to intervene with a particular group. In this case, preventing young offenders from continuing to offend with the hope that by doing so, this will reduce likely government expenditure in the future.

## Diagram

### A — Citizens-experience map: easier interaction with government in a digital world

```mermaid
flowchart LR
    a1["People know where to start when seeking services or meeting their obligations"]
    a2a["People can find, and understand, the information they need and know what to do next when using government services"]
    a2b["People find government services have high usability values"]
    a2c["People do not have to provide the same information to different agencies"]
    a2d["People trust their information will be securely managed"]
    a3["People have a consistently high quality experience when interacting with government"]
    a3b["People can shift channels easily when they want to"]
    a4a["Where possible, services are delivered automatically without people having to apply for them"]
    a4b["Seamless services not requiring people to navigate multiple government agencies"]
    a4c["People can easily prove who they are and their situation when interacting with government"]
    a5["People find it easier to interact with government"]
    a1 --> a2a --> a3 --> a4a --> a5
    a1 --> a2b --> a3
    a1 --> a2c --> a3b --> a4b --> a5
    a1 --> a2d --> a3b
    a3 --> a4c --> a5
```

### B — Citizens-experience map for young offenders

```mermaid
flowchart LR
    b1a["Young offender's supported back into suitable learning environment"]
    b1b["Young offenders' health issue met"]
    b1c["Young offenders' psychological and mental health needs met"]
    b1d["Young offender's cultural identity needs met"]
    b1e["Young offender's essential housing/financial and support needs met"]
    b2a["Young offender exposed to positive role models"]
    b2b["Young offender exposed to positive peer relationship"]
    b3a["Young offender cared for by their family to the extent possible"]
    b3b["Young offender learns to be more responsible"]
    b3c["Young offender's rights respected"]
    b3d["Young offender has continuity in their life rather than disruption"]
    b4["Young offenders have better outcomes"]
    b1a --> b2a --> b3a --> b4
    b1b --> b2a --> b3b --> b4
    b1c --> b2b --> b3c --> b4
    b1d --> b2b --> b3d --> b4
    b1e --> b2a
```

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
