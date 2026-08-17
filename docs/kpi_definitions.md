# KPI Definitions

## Eligible Completed Flight
`cancelled = 0`, `diverted = 0`, and arrival delay is available.

## On-Time Arrival
Eligible completed flight with `arr_delay < 15`.

## On-Time Arrival Rate
`SUM(on_time_flag) / SUM(eligible_completed_flag)`

## 15+ Minute Delay
Eligible completed flight with `arr_delay >= 15`.

## Delay Rate
`SUM(delay_15_flag) / SUM(eligible_completed_flag)`

## Severe Delay
Eligible completed flight with `arr_delay >= 60`.

## Cancellation Rate
`SUM(cancelled) / COUNT(flights)`

## Diversion Rate
`SUM(diverted) / COUNT(flights)`

## Average Arrival Delay
Average `arr_delay` among eligible completed flights. Negative values mean early arrival.

## Delay Cause Share
Delay-cause minutes / sum of the five reported cause-minute fields.

## Route
`origin + " → " + dest`
