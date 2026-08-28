# KPI Validation Checklist

This checklist is the final quality gate before publishing or updating the Tableau dashboards. It is designed to make the portfolio analysis reproducible, internally consistent, and easy to audit during a technical or business interview.

## 1. Dataset Scope

- [ ] Confirm the dashboard is using the intended 2024 sample dataset.
- [ ] Confirm total records loaded = **10,000 flights** before dashboard-specific filters.
- [ ] Confirm the date range covers **2024-01-01 through 2024-12-31**.
- [ ] Confirm cancelled and diverted flights are retained in the base dataset so disruption KPIs can be calculated correctly.
- [ ] Confirm null arrival-delay values are excluded only from completed-flight arrival metrics, not from overall flight counts.

## 2. Core KPI Reconciliation

Validate the unfiltered dashboard against the reference outputs.

| KPI | Expected sample result | Validation rule |
|---|---:|---|
| Flights analyzed | 10,000 | `COUNT(flights)` |
| On-time arrival rate | 78.46% | `SUM(on_time_flag) / SUM(eligible_completed_flag)` |
| 15+ minute delay rate | 21.54% | `SUM(delay_15_flag) / SUM(eligible_completed_flag)` |
| Severe delay rate | 7.81% | severe completed flights / eligible completed flights |
| Cancellation rate | 1.22% | `SUM(cancelled) / COUNT(flights)` |
| Diversion rate | 0.42% | `SUM(diverted) / COUNT(flights)` |
| Average arrival delay | 7.5 min | average among eligible completed flights |
| Median arrival delay | -6.0 min | median among eligible completed flights |

- [ ] On-time rate + 15+ minute delay rate = approximately **100%** for eligible completed flights.
- [ ] Cancellation and diversion rates use all flights as the denominator.
- [ ] Average and median arrival delay exclude cancelled/diverted flights and null arrival-delay records.
- [ ] Percentage fields are formatted consistently across dashboards.

## 3. Filter Integrity

For every global filter (airline, month, airport, route, day, time band):

- [ ] KPI cards respond to the filter as intended.
- [ ] Trend charts and benchmark charts use the same filter scope unless explicitly documented otherwise.
- [ ] A filter does not unintentionally remove cancelled/diverted records from disruption KPIs.
- [ ] Clearing all filters returns the reference KPI values above.
- [ ] Multi-select filters do not create duplicate flight counts.

## 4. Dashboard 1 — Executive Operations Overview

- [ ] Monthly flight volume reconciles to 10,000 when all months are summed.
- [ ] Monthly reliability trend uses the same completed-flight denominator as the KPI cards.
- [ ] Delay-cause shares are based only on reported cause minutes.
- [ ] Delay-cause shares sum to approximately 100% when all five cause categories are visible.
- [ ] Tooltips clearly distinguish sample findings from full-population claims.

## 5. Dashboard 2 — Airline Performance Benchmark

- [ ] Airline flight volumes sum to 10,000.
- [ ] Scatter-plot on-time rates match the airline ranking view for the same carrier.
- [ ] Carriers with very low volume are not presented as directly comparable without a volume caveat.
- [ ] Average arrival delay uses eligible completed flights only.
- [ ] Cancellation and severe-delay metrics retain their correct denominators.

## 6. Dashboard 3 — Airport & Route Intelligence

- [ ] Origin-airport flight volumes reconcile with the route-level data.
- [ ] Route is consistently defined as `origin + " → " + dest`.
- [ ] Route rankings include a minimum-volume guardrail before labeling a route high risk.
- [ ] Day-of-week and scheduled-departure time bands use the intended chronological sort order.
- [ ] Distance-band labels are ordered logically rather than alphabetically.
- [ ] Drill-down filters preserve the same KPI definitions used in Dashboards 1 and 2.

## 7. Cross-Dashboard Consistency

- [ ] The same KPI name always means the same formula.
- [ ] Colors and labels represent the same operational state across dashboards.
- [ ] Dashboard titles state when results are based on the 10,000-row sample.
- [ ] Tooltips use consistent units: percentages, minutes, flight counts, and delay-cause minutes.
- [ ] No worksheet uses `AVG(flag)` when the intended denominator is different from all visible records.

## 8. Pre-Publish Sign-Off

Before publishing to Tableau Public:

- [ ] Reset dashboards to a clean default view.
- [ ] Test all interactive filters and highlight actions.
- [ ] Check dashboard layout at the intended desktop resolution.
- [ ] Confirm no broken fields, null aliases, or accidental `Abc` placeholders are visible.
- [ ] Capture final screenshots for the repository.
- [ ] Add/update the Tableau Public URL in `README.md`.
- [ ] Re-run the KPI reconciliation after the final workbook save.

## Why This Matters

A dashboard is not production-ready simply because the visuals look correct. This checklist separates **visual QA** from **metric QA** and gives every headline number a traceable validation path back to the project definitions and processed outputs.
