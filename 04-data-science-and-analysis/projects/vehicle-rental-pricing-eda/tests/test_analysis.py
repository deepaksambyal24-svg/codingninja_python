import pandas as pd
import pytest

from analysis import load_data, summarize_data


def sample_data():
    return pd.DataFrame({
        "car_id": [1, 2, 3],
        "car_model": ["Model A", "Model B", "Model C"],
        "car_type": ["SUV", "Sedan", "SUV"],
        "branch_id": [1, 1, 2],
        "daily_rate": [3000, 2000, 4000],
        "fuel_type": ["Diesel", "Petrol", "Electric"],
    })


def test_summary_calculates_expected_metrics():
    result = summarize_data(sample_data())
    assert result["records"] == 3
    assert result["unique_models"] == 3
    assert result["branches"] == 2
    assert result["average_daily_rate"] == pytest.approx(3000)
    assert result["median_daily_rate"] == pytest.approx(3000)
    assert result["rate_by_type"].loc["SUV"] == pytest.approx(3500)


def test_load_data_rejects_missing_columns(tmp_path):
    source = tmp_path / "invalid.csv"
    pd.DataFrame({"car_model": ["Example"]}).to_csv(source, index=False)
    with pytest.raises(ValueError, match="missing required columns"):
        load_data(source)


def test_load_data_drops_rows_with_missing_required_values(tmp_path):
    source = tmp_path / "sample.csv"
    data = sample_data()
    data.loc[1, "daily_rate"] = None
    data.to_csv(source, index=False)
    result = load_data(source)
    assert len(result) == 2
    assert result["daily_rate"].notna().all()


def test_load_data_rejects_negative_rates(tmp_path):
    source = tmp_path / "negative.csv"
    data = sample_data()
    data.loc[0, "daily_rate"] = -1
    data.to_csv(source, index=False)
    with pytest.raises(ValueError, match="non-negative"):
        load_data(source)
