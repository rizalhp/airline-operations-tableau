# Tableau Calculated Fields Playbook

This guide standardizes the core Tableau calculations used across the airline operations dashboards. The formulas are based on the engineered fields created by `scripts/prepare_data.py` and are designed to keep KPI definitions consistent between worksheets.

## 1. Reliability KPIs

### On-Time Arrival Rate

```tableau
SUM([on_time_flag]) / SUM([eligible_completed_flag])
```

**Format:** Percentage, 1 decimal place  
**Interpretation:** Share of eligible completed flights arriving less than 15 minutes late.

### 15+ Minute Delay Rate

```tableau
SUM([delay_15_flag]) / SUM([eligible_completed_flag])
```

**Format:** Percentage, 1 decimal place  
**Interpretation:** Share of eligible completed flights arriving at least 15 minutes late.

### Severe Delay Rate (60+ min)

```tableau
SUM([severe_delay_60_flag]) / SUM([eligible_completed_flag])
```

**Format:** Percentage, 1 decimal place  
**Interpretation:** Share of eligible completed flights arriving at least 60 minutes late.

### Cancellation Rate

```tableau
AVG([cancelled])
```

**Format:** Percentage, 1 decimal place  
**Interpretation:** Share of scheduled flight records marked as cancelled.

### Diversion Rate

```tableau
AVG([diverted])
```

**Format:** Percentage, 1 decimal place  
**Interpretation:** Share of scheduled flight records marked as diverted.

## 2. Delay Severity Metrics

### Average Arrival Delay

```tableau
AVG(
    IF [eligible_completed_flag] = 1 THEN [arr_delay] END
)
```

**Format:** Number, 1 decimal place with suffix ` min`.

### Delayed Flights

```tableau
SUM([delay_15_flag])
```

### Severe Delayed Flights

```tableau
SUM([severe_delay_60_flag])
```

## 3. Route and Airport Analysis

### Route Flight Volume

```tableau
COUNT([fl_date])
```

Use this as a volume control before interpreting route-level percentages. Small-sample routes can produce unstable delay rates.

### Route Delay Rate

```tableau
SUM([delay_15_flag]) / SUM([eligible_completed_flag])
```

Recommended use: place `route` on Rows and filter to routes above a minimum flight-volume threshold before ranking.

### Origin On-Time Rate

```tableau
SUM([on_time_flag]) / SUM([eligible_completed_flag])
```

Place `origin` on Rows or Detail to compare airport-level reliability.

## 4. Delay Cause Analysis

### Total Reported Delay Minutes

```tableau
SUM([total_delay_cause_minutes])
```

### Delay Cause Share

When using `primary_delay_cause` as the dimension:

```tableau
SUM([total_delay_cause_minutes])
/
TOTAL(SUM([total_delay_cause_minutes]))
```

Set **Compute Using** to `primary_delay_cause` and format as a percentage.

## 5. Dashboard 3 Heatmap Setup

For the day-of-week × departure-time heatmap:

- **Rows:** `day_name`
- **Columns:** `departure_time_band`
- **Color:** 15+ Minute Delay Rate
- **Label:** optional flight volume or delay rate
- **Filter:** airline, origin, destination, month

Keep `day_name` sorted in calendar order rather than alphabetical order.

## 6. Month Display

If Tableau imports `month` as a numeric field, create:

```tableau
CASE [month]
WHEN 1 THEN "January"
WHEN 2 THEN "February"
WHEN 3 THEN "March"
WHEN 4 THEN "April"
WHEN 5 THEN "May"
WHEN 6 THEN "June"
WHEN 7 THEN "July"
WHEN 8 THEN "August"
WHEN 9 THEN "September"
WHEN 10 THEN "October"
WHEN 11 THEN "November"
WHEN 12 THEN "December"
END
```

Sort the resulting month label by the original numeric `month` field to preserve chronological order.

## 7. Portfolio Quality Checks

Before publishing a Tableau dashboard:

1. Verify that rate denominators use `eligible_completed_flag` where appropriate.
2. Keep cancellation and diversion rates based on all scheduled flight rows.
3. Apply minimum-volume thresholds before ranking routes or small airports.
4. Label the dashboard as **sample-based analysis** because the repository analysis uses the real 10,000-row sample rather than the full 7M+ row population.
5. Cross-check headline KPI cards against `data/processed/kpi_summary.csv` before publishing.

These conventions reduce metric drift between worksheets and make the Tableau story easier to audit and reproduce.
