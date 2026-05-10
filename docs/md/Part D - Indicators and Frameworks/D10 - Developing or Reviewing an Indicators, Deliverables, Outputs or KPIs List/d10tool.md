---
source_pdf: docs/pdf/d10tool.pdf
pair: d10
kind: tool
---

# DoView Tool D10 — Developing or Reviewing an Indicators, Deliverables, Outputs or KPIs List

> **Pair:** [Question](d10question.md) · Tool (this page)

To develop, or review, a deliverables list, build the relevant DoView strategy/outcomes diagram as in 'A' below using the DoView Drawing Rules (B7). Then select relevant deliverables using the Deliverables, Outputs and KPIs Checklist (D9) — the ones below with an '@' next to them. If reviewing the deliverables list given in 'B' below, simply draw the relevant DoView strategy/outcomes diagram in the same way as in 'A'. From this, you might conclude that indicators 1 and 2 are subsumed by 4 (quality) and 5 (quantity), so you might only use 4 and 5. Also, that indicator 9, because it is not-necessarily controllable, should not be in a deliverables list if you are using controllables-only contracting (Types 1 - 3) in the Types of Contracting for Outcomes Or Outputs (E3).

## Diagram

### A — DoView strategy/outcomes diagram with indicators

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

`@` = Controllable indicators.

### B — Deliverables list being reviewed

- 001 Percentage archers with archery degree @
- 002 Average time to remove an arrow from quiver @
- 004 How many occasions bulls-eyes accurately identified @
- 005 Number of arrows fired per hour @
- 009 Number of arrows hitting the bulls-eye per hour

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
