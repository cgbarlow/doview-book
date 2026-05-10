---
source_pdf: docs/pdf/h1tool.pdf
pair: h1
kind: tool
---

# DoView Tool H1 — Reporting Indicator and Evaluation Results Back Against a DoView Strategy Diagram

> **Pair:** [Question](h1question.md) · Tool (this page)

This tool shows an Archery Initiative DoView strategy/outcomes diagram with indicator results (numbered 001–009) and evaluation findings (numbered 01–04) reported directly back against the relevant steps in the diagram.

## Diagram

```mermaid
flowchart LR
    A1["Well trained archers"]
    A2["Arrows light enough that they can potentially reach the bull's-eye"]
    A3["Good quality bows"]
    A4["Arrows sharp enough"]
    B1["Arrows taken out of quiver efficiently"]
    B2["Arrows correctly notched onto the bowstring"]
    B3["Bowstring pulled back far enough"]
    C1["Correct bull's-eye accurately identified"]
    C2["Bow lined up with bull's-eye"]
    C3["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    D["Sufficient number of arrows fired from bow"]
    E["Arrows get past any barriers put up in the way"]
    F["Arrows still heading in the right direction after passing any barriers"]
    G1["Sufficient number of arrows still going three-quarters of the way up the range"]
    G2["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    H["Sufficient arrows hit the bull's-eye"]

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

### Indicator results reported against steps

| Indicator | Step | Result |
|---|---|---|
| 001 Percentage archers with Archery Degree | Well trained archers | 20% |
| 002 Average time to remove an arrow from quiver | Arrows taken out of quiver efficiently | 1 sec |
| 003 Average distance bowstring pulled back | Bowstring pulled back far enough | 40 cm |
| 004 Percentage of archers accurately identify bull's-eye | Correct bull's-eye accurately identified | 75% |
| 005 Number of arrows fired per hour | Sufficient number of arrows fired from bow | 85 |
| 006 Percent arrows get past barriers | Arrows get past barriers | 63% |
| 007 Percent arrows still heading in the right direction after passing any barriers | Arrows still heading right after barriers | 52% |
| 008 Percent arrows still going three-quarters up the range | Sufficient number three-quarters up | 34% |
| 009 Number of arrows hitting the bulls-eye per hour | Sufficient arrows hit the bull's-eye | 28 |

### Evaluation findings reported against steps

| Eval Q | Step | Finding |
|---|---|---|
| 01 Can lighter arrows be sourced from another supplier? | Arrows light enough | Alternative supplier sourced |
| 02 What are the ways arrows can be taken out of the quiver? | Arrows taken out of quiver efficiently | Three techniques identified and taught to archers |
| 03 Are there any ways that the number of arrows fired can be increased? | Sufficient number of arrows fired from bow | Additional staff employed to feed arrows to archers |
| 04 Did the program increase the number of arrows hitting the bull's-eye? | Sufficient arrows hit the bull's-eye | Experimental impact evaluation design proved it did. The effect size was a 30% increase. |

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
