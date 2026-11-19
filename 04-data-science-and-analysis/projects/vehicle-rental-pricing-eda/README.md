# Vehicle Rental Pricing — Exploratory Data Analysis

A small, reproducible Python EDA project using the repository's sample vehicle-rental dataset. It explores listed daily rental rates by vehicle type and describes the sample fleet mix by fuel type.

> **Dataset limitation:** the included CSV contains only 12 sample records. Outputs demonstrate an analysis workflow; they are not statistically reliable market research or business recommendations.

## Questions explored

1. What are the average and median listed daily rental rates?
2. How do average rates differ across vehicle categories?
3. How is the sample fleet distributed across fuel types?
4. How many distinct vehicle models and branches appear in the sample?

## Tools

Python, Pandas, Matplotlib and pytest.

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

The script prints descriptive summaries and saves two charts in the project's `outputs/` directory.

## Run tests

```bash
python -m pytest 04-data-science-and-analysis/projects/vehicle-rental-pricing-eda/tests -v
```

## Method

- Validate expected columns before analysis.
- Convert rate and branch fields to numeric values.
- Exclude rows missing required analysis fields and reject negative rates.
- Calculate descriptive metrics and grouped averages with Pandas.
- Save Matplotlib charts for average rate by vehicle type and fleet count by fuel type.

## Interpretation and next steps

Because this is a tiny sample, the analysis is intentionally descriptive. For business use, obtain a larger representative dataset, inspect outliers and data collection methods, document currency and rate definitions, and compare results across time and locations. Future extensions could include confidence intervals, statistical tests, demand/occupancy data, and a carefully validated pricing model.
