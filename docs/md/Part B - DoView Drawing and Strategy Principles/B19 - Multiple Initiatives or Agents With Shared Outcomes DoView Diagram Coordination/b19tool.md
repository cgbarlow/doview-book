---
source_pdf: docs/pdf/b19tool.pdf
pair: b19
kind: tool
---

# DoView Tool B19 — Multiple Initiatives or Agents With Shared Outcomes DoView Diagram Coordination

> **Pair:** [Question](b19question.md) · Tool (this page)

## Diagram

The page is a three-tier visual alignment diagram. The top tier is a shared cross-agency DoView strategy/outcomes diagram (a left-to-right drill-down of grouped boxes). The middle tier shows eleven collaborative or individual projects (P01–P11). The bottom tier shows the contributing organizations, initiatives or human/AI agents (the page illustrates three: Children's Commissioner, Department of Conservation, and Ministry of Justice). Arrows from the bottom tier go up to the projects each agent is part of, and arrows from the projects go up to the boxes in the shared DoView each project is focused on — making the cross-agency line-of-sight visible.

```mermaid
flowchart BT
    subgraph DoView["DoView Strategy/outcomes diagram (shared)"]
        direction LR
        c1["Boxes (column 1)"] --> c2["Boxes (column 2)"] --> c3["Boxes (column 3)"] --> c4["Box (column 4)"] --> c5["Outcome"]
    end
    subgraph Projects["Collaborative or individual projects"]
        direction LR
        P01 --- P02 --- P03 --- P04 --- P05 --- P06 --- P07 --- P08 --- P09 --- P10 --- P11
    end
    subgraph Agents["Organizations, initiatives or human / AI agents"]
        direction LR
        A1["Children's Commissioner"]
        A2["Department of Conservation"]
        A3["Ministry of Justice"]
    end
    A1 --> P01
    A1 --> P03
    A1 --> P05
    A2 --> P02
    A2 --> P04
    A2 --> P06
    A2 --> P08
    A3 --> P07
    A3 --> P09
    A3 --> P10
    A3 --> P11
    P01 --> c1
    P02 --> c1
    P03 --> c2
    P04 --> c2
    P05 --> c2
    P06 --> c3
    P07 --> c3
    P08 --> c3
    P09 --> c4
    P10 --> c4
    P11 --> c5
```

The three layers — DoView strategy/outcomes diagram (top), collaborative or individual projects (middle), and organizations / initiatives / human or AI agents (bottom) — let everyone see at a glance which agents are contributing through which projects to which shared steps and outcomes.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
