# Tableau Calculated Fields

The preprocessing script already creates the main flags. If calculated directly in Tableau:

## On-Time Rate
```tableau
SUM([on_time_flag]) / SUM([eligible_completed_flag])
```

## Delay Rate
```tableau
SUM([delay_15_flag]) / SUM([eligible_completed_flag])
```

## Severe Delay Rate
```tableau
SUM([severe_delay_60_flag]) / SUM([eligible_completed_flag])
```

## Cancellation Rate
```tableau
SUM([cancelled]) / COUNT([fl_date])
```

## Diversion Rate
```tableau
SUM([diverted]) / COUNT([fl_date])
```

## Avg Arrival Delay
```tableau
AVG(
    IF [eligible_completed_flag] = 1
    THEN [arr_delay]
    END
)
```

## Delay Cause Share
Use Measure Names / Measure Values for `carrier_delay`, `weather_delay`, `nas_delay`, `security_delay`, and `late_aircraft_delay`.

## Reliability Label
```tableau
IF [On-Time Rate] >= 0.85 THEN "Strong"
ELSEIF [On-Time Rate] >= 0.75 THEN "Watch"
ELSE "High Risk"
END
```
