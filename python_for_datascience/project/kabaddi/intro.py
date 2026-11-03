import pandas as pd
import numpy as np
import pathlib
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.display import display
import missingno as msno


events_df=pd.read_csv('DS_events.csv',low_memory=False)

# zero non null values means all columns are null
# display(df.tail(3))
# display(events_df.sample(5,random_state=42))
missing = pd.DataFrame({

    "n_missing": events_df.isnull().sum(),

    "missing_%": (events_df.isnull().mean() * 100).round(1),

}).sort_values("missing_%", ascending=False)

display(missing)
try:

    import missingno as msno

    msno.matrix(events_df.sample(3000, random_state=0), figsize=(12, 5))

    plt.show()

except ImportError:

    print("missingno not installed: pip install missingno")

# Share of rows where the detailed points are recorded, by event type

(events_df.assign(has_detail=events_df["raid_touch_points"].notna())

          .groupby("event")["has_detail"].mean().round(3).sort_values(ascending=False))

#####################
raids_only = events_df[events_df["event"].isin(["Successful Raid", "Unsuccessful Raid", "Empty Raid"])]

by_match = (raids_only.assign(has_detail=raids_only["raid_touch_points"].notna())

                      .groupby("match_id")["has_detail"].mean())

print("Matches:", len(by_match))

print("  detail on every raid :", int((by_match == 1).sum()))

print("  detail on no raid    :", int((by_match == 0).sum()))

print("  partial              :", int(((by_match > 0) & (by_match < 1)).sum()))

#######################
print(events_df.describe().T)
display(events_df.describe(include="all").T.head(15))
# data type and unique values
display(pd.DataFrame({"dtype": events_df.dtypes.astype(str), "n_unique": events_df.nunique()}))

# data conversion
points_columns = [c for c in events_df.columns if c.endswith("points")]

# Method 1: pd.to_numeric turns unparseable text into NaN instead of raising

for c in points_columns:
    events_df[c] = pd.to_numeric(events_df[c], errors="coerce")

# Method 2: astype. Plain int fails when the column has missing values:

try:

    events_df["raid_points"].astype(int)

except Exception as e:

    print("astype(int) fails ->", type(e).__name__, ":", str(e)[:70])

# ...so use pandas' nullable integer type, which keeps <NA>

events_df["raid_points"] = events_df["raid_points"].astype("Int64")

events_df["defending_points"] = events_df["defending_points"].astype("Int64")

##########################3
bool_like = ["do_or_die", "super_raid", "super_tackle", "review.review_taken"]

for c in bool_like:

    events_df[c] = events_df[c].map({True: 1, False: 0, "True": 1, "False": 0}).astype("Int8")


# id column convert to int 64 vlue not flot
# ID columns arrive as float only because they contain NaN. Make them integer IDs (still allowing <NA>).

id_columns = ["defender_id", "defending_team_id", "player_id", "raider_id", "raiding_team_id",

              "team_id", "status_id", "substituted_by", "review.team_id"]

for c in id_columns:

    events_df[c] = events_df[c].astype("Int64")

# remove duplicate rows
n_dup = events_df.duplicated().sum()

print(f"Duplicate rows: {n_dup}")

print(f"Duplicate rows ignoring Column1: {events_df.drop(columns='Column1').duplicated().sum()}")

before = len(events_df)

events_df = events_df.drop_duplicates()

print(f"Rows dropped: {before - len(events_df)}")


# remove null coumns
all_null = events_df.columns[events_df.isnull().all()].tolist()

print("Columns that are 100% empty:", all_null)

events_df = events_df.drop(columns=all_null)

# nearly emply
# Nearly-empty columns: look first, don't drop blindly

sparse = (events_df.isnull().mean() * 100).round(1)

display(sparse[sparse > 90].sort_values(ascending=False).to_frame("missing_%"))
# Decisions by column type:
# . Points columns: blank means "no points scored / not applicable", so filling with O is reasonable for totals. Caution: for the detail
# columns (touch, bonus, ... ) a O in a match without detail means "unknown", not "zero". That is why we keep the
# has_detail_points flag and use it in later analyses.
# . ID columns: a missing ID is not zero. Keep <NA> (the original text
# · Very sparse columns (≥99% missing): do not impute.
#
# would turn numeric IDs into text).

events_df["has_detail_points"] = events_df["raid_touch_points"].notna()

raw_raid_points = events_df["raid_points"].astype("float").copy()  # kept for the imputation demo

events_df[points_columns] = events_df[points_columns].fillna(0)

print(events_df[points_columns].isnull().sum().sum(), "missing values left in points columns")

# demo for differnet impouttion change the data
# Mean and median filling keep the mean but shrink the spread; filling with O lowers the mean. None is "right": it depends on what a blank
# means.
#
# When not to impute
#
# 1. The fact that a value is missing carries information (e.g. a medical test not ordered).
# 2. Too much is missing (> 50%): imputation mostly invents data.
# 3. Data is not missing at random (NMAR) (e.g. high earners skipping the income question).
# 4. Imputation introduces bias (e.g. forward-filling a time series).
# 5. It distorts the distribution, which happens with mean-filling skewed data.
# # Link to the statistics module: MCAR vs MAR vs NMAR.

demo = pd.DataFrame({

    "original (NaN kept)": raw_raid_points,

    "fill with 0":         raw_raid_points.fillna(0),

    "fill with mean":      raw_raid_points.fillna(raw_raid_points.mean()),

    "fill with median":    raw_raid_points.fillna(raw_raid_points.median()),

})

display(demo.agg(["count", "mean", "std"]).round(3))


#most negative  clipping
neg = events_df.loc[events_df["raid_points"] < 0]

print("Negative raid_points:", len(neg))

display(neg["raid_points"].value_counts().to_frame("rows"))

display(neg["event"].value_counts().to_frame("rows"))



#########################3
events_df["raid_points_raw"] = events_df["raid_points"]  # audit trail

events_df["raid_points_was_negative"] = events_df["raid_points"] < 0

# Method A: lambda / apply (the textbook way)

tmp = events_df["defending_points"].astype(float).apply(lambda x: max(x, 0))

# Method B: vectorised clip (faster, same result)

clipped = events_df[points_columns].clip(lower=0)

assert tmp.equals(clipped["defending_points"].astype(float))

events_df[points_columns] = clipped

print("min of each points column:", events_df[points_columns].min().to_dict())

# consistency in categorical text columns
text_cols = ["event", "event_text", "reason", "clock", "score"]

for c in text_cols:
    events_df[c] = events_df[c].str.strip()  # remove stray whitespace

events_df["event"] = events_df["event"].str.title()  # consistent Proper Case

events_df["event_text_lower"] = events_df["event_text"].str.lower()

print(events_df["event"].unique())


#data transformation
