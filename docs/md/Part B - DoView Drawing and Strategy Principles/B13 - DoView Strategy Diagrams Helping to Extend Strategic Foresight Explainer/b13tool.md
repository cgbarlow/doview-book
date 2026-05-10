---
source_pdf: docs/pdf/b13tool.pdf
pair: b13
kind: tool
---

# DoView Tool B13 — DoView Strategy Diagrams Helping to Extend Strategic Foresight Explainer

> **Pair:** [Question](b13question.md) · Tool (this page)

DoView Strategy/outcomes diagrams allow us to project our strategic thinking into the future because they include the dimensions of time and sequence. They do this in a way that 'flat' sets of outcomes and strategies within traditional strategic plans that do not visualize the 'This-Then' structure do not.

When you look at these lower-level steps on the left of the DoView ... your eye is immediately drawn to these higher-level outcomes as they follow a left-to-right 'This-Then' progression. This helps you to focus on the future.

## Diagram

```mermaid
flowchart LR
    subgraph col1["Inputs (lower-level)"]
        a1["Well trained archers"]
        a2["Good quality bows"]
        a3["Arrows sharp enough"]
        a4["Arrows light enough that they can potentially reach the bulls-eye"]
    end
    subgraph col2["Preparation"]
        b1["Arrows taken out of quiver efficiently"]
        b2["Arrows correctly notched onto the bow string"]
        b3["Bow string pulled back far enough"]
    end
    subgraph col3["Aim"]
        c1["Correct target accurately identified"]
        c2["Bow lined up with bullseye"]
        c3["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    end
    subgraph col4["Firing"]
        d1["Sufficient number of arrows fired from bow"]
    end
    subgraph col5["Flight (higher-level)"]
        e1["Arrows get past any barriers put up in the way"]
        e2["Arrows still heading in the right direction after passing any barriers"]
        e3["Sufficient number of arrows still going three-quarters of the way up the range"]
        e4["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    end
    final["Sufficient arrows hit the bulls-eye"]
    col1 --> col2 --> col3 --> col4 --> col5 --> final
```

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
