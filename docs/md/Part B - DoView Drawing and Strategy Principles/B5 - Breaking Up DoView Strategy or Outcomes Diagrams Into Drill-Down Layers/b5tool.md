---
source_pdf: docs/pdf/b5tool.pdf
pair: b5
kind: tool
---

# DoView Tool B5 — Breaking Up DoView Strategy/Outcomes Diagrams Into Drill-Down Layers

> **Pair:** [Question](b5question.md) · Tool (this page)

For DoView strategy/outcomes diagrams to be able to be used at the heart of strategy, planning, innovation, implementation and reporting, they need to be able to be used right across all 'communications platforms' used in these settings. Ideally visual strategy diagrams will be optimized for use on the 'lowest common denominator' of communications platforms — when dataprojected or on a tablet. This lowest common denominator approach means that the same diagram can then be read and worked with on any larger-format communications platform. For instance, printed out on larger paper, seen electronically on larger desktop screens or all of the drill-down layers can be placed on a single poster version. 'A' below is the overview page of a Archery Initiative strategy/outcomes diagram. 'B' shows a single drill-down page for 'Skilled and high-performing archers' providing much more detail.

## Diagram

### A — Overview page

```mermaid
flowchart LR
    a1["Well run and administered Archery Initiative"]
    a2["Arrows and bows of sufficiently high quality"]
    a3["Skilled and high-performing archers"]
    final["Sufficient arrows hit the bull's-eye"]
    a1 --> final
    a2 --> final
    a3 --> final
```

### B — Drill-down page for 'Skilled and high-performing archers'

```mermaid
flowchart LR
    subgraph col1["Recruitment pool"]
        b1["Sufficient archers who could potentially be recruited"]
        b2["Sufficient advertising for archers for the Archery Initiative"]
        b3["Sufficient archers apply for positions with the Archery Initiative"]
    end
    subgraph col2["Recruitment process"]
        c1["Clear competencies for archers identified"]
        c2["Good interviewing and recruitment process"]
        c3["Robust background checks on archers"]
    end
    subgraph col3["Development & retention"]
        d1["Sufficient professional development for archers"]
        d2["Sufficient career pathway for archers"]
        d3["Sufficient remuneration for archers"]
    end
    subgraph col4["Management"]
        e1["Quality work environment and work culture"]
        e2["Sufficient management and supervision of archers"]
        e3["Sufficient outcomes tracking and monitoring regarding archers performance"]
    end
    subgraph col5["Technique"]
        f1["Arrows taken out of quiver efficiently"]
        f2["Arrows correctly notched onto the bowstring"]
        f3["Bowstring pulled back far enough"]
    end
    subgraph col6["Aim"]
        g1["Correct target accurately identified"]
        g2["Bow lined up with bull's-eye"]
        g3["Sufficient adjustment to direction of arrows to allow for cross-winds"]
    end
    final["Skilled and high-performing archers"]
    col1 --> col2 --> col3 --> col4 --> col5 --> col6 --> final
```

---

*Source: DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025). DoView Planning.Org. Copyright Dr Paul W Duignan.*
