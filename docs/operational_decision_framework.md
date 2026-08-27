# Operational Decision Framework

This document translates the Tableau analysis into a practical decision framework for airline operations teams. It connects reliability metrics to actions that can be prioritized, monitored, and reviewed.

## Decision Objective

Use the dashboard to identify where operational disruption is concentrated and determine whether the most appropriate response is schedule adjustment, turnaround improvement, airport-level intervention, or disruption-management planning.

## Diagnostic Flow

1. **Locate the reliability gap**
   - Start with On-Time Arrival Rate, 15+ Minute Delay Rate, Severe Delay Rate, Cancellation Rate, and Diversion Rate.
   - Compare monthly performance to identify whether disruption is persistent or concentrated in specific periods.

2. **Identify the operating segment**
   - Compare airlines, airports, routes, departure windows, and distance bands.
   - Prioritize segments with both meaningful flight volume and elevated disruption rates.

3. **Separate frequency from severity**
   - High delay rate indicates frequent disruption.
   - High average delay or severe-delay rate indicates larger passenger and operational impact.
   - Segments that rank high on both dimensions should receive the highest attention.

4. **Review reported delay causes**
   - Compare carrier, weather, NAS, security, and late-aircraft delay minutes.
   - Use the dominant cause as a diagnostic signal rather than assuming every delay is operationally controllable.

5. **Select an intervention and monitor the KPI**
   - Define the operational action, owner, target segment, and KPI that should improve after the intervention.

## Intervention Matrix

| Analytical Signal | Possible Operational Response | KPI to Monitor |
|---|---|---|
| High delay rate in a departure-time window | Review schedule padding, gate planning, and turnaround assumptions | 15+ Minute Delay Rate |
| High severe-delay rate on a high-volume route | Prioritize route-level disruption planning and recovery capacity | Severe Delay Rate |
| Low airport on-time rate across multiple carriers/routes | Investigate airport congestion, ground-process constraints, or network effects | On-Time Arrival Rate |
| High carrier-delay contribution | Review controllable operational processes and resource allocation | Carrier Delay Minutes |
| High late-aircraft delay contribution | Examine inbound aircraft dependencies and schedule propagation risk | Late Aircraft Delay Minutes |
| Elevated cancellation rate | Review recovery options, reserve capacity, and disruption response | Cancellation Rate |
| High disruption concentrated on specific days/times | Adjust staffing and operational readiness to risk windows | Delay / Cancellation Rate by time window |

## Prioritization Logic

A simple prioritization approach for the dashboard is:

**Priority = Operational Impact × Volume × Actionability**

- **Operational Impact:** severity of delay, cancellation, or diversion.
- **Volume:** number of flights exposed to the problem.
- **Actionability:** degree to which the issue can reasonably be influenced by operational decisions.

This avoids overreacting to a route or airport with a poor percentage based on very few flights.

## Example Management Questions

- Which high-volume routes combine below-average on-time performance with high severe-delay risk?
- Are disruptions concentrated in specific departure windows that may justify staffing or schedule changes?
- Which airports repeatedly appear as reliability bottlenecks across different airlines or routes?
- Is poor performance primarily associated with controllable carrier delay or external causes such as weather and NAS delay?
- Which operational interventions should be tested first based on expected impact and actionability?

## Review Cadence

For an operational reporting workflow, the dashboard can support a recurring monthly review:

1. Compare current-period reliability with the previous period.
2. Identify the largest negative movements.
3. Drill down to airline, airport, route, and time-window drivers.
4. Record the likely cause and proposed action.
5. Recheck the same KPI in the next reporting cycle to assess whether performance improved.

## Portfolio Note

The repository currently uses a real 10,000-row sample of 2024 U.S. domestic flight data. Findings should therefore be treated as sample-level analytical results rather than exact population estimates. The framework is designed to remain applicable when the same workflow is run against the full dataset.
