# Vehicle Rental Pricing — Exploratory Data Analysis

A small, reproducible Python EDA project built around the repository's sample vehicle-rental dataset. It explores how listed daily rental rates vary by vehicle type and describes the fleet mix across fuel types.

> **Dataset limitation:** the included CSV contains only 12 sample records. Treat the outputs as a demonstration of an analysis workflow, not as statistically reliable market research or business recommendations.

## Questions explored

1. What is the average and median listed daily rental rate?
2. How do average rates differ across vehicle categories?
3. How is the sample fleet distributed across fuel types?
4. How many distinct vehicle models and branches appear in the sample?

## Tools

- Python
- Pandas
- Matplotlib
- pytest

## Project layout

```text
vehicle-rental-pricing-eda/
├── README.md
├── analysis.py
└── tests/
    └── test_analysis.py
```

The source dataset is maintained once at [../../datasets/cars.csv](../../datasets/cars.csv).

## Run locally

From the repository root:

```bash
python -m pip install pandas matplotlib pytest
python 04-data-science-and-analysis/projects/vehicle-rental-pricing-eda/analysis.py
```

The script prints descriptive summaries and creates two charts in the project's `outputs/` directory.

## Run tests

```bash
python -m pytest 04-data-science-and-analysis/projects/vehicle-rental-pricing-eda/tests -v
```

## Method

- Validate expected columns before analysis.
- Convert rate and branch fields to numeric values.
- Exclude records missing required analysis fields.
- Reject negative daily rates.
- Calculate descriptive metrics and grouped averages with Pandas.
- Save Matplotlib charts for rate by vehicle type and fleet count by fuel type.

## Interpretation and next steps

Because this is a tiny sample, the analysis is intentionally descriptive. Before using a similar workflow for a business decision, obtain a larger representative dataset, inspect outliers and data collection methods, document currency and rate definitions, and compare results across time and locations. Future extensions could include confidence intervals, statistical tests, demand/occupancy data, and a carefully validated pricing model.
