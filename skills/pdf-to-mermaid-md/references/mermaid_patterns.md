# DoView diagram patterns → Mermaid

Worked examples of the diagram archetypes that show up in DoView (and similar planning) PDFs. Match the source PDF's diagram to the closest pattern below and adapt.

## 1. Cyclic step flow (A → B → C → D → E → A)

Source: a numbered/lettered ring of steps where each step feeds the next and the last loops back.

```mermaid
flowchart LR
    A["A — Show outcomes & steps in a DoView diagram"]
    B["B — Focus activities on priorities"]
    C["C — Measure and set accountabilities"]
    D["D — Evaluate success and impact"]
    E["E — Dashboard results & improve performance"]
    A --> B --> C --> D --> E --> A
```

If the cycle is more visually circular than linear, `flowchart TB` with the loop arrow drawn explicitly works:

```mermaid
flowchart TB
    A --> B --> C
    C --> D --> E
    E -- loops back --> A
```

## 2. Linear pipeline / progression

Source: a top-to-bottom or left-to-right arrow with stacked boxes representing stages over time.

```mermaid
flowchart TD
    n1["Free-form text-based planning documents"]
    n2["Table-based planning documents"]
    n3["Increasing use of ad hoc static diagrams"]
    n4["Standardized DoView diagram-based, used in some parts of planning"]
    n5["DoView diagram-based tools across all levels"]
    n1 --> n2 --> n3 --> n4 --> n5
```

If the source labels the endpoints (e.g. NOW / FUTURE), put those as prose under the diagram rather than forcing them into Mermaid:

> **NOW** is roughly the middle of the chain (boxes 3–4). **FUTURE** is the bottom box.

This keeps the diagram clean and the temporal labels readable.

## 3. Comparison matrix (rows × steps)

Source: a table with row labels (functions, scenarios) and chips/letters in columns indicating which apply.

A markdown table is almost always clearer than a Mermaid diagram here:

| Function | Steps |
|---|---|
| Strategic planning & priority setting | A, B |
| Program evaluation | A, D, E |
| Evidence-based practice | A |

Use Mermaid only if the matrix has *visual* structure (arrows linking cells, grouped subgraphs) that a table cannot carry.

## 4. Drill-down / outcomes tree

Source: a hierarchy of outcomes, with a top-level outcome decomposing into intermediate and then activity-level steps.

```mermaid
flowchart TD
    top["Top-level outcome: Healthy community"]
    mid1["Intermediate: Reduced smoking rates"]
    mid2["Intermediate: Improved nutrition"]
    a1["Activity: Smoking cessation programme"]
    a2["Activity: Tobacco tax advocacy"]
    a3["Activity: School nutrition curriculum"]
    top --> mid1
    top --> mid2
    mid1 --> a1
    mid1 --> a2
    mid2 --> a3
```

For deep trees, keep node labels short and put the longer descriptions in prose afterwards.

## 5. Two-column comparison (e.g. NOW vs FUTURE)

Source: side-by-side columns, often with an arrow connecting them.

```mermaid
flowchart LR
    subgraph NOW
        n1["Free-form text-based"]
        n2["Table-based"]
        n3["Ad hoc diagrams"]
    end
    subgraph FUTURE
        f1["Standardized DoView diagrams"]
        f2["Used across all planning levels"]
    end
    NOW --> FUTURE
```

## 6. Process with feedback loop

Source: a forward chain of steps with an arrow looping back from a later step to an earlier one.

```mermaid
flowchart LR
    plan["Plan"] --> act["Act"] --> measure["Measure"] --> review["Review"]
    review -- "feeds back into" --> plan
```

## 7. Single concept with annotations

Source: a single central box surrounded by labels or notes.

Often these are clearer as prose plus a small diagram:

```mermaid
flowchart TD
    core["DoView strategy/outcomes diagram"]
    a["Used for strategic planning"]
    b["Used for performance measurement"]
    c["Used for evaluation"]
    d["Used for reporting"]
    core --- a
    core --- b
    core --- c
    core --- d
```

## When NOT to use Mermaid

- The visual is decorative (a logo, an icon, a stock photograph).
- The visual relies on spatial layout that Mermaid can't reproduce (e.g. a hand-drawn sketch where position carries meaning beyond connections).
- The "diagram" is really a list with bullet points styled as boxes — just use a markdown list.

In these cases, describe the visual in one sentence under `## Diagram` and add `_This page contains a visual that does not translate cleanly to Mermaid; described above._`

## Tips

- Keep node labels short. If the PDF box has 3 lines of text, put the first line in the node label and the rest in prose under the diagram.
- Quote node labels with `"..."` whenever they contain spaces, punctuation, or parentheses.
- Use `flowchart` (not the older `graph`) — it has better layout and label support.
- Don't try to match the PDF's exact visual style. A clean Mermaid diagram that captures the *connections* is more valuable than a baroque one that tries to mimic colours and shapes.
