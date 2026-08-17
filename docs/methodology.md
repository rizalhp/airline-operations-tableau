# Methodology

## Dataset
The current development dataset is the real 10,000-row sample distributed with the 2024 Kaggle compilation. It contains the same selected 35 fields as the full BTS-derived file and spans all months of 2024.

## Why use the sample during development?
A 10,000-row flight-level sample is sufficient to design Tableau calculations, filters, interactions, and dashboard layout quickly. Final published results can later be refreshed against the full 7M+ row dataset without changing the analytical definitions.

## Delay definition
The portfolio uses the 15-minute arrival threshold:
- On-time: arrival delay < 15 minutes.
- Delayed: arrival delay >= 15 minutes.
- Severe delay: arrival delay >= 60 minutes.

Cancelled and diverted flights are excluded from the on-time denominator and are analyzed as separate disruption KPIs.

## Interpretation rule
All current numeric findings are labeled **sample findings**. They are not asserted to be exact population statistics for all U.S. domestic flights in 2024.
