# Find the most favourable cluster to trade
def fav_clusters(print_choice=False):
    # import necessary modules
    import re
    import string

    # Pick the most favourable cluster to trade
    chosen_cluster = mean_growth_df.sort_values(by=['Mean Growth', 'Growth Probability'], ascending=[False, False]).iloc[0, 0]
    chosen_cluster_num = int(re.search(r'degrees_c(\d)', chosen_cluster).group(1))
    if print_choice:
        print("Chosen cluster:", chosen_cluster_num)
    cluster_variable = f'cluster_{chosen_cluster_num}_returns'
    return chosen_cluster_num, cluster_variable

chosen_cluster_num, cluster_variable = fav_clusters()

# Select random ticker symbols from the chosen cluster
def select_random_symbols(symbols, num_items):
    if num_items > len(symbols):
        raise ValueError("Number of items to be selected cannot be greater than the number of available symbols.")
    return random.sample(symbols, num_items)


symbols = list(eval(cluster_variable).columns)[1:]
print("Chosen cluster symbols:", symbols)
tickers = select_random_symbols(symbols, 3)
print ("Randomly selected tickers:", tickers)

# Tickers being passed on to find their network neighbors

def find_net_neighbors(chosen_cluster_num, tickers):
    # Find all network neighbors of these stocks
    all_neighbors = set()
    chosen_cluster_num = int(chosen_cluster_num)
    network_variable = f'network_c{chosen_cluster_num}'
    network_df = eval(network_variable)

    for ticker in tickers:
        # Get the row corresponding to the stock
        neighbors = network_df.loc[ticker]

        # Add the tickers of all neighbors (where the value is 1 or non-zero)
        all_neighbors.update(neighbors[neighbors != 0].index)

    # Remove the original stocks from the neighbors set
    all_neighbors = all_neighbors.difference(tickers)
    print(all_neighbors)

    return all_neighbors

all_neighbors = find_net_neighbors(chosen_cluster_num, tickers)

# Choose the top 5 stocks among the neighbor list according to their upper confidence bound
start_date = '2018-02-09'
def ci_select(all_neighbors, print_choice=False):
    # Select corresponding stocks from ci_df
    filtered_ci_df = ci_df.loc[ci_df.index.intersection(all_neighbors)]

    if print_choice:
        print(filtered_ci_df)

    # Sort by 'Upper Bound' and pick the 5 stocks with the highest upper bound ci
    top5 = list(filtered_ci_df.sort_values(by='Upper Bound', ascending=False).head(5).index)
    return top5

top5 = ci_select(all_neighbors)
print(top5)

# Check if prices on a given date exist
def check_prices_on_date(prices_df: pd.DataFrame, tickers: list, date: str) -> bool:
    """
    Checks if all tickers have both opening and closing prices on the given date.

    :param prices_df: DataFrame containing the prices with date as index and columns like '{ticker}_open', '{ticker}_close'
    :param tickers: List of ticker symbols to check
    :param date: The date for which prices are to be checked (as a string or datetime)
    :return: True if all tickers have valid prices, False otherwise
    """
    try:
        # Get opening and closing prices for the tickers on the given date
        opening_prices = prices_df.loc[date, [f'{ticker}_open' for ticker in tickers]]
        closing_prices = prices_df.loc[date, [f'{ticker}_close' for ticker in tickers]]

        # Check if there are any missing (NaN) values in the opening or closing prices
        if opening_prices.isnull().any() or closing_prices.isnull().any():
            print("Some tickers are missing opening or closing prices on the given date.")
            return False
        else:
            return True
    except KeyError as e:
        print(f"KeyError: {e}. The date or tickers might be missing in the data.")
        return False

if check_prices_on_date(all_prices, top5, start_date):
    print("All tickers have valid prices.")
else:
    print("Some tickers are missing prices.")


# Update the configuration dictionary for Kelly optimization

def update_config(config, capital=None, risk_free_rate=0.02, kelly_fraction=1.0):
    if capital is not None:
        config['capital'] = capital
    if risk_free_rate is not None:
        config['annual_risk_free_rate'] = risk_free_rate
    if kelly_fraction is not None:
        config['kelly_fraction'] = kelly_fraction

#update_config(config, capital=2000, risk_free_rate=0.03, kelly_fraction=0.5)

update_config(config, capital=1000)

# Run Kelly optimization
optimized_portfolio = kelly_optimization(daily_growth, top5, config)

# Allocate and buy stocks at opening price
total_capital = config['capital']
allocation_df, remaining_capital = allocate_capital_lp(optimized_portfolio, all_prices, total_capital, start_date)

# Output results
print(allocation_df)
print(f"Leftover Capital: {remaining_capital:.2f}")

# Sell stocks at the end of the day
# start_date = '2018-02-09'
initial_balance = remaining_capital  # Use the remaining capital from the allocation

updated_balance, total_proceeds = sell_portfolio(allocation_df, all_prices, start_date, initial_balance)
print("Updated balance:", updated_balance, "total_proceeds:", total_proceeds)