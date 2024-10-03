# Here we finally apply some rules for portfolio selection based on what we found so far #
# We won't be able to beat the S&P 500 overall, at least not when trying a network based approach,
# sampling from the whole index.
# But we can outperform certain market segments that came out of our clustering exercise.
# Three out of five clusters have positive degree-growth correlations,
# the tech (cluster 3) and the consumer products cluster (cluster 4) have really good growth potential,
# whereas the utility / energy cluster (cluster 0) has rather small returns.
# The other clusters we will also examine, but they have negative degree-growth correlations and in part actually negative growth prospects (cluster 1).

import numpy as np
import random

# We focus on cluster 3 first. NOTE THAT cluster numbers are NOT FIXED! CHECK CLUSTERS!!
# Step one: Draw a random sample of 3 stocks and sample the neighbors of these stocks.
def select_random_symbols(symbols, num_items):
    if num_items > len(symbols):
        raise ValueError("Number of items to be selected cannot be greater than the number of available symbols.")
    return random.sample(symbols, num_items)
symbols = list(cluster_3_returns.columns)[1:]
tickers = select_random_symbols(symbols, 3)
print (tickers)

# Find all network neighbors of these stocks
all_neighbors = set()

for ticker in tickers:
    # Get the row corresponding to the stock
    neighbors = network_c3.loc[ticker]

    # Add the tickers of all neighbors (where the value is 1 or non-zero)
    all_neighbors.update(neighbors[neighbors != 0].index)

# Remove the original stocks from the neighbors set
all_neighbors = all_neighbors.difference(tickers)
print(all_neighbors)

# Select corresponding stocks from ci_df
filtered_ci_df = ci_df.loc[ci_df.index.intersection(all_neighbors)]
print(filtered_ci_df)

# Sort by 'Upper Bound' and pick the 5 stocks with the highest upper bound ci
top5 = list(filtered_ci_df.sort_values(by='Upper Bound', ascending=False).head(5).index)
top_returns = daily_growth.loc[0:,['Date'] + top5]
print(top_returns.describe())
print(avg_growth.describe())

optimized_portfolio = kelly_optimization(daily_growth, top5, config)
print(optimized_portfolio)  # We can now do this for every trading day and see how well it works.

# Load historical price data
# Ticker_x is opening price, Ticker_y is closing price (NOT adj_close)
all_prices = pd.read_csv('merged_all.csv')
all_prices.columns = all_prices.columns.str.replace('_x', '_open')
all_prices.columns = all_prices.columns.str.replace('_y', '_close')
all_prices['Date'] = pd.to_datetime(all_prices['Date'])
all_prices.set_index('Date', inplace=True)

# Remember the configuration dictionary for the Kelly optimization
config = {
     'capital': 1000,
     'annual_risk_free_rate': 0.02,
     'kelly_fraction': 1.0
}

# We can define the capital in the config dictionary and pass that on to the function below
# total_capital = config['capital']

# Function to allocate capital
import pandas as pd
import pytz
import pulp

def allocate_capital_lp(allocation_df, prices_df, total_capital, trading_date):
    # Convert start_date to datetime and filter prices_df for the given date
    trading_date = pd.to_datetime(trading_date).tz_localize('UTC')

    if trading_date not in prices_df.index:
        raise ValueError(f"No price data available for the trading date: {trading_date}")

    # Extract opening prices for the allocation day
    opening_prices_on_date = prices_df.loc[trading_date, [f'{ticker}_open' for ticker in allocation_df.index]]

    # Initialize result columns
    allocation_df['Shares_Bought'] = 0
    allocation_df['Actual_Allocation'] = 0
    remaining_capital = total_capital

    total_price_paid = 0  # New variable to track the total cost

    # Sort stocks by highest weight first
    allocation_df = allocation_df.sort_values(by='Weights', ascending=False)

    tickers = allocation_df.index.tolist()

    # Loop through and allocate capital
    for ticker in tickers:
        open_price = opening_prices_on_date[f'{ticker}_open']
        weight = allocation_df.loc[ticker, 'Weights']
        suggested_allocation = total_capital * weight

        # Calculate how many shares we can buy based on available capital and stock's open price
        shares_to_buy = int(suggested_allocation // open_price)

        # If shares can be bought
        if shares_to_buy > 0:
            allocation_cost = shares_to_buy * open_price
            allocation_df.loc[ticker, 'Shares_Bought'] = shares_to_buy
            allocation_df.loc[ticker, 'Actual_Allocation'] = allocation_cost
            remaining_capital -= allocation_cost
            total_price_paid += allocation_cost  # Add to total price paid

            print(f"Bought {shares_to_buy} shares of {ticker} at {open_price:.2f} for {allocation_cost:.2f}")

    # Print the total price paid for the shares at the start of the day
    print(f"\nTotal Price Paid for Shares at Start of Day: {total_price_paid:.2f}")

    return allocation_df, remaining_capital

# Run the allocation
total_capital = config['capital']
trading_date = '2018-05-25'
allocation_df, remaining_capital = allocate_capital_lp(optimized_portfolio, all_prices, total_capital, trading_date)

# Output results
print(allocation_df)
print(f"Leftover Capital: {remaining_capital:.2f}")


# Checking for timezone aware timestamps

def allocate_capital_lp(allocation_df, prices_df, total_capital, trading_date):
    # Convert trading_date to datetime if it's not already
    trading_date = pd.to_datetime(trading_date)

    # Check if the trading_date is timezone-aware, and localize it if it's not
    if trading_date.tzinfo is None or trading_date.tzinfo.utcoffset(trading_date) is None:
        trading_date = trading_date.tz_localize('UTC')
    else:
        trading_date = trading_date.tz_convert('UTC')

    if trading_date not in prices_df.index:
        raise ValueError(f"No price data available for the trading date: {trading_date}")

    # Extract opening prices for the allocation day
    opening_prices_on_date = prices_df.loc[trading_date, [f'{ticker}_open' for ticker in allocation_df.index]]

    # Initialize result columns
    allocation_df['Shares_Bought'] = 0
    allocation_df['Actual_Allocation'] = 0
    remaining_capital = total_capital

    total_price_paid = 0  # New variable to track the total cost

    # Sort stocks by highest weight first
    allocation_df = allocation_df.sort_values(by='Weights', ascending=False)

    tickers = allocation_df.index.tolist()

    # Loop through and allocate capital
    for ticker in tickers:
        open_price = opening_prices_on_date[f'{ticker}_open']
        weight = allocation_df.loc[ticker, 'Weights']
        suggested_allocation = total_capital * weight

        # Calculate how many shares we can buy based on available capital and stock's open price
        shares_to_buy = int(suggested_allocation // open_price)

        # If shares can be bought
        if shares_to_buy > 0:
            allocation_cost = shares_to_buy * open_price
            allocation_df.loc[ticker, 'Shares_Bought'] = shares_to_buy
            allocation_df.loc[ticker, 'Actual_Allocation'] = allocation_cost
            remaining_capital -= allocation_cost
            total_price_paid += allocation_cost  # Add to total price paid

            print(f"Bought {shares_to_buy} shares of {ticker} at {open_price:.2f} for {allocation_cost:.2f}")

    # Print the total price paid for the shares at the start of the day
    print(f"\nTotal Price Paid for Shares at Start of Day: {total_price_paid:.2f}")

    return allocation_df, remaining_capital

# Run the allocation
total_capital = config['capital']
trading_date = '2018-05-25'
allocation_df, remaining_capital = allocate_capital_lp(optimized_portfolio, all_prices, total_capital, trading_date)

# Output results
print(allocation_df)
print(f"Leftover Capital: {remaining_capital:.2f}")

