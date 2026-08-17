#!/usr/bin/env python3
"""Prepare the real 2024 flight sample/full CSV for Tableau.

Usage:
    python scripts/prepare_data.py <path-to-flight-csv>
"""
import csv
import json
import sys
from pathlib import Path
from statistics import mean, median
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "sample" / "flight_data_2024_sample.csv"
out_dir = ROOT / "data" / "processed"
out_dir.mkdir(parents=True, exist_ok=True)

def fnum(v):
    if v is None or v == "": return None
    try: return float(v)
    except Exception: return None

def inum(v):
    v = fnum(v)
    return int(v) if v is not None else None

def fmt_hhmm(v):
    n = inum(v)
    if n is None: return ""
    if n == 2400: n = 0
    hh, mm = n // 100, n % 100
    return f"{hh:02d}:{mm:02d}" if hh <= 23 and mm <= 59 else ""

def dep_band(v):
    n = inum(v)
    if n is None: return "Unknown"
    if n == 2400: n = 0
    hh = n // 100
    if hh <= 5: return "00:00–05:59"
    if hh <= 11: return "06:00–11:59"
    if hh <= 16: return "12:00–16:59"
    if hh <= 20: return "17:00–20:59"
    return "21:00–23:59"

def dist_band(v):
    x = fnum(v)
    if x is None: return "Unknown"
    if x <= 500: return "≤500 mi"
    if x <= 1000: return "501–1,000 mi"
    if x <= 1500: return "1,001–1,500 mi"
    if x <= 2500: return "1,501–2,500 mi"
    return ">2,500 mi"

DOW = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
CAUSES = [("carrier_delay","Carrier"),("weather_delay","Weather"),("nas_delay","NAS"),("security_delay","Security"),("late_aircraft_delay","Late Aircraft")]

with src.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

required = {"month","day_of_week","fl_date","op_unique_carrier","origin","dest","crs_dep_time","arr_delay","cancelled","diverted","distance"}
missing = required - set(rows[0])
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

extra = ["day_name","route","scheduled_dep_time","scheduled_dep_hour","departure_time_band","distance_band","eligible_completed_flag","on_time_flag","delay_15_flag","severe_delay_60_flag","total_delay_cause_minutes","primary_delay_cause"]
fields = list(rows[0].keys()) + extra
processed = []

for r in rows:
    rr = dict(r)
    cancelled = inum(r.get("cancelled")) or 0
    diverted = inum(r.get("diverted")) or 0
    arr = fnum(r.get("arr_delay"))
    eligible = int(cancelled == 0 and diverted == 0 and arr is not None)
    rr["day_name"] = DOW.get(inum(r.get("day_of_week")), "Unknown")
    rr["route"] = f'{r.get("origin","")} → {r.get("dest","")}'
    rr["scheduled_dep_time"] = fmt_hhmm(r.get("crs_dep_time"))
    dep = inum(r.get("crs_dep_time"))
    rr["scheduled_dep_hour"] = "" if dep is None else (0 if dep == 2400 else dep // 100)
    rr["departure_time_band"] = dep_band(r.get("crs_dep_time"))
    rr["distance_band"] = dist_band(r.get("distance"))
    rr["eligible_completed_flag"] = eligible
    rr["on_time_flag"] = int(eligible and arr < 15)
    rr["delay_15_flag"] = int(eligible and arr >= 15)
    rr["severe_delay_60_flag"] = int(eligible and arr >= 60)
    vals = [(label, fnum(r.get(field)) or 0) for field, label in CAUSES]
    rr["total_delay_cause_minutes"] = sum(v for _, v in vals)
    label, value = max(vals, key=lambda x: x[1])
    rr["primary_delay_cause"] = label if value > 0 else "None / Not Reported"
    processed.append(rr)

with (out_dir / "flights_2024_tableau_ready.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(processed)

eligible = sum(int(r["eligible_completed_flag"]) for r in processed)
on = sum(int(r["on_time_flag"]) for r in processed)
delayed = sum(int(r["delay_15_flag"]) for r in processed)
severe = sum(int(r["severe_delay_60_flag"]) for r in processed)
cancelled = sum((inum(r["cancelled"]) or 0) for r in rows)
diverted = sum((inum(r["diverted"]) or 0) for r in rows)
arrivals = [fnum(r["arr_delay"]) for r in rows if fnum(r["arr_delay"]) is not None and (inum(r["cancelled"]) or 0) == 0 and (inum(r["diverted"]) or 0) == 0]
dates = [datetime.fromisoformat(r["fl_date"]).date() for r in rows]

summary = {
    "rows": len(rows),
    "date_min": min(dates).isoformat(),
    "date_max": max(dates).isoformat(),
    "on_time_rate": on / eligible,
    "delay_15_rate": delayed / eligible,
    "severe_delay_60_rate": severe / eligible,
    "cancellation_rate": cancelled / len(rows),
    "diversion_rate": diverted / len(rows),
    "avg_arrival_delay_minutes": mean(arrivals),
    "median_arrival_delay_minutes": median(arrivals),
}
(out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
