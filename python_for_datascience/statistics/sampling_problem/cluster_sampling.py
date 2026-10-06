import pandas as pd
import numpy as np

df = pd.read_csv('cluster_data.csv')

# Get all clusters
clus = df['product'].unique()

# Randomly select 5 clusters
np.random.seed(42)
cluster_sample = np.random.choice(clus, 5, replace=False)

print("Selected clusters:", cluster_sample)

# Take 50 observations from each selected cluster
sample = (
    df[df['product'].isin(cluster_sample)]
    .groupby('product').sample(n=50, random_state=42, replace=True))


# Mean and median from the sample
sample_stats = sample.groupby('product')['price'].agg(
    ['mean', 'median']
)

# Actual mean and median from ALL observations
actual_stats = df[
    df['product'].isin(cluster_sample)
].groupby('product')['price'].agg(
    ['mean', 'median']
)

# Compare sample vs actual
comparison = sample_stats.join(
    actual_stats,
    lsuffix='_sample',
    rsuffix='_actual'
)

print(comparison)