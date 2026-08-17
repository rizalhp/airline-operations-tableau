# Tableau Dashboard Blueprint

## 1. Executive Operations Overview
**Question:** How healthy was the flight network?

Top KPI strip:
- Flights
- On-Time Arrival Rate
- Delay Rate
- Severe Delay Rate
- Cancellation Rate
- Avg Arrival Delay

Charts:
- Monthly On-Time Rate + Cancellation Rate
- Delay Cause Share
- Airline Volume vs On-Time Rate
- Executive insight text

## 2. Airline Performance Benchmark
**Question:** Which carriers balance scale and reliability best?

Charts:
- Airline On-Time Rate ranking
- Flights vs On-Time Rate scatter
- Avg Arrival Delay
- Severe Delay Rate
- Root-cause stacked bars

## 3. Airport & Route Intelligence
**Question:** Where and when is operational risk concentrated?

Charts:
- Origin airport map / ranking
- Route Volume vs Delay Rate
- Day-of-week × Departure Time Band heatmap
- Distance-band performance
- High-risk route table

## Interaction Design
- Global filters: Month, Airline, Origin, Destination
- Click airline / airport charts to cross-filter
- Keep operational-risk colors consistent:
  - green = stronger reliability
  - amber = moderate risk
  - red = high disruption risk
