---
source_pdf: docs/pdf/b23tool.pdf
pair: b23
kind: tool
---

# DoView Tool B23 — DoView 'What-If' Planning

> **Pair:** [Question](b23question.md) · Tool (this page)

It is difficult to plan in times such as the present when we face convulsive change. Rather than decision-makers attempting to achieve a consensus on the likely future strategic environment, it is better to use DoView What-If Planning. In DoView-based scenario planning, you develop more than one DoView diagram or subpart of a DoView diagram, in addition to developing 'Switch Indicators'. When these indicators cross certain thresholds, they trigger you to change your 'Current What-If DoView' to an alternative one. You then use the alternative one as the basis for your ongoing strategy. Below, when the Switch Indicator reaches a threshold it triggers moving from What-If 1 DoView (A below) to What-If 2 DoView Subsection (B below) in the Archery Initiative DoView (B4).

## Diagram

### A — What-If 1: Business as Usual DoView

```mermaid
flowchart LR
    a1["Correct target accurately identified"]
    a2["Arrows lined up with bull's-eye"]
    a3["Sufficient adjustment to aiming of arrows to allow for cross-winds"]
    a4["Sufficient number of arrows fired from bow"]
    a5["Arrows get past any barriers in the way"]
    a6["Arrows still heading in the right direction after passing any barriers"]
    a7["Arrows still flying three-quarters of the way up the range"]
    a8["Arrows still heading in the right direction three-quarters of the way up the range"]
    a9["Sufficient arrows hit the bull's-eye"]
    a1 --> a4
    a2 --> a4
    a3 --> a4
    a4 --> a5 --> a6 --> a7 --> a9
    a6 --> a8 --> a9
```

**Switch Indicator (M001):** Number of barriers on the range counted (functions as What-If Planning Switch Indicator triggering a switch to What-If 2 when number of barriers greater than 3.)

### B — What-If 2: Additional Barriers DoView Subsection

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

When M001 crosses its threshold, the Current What-If DoView switches from A to B and B becomes the basis for ongoing strategy.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
