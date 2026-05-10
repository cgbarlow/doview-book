---
source_pdf: docs/pdf/f1tool.pdf
pair: f1
kind: tool
---

# DoView Tool F1 — Using a DoView Strategy/Outcomes Diagram for Performance Improvement

> **Pair:** [Question](f1question.md) · Tool (this page)

This DoView strategy/diagram from the 'Archery Initiative' Strategy/Outcomes Diagram Example (B4) shows how such a diagram can be used for performance improvement diagnosis and identifying Performance Improvement Projects (PIPs) to fix the problems.

## Diagram

```mermaid
flowchart LR
    archers["Well trained archers"]
    bows["Good quality bows"]
    sharp["Arrows sharp enough"]
    light["Arrows light enough that they can potentially reach the bull's-eye<br/>RED — PROBLEM: Some arrows are too heavy<br/>SOLUTION: PIP01 Arrow quality control project. 30 Nov. Operations Manager."]
    quiver["Arrows taken out of quiver efficiently<br/>RED — PROBLEM: Different archers are better/worse at pulling arrows from quiver<br/>SOLUTION: PIP02 Arrow out of quiver training project. 30 Feb and ONGOING. Training Manager."]
    notched["Arrows correctly notched onto the bowstring"]
    pulled["Bow string pulled back far enough"]
    targetID["Correct target accurately identified"]
    linedUp["Bow lined up with bull's-eye"]
    crosswind["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    fired["Sufficient number of arrows fired from bow<br/>ORANGE — PROBLEM: Insufficient arrows fired per hour<br/>SOLUTION: Dealt with by PIP02 — arrow out of quiver training project"]
    barriers["Arrows get past any barriers put up in the way"]
    afterBarriers["Arrows still heading in the right direction after passing any barriers"]
    threeQGoing["Sufficient number of arrows still going three-quarters of the way up the range<br/>ORANGE — PROBLEM: Arrows sometimes not getting to the target<br/>SOLUTION: Dealt with by PIP01 — arrow quality control project"]
    threeQDir["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    hit["Sufficient arrows hit the bull's-eye"]

    archers --> notched
    bows --> notched
    sharp --> notched
    light --> notched
    quiver --> notched
    notched --> linedUp
    pulled --> linedUp
    targetID --> fired
    linedUp --> fired
    crosswind --> fired
    fired --> barriers
    barriers --> afterBarriers
    afterBarriers --> threeQGoing
    afterBarriers --> threeQDir
    threeQGoing --> hit
    threeQDir --> hit
```

Each box is examined diagnostically and marked with a traffic light. Red and orange boxes get a Performance Improvement Project (PIP) attached, naming the problem, the project that addresses it, the deadline, and the responsible role.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
