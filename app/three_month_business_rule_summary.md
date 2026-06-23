# Three-Month Business Rule Validation

**Issuer / month:** 15105 / 2026 / 01
**Generated:** 2026-06-23T03:46:39+00:00

Read-only investigation — no records removed, no logic changed.

## Dashboard gap by status

### CONFIRM

- Expected (Chandra): 1240
- Current dashboard: 1292
- Remaining difference: +52
- Explained by best rule: 7
- Remaining unexplained: 43

### CANCEL

- Expected (Chandra): 47
- Current dashboard: 52
- Remaining difference: +5
- Explained by best rule: 4
- Remaining unexplained: 1

### TERM

- Expected (Chandra): 217
- Current dashboard: 219
- Remaining difference: +2
- Explained by best rule: 1
- Remaining unexplained: 1

## Rule comparison (which interpretation fits Chandra best?)

No single rule explains ≥80% of the gap. Best candidate: 'Special_Enrollment_Cancel' at 20.3% — hypothesis NOT sufficient alone.

| Rule | Explained | % Gap | Confidence |
|------|-----------|-------|------------|
| Special_Enrollment_Cancel | 12/59 | 20.3% | Low |
| Forward_Three_Month | 7/59 | 11.9% | Low |
| Enrollment_Anchored_Window | 7/59 | 11.9% | Low |
| Current_Month_Centered | 4/59 | 6.8% | Low |

**Best candidate:** Special_Enrollment_Cancel

- Explains 7/52 CONFIRM, 4/5 CANCEL, 1/2 TERM gap enrollments

## Unexplained record categories (after best rule)

- Maintenance-only: 45

## Interpretations tested

1. **Forward-only** — current month + next 2 months
2. **Enrollment-anchored** — enrollment start month + 2 following months (bidirectional within window)
3. **Current-month centered** — previous + current + next month
4. **Special enrollment cancel** — cancel/term within 3 months of enrollment/effective date

> This analysis does NOT implement any rule. Production pipeline unchanged.
