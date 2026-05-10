---
source_pdf: docs/pdf/c1tool.pdf
pair: c1
kind: tool
---

# DoView Tool C1 — Setting Priorities Onto a Strategy/Outcomes Diagram

> **Pair:** [Question](c1question.md) · Tool (this page)

The boxes in the illustrative strategy/outcomes diagram for an 'Archery Initiative' have been marked to show 'A' and 'B' priorities. Priority setting is based on: 1) identifying steps that ideally need to be improved within the current planning period; and, 2) available resources taking into account all of the potential priorities in 1 above.

## Diagram

```mermaid
flowchart LR
    archers["Well trained archers"]
    bows["Good quality bows"]
    sharp["Arrows sharp enough (A)"]
    light["Arrows light enough that they can potentially reach the bulls-eye (A)"]
    quiver["Arrows taken out of quiver efficiently (B)"]
    notched["Arrows correctly notched onto the bow string"]
    pulled["Bow string pulled back far enough (A)"]
    target["Correct target accurately identified"]
    lined["Bow lined up with bullseye"]
    crosswind["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    fired["Sufficient number of arrows fired from bow"]
    barriers["Arrows get past any barriers put up in the way"]
    afterbarriers["Arrows still heading in the right direction after passing any barriers"]
    threequarters_going["Sufficient number of arrows still going three-quarters of the way up the range"]
    threequarters_heading["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    bullseye["Sufficient arrows hit the bulls-eye"]

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
    afterbarriers --> threequarters_going
    afterbarriers --> threequarters_heading
    threequarters_going --> bullseye
    threequarters_heading --> bullseye
```

Priority chips on the diagram: **A** — Arrows sharp enough; Arrows light enough that they can potentially reach the bulls-eye; Bow string pulled back far enough. **B** — Arrows taken out of quiver efficiently.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
