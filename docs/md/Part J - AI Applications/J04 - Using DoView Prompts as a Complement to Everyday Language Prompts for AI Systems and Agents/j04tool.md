---
source_pdf: docs/pdf/j4tool.pdf
pair: j04
kind: tool
---

# DoView Tool J4 — Using DoView Prompts as a Complement to Everyday Language Prompts for AI Systems and Agents

> **Pair:** [Question](j04question.md) · Tool (this page)

DoView strategy/outcomes diagrams are used in organizational and initiative planning to check what an organization is planning to do and oversee and manage how it takes action in the world. Exactly the same approach should be explored to check how AI agents are interpreting users' everyday language prompts and overseeing and managing them as they act in the world. 'A' below shows a mockup of an AI-generated DoView feeding back to a user what an AI agent thinks a user is asking with their prompt about planning a cycling trip overseas. 'B' shows a DoView progress report from the AI Agent of what it has done and questions it wants the user to answer for it to proceed.

## Diagram

### A — DoView showing what the AI agent plans to do

```mermaid
flowchart LR
    s1["Transport options identified and matched to trip purpose"]
    s2["Accommodation options identified and matched to trip purpose"]
    s3["Route options identified and matched to trip purpose"]
    d1["Daily itinerary drafted"]
    d2["Emergency contacts identified"]
    d3["Tailored packing list prepared"]
    a1["Draft itinerary agreed to"]
    a2["Travel dates agreed to and finalized"]
    b1["Air travel booked"]
    b2["Other transport booked"]
    b3["Accommodation booked (affordable, child friendly)"]
    b4["Travel insurance arranged"]
    b5["Visas applied for"]
    o1["Trip takes in a variety of scenery"]
    o2["Safest roads cycled"]
    o3["Affordable child-friendly accommodation"]
    o4["Most affordable transport secured"]
    o5["Appropriate visas granted"]
    f1["Safe return completed, any difficulties well managed"]
    f2["Good and memorable holiday"]
    f3["Stayed within budget"]

    s1 --> d1
    s2 --> d1
    s3 --> d1
    d1 --> a1
    d2 --> a1
    d3 --> a1
    a1 --> b1
    a2 --> b1
    b1 --> o1
    b2 --> o4
    b3 --> o3
    b4 --> f1
    b5 --> o5
    o1 --> f2
    o2 --> f1
    o3 --> f2
    o4 --> f3
    o5 --> f1
```

### B — Portion of DoView showing what the AI agent has done and questions for user

| Box | Status | Note from AI agent |
|---|---|---|
| Transport options identified and matched to trip purpose | Done | — |
| Accommodation options identified and matched to trip purpose | Done | — |
| Route options identified and matched to trip purpose | Done | — |
| Daily itinerary drafted | Done | — |
| Emergency contacts identified | Done | — |
| Tailored packing list prepared | Done | — |
| Draft itinerary agreed to | Done | — |
| Travel dates agreed to and finalized | Question | "Proving difficult to get flights on first day, could you leave a day later?" |
| Air travel booked | Pending | "Will book once you confirm dates." |
| Other transport booked | Done | — |
| Accommodation booked (affordable, child friendly) | Question | "Accommodation on third day more expensive but cheaper accommodation not so suitable for children. OK to book?" |
| Travel insurance arranged | Done | — |
| Visas applied for | Done | — |

---

*Source: Outcomes Theory & DoView Planning. DoViewPlanning.Org Copyright Dr Paul Duignan 2025. DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025).*
