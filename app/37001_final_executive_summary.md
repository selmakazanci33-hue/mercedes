# Final Executive Summary

**Issuer:** 37001
**Primary business model:** Model H (Chandra-like dashboard aggregation)

## Primary conclusion

At raw event level XML contains many maintenance/duplicate/superseded transactions (11,995 raw rows). At Chandra-like dashboard aggregation level, Azure and XML match on **0 of 28** groups; Azure has **no** extra groups. Remaining mismatch is **28** XML-only aggregated groups.

## Model H dashboard metrics

| Metric | Value |
|--------|-------|
| XML dashboard groups | 28 |
| Azure dashboard groups | 0 |
| Matched groups | 0 |
| XML not in Azure (groups) | 28 |
| Azure not in XML (groups) | 0 |
| Group match rate | 0.0% |
| Status match rate (matched groups) | 0.0% |
| Count accuracy on matched groups | 0.0% |

## Diagnostic comparisons (not primary)

- **Raw event comparison** — high XML volume from transaction-level 834 events.
- **Lifecycle snapshot comparison** — member/policy grain; month-basis effects remain.
- **Model H** — issuer/year/month/insurance_type/status enrollment/enrollee/subscriber counts.

## Outputs

- `outputs/comparison/final_business_result.html`
- `outputs/debug/model_h_xml_vs_azure_detail.csv`
- `outputs/debug/model_h_xml_not_in_azure.csv`

