# Final Executive Summary

**Issuer:** 15105
**Primary business model:** Model H (Chandra-like dashboard aggregation)

## Primary conclusion

At raw event level XML contains many maintenance/duplicate/superseded transactions (40,509 raw rows). At Chandra-like dashboard aggregation level, Azure and XML match on **20 of 24** groups; Azure has **no** extra groups. Remaining mismatch is **4** XML-only aggregated groups.

## Model H dashboard metrics

| Metric | Value |
|--------|-------|
| XML dashboard groups | 24 |
| Azure dashboard groups | 20 |
| Matched groups | 20 |
| XML not in Azure (groups) | 4 |
| Azure not in XML (groups) | 0 |
| Group match rate | 83.33% |
| Status match rate (matched groups) | 100.0% |
| Count accuracy on matched groups | 34.07% |

## Diagnostic comparisons (not primary)

- **Raw event comparison** — high XML volume from transaction-level 834 events.
- **Lifecycle snapshot comparison** — member/policy grain; month-basis effects remain.
- **Model H** — issuer/year/month/insurance_type/status enrollment/enrollee/subscriber counts.

## Outputs

- `outputs/comparison/final_business_result.html`
- `outputs/debug/model_h_xml_vs_azure_detail.csv`
- `outputs/debug/model_h_xml_not_in_azure.csv`

