---
source_pdf: docs/pdf/d11tool.pdf
pair: d11
kind: tool
---

# DoView Tool D11 — Proxy Indicator Level-Assessment Tool

> **Pair:** [Question](d11question.md) · Tool (this page)

This tool shows the importance of revealing the level at which proxy indicators are located within the relevant DoView strategy/outcomes diagram. Proxy or surrogate indicators are indicators that are lower down a DoView diagram because you cannot find a suitable indicator at a higher level. You can assess the level of the two proxy indicators as shown below because they are shown against a DoView strategy/outcomes diagram. You can see that the proxy indicator shown in 'B' is higher up the diagram than the one that is shown in 'A'.

## Diagram

### A — Proxy indicator lower down the strategy diagram

Indicator `003 Average distance bow string pulled back` is attached to the low-level "Bow string pulled back far enough" box.

```mermaid
flowchart LR
    quiver["Arrows taken out of quiver efficiently"]
    notched["Arrows correctly notched onto the bow string"]
    pulled["Bow string pulled back far enough<br/>(003 Average distance bow string pulled back) ← proxy"]
    bullseye_id["Correct bulls-eye accurately identified"]
    lined["Bow lined up with bullseye"]
    adjust["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    fired["Sufficient number of arrows fired from bow"]
    past["Arrows get past any barriers put up in the way"]
    afterbar["Arrows still heading in the right direction after passing any barriers"]
    threequarters_dir["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    threequarters_up["Sufficient number of arrows still going three-quarters of the way up the range"]
    hit["Sufficient arrows hit the bulls-eye"]

    quiver --> lined
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

### B — Proxy indicator higher up the strategy diagram

Indicator `005 Number of arrows fired per hour` is attached to the higher-level "Sufficient number of arrows fired from bow" box.

```mermaid
flowchart LR
    quiver["Arrows taken out of quiver efficiently"]
    notched["Arrows correctly notched onto the bow string"]
    pulled["Bow string pulled back far enough"]
    bullseye_id["Correct bulls-eye accurately identified"]
    lined["Bow lined up with bullseye"]
    adjust["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    fired["Sufficient number of arrows fired from bow<br/>(005 Number of arrows fired per hour) ← proxy"]
    past["Arrows get past any barriers put up in the way"]
    afterbar["Arrows still heading in the right direction after passing any barriers"]
    threequarters_dir["Sufficient number of arrows still heading in the right direction three-quarters of the way up the range"]
    threequarters_up["Sufficient number of arrows still going three-quarters of the way up the range"]
    hit["Sufficient arrows hit the bulls-eye"]

    quiver --> lined
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

The proxy in B sits closer to the desired top-level outcome ("Sufficient arrows hit the bulls-eye") than the proxy in A, making it a better proxy indicator.

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
