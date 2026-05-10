---
source_pdf: docs/pdf/c7tool.pdf
pair: c7
kind: tool
---

# DoView Tool C7 — Outputs/Deliverables Groupings Hiding Links Between Individual Outputs and Outcomes Explainer

> **Pair:** [Question](c7question.md) · Tool (this page)

'A' shows a group of outputs (deliverables) where all of the individual outputs just happen to focus on influencing a single outcome (Outcome 1). In such a case, only showing the relationship between Output Group 1 and the higher-level Outcome 1 does not hide which outputs are focused on which outcome(s). However, in 'B', the outputs in Output Group 2 focus on multiple outcomes, but which outputs focus on which outcomes is hidden. Therefore, it is impossible to rigorously determine the extent of line-of-sight alignment. There might be only a single individual output that is focused on Outcomes 2 and 3, or there may be more. The only way to deal with this is in 'C', which shows the full fine-grained DoView strategy/outcomes diagram showing all of the connections between individual outputs and high-level outcomes. So, from the representation in C, for instance, you can check alignment and see that the outputs in Output Group 2 focus more on Outcome 1 than on Outcomes 2 or 3.

## A — Single-outcome group (no information loss)

```mermaid
flowchart LR
    o11["Output 1.1"]
    o12["Output 1.2"]
    o13["Output 1.3"]
    o14["Output 1.4"]
    G1["Outputs Group 1"]
    O1["Outcome 1"]

    o11 --- G1
    o12 --- G1
    o13 --- G1
    o14 --- G1
    G1 --> O1
```

## B — Multi-outcome group, individual links hidden

```mermaid
flowchart LR
    o21["Output 2.1"]
    o22["Output 2.2"]
    o23["Output 2.3"]
    o24["Output 2.4"]
    G2["Outputs Group 2"]
    O1["Outcome 1"]
    O2["Outcome 2"]
    O3["Outcome 3"]

    o21 --- G2
    o22 --- G2
    o23 --- G2
    o24 --- G2
    G2 --> O1
    G2 --> O2
    G2 --> O3
```

## C — Full fine-grained DoView showing every individual link

```mermaid
flowchart LR
    o21["Output 2.1"]
    o22["Output 2.2"]
    o23["Output 2.3"]
    o24["Output 2.4"]
    G2["Outputs Group 2"]
    O1["Outcome 1"]
    O2["Outcome 2"]
    O3["Outcome 3"]

    o21 -.-> G2
    o22 -.-> G2
    o23 -.-> G2
    o24 -.-> G2
    o21 --> O1
    o22 --> O1
    o23 --> O1
    o23 --> O2
    o24 --> O1
    o24 --> O3
```

In this fine-grained version you can check alignment directly: the outputs in Output Group 2 focus more on Outcome 1 than on Outcomes 2 or 3.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
