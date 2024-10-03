# We now create some benchmarks about the performance of individual stocks #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.stats as stats


daily_growth = pd.read_csv('daily_growth.csv')

# Rename columns to only ticker names
daily_growth.columns = daily_growth.columns.str.replace('_growth', '')

# Calculate overall statistics for entire dataframe
flattened_data = daily_growth.iloc[0:, 1:505].values.flatten()
overall_mean = np.nanmean(flattened_data)
overall_min = np.nanmin(flattened_data)
overall_max = np.nanmax(flattened_data)
overall_std = np.nanstd(flattened_data)

# Some distributions
def distr_plot(ticker):
    # calculate mean and SD
    mean = daily_growth[ticker].mean()
    std = daily_growth[ticker].std()

    # create histogram and KDE
    daily_growth[ticker].plot.hist(bins=50, density=True, alpha=0.6, color='g')
    daily_growth[ticker].plot.kde(label='KDE estimate', color='g')

    # determine plot range and number of ticks
    xmin, xmax = -0.1, 0.1
    plt.xlim(xmin, xmax)
    plt.xticks(np.linspace(xmin, xmax, 10))

    # plot normal distribution
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std)
    plt.plot(x, p, 'k', linewidth=2, label='Normal Distribution')

    # format x-axis labels
    plt.gca().set_xticklabels([f'{tick:.2f}' for tick in np.linspace(xmin, xmax, 10)])

    plt.legend()
    plt.show()

distr_plot('NVDA')

# Plot all distributions and save them in a separate folder

def print_distr_plot(ticker, save_path):
    # calculate mean and SD
    mean = daily_growth[ticker].mean()
    std = daily_growth[ticker].std()

    # create histogram and KDE
    daily_growth[ticker].plot.hist(bins=50, density=True, alpha=0.6, color='g')
    daily_growth[ticker].plot.kde(label='KDE estimate', color='g')

    # determine plot range and number of ticks
    xmin, xmax = -0.1, 0.1
    plt.xlim(xmin, xmax)
    plt.xticks(np.linspace(xmin, xmax, 10))

    # plot normal distribution
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std)
    plt.plot(x, p, 'k', linewidth=2, label='Normal Distribution')

    # format x-axis labels
    plt.gca().set_xticklabels([f'{tick:.2f}' for tick in np.linspace(xmin, xmax, 10)])

    plt.legend()
    plt.savefig(save_path)
    plt.close()

save_path = "Distr_plots"
for ticker in daily_growth.columns[1:]:
    save_path = f"Distr_plots/{ticker}_distribution.png"
    print_distr_plot(ticker, save_path)

# calculate probability of growth or loss (binary)

is_growing = lambda x: np.nan if np.isnan(x) else (1 if x >= 0 else 0)
is_losing = lambda x: np.nan if np.isnan(x) else (0 if x >= 0 else 1)
binary_growth = daily_growth.iloc[0:, 1:].applymap(is_growing)

# growth probabilities for each ticker

growth_probability = binary_growth.apply(lambda col: col.sum() / col.notna().sum())
print(growth_probability.sort_values(ascending=False).head(10))
print(growth_probability.sort_values(ascending=True).head(10))

growth_probability.plot.hist(bins=50, density=True, alpha=0.6, color='g')
plt.show()

# expected loss in case of negative growth
mean_negative_growth = daily_growth.iloc[:, 1:].apply(lambda col: col[col < 0].mean())

# expected growth in case of positive growth
mean_positive_growth = daily_growth.iloc[:, 1:].apply(lambda col: col[col >= 0].mean())

# expected growth overall
avg_growth = daily_growth.iloc[:, 1:].apply(lambda col: col.mean())

# standard deviation of average growth
std_growth = daily_growth.iloc[:, 1:].apply(lambda col: col.std())

# lower and upper bound confidence interval growth

# Z-score for 95% confidence interval
z_value = stats.norm.ppf(0.975)

# Function to calculate the confidence interval
def confidence_interval(col):
    mean = col.mean()
    std = col.std()
    n = col.notna().sum()  # Number of non-NaN observations
    margin_of_error = z_value * (std / np.sqrt(n))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return pd.Series([lower_bound, upper_bound])

# Apply the function to each column (excluding 'Date')
ci_df = daily_growth.iloc[:, 1:].apply(confidence_interval)

# Convert the result into a DataFrame and rename columns
ci_df = ci_df.T  # Transpose to get tickers as rows
ci_df.columns = ['Lower Bound', 'Upper Bound']

print(ci_df)


