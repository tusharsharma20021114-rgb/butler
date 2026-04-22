# Decision Frameworks — Butler Reference

## When to Use Which Framework

| Decision Type | Framework | Best For |
|--------------|-----------|----------|
| Comparing 2+ options with multiple criteria | **Weighted Decision Matrix** | Hiring, vendor selection, technology choices |
| Understanding strengths and weaknesses | **SWOT Analysis** | Strategy, project evaluation, competitive analysis |
| Quick binary decision | **Pros/Cons List** | Go/no-go decisions, simple trade-offs |
| Evaluating risk | **Risk Assessment Matrix** | Project planning, investment decisions |
| Reversible vs. irreversible decisions | **Two-Way Door Test** | Fast decisions about reversible choices |

## Weighted Decision Matrix

### Process
1. List all options (minimum 2).
2. Define evaluation criteria (minimum 2).
3. Assign weights to criteria (must total 100%).
4. Score each option on each criterion (1-10 scale).
5. Calculate weighted scores.
6. The highest score is the recommended option.

### Scoring Guide
| Score | Meaning |
|-------|---------|
| 9-10 | Excellent — exceeds all expectations |
| 7-8 | Good — meets expectations well |
| 5-6 | Adequate — meets minimum requirements |
| 3-4 | Below average — has notable deficiencies |
| 1-2 | Poor — fails to meet requirements |

### Use `scripts/decision-matrix.py` for automated calculation.

## SWOT Analysis

```
┌──────────────────────┬──────────────────────┐
│    STRENGTHS (S)     │    WEAKNESSES (W)    │
│    Internal +        │    Internal -         │
│                      │                      │
│  What do we do well? │  Where do we lack?   │
│  What advantages?    │  What to improve?    │
│  What resources?     │  What limitations?   │
├──────────────────────┼──────────────────────┤
│  OPPORTUNITIES (O)   │     THREATS (T)      │
│    External +        │    External -         │
│                      │                      │
│  What trends favor?  │  What obstacles?     │
│  What gaps to fill?  │  What competitors?   │
│  What changes help?  │  What risks exist?   │
└──────────────────────┴──────────────────────┘
```

### How to Use
1. Brainstorm items for each quadrant (aim for 3-5 per quadrant).
2. Cross-reference: How can Strengths exploit Opportunities? How can you mitigate Threats using Strengths?
3. Prioritize: Which items have the biggest impact?

## Pros/Cons List — Enhanced

Don't just list pros and cons. **Weight them**:

```
Option: [Decision]

PROS                          Weight (1-5)
+ Lower cost                      4
+ Faster to implement              3
+ Team already has expertise        5

CONS                          Weight (1-5)
- Less scalable long-term          4
- Missing feature X                2
- Vendor lock-in risk              3

Pro Score:  12
Con Score:   9
Net Score:  +3 → Lean toward YES
```

## Risk Assessment Matrix

```
              IMPACT
         Low    Med    High
  High  [ M ]  [ H ]  [ !! ]
PROB Med [ L ]  [ M ]  [ H ]
  Low   [ L ]  [ L ]  [ M ]
```

| Rating | Action |
|--------|--------|
| !! Critical | Must mitigate before proceeding |
| H High | Develop mitigation plan |
| M Medium | Monitor and plan contingency |
| L Low | Accept and proceed |

### Process
1. Identify all risks.
2. Rate each risk's **probability** (low/medium/high).
3. Rate each risk's **impact** (low/medium/high).
4. Plot on the matrix.
5. Focus mitigation efforts on high-probability, high-impact risks.

## Two-Way Door Test (Amazon's Framework)

**One-way door**: Irreversible or very costly to reverse. Requires careful analysis.
**Two-way door**: Easily reversible. Decide fast, learn from results.

### Decision Rule
- If it's a **two-way door**: Make the decision quickly. You can always walk back through.
- If it's a **one-way door**: Slow down, gather data, consult stakeholders, use a weighted decision matrix.

### Examples
| Decision | Door Type | Approach |
|----------|-----------|----------|
| Try a new tool for a week | Two-way | Just try it |
| Sign a 3-year contract | One-way | Full analysis |
| Rename a variable | Two-way | Just do it |
| Choose a database architecture | One-way | Decision matrix + team review |
| A/B test a new landing page | Two-way | Ship it, measure |
| Hire a senior engineer | One-way | Structured evaluation |
