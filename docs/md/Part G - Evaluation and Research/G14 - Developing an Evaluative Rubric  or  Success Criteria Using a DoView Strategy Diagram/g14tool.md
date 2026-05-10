---
source_pdf: docs/pdf/g14tool.pdf
pair: g14
kind: tool
---

# DoView Tool G14 — Developing an Evaluative Rubric / Success Criteria Using a DoView Strategy Diagram

> **Pair:** [Question](g14question.md) · Tool (this page)

You can summarize whether or not an organization, agency, provider, policy or initiative is 'successful' using a sliding scale of success (e.g. from 3 to 1). To do this, develop a set of criteria to determine where an initiative is positioned on this scale. Such a set of criteria is often called a rubric, success criteria list or a maturity model. You can use a DoView strategy/outcomes diagram to either develop such a rubric or to assess how comprehensive an existing rubric is. The success criteria below have been developed from the gray boxes in the DoView outcomes diagram below.

## Rubric / Success Criteria

### 3. Successful initiative

- All archers have a basic degree in archery and a third or more an advanced degree
- All bows are less than two years old and from a reputable brand
- Bow strings pulled back to 100% of stretch 95% of the time
- Each archer fires at least 15 arrows a minute
- Bow lined up with bullseye 95% of the time

### 2. Partially successful initiative

- 50% of archers have at least a basic degree in archery
- All bows are less than five years old and from a reputable brand
- Bow strings pulled back to 75% of stretch 95% of the time
- Each archer fires at least 10 arrows a minute
- Bow lined up with bullseye 75% of the time

### 1. Unsuccessful initiative

- Less than 25% of archers have at least a basic degree in archery
- Some bows are more than 8 years old and many are from unreliable brands
- Bow strings pulled back to less than 50% of stretch 95% of the time
- Many archers firing less than 5 arrows a minute
- Bow lined up with bullseye less than 60% of the time

## Diagram

```mermaid
flowchart LR
    subgraph inputs["Inputs"]
        n1["Well trained archers"]
        n2["Good quality bows"]
        n3["Arrows sharp enough"]
        n4["Arrows light enough that they can potentially reach the bulls-eye"]
    end
    subgraph prep["Preparation"]
        n5["Arrows taken out of quiver efficiently"]
        n6["Arrows correctly notched onto the bow string"]
        n7["Bow string pulled back far enough"]
    end
    subgraph aim["Aim"]
        n8["Correct target accurately identified"]
        n9["Bow lined up with bullseye"]
        n10["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    end
    n11["Sufficient number of arrows fired from bow"]
    n12["Arrows get past any barriers put up in the way"]
    n13["Arrows still heading in the right direction after passing any barriers"]
    n14["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    n15["Sufficient number of arrows still going three-quarters of the way up the range"]
    n16["Sufficient arrows hit the bulls-eye"]
    inputs --> prep --> aim --> n11 --> n12 --> n13 --> n14 --> n15 --> n16
```

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
