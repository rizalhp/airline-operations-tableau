# Data Dictionary

## Source fields

| Column | Type | Kaggle null % | Example |
|---|---|---:|---|
| `year` | Int64 | 0.00% | 2024 |
| `month` | Int64 | 0.00% | 1 |
| `day_of_month` | Int64 | 0.00% | 1 |
| `day_of_week` | Int64 | 0.00% | 1 |
| `fl_date` | datetime64[ns] | 0.00% | 2024-01-01 00:00:00 |
| `op_unique_carrier` | object | 0.00% | 9E |
| `op_carrier_fl_num` | float64 | 0.00% | 4814.0 |
| `origin` | object | 0.00% | JFK |
| `origin_city_name` | object | 0.00% | New York, NY |
| `origin_state_nm` | object | 0.00% | New York |
| `dest` | object | 0.00% | DTW |
| `dest_city_name` | object | 0.00% | Detroit, MI |
| `dest_state_nm` | object | 0.00% | Michigan |
| `crs_dep_time` | Int64 | 0.00% | 1252 |
| `dep_time` | float64 | 1.31% | 1247.0 |
| `dep_delay` | float64 | 1.31% | -5.0 |
| `taxi_out` | float64 | 1.35% | 31.0 |
| `wheels_off` | float64 | 1.35% | 1318.0 |
| `wheels_on` | float64 | 1.38% | 1442.0 |
| `taxi_in` | float64 | 1.38% | 7.0 |
| `crs_arr_time` | Int64 | 0.00% | 1508 |
| `arr_time` | float64 | 1.38% | 1449.0 |
| `arr_delay` | float64 | 1.61% | -19.0 |
| `cancelled` | int64 | 0.00% | 0 |
| `cancellation_code` | object | 98.64% | B |
| `diverted` | int64 | 0.00% | 0 |
| `crs_elapsed_time` | float64 | 0.00% | 136.0 |
| `actual_elapsed_time` | float64 | 1.61% | 122.0 |
| `air_time` | float64 | 1.61% | 84.0 |
| `distance` | float64 | 0.00% | 509.0 |
| `carrier_delay` | int64 | 0.00% | 0 |
| `weather_delay` | int64 | 0.00% | 0 |
| `nas_delay` | int64 | 0.00% | 0 |
| `security_delay` | int64 | 0.00% | 0 |
| `late_aircraft_delay` | int64 | 0.00% | 0 |

## Engineered fields

| Field | Definition |
|---|---|
| `day_name` | Day-of-week label |
| `route` | Origin → Destination |
| `scheduled_dep_time` | Human-readable scheduled local departure |
| `scheduled_dep_hour` | Scheduled departure hour |
| `departure_time_band` | Five operational time bands |
| `distance_band` | Route distance category |
| `eligible_completed_flag` | Completed, non-diverted flight with arrival-delay value |
| `on_time_flag` | Eligible flight arriving <15 min late |
| `delay_15_flag` | Eligible flight arriving ≥15 min late |
| `severe_delay_60_flag` | Eligible flight arriving ≥60 min late |
| `total_delay_cause_minutes` | Sum of five reported delay-cause minute fields |
| `primary_delay_cause` | Cause field with the largest reported minutes for that row |
