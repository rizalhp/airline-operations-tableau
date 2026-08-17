# U.S. Airline Operations & Delay Intelligence — 2024

Tableau business-intelligence portfolio project analyzing U.S. domestic flight reliability using **real 2024 flight-level data** sourced from the U.S. Department of Transportation Bureau of Transportation Statistics (BTS) and distributed as a cleaned Kaggle compilation.

## Current Data Scope

The repository currently uses the **real 10,000-row sample** supplied with the Kaggle dataset. It covers **2024-01-01 through 2024-12-31** and preserves the same 35-column schema as the 7M+ row full dataset.

> Sample-level findings are explicitly labeled as sample results and should not be interpreted as exact population estimates for every U.S. domestic flight in 2024.

## Sample Executive Results

| KPI | Result |
|---|---:|
| Flights analyzed | **10,000** |
| On-time arrival rate | **78.46%** |
| 15+ minute delay rate | **21.54%** |
| Severe delay rate (60+ min) | **7.81%** |
| Cancellation rate | **1.22%** |
| Diversion rate | **0.42%** |
| Avg. arrival delay | **7.5 min** |
| Median arrival delay | **-6.0 min** |

## Business Questions

1. How reliable were flight operations across the year?
2. Which airlines and airports showed the strongest and weakest reliability?
3. Which routes and departure windows carried the highest disruption risk?
4. Which reported delay causes contributed the most delay minutes?
5. How can an operations team prioritize schedule, turnaround, and disruption-management interventions?

## Planned Tableau Story

### Dashboard 1 — Executive Operations Overview
- Flight volume
- On-Time Arrival Rate
- 15+ minute Delay Rate
- Cancellation Rate
- Diversion Rate
- Severe Delay Rate
- Monthly reliability trend
- Delay-cause mix

### Dashboard 2 — Airline Performance Benchmark
- Volume vs On-Time Rate scatter
- Airline ranking
- Average arrival delay
- Cancellation / severe-delay benchmark
- Root-cause comparison

### Dashboard 3 — Airport & Route Intelligence
- Airport performance
- Route volume vs delay risk
- Day-of-week × departure-time heatmap
- Distance-band analysis
- High-risk route drill-down

## Data Source & License

- **Primary source:** U.S. Department of Transportation — Bureau of Transportation Statistics (BTS), Reporting Carrier On-Time Performance.
- **Portfolio dataset:** Kaggle — *Flight Delay Dataset — 2024* by Hrishit Patil, a cleaned merge of monthly BTS TranStats files.
- **Dataset license:** CC0 / Public Domain as stated on the Kaggle dataset page.

## Status

**Data audit and preprocessing complete.** Next milestone: build and publish the three interactive Tableau dashboards, then add the Tableau Public URL and screenshots to this repository.
