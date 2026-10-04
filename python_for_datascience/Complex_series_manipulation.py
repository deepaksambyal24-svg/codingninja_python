mport numpy as np
import pandas as pd

# Write your code here
# Set the seed for reproducibility
np.random.seed(42)

# Create a Series
series = pd.Series(np.random.randint(1, 101, 10))

# Access Specific Elements and Create a New Series
series = pd.Series([series.iloc[2],series.iloc[4], series.iloc[6]])

# Compute Statistics
mean_value = series.mean()
median_value = series.median()
std_value = series.std()

print(round(mean_value,2))
print(round(median_value,2))
print(round(std_value,2))

# Replace Values
series = series.apply(lambda x: median_value if x < mean_value else x)

# Print Results
print(round(series,2))