---
source_pdf: docs/pdf/f6tool.pdf
pair: f6
kind: tool
---

# DoView Tool F6 — Embedding Evidence in DoView Strategy/Outcomes Diagram Templates Tool

> **Pair:** [Question](f6question.md) · Tool (this page)

You can construct DoView strategy/outcomes diagrams as template strategy/outcomes diagrams and embed evidence within them. If practitioners and planners then use these in their planning and implementation work, evidence-based practice can be fostered without requiring additional work on the part of practitioners and planners. It does not even matter whether practitioners and planners are even particularly aware that they are using evidence-based practice when their work is being guided in this way.

## Diagram

### Current approach

```mermaid
flowchart LR
    subgraph researchers["Work researchers do"]
        c1["Basic research"]
        c2["AI assisted evidence summaries"]
        c1 --> c2
    end
    subgraph practitioners["Work practitioners & planners have to do"]
        c3["Practitioner or planner reads evidence summaries"]
        c4["Practitioner or planner uses evidence in their work"]
        c3 --> c4
    end
    c2 --> c3
```

### Evidence-embedded DoView strategy/outcomes diagram template approach

```mermaid
flowchart LR
    subgraph researchers2["Work researchers do"]
        e1["Basic research"]
        e2["AI assisted evidence summaries"]
        e1 --> e2
    end
    subgraph rfo["Work researchers, funders or others do"]
        e3["Evidence embedded in template DoView strategy diagrams"]
    end
    subgraph practitioners2["Work practitioners & planners have to do"]
        e4["Using evidence-based DoViews means evidence is embedded in practice"]
    end
    e2 --> e3 --> e4
```

In the current approach, practitioners and planners have to actively read evidence summaries before using them. In the evidence-embedded approach, the work of integrating evidence is done upstream — practitioners get evidence-based practice automatically by using the templates.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
