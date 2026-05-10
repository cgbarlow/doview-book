---
source_pdf: docs/pdf/g7tool.pdf
pair: g7
kind: tool
---

# DoView Tool G7 — Mapping a Set of Evaluation Questions Onto a Strategy/Outcomes Diagram

> **Pair:** [Question](g7question.md) · Tool (this page)

Below evaluation questions are shown on an illustrative 'Archery Initiative' DoView strategy/outcomes diagram (B4). Use this approach to identify duplicate evaluation questions and find the level at which any evaluation question is struck. Then use the Generic Evaluation Questions List (G4) to check if it is a comprehensive set of questions.

## Diagram

```mermaid
flowchart LR
    s1["Well trained archers"]
    s2["Good quality bows"]
    s3["Arrows sharp enough"]
    s4["Arrows light enough that they can potentially reach the bulls-eye"]
    s5["Arrows correctly notched onto the bow string"]
    s6["Arrows taken out of quiver efficiently"]
    s7["Bow string pulled back far enough"]
    s8["Correct bulls-eye accurately identified"]
    s9["Bow lined up with bullseye"]
    s10["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    s11["Sufficient number of arrows fired from bow"]
    s12["Arrows get past any barriers put up in the way"]
    s13["Arrows still heading in the right direction after passing any barriers"]
    s14["Sufficient number of arrows still going three-quarters of the way up the range"]
    s15["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    s16["Sufficient arrows hit the bulls-eye"]
    s1 --> s5
    s2 --> s5
    s3 --> s5
    s4 --> s5
    s5 --> s8
    s6 --> s8
    s7 --> s8
    s8 --> s11
    s9 --> s11
    s10 --> s11
    s11 --> s12 --> s13 --> s14
    s13 --> s15
    s14 --> s16
    s15 --> s16
```

### Evaluation questions mapped to the diagram

| ID | Type | Question | Mapped to |
|---|---|---|---|
| 01 | IMPLEMENTATION EVALUATION | Can lighter arrows be sourced from another supplier? | "Arrows light enough that they can potentially reach the bulls-eye" |
| 02 | IMPLEMENTATION EVALUATION | Can the archers be trained to better allow for cross-winds? | "Sufficient adjustment to direction of arrows to allow for cross-winds" |
| 04 (process) | PROCESS EVALUATION | What management practices did the archers find supportive? | Cross-cutting (process / context) |
| 04 | IMPACT EVALUATION | Did the Archery Agency lead to more arrows hitting the bulls-eye? | "Sufficient arrows hit the bulls-eye" |
| 04a | IMPACT EVALUATION (duplicate of Q 04) | Did the Archery Agency achieve its outcome? | "Sufficient arrows hit the bulls-eye" |

The flow on the diagram runs left to right from IMPLEMENTATION EVALUATION through PROCESS EVALUATION to IMPACT EVALUATION. Implementation evaluation questions sit to the left of the diagram; impact evaluation questions sit to the right.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
