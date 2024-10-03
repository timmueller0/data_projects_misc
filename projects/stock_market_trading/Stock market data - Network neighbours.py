# This will create the correlation matrix between all the daily returns and create a network from it #
# From the network, only the network neighbours can be selected, and if there is a positive degree-return correlation,
# the daily returns of the neighbours should exceed the average returns. #

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create a correlation matrix from daily_growth
correlations = daily_growth.iloc[:, 1:].corr()

# Set the diagonal to 0 or np.nan
np.fill_diagonal(correlations.values, np.nan)

# reassign the column names (tickers) and set as index
correlations.columns = list(daily_growth.columns)[1:]
correlations.index = list(daily_growth.columns)[1:]

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlations, annot=False, cmap='coolwarm', vmin=-1, vmax=1)
plt.show()

# Calculate overall statistics for entire dataframe
flattened_data = correlations.values.flatten()
overall_mean = np.nanmean(flattened_data)
overall_min = np.nanmin(flattened_data)
overall_max = np.nanmax(flattened_data)
overall_std = np.nanstd(flattened_data)

# create a dataframe that sets all correlations >= 1 SD above mean to 1, else to 0
def create_net (df):
    """Assumed that 1st column is a date, therefore disregarded"""

    # calculate correlations
    correlations = df.iloc[:, 1:].corr()

    # Set the diagonal to np.nan
    np.fill_diagonal(correlations.values, np.nan)

    # reassign the column names (tickers) and set as index
    correlations.columns = list(df.columns)[1:]
    correlations.index = list(df.columns)[1:]

    # Calculate overall statistics for entire dataframe
    flattened_data = correlations.values.flatten()
    overall_mean = np.nanmean(flattened_data)
    overall_min = np.nanmin(flattened_data)
    overall_max = np.nanmax(flattened_data)
    overall_std = np.nanstd(flattened_data)
    cut_off = overall_mean + 1 * overall_std

    # Assign 1 to every value >= cut_off, else 0
    correlations = correlations.map(lambda x: 1 if x >= cut_off else 0)

    print("Mean correlation: ", overall_mean)
    print("Min correlation: ", overall_min)
    print("Max correlation: ", overall_max)
    print("Std correlation: ", overall_std)
    print("Cut off: ", cut_off)

    return correlations

network = create_net(daily_growth)

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(network, annot=False, cmap='coolwarm', vmin=0, vmax=1)
plt.show()

# calculate network degree of each stock
degrees = pd.DataFrame(network.apply(lambda x: np.nansum(x)), columns=['Degree'])

# avg_growth has been calculated previously
avg_growth = pd.DataFrame(avg_growth, columns=['Average Growth'])

# merge degree and avg_growth
degrees_growth = pd.merge(left = degrees, right = avg_growth, left_index=True, right_index=True)

# Degree - growth correlation
print(degrees_growth.corr())








