---
source_pdf: docs/pdf/b6tool.pdf
pair: b06
kind: tool
---

# DoView Tool B6 — A Real-World Interactive Drill-Down DoView Strategy/Outcome Diagram Example

> **Pair:** [Question](b06question.md) · Tool (this page)

An example of an interactive drill-down DoView strategy/outcomes diagram for regional development with the drilled-down subpage under the 'Exuberant economy' box shown.

## Diagram

### Regional Development Overview Page

```mermaid
flowchart LR
    a1["Well-run region"]
    a2["Community and stakeholder engagement"]
    a3["Exuberant economy"]
    a4["Stunning environment"]
    a5["Thriving communities"]
    a6["Vibrant cultures"]
    final["A sustainable, economically thriving inclusive region"]
    a1 --> a2
    a2 --> a3
    a2 --> a4
    a2 --> a5
    a2 --> a6
    a3 --> final
    a4 --> final
    a5 --> final
    a6 --> final
```

### Drill-down page — Exuberant economy

```mermaid
flowchart LR
    subgraph col1["Foundations"]
        b1["The nature and extent of potential economic activity in the region understood"]
        b2["The special role of indigenous people in economic development recognized"]
        b3["Natural resources used in a sustainable manner (e.g. land use)"]
        b4["The business and technical acumen of the business community fully utilized"]
    end
    subgraph col2["Brokerage & focus"]
        c1["Sustainable economic development opportunities effectively brokered"]
        c2["Economic activity focused on areas and opportunities that retain as much wealth as possible in the region"]
        c3["High quality jobs promoted"]
        c4["Barriers to growth identified and addressed"]
    end
    subgraph col3["Capture value"]
        d1["Local competitive advantage built on"]
        d2["The full value chain related to economic activity exploited"]
    end
    subgraph col4["Region-level outcomes"]
        e1["The region's full economic potential captured"]
        e2["Income retained in the region"]
    end
    subgraph col5["Population outcomes"]
        f1["People get ahead and reach their full economic potential"]
        f2["Unemployment in the region reduced"]
        f3["Increased household earnings in the district"]
        f4["Opportunities for different population groups opened up (e.g. women)"]
        f5["Workforce age distribution rebalanced"]
        f6["Less social service spending because less people need them"]
    end
    final["Exuberant economy"]
    col1 --> col2 --> col3 --> col4 --> col5 --> final
```

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
