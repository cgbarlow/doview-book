---
source_pdf: docs/pdf/c5tool.pdf
pair: c5
kind: tool
---

# DoView Tool C5 — Baseline Review Undertaken Against a DoView Strategy/Outcomes Diagram

> **Pair:** [Question](c5question.md) · Tool (this page)

A 'baseline review' of an 'Archery Initiative' can be undertaken against an existing DoView strategy/outcomes diagram. This baseline review is recommending the current 'A' priority 'Arrows light enough that they can potentially reach the bull's-eye' is no longer be a priority to because it is believed arrow weights are not currently a limiting factor. Therefore the relevant project [P02] can be de-funded. A baseline review working from an existing DoView diagram is a more efficient and transparent process than just relying on the baseline review team's mental model of the steps and outcomes that should be pursued.

## Diagram

```mermaid
flowchart LR
    archers["Well trained archers"]
    bows["Good quality bows"]
    sharp["Arrows sharp enough"]
    light["Arrows light enough that they can potentially reach the bulls-eye (A — proposed de-priority)"]
    quiver["Arrows taken out of quiver fast enough (B)"]
    notched["Arrows correctly notched onto the bow string"]
    pulled["Bow string pulled back far enough (A)"]
    target["Correct target accurately identified"]
    lined["Arrows lined up with bullseye"]
    crosswind["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    fired["Sufficient arrows fired from bow"]
    barriers["Sufficient arrows get past any barriers put up in the way"]
    afterbarriers["Sufficient arrows still heading in the right direction after passing any barriers"]
    threequarters_flying["Sufficient arrows still flying three-quarters of the way up the range"]
    threequarters_heading["Sufficient arrows still heading in the right direction three-quarters of the way up the range"]
    bullseye["Sufficient arrows hit the bulls-eye"]

    P01["[P01] Arrow out of quiver training project"]
    P02["[P02] Arrows sufficiently light quality control project — DE-FUND"]
    P03["[P03] Bow arm strengthening exercises project"]

    archers --> notched
    bows --> notched
    sharp --> notched
    light --> notched
    quiver --> target
    notched --> target
    pulled --> lined
    target --> lined
    lined --> crosswind
    crosswind --> fired
    fired --> barriers
    barriers --> afterbarriers
    afterbarriers --> threequarters_flying
    afterbarriers --> threequarters_heading
    threequarters_flying --> bullseye
    threequarters_heading --> bullseye

    P01 --> quiver
    P02 -. "de-fund" .-> light
    P03 --> pulled
```

De-fund project [P02] because the box it is focused on is no longer a priority.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
