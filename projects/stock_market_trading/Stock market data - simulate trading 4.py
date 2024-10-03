# DOMAIN ERROR IN KELLY OPTIMIZATION NEEDS FIXING, EQUAL ALLOCATION TO STOCKS!! # '

# Find the most favourable cluster to trade
chosen_cluster_num, cluster_variable = fav_clusters()

# Define start date
start_date = '2024-01-02'

# Define the number of trading days to simulate
n_days = 90

# Set initial capital in the config
initial_capital = 100000
update_config(config, capital=initial_capital)

# Extract trading days with error handling (checks if chosen time period is available in all_prices)
trading_days = get_trading_days(all_prices, start_date, n_days)

# Set current capital to the initial capital
current_capital = initial_capital

# Initialize a list to store performance data
performance_data = []

# Initialize a list to store portfolios
portfolios = []

# Simulate the trading strategy over the extracted trading days
for trading_date in trading_days:
    print(f"\nSimulating for trading date: {trading_date}")

    # Record the starting balance for the day
    starting_balance = current_capital

    # Continue retrying until top5 stocks have valid prices
    valid_prices = False
    while not valid_prices:
        # Step 1: Select random ticker symbols from the chosen cluster
        symbols = list(eval(cluster_variable).columns)[1:]
        print("Chosen cluster symbols:", symbols)
        tickers = select_random_symbols(symbols, 3)
        print("Randomly selected tickers:", tickers)

        # Step 2: Find network neighbors for the selected tickers
        all_neighbors = find_net_neighbors(chosen_cluster_num, tickers)

        # Step 3: Choose the top 5 stocks based on upper confidence bound (UCB)
        top5 = ci_select(all_neighbors, print_choice=True)

        # Step 4: Check if top5 stocks have opening and closing prices for the given date
        if check_prices_on_date(all_prices, top5, trading_date):
            print("All tickers have valid prices.")
            valid_prices = True  # Set flag to exit loop when valid prices are found
        else:
            print("Some tickers are missing prices. Re-trying with new selections...")

    # Update config with current capital before Kelly optimization
    update_config(config, capital=current_capital)

    # Run Kelly optimization
    optimized_portfolio = kelly_optimization(daily_growth, top5, config)

    # Allocate and buy stocks at opening price
    allocation_df, remaining_capital = allocate_capital_lp(optimized_portfolio, all_prices, current_capital, trading_date)

    # Output results from allocation
    print(allocation_df)
    print(f"Leftover Capital: {remaining_capital:.2f}")

    # Sell stocks at the end of the same day
    initial_balance = remaining_capital
    updated_balance, total_proceeds = sell_portfolio(allocation_df, all_prices, trading_date, initial_balance)
    print("Updated balance:", updated_balance, "total_proceeds:", total_proceeds)

    # Update the current capital with the total proceeds for the next trading day
    current_capital = updated_balance
    print(f"Updated balance after selling: {current_capital:.2f}")

    # Record the portfolio of the day
    portfolios.append({
        'Trading Date': trading_date,
        'Portfolio': optimized_portfolio
    })

    # Record the performance for the day
    performance_data.append({
        'Trading Date': trading_date,
        'Starting Balance': starting_balance,  # Balance at the start of the trading day
        'Updated Balance': updated_balance,  # Balance after selling
        'Total Proceeds': total_proceeds
    })

# End of simulation: Output the final capital after all trading days
print(f"\nSimulation completed. Final capital after {n_days} trading days: {current_capital:.2f}")
print("Total profits (in percent):", (current_capital - initial_capital) / initial_capital * 100 )

import pandas as pd
import matplotlib.pyplot as plt

# Turn performance_data into a DataFrame
performance_df = pd.DataFrame(performance_data)
portfolios = pd.DataFrame(portfolios)

# Plotting the data
plt.figure(figsize=(10, 6))
#plt.plot(performance_df['Trading Date'], performance_df['Starting Balance'], label='Starting Balance', marker='o')
plt.plot(performance_df['Trading Date'], performance_df['Updated Balance'], label='Updated Balance', marker='o')
plt.xlabel('Trading Date')
plt.ylabel('Balance')
plt.title('Performance Over Trading Days')
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.legend()
plt.grid()
plt.tight_layout()  # Adjust layout to make room for labels
plt.show()
