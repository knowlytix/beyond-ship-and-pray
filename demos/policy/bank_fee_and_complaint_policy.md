# Retail Banking — Fee Schedule & Complaint-Handling Policy

*Internal policy document. Version 2026.1. Owner: MRM / Compliance.*

This is a **policy document**. It is **extracted offline** into the governance
store (exact-numeric memory + a workflow graph) that the runtime gates and the
verifier enforce. The agent never free-interprets this text at runtime — it acts
against the extracted, verified facts.

## 1. Complaint-handling workflow (required order)

Every complaint must be handled in this order; steps may not be skipped:

```
classify → extract → search_policy → flag_regulatory → draft_response
```

- **classify** — categorize the complaint
- **extract** — pull the relevant account facts
- **search_policy** — find the governing policy/section
- **flag_regulatory** — flag any regulatory exposure
- **draft_response** — draft the customer reply

A response may not be drafted before policy search and regulatory review.
An agent that cannot proceed safely must **escalate** to a human.

## 2. Fee schedule (current, exact)

| Fee | Amount | Basis |
|---|---|---|
| Overdraft | **$35** | per occurrence |
| NSF (returned check) | **$35** | per event |
| Late payment | **$25** | per event |
| Domestic wire | **$30** | per transaction |
| International wire | **$45** | per transaction |
| Stop payment | **$30** | per request |
| Paper statement | **$3** | per month |

These amounts are authoritative. Any customer-facing statement of a fee must
match this schedule exactly.

## 3. Fee reversals & waivers

- A fee reversal or waiver **requires supervisor approval** and must be logged.
- An agent may not promise a reversal in a draft response without approval.

## 4. Regulatory

- **UDAAP**: any single fee at or above **$500** is flagged as a potential
  unfair/abusive fee and routed to compliance before any customer communication.

## 5. Data handling

- Customer PII (SSN, card, account numbers) must not appear in drafted responses
  or be carried in case notes without justification; such cases are escalated.
