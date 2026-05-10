---
source_pdf: docs/pdf/c8tool.pdf
pair: c08
kind: tool
---

# DoView Tool C8 — Problem with Measurement-Homogeneous Output (Deliverable) Groups Obscuring The Links Between Individual Outputs and Outcomes Explainer

> **Pair:** [Question](c08question.md) · Tool (this page)

In some outcomes systems, outputs (deliverables) are grouped into output groups based on the outputs being able to be measured in similar ways. This is to make it easier and quicker to measure whether a large group of outputs has been delivered. However, if only a 'homogeneous measurement output groups' relationship with higher-level outcomes is reported on, the detailed DoView Visual Alignment information, which could be captured within a DoView strategy/outcomes diagram shown in 'A' will be lost. This happens if only representation 'B' is available. This is because 'B' does not show the detail of which grey outputs 1, 3, 4, 6 (only grouped because they are all measured in the same way) are linked to which outcomes.

## A — Full DoView Visual Alignment (individual outputs to outcomes)

```mermaid
flowchart LR
    o1["Output 1 (homogeneous group)"]
    o2["Output 2"]
    o3["Output 3 (homogeneous group)"]
    o4["Output 4 (homogeneous group)"]
    o5["Output 5"]
    o6["Output 6 (homogeneous group)"]
    o7["Output 7"]
    O1["Outcome 1"]
    O2["Outcome 2"]
    O3["Outcome 3"]

    o1 --> O1
    o1 --> O2
    o2 --> O1
    o3 --> O2
    o3 --> O3
    o4 --> O1
    o4 --> O3
    o5 --> O2
    o6 --> O3
    o7 --> O3
```

## B — Only the homogeneous group → outcomes link is shown (detail lost)

```mermaid
flowchart LR
    o1["Output 1"]
    o3["Output 3"]
    o4["Output 4"]
    o6["Output 6"]
    HMG["Homogeneous Measurement Output Group"]
    O1["Outcome 1"]
    O2["Outcome 2"]
    O3["Outcome 3"]

    o1 --- HMG
    o3 --- HMG
    o4 --- HMG
    o6 --- HMG
    HMG --> O1
    HMG --> O2
    HMG --> O3
```

In B, you can no longer tell which individual grey outputs (1, 3, 4, 6) are aligned to which outcomes — the fine-grained alignment information has been hidden by reporting only at the group level.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
