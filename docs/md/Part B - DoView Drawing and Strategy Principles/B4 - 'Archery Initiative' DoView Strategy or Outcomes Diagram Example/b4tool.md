---
source_pdf: docs/pdf/b4tool.pdf
pair: b4
kind: tool
---

# DoView Tool B4 — 'Archery Initiative' DoView Strategy/Outcomes Diagram Example

> **Pair:** [Question](b4question.md) · Tool (this page)

Below is a simple fabricated example of a DoView strategy/outcomes diagram. It is conceptually similar to actual DoView strategy/outcomes diagrams used in practice. On the right of such diagrams, you can see the final outcome(s), and on the left, all of the steps it is believed are necessary to achieve the high-level outcome(s) set out in a simple 'This-Then' format.

## Diagram

```mermaid
flowchart LR
    subgraph col1["Inputs"]
        a1["Well trained archers"]
        a2["Good quality bows"]
        a3["Arrows sharp enough"]
        a4["Arrows light enough that they can potentially reach the bull's-eye"]
    end
    subgraph col2["Preparation"]
        b1["Arrows taken out of quiver fast enough"]
        b2["Arrows correctly notched onto the bowstring"]
        b3["Bowstring pulled back far enough"]
    end
    subgraph col3["Aim"]
        c1["Correct target accurately identified"]
        c2["Arrows lined up with bull's-eye"]
        c3["Sufficient adjustment to aiming of arrows to allow for cross-winds"]
    end
    subgraph col4["Firing"]
        d1["Sufficient number of arrows fired from bow"]
    end
    subgraph col5["Flight"]
        e1["Arrows get past any barriers in the way"]
        e2["Arrows still heading in the right direction after passing any barriers"]
        e3["Arrows still heading in the right direction three-quarters of the way up the range"]
        e4["Arrows still flying three-quarters of the way up the range"]
    end
    final["Sufficient arrows hit the bull's-eye"]
    col1 --> col2 --> col3 --> col4 --> col5 --> final
```

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
