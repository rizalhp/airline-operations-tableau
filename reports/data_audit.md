# Data Audit — 10,000-Row Real 2024 Sample

This report is computed from the uploaded Kaggle sample, not from synthetic data.

- Rows: **10,000**
- Columns: **35** source columns + **12** engineered Tableau fields
- Date coverage: **2024-01-01 → 2024-12-31**
- Cancelled rows: **122 (1.22%)**
- Diverted rows: **42 (0.42%)**

## Important missingness

- `dep_time`: **1.16%** null in the sample
- `dep_delay`: **1.16%** null in the sample
- `arr_time`: **1.27%** null in the sample
- `arr_delay`: **1.64%** null in the sample
- `actual_elapsed_time`: **1.64%** null in the sample
- `air_time`: **1.64%** null in the sample
- `cancellation_code`: **98.78%** null in the sample

The high null percentage in `cancellation_code` is expected because the field is populated only for cancelled flights.

## Engineered fields

- `route`
- `day_name`
- `scheduled_dep_time`
- `scheduled_dep_hour`
- `departure_time_band`
- `distance_band`
- `eligible_completed_flag`
- `on_time_flag`
- `delay_15_flag`
- `severe_delay_60_flag`
- `total_delay_cause_minutes`
- `primary_delay_cause`
