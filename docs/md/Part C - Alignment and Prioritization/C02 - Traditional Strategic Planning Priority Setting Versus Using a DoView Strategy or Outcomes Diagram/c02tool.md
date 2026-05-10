---
source_pdf: docs/pdf/c2tool.pdf
pair: c02
kind: tool
---

# DoView Tool C2 — Traditional Strategic Planning Priority Setting Versus Using a DoView Strategy/Outcomes Diagram

> **Pair:** [Question](c02question.md) · Tool (this page)

The traditional strategic planning approach of identifying priority strategies using the 'Archery Initiative' is shown in 'A'. If you are asked to critique this list of priorities within a normal text-based strategic plan, you have to have an implicit strategy/outcomes diagram in your head to identify alternative priorities. 'B' shows the DoView Planning approach where you build a DoView strategy/outcomes diagram that includes all wide set of possible steps (boxes) you might use. You then select your current priorities from amongst these boxes. Critiquing this is easy because you can immediately see the boxes that have NOT been selected as priorities and ask questions such as: 'Why is 'training and bow quality' not a priority at the moment?'

## A — Current strategic priorities as set out in a traditional text-based strategic plan

- Priority: Arrows light enough that they can potentially reach the bulls-eye
- Priority: Arrows taken out of quiver efficiently
- Priority: Bow string pulled back far enough

## B — A DoView strategy/outcomes diagram allows you to also query why boxes have not been made a priority

Looking at the DoView immediately prompts questions such as: 'Why are training and bow quality' not a priority at the moment?'

```mermaid
flowchart LR
    archers["Well trained archers"]
    bows["Good quality bows"]
    sharp["Arrows sharp enough"]
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

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
