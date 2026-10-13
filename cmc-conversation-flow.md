# CMC Knowledge Assistant — Conversation Flow

```
User Query
    │
    ▼
┌─────────────┐
│ Intent      │
│ Classifier  │
└──────┬──────┘
       │
   ┌───┴───┐
   │       │
   ▼       ▼
Manufacturing  Formulation  Regulatory
   │       │       │
   ▼       ▼       ▼
┌─────────────────────┐
│ RAG Retrieval       │
│ (Scientific Docs)   │
└──────┬──────────────┘
       │
       ▼
┌─────────────┐
│ Response    │─── Low confidence? ──→ Fallback
│ Generator   │                            │
└──────┬──────┘                            ▼
       │                          Human Escalation
       ▼
  User Feedback
       │
       ▼
  Context Update
```

## Intent Map
| Intent | Example | Action |
|--------|---------|--------|
| Manufacturing | "What is the batch process for..." | Retrieve SOP docs |
| Formulation | "Show excipient ratios for..." | Retrieve formulation docs |
| Regulatory | "What are the filing requirements..." | Retrieve regulatory docs |
| Out-of-scope | Unrelated query | Fallback → human |

## Fallback Strategy
1. Clarifying question (1st attempt)
2. Suggest related topics (2nd attempt)
3. Human handoff with context summary
