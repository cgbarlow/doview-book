---
source_pdf: docs/pdf/i2tool.pdf
pair: i2
kind: tool
---

# DoView Tool I2 — How To Put a DoView Strategy/Outcomes Diagram into Existing Planning and Reporting Documents

> **Pair:** [Question](i2question.md) · Tool (this page)

The format of government planning and reporting documents is determined by legislative requirements and conventions about how they should be structured. An easy way to start using DoView strategy/outcomes diagrams is to put the relevant subpage from the agency or initiative's DoView diagram at the top of each chapter in reports, while the rest of the document is in the required format. The overview of an agency or initiative's DoView diagram can go in the introductory chapter, and each chapter about the agency or initiative's work can start with the relevant drill-down subpage. In some cases this has already been done in official government documentation where agencies have been using DoView Planning. Below shows the start of the introductory chapter of an 'Archery Initiative Plan' (B4).

## Diagram

### 1. Introduction to the Archery Initiative Plan

```mermaid
flowchart LR
    A1["Well trained archers"]
    A2["Good quality bows"]
    A3["Arrows sharp enough"]
    A4["Arrows light enough that they can potentially reach the bull's-eye"]
    B1["Arrows taken out of quiver efficiently"]
    B2["Arrows correctly notched onto the bowstring"]
    B3["Bowstring pulled back far enough"]
    C1["Correct target accurately identified"]
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

*The overview DoView strategy/outcomes diagram above shows the Archery Initiative's outcome: 'To ensure that sufficient arrows hit the bull's-eye'. The steps that we are pursuing to achieve this in our work are shown in the boxes in the diagram to the left of the outcome.*

*Our performance indicators are as follows . . .*

*The priorities are as follows . . .*

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
