"""Exploratory analysis of a small vehicle-rental pricing dataset.

Run from any working directory:
    python 04-data-science-and-analysis/projects/vehicle-rental-pricing-eda/analysis.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR.parents[1] / "datasets" / "cars.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"

REQUIRED_COLUMNS = {
    "car_id", "car_model", "car_type", "branch_id", "daily_rate", "fuel_type"
}


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the CSV and validate the columns and core numeric fields."""
    data = pd.read_csv(path)
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing_columns)}")

    data = data.copy()
    data["daily_rate"] = pd.to_numeric(data["daily_rate"], errors="coerce")
    data["branch_id"] = pd.to_numeric(data["branch_id"], errors="coerce")
    data = data.dropna(subset=["daily_rate", "car_type", "fuel_type"])
    if data.empty:
        raise ValueError("No usable records remain after validating required fields.")
    if (data["daily_rate"] < 0).any():
        raise ValueError("Daily rates must be non-negative.")
    return data


def summarize_data(data: pd.DataFrame) -> dict:
    """Return concise descriptive and grouped summaries."""
    return {
        "records": int(len(data)),
        "unique_models": int(data["car_model"].nunique()),
        "branches": int(data["branch_id"].nunique()),
        "average_daily_rate": float(data["daily_rate"].mean()),
        "median_daily_rate": float(data["daily_rate"].median()),
        "rate_by_type": data.groupby("car_type")["daily_rate"].mean().sort_values(ascending=False),
        "fleet_by_fuel": data["fuel_type"].value_counts().sort_values(ascending=False),
    }


def save_charts(data: pd.DataFrame, output_dir: Path = OUTPUT_DIR) -> list[Path]:
    """Save two basic charts and return their paths."""
    output_dir.mkdir(parents=True, exist_ok=True)
    chart_paths = []

    rate_by_type = data.groupby("car_type")["daily_rate"].mean().sort_values(ascending=False)
    ax = rate_by_type.plot(kind="bar", figsize=(8, 5))
    ax.set_title("Average Daily Rental Rate by Vehicle Type")
    ax.set_xlabel("Vehicle type")
    ax.set_ylabel("Average daily rate")
    ax.tick_params(axis="x", rotation=30)
    ax.figure.tight_layout()
    rate_path = output_dir / "average_rate_by_vehicle_type.png"
    ax.figure.savefig(rate_path, dpi=150)
    plt.close(ax.figure)
    chart_paths.append(rate_path)

    fuel_counts = data["fuel_type"].value_counts()
    ax = fuel_counts.plot(kind="bar", figsize=(8, 5))
    ax.set_title("Fleet Count by Fuel Type")
    ax.set_xlabel("Fuel type")
    ax.set_ylabel("Number of vehicles")
    ax.tick_params(axis="x", rotation=0)
    ax.figure.tight_layout()
    fuel_path = output_dir / "fleet_by_fuel_type.png"
    ax.figure.savefig(fuel_path, dpi=150)
    plt.close(ax.figure)
    chart_paths.append(fuel_path)

    return chart_paths


def main() -> None:
    data = load_data()
    summary = summarize_data(data)

    print("VEHICLE RENTAL PRICING — EXPLORATORY SUMMARY")
    print(f"Records: {summary['records']}")
    print(f"Unique models: {summary['unique_models']}")
    print(f"Branches represented: {summary['branches']}")
    print(f"Average daily rate: {summary['average_daily_rate']:.2f}")
    print(f"Median daily rate: {summary['median_daily_rate']:.2f}")
    print("\nAverage daily rate by vehicle type:")
    print(summary["rate_by_type"].round(2).to_string())
    print("\nFleet count by fuel type:")
    print(summary["fleet_by_fuel"].to_string())

    for chart in save_charts(data):
        print(f"Saved chart: {chart.relative_to(PROJECT_DIR)}")


if __name__ == "__main__":
    main()
