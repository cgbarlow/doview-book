---
source_pdf: docs/pdf/c3tool.pdf
pair: c03
kind: tool
---

# DoView Tool C3 — DoView Visual Alignment

> **Pair:** [Question](c03question.md) · Tool (this page)

Below the 'Archery Initiative's' projects have been mapped onto the initiative's DoView strategy/outcomes diagram to check for 'line-of-sight' alignment. There is a lack of alignment for the gray 'A' priority box 'Arrows sharp enough' because no projects are mapped onto it. Either it is not a priority, or it should have one or more projects mapping onto it.

## Diagram

```mermaid
flowchart LR
    archers["Well trained archers"]
    bows["Good quality bows"]
    sharp["Arrows sharp enough (A) — no project mapped"]
    light["Arrows light enough that they can potentially reach the bulls-eye (A)"]
    quiver["Arrows taken out of quiver fast enough (B)"]
    notched["Arrows correctly notched onto the bow string"]
    pulled["Bow string pulled back far enough (A)"]
    target["Correct target accurately identified"]
    lined["Arrows lined up with bullseye"]
    crosswind["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    fired["Sufficient number of arrows fired from bow"]
    barriers["Arrows get past any barriers put up in the way"]
    afterbarriers["Arrows still heading in the right direction after passing any barriers"]
    threequarters_flying["Arrows still flying three-quarters of the way up the range"]
    threequarters_heading["Arrows still heading in the right direction three-quarters of the way up the range"]
    bullseye["Sufficient arrows hit the bulls-eye"]

    P01["[P01] Arrow out of quiver training project"]
    P02["[P02] Arrows sufficiently light quality control project"]
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
    P02 --> light
    P03 --> pulled
```

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
