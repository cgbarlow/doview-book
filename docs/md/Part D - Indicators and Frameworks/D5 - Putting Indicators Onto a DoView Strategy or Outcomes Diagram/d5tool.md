---
source_pdf: docs/pdf/d5tool.pdf
pair: d5
kind: tool
---

# DoView Tool D5 — Putting Indicators Onto a DoView Strategy/Outcomes Diagram

> **Pair:** [Question](d5question.md) · Tool (this page)

Indicators can be put onto a DoView strategy/outcomes diagram to show which boxes they measure and their level within the diagram. You can mark controllable indicators with a '@' to differentiate them from higher-level not-necessarily controllable indicators (usually described as outcomes) for clearer accountability, delegation, and contracting discussions.

## Diagram

The DoView uses an archery metaphor. Boxes describe steps and outcomes in the archery process; indicators (numbered 001–009) are attached to specific boxes. `@` marks controllable indicators; unmarked indicators are not-necessarily controllable (outcomes).

```mermaid
flowchart LR
    archers["Well trained archers<br/>(001 Percentage archers with archery degree @)"]
    bows["Good quality bows"]
    sharp["Arrows sharp enough"]
    light["Arrows light enough that they can potentially reach the bulls-eye"]
    quiver["Arrows taken out of quiver efficiently<br/>(002 Average time to remove an arrow from quiver @)"]
    notched["Arrows correctly notched onto the bow string"]
    pulled["Bow string pulled back far enough<br/>(003 Average distance bow string pulled back @)"]
    bullseye_id["Correct bulls-eye accurately identified<br/>(004 Percent occasions bulls-eyes accurately identified @)"]
    lined["Bow lined up with bullseye"]
    adjust["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    fired["Sufficient number of arrows fired from bow<br/>(005 Number of arrows fired per hour @)"]
    past["Arrows get past any barriers put up in the way<br/>(006 Percent arrows get past barriers)"]
    afterbar["Arrows still heading in the right direction after passing any barriers<br/>(007 Percent arrows still heading in the right direction after passing any barriers)"]
    threequarters_dir["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    threequarters_up["Sufficient number of arrows still going three-quarters of the way up the range<br/>(008 Percent arrows still going three-quarters up the range)"]
    hit["Sufficient arrows hit the bulls-eye<br/>(009 Number of arrows hitting the bulls-eye per hour)"]

    archers --> notched
    bows --> notched
    sharp --> notched
    light --> notched
    quiver --> notched
    notched --> lined
    pulled --> lined
    bullseye_id --> lined
    lined --> fired
    adjust --> fired
    fired --> past
    past --> afterbar
    afterbar --> threequarters_dir
    afterbar --> threequarters_up
    threequarters_dir --> hit
    threequarters_up --> hit
```

`@` = Controllable indicators. Indicators without `@` are not-necessarily controllable (typically outcome-level).

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
