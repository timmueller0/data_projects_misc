# Now it's time to sell. Here we act as day traders and sell each portfolio on the same day for the closing price. #
def sell_portfolio(allocation_df, prices_df, start_date, initial_balance):
    # Ensure start_date is a datetime object and timezone-aware
    if not isinstance(start_date, pd.Timestamp):
        start_date = pd.to_datetime(start_date)
    if start_date.tzinfo is None:
        start_date = start_date.tz_localize('UTC')

    # Ensure initial_balance is numeric
    print(initial_balance)
    if not isinstance(initial_balance, (int, float)):
        raise ValueError(f"Initial balance should be a numeric type, got {type(initial_balance)}")


    # Check if start_date is in prices_df index
    if start_date not in prices_df.index:
        print(f"Available dates in prices_df: {prices_df.index}")
        raise ValueError(f"No price data available for the start date: {start_date}")

    # Extract closing prices for the sale date (same day for day trading)
    closing_prices_on_date = prices_df.loc[start_date, [f'{ticker}_close' for ticker in allocation_df.index]]

    # Initialize total sale proceeds
    total_sale_proceeds = 0

    # Calculate the sale value for each stock
    for ticker in allocation_df.index:
        try:
            shares_sold = allocation_df.loc[ticker, 'Shares_Bought']
            closing_price = closing_prices_on_date[f'{ticker}_close']

            sale_value = shares_sold * closing_price
            total_sale_proceeds += sale_value
        except KeyError:
            print(f"Ticker '{ticker}' not found in allocation_df. Skipping.")
            continue

        # Print out sale details
        print(f"Sold {shares_sold} shares of {ticker} at {closing_price:.2f} for a total of {sale_value:.2f}")

    # Update the account balance
    updated_balance = initial_balance + total_sale_proceeds

    # Return updated balance and total proceeds from selling
    return updated_balance, total_sale_proceeds

start_date = '2018-02-09'
initial_balance = remaining_capital  # Use the remaining capital from the allocation

updated_balance, total_proceeds = sell_portfolio(allocation_df, all_prices, start_date, initial_balance)
print("Updated balance:", updated_balance, "total_proceeds:", total_proceeds)

