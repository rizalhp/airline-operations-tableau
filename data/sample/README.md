# Sample Data

The analysis and KPI outputs in this repository were computed from the **real 10,000-row Kaggle sample** uploaded during project development.

To keep Git history lightweight, row-level CSV files are not versioned. This folder contains the dataset-provided data dictionary.

To reproduce:
1. Download `flight_data_2024_sample.csv` or the full `flight_data_2024.csv` from the Kaggle source.
2. Place it anywhere locally.
3. Run `python scripts/prepare_data.py <path-to-csv>`.

For the final Tableau Public version, the full 7M+ row source can be used without changing the KPI definitions or dashboard logic.
