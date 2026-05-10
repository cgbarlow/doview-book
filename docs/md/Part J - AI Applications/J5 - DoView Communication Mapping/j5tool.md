---
source_pdf: docs/pdf/j5tool.pdf
pair: j5
kind: tool
---

# DoView Tool J5 — DoView Communication Mapping

> **Pair:** [Question](j5question.md) · Tool (this page)

Most business and private communication focuses on what action to take next. DoView strategy/outcomes diagrams capture the 'This-Then' logic of desired outcomes and the steps needed to achieve them. DoView Communications Mapping could be implemented by building AI apps that create DoViews of what you want to achieve. Then all of your incoming messages, regardless of channel, could be split into summary snippets relevant to particular boxes within the DoView. You could review the messages and respond directly from each box. Eventually, your DoView diagrams could sync with others, so your replies land on similar boxes within their DoView. While new interfaces would be needed, AI can already build quality DoViews, and there are no technical barriers to AI splitting up and summarizing messages. So you would open your computer and, as below, see a DoView mapping of all relevant communications received overnight.

## Diagram

```mermaid
flowchart LR
    s1["Transport options identified and matched to trip purpose"]
    s2["Accommodation options identified and matched to trip purpose"]
    s3["Route options identified and matched to trip purpose"]
    d1["Daily itinerary drafted"]
    d2["Emergency contacts identified"]
    d3["Tailored packing list prepared"]
    a1["Draft itinerary agreed to"]
    a2["Travel dates finalized"]
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

### Communications mapped onto DoView boxes (sample overnight messages)

| Box | Channel / sender | Message snippet |
|---|---|---|
| Daily itinerary drafted | (user prompt) | "You can either leave to come home at 7 am or in the late afternoon on the last day?" |
| Air travel booked | Sam (FlightDesk) | "Best fare dropped $85 - should I book it?" |
| Accommodation booked (affordable, child friendly) | Anna (Green Hostels) | "Family room with foldout bed for child, $200 - Confirm." |
| Travel insurance arranged | Ravi (Travel Cover) | "Policy activates on the day you leave the country and we have received your payment." |
| Visas applied for | Lisa (Visa Pro) | "You need to retake the photo please resend." |
| Safest roads cycled | Carlos (Cycle Tours) | "Updated map - section 4 shows that there is a dedicated cycle lane." |

---

*Source: Outcomes Theory & DoView Planning. DoViewPlanning.Org Copyright Dr Paul Duignan 2025. DOVIEW PLANNING AND PRACTICAL OUTCOMES THEORY HANDBOOK (2025).*
