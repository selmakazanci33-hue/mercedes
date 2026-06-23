# Maintenance Code Business Investigation

**Issuer / month:** 15105 / 2026 / 01
**Generated:** 2026-06-23T04:20:05+00:00

Read-only simulation — production pipeline unchanged.

## Current dashboard gap vs Chandra

- CONFIRM: 1292 vs 1240 (gap +52)
- CANCEL: 52 vs 47
- TERM: 219 vs 217

## 1. Top maintenance codes by frequency

- `021` — 31751 records (78.38%): Confirmed/Effectuated
- `024` — 8758 records (21.62%): Terminated

## 2. Individual code with largest gap reduction

- **Code:** `021`
- **Description:** Confirmed/Effectuated
- **Simulated CONFIRM:** 0
- **Gap reduced:** 1292 (remaining -1240)
- **Records affected:** 1300

## 3. Best combination (top 10 codes, sizes 1–3)

- **Combination:** `021`
- **Simulated CONFIRM:** 0
- **Gap reduced:** 1292 (remaining -1240)
- **Records affected:** 1300

## 4. Do maintenance transactions explain Chandra's dashboard?

Excluding maintenance code(s) in simulation reduces the CONFIRM gap by **1292** of **52** (2484.6%).

**Confidence level:** High

## 5. Recommendation

The current evidence suggests that excluding maintenance code(s) **021** reduces the CONFIRM gap from **52** to **-1240** records (1292 removed in simulation), making this the strongest maintenance-related business-rule candidate discovered so far.

> This analysis does NOT implement any rule. Production pipeline unchanged.
