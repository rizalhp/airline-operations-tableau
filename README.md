# U.S. Airline Operations & Delay Intelligence — 2024

Tableau business-intelligence portfolio project analyzing U.S. domestic flight reliability using **real 2024 flight-level data** sourced from the U.S. Department of Transportation Bureau of Transportation Statistics (BTS) and distributed as a cleaned Kaggle compilation.

## Current Data Scope

The analysis is computed from the **real 10,000-row sample** supplied with the Kaggle dataset. It covers **2024-01-01 through 2024-12-31** and preserves the same 35-column schema as the 7M+ row full dataset. To keep Git history lightweight, the row-level sample is **not versioned**; the repository stores the source data dictionary, reproducible preprocessing code, and aggregated outputs computed from the real 10,000-row sample.

> Sample-level findings below are explicitly labeled as sample results and should not be interpreted as exact population estimates for every U.S. domestic flight in 2024.

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

## Tableau Story

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

## Data Engineering

`scripts/prepare_data.py` validates the 35 source fields and creates Tableau-friendly features including `route`, `day_name`, scheduled-departure fields, distance bands, operational flags, and delay-cause fields.

## Documentation

- [`docs/methodology.md`](docs/methodology.md) — analytical scope, sampling notes, and preprocessing methodology
- [`docs/data_dictionary.md`](docs/data_dictionary.md) — source and engineered field definitions
- [`docs/kpi_definitions.md`](docs/kpi_definitions.md) — business KPI definitions
- [`docs/kpi_validation_checklist.md`](docs/kpi_validation_checklist.md) — pre-publish metric reconciliation, filter integrity, and cross-dashboard QA checklist
- [`docs/dashboard_blueprint.md`](docs/dashboard_blueprint.md) — intended Tableau dashboard structure
- [`docs/tableau_calculated_fields.md`](docs/tableau_calculated_fields.md) — reusable Tableau formulas, formatting rules, route-volume guardrails, and dashboard QA checks
- [`docs/operational_decision_framework.md`](docs/operational_decision_framework.md) — translates dashboard signals into prioritization logic, management questions, and operational actions

## Repository Structure

```text
airline-operations-tableau/
├── README.md
├── data/
│   ├── sample/
│   │   ├── README.md
│   │   └── flight_data_2024_data_dictionary.csv
│   └── processed/
│       ├── kpi_summary.csv
│       ├── airline_summary.csv
│       ├── monthly_summary.csv
│       ├── delay_cause_summary.csv
│       └── summary.json
├── docs/
│   ├── dashboard_blueprint.md
│   ├── data_dictionary.md
│   ├── kpi_definitions.md
│   ├── kpi_validation_checklist.md
│   ├── methodology.md
│   ├── operational_decision_framework.md
│   └── tableau_calculated_fields.md
├── reports/
├── scripts/
└── tableau/
```

## Data Source & License

- **Primary source:** U.S. Department of Transportation — Bureau of Transportation Statistics (BTS), Reporting Carrier On-Time Performance.
- **Portfolio dataset:** Kaggle — *Flight Delay Dataset — 2024* by Hrishit Patil, a cleaned merge of monthly BTS TranStats files.
- **Dataset license:** CC0 / Public Domain as stated on the Kaggle dataset page.

## Reproduce the Tableau Dataset

```bash
python scripts/prepare_data.py <path-to-flight-csv>
```

The script writes a Tableau-ready output to `data/processed/`.

## Status

**Data audit and preprocessing complete. Dashboard 1 and Dashboard 2 are complete; Dashboard 3 (Airport & Route Intelligence) is in progress.** Next milestone: finish Dashboard 3, publish the Tableau story, and add the Tableau Public URL plus dashboard screenshots to this repository.
