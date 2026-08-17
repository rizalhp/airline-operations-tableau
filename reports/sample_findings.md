# Sample Findings — U.S. Flight Operations 2024

> **Scope:** These figures are computed from the real 10,000-row Kaggle sample covering 1 Jan–31 Dec 2024. They are useful for dashboard development and portfolio demonstration, but should not be presented as exact population estimates for all 7M+ flights.

## Executive Snapshot

- **On-time arrival rate:** 78.46%
- **15+ minute delay rate:** 21.54%
- **60+ minute severe-delay rate:** 7.81%
- **Cancellation rate:** 1.22%
- **Diversion rate:** 0.42%
- **Average arrival delay:** 7.5 minutes
- **Median arrival delay:** -6.0 minutes

## Operational Signals

- Among airlines with at least 300 sample flights, **YX** recorded the strongest on-time rate at **88.50%**, while **AA** recorded **71.91%**.
- Among origin airports with at least 100 eligible sample flights, **MIA** had the highest 15+ minute delay rate at **34.38%**; **SLC** had the lowest at **15.27%**.
- **July** was the weakest sample month for on-time arrivals at **68.14%**; **October** was strongest at **88.10%**.
- **Late Aircraft** represented the largest share of reported delay-cause minutes at **40.59%**.

## Portfolio Interpretation

The dashboard should emphasize reliability trade-offs rather than only raw delay minutes: airlines and airports with large flight volumes can generate many delay minutes even when their delay rate is moderate. Use both **volume** and **rate** in benchmark views.
