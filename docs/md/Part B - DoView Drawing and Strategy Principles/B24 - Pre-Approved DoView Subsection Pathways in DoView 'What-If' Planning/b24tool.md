---
source_pdf: docs/pdf/b24tool.pdf
pair: b24
kind: tool
---

# DoView Tool B24 — Pre-Approved DoView Subsection Pathways in DoView 'What-If' Planning

> **Pair:** [Question](b24question.md) · Tool (this page)

In DoView What-If Planning (B23), when trigger indicators reach their threshold, you move to a new 'Current What-If DoView subsection' for planning and implementation. In some What-If DoView subsections, you have time to deliberate and decide which boxes to prioritize. If timing is tight when a particular What-If subsection is triggered, you can pre-approve a pathway to act fast. The Archery Initiative (B4) below shows three What-If DoView subsections: What-If 1: Business As Usual, What-If 2: Additional Barriers, and What-If 3: Person Shot on the Archery Range. In What-If 2, you have time to deliberate on which middle boxes are priorities. However, if What-If 3 is triggered, you implement all boxes as A priorities immediately in order to respond fast enough.

## Diagram

### What-If 1 — Business As Usual

```mermaid
flowchart LR
    a1["Correct target accurately identified"]
    a2["Arrows lined up with bullseye"]
    a3["Sufficient adjustment to aiming of arrows to allow for cross-winds"]
    a4["Sufficient number of arrows fired from bow"]
    a5["Arrows get past any barriers in the way"]
    a6["Arrows still heading in the right direction after passing any barriers"]
    a7["Arrows still flying three-quarters of the way up the range"]
    a8["Arrows still heading in the right direction three-quarters of the way up the range"]
    a9["Sufficient arrows hit the bulls-eye"]
    a1 --> a4
    a2 --> a4
    a3 --> a4
    a4 --> a5 --> a6 --> a7 --> a9
    a6 --> a8 --> a9
```

### Switch Indicators

- **M001** — Number of barriers on the range counted (functions as What-If Planning Switch Indicator triggering a switch to What-If 2 when number of barriers greater than 3).
- **M002** — Someone is shot by an arrow on the archer range. A What-If Switch Indicator triggering switching to What-If 3 which has a pre-approved pathway of all boxes being A priorities which you immediately implement.

### What-If 2 — Additional Barriers (deliberate; prioritize as normal)

```mermaid
flowchart LR
    b1["New barriers on range identified and mapped"]
    b2a["New firing positon built for archers"]
    b2b["Archers receive additional training on shooting past barriers"]
    b2c["Archers given crossbows, while more expensive they are more likely to get past barriers"]
    b3["Ongoing monitoring of barrier-related incidents"]
    b1 --> b2a --> b3
    b1 --> b2b --> b3
    b1 --> b2c --> b3
```

### What-If 3 — Person Shot on the Archery Range (pre-approved; all boxes are A priorities, implement immediately)

```mermaid
flowchart LR
    c1["Ambulance called (A)"]
    c2["Police called (A)"]
    c3["Archery range closed down (A)"]
    c4["Police take statements from witnesses (A)"]
    c1 --> c3 --> c4
    c2 --> c3
```

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
