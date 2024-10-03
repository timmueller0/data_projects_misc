import random
import pandas as pd

def select_random_stocks(all_stocks, n=5):
    return random.sample(all_stocks, n)

# Initialize benchmark variables
benchmark_performance = []

# Select random stocks for the benchmark at the beginning
all_stocks = list(eval(cluster_variable).columns)[1:]  # Assuming this contains all stock symbols
benchmark_tickers = select_random_stocks(all_stocks, 5)
print(f"Benchmark stocks selected: {benchmark_tickers}")

# Allocate initial capital to the benchmark portfolio
benchmark_allocation_df = pd.DataFrame(index=benchmark_tickers,
                                       columns=['Weights', 'Capital_Allocation', 'Shares_Bought', 'Actual_Allocation'])
benchmark_allocation_df['Weights'] = [1 / 5] * 5  # Equal weight for simplicity
initial_benchmark_capital = 100000

# Get initial prices on start date
initial_prices = all_prices.loc[trading_days[0], [f'{ticker}_open' for ticker in benchmark_tickers]]

# Calculate shares to buy based on initial prices
for ticker in benchmark_tickers:
    open_price = initial_prices[f'{ticker}_open']
    suggested_allocation = initial_benchmark_capital * (1 / 5)
    shares_to_buy = int(suggested_allocation // open_price)

    benchmark_allocation_df.loc[ticker, 'Shares_Bought'] = shares_to_buy
    benchmark_allocation_df.loc[ticker, 'Actual_Allocation'] = shares_to_buy * open_price

# Track the portfolio value at each trading day
current_benchmark_value = initial_benchmark_capital - benchmark_allocation_df['Actual_Allocation'].sum()
benchmark_performance.append({'Trading Date': trading_days[0], 'Benchmark Value': current_benchmark_value})

# Simulate benchmark performance over the extracted trading days
for trading_date in trading_days:
    print(f"\nCalculating benchmark value for trading date: {trading_date}")

    # Update benchmark portfolio value based on current prices
    current_benchmark_value = 0
    for ticker in benchmark_tickers:
        current_price = all_prices.loc[trading_date, f'{ticker}_close']
        current_benchmark_value += current_price * benchmark_allocation_df.loc[ticker, 'Shares_Bought']

    benchmark_performance.append({'Trading Date': trading_date, 'Benchmark Value': current_benchmark_value})

# Convert the benchmark performance to a DataFrame
benchmark_df = pd.DataFrame(benchmark_performance)

plt.figure(figsize=(10, 6))
plt.plot(benchmark_df['Trading Date'].iloc[1:], benchmark_df['Benchmark Value'].iloc[1:], label='Benchmark', marker='o')
plt.plot(performance_df['Trading Date'], performance_df['Updated Balance'], label='Updated Balance', marker='o')
plt.xlabel('Trading Date')
plt.ylabel('Balance')
plt.title('Performance Over Trading Days')
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.legend()
plt.grid()
plt.tight_layout()  # Adjust layout to make room for labels
plt.show()


