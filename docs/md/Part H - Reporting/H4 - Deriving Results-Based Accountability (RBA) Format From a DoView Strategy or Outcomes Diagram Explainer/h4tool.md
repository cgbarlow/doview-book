---
source_pdf: docs/pdf/h4tool.pdf
pair: h4
kind: tool
---

# DoView Tool H4 — Deriving Results-Based Accountability (RBA) Format From a DoView Strategy/Outcomes Diagram Explainer

> **Pair:** [Question](h4question.md) · Tool (this page)

Indicators can be located from a DoView strategy/outcomes diagram and then tagged with the type of Results Based Accountability (RBA) indicator they are (in B below). Then they can simply be rearranged under the Results Based Accountability indicator headings to provide an RBA report (in A below). This example uses the 'Archery Initiative' example (B4).

## Diagram

### A — Indicators rearranged under RBA headings

| RBA heading | Indicators |
|---|---|
| How much did we do? | 005 Number of arrows fired per hour @ #How much did we do? |
| How well did we do? | 002 Average time to remove an arrow from quiver @ #How well did we do?; 006 Cost for firing each arrow @ #How well did we do?; 003 Average distance bowstring pulled back @ #How well did we do? |
| Is anyone better off? | 009 Number of arrows hitting the bull's-eye per hour #Is anyone better off?; 011 Money saved by arrows hitting the target #Is anyone better off? |

\* @ = Controllable indicators

### B — Indicators tagged on the DoView strategy/outcomes diagram

```mermaid
flowchart LR
    A1["Well trained archers<br/>001 Percentage archers with Archery Degree @ #Learning and growth"]
    A2["Arrows light enough that they can potentially reach the bull's-eye"]
    A3["Good quality bows"]
    A4["Arrows sharp enough"]
    B1["Arrows taken out of quiver efficiently<br/>002 Average time to remove an arrow from quiver @ #How well did we do?"]
    B2["Arrows correctly notched onto the bowstring"]
    B3["Bowstring pulled back far enough<br/>003 Average distance bowstring pulled back @ #How well did we do?"]
    C1["Correct bull's-eye accurately identified<br/>004 Percent occasions bull's-eyes accurately identified @ #Internal business process"]
    C2["Bow lined up with bull's-eye"]
    C3["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    D["Sufficient number of arrows fired from bow<br/>005 Number of arrows fired per hour @ #How much did we do?"]
    E["Arrows get past any barriers put up in the way<br/>006 Percent arrows get past barriers"]
    F["Arrows still heading in the right direction after passing any barriers<br/>007 Percent arrows still heading in the right direction after passing any barriers"]
    G1["Sufficient number of arrows still going three-quarters of the way up the range<br/>008 Percent arrows still going three-quarters up the range"]
    G2["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    H["Sufficient arrows hit the bull's-eye<br/>009 Number of arrows hitting the bull's-eye per hour #Customer perspective"]

    A1 --> B1
    A2 --> B1
    A3 --> B1
    A4 --> B1
    B1 --> C1
    B2 --> C1
    B3 --> C1
    C1 --> D
    C2 --> D
    C3 --> D
    D --> E --> F --> G1
    F --> G2
    G1 --> H
    G2 --> H
```

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
