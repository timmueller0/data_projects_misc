# Get trading days for multiple day execution
def get_trading_days(all_prices: pd.DataFrame, start_date: str, n_days: int) -> list:
    """
    Function to extract up to n continuous trading days starting from the start_date.
    If fewer than n days are available, it will return all remaining days.
    """
    # Ensure the index is in datetime format
    all_prices.index = pd.to_datetime(all_prices.index)

    # Get the position of the start_date in the index
    try:
        start_idx = all_prices.index.get_loc(start_date)
    except KeyError:
        raise ValueError(f"Start date {start_date} is not in the dataset.")

    # Get the slice of trading dates, ensuring we don't exceed the available days
    end_idx = min(start_idx + n_days, len(all_prices.index))
    trading_days = all_prices.index[start_idx:end_idx]

    # Check if fewer days than requested are available
    if len(trading_days) < n_days:
        print(f"Warning: Only {len(trading_days)} trading days are available after {start_date}.")

    return trading_days.tolist()


# Example usage
start_date = '2023-09-01'
n_days = 30  # Number of trading days to simulate
trading_days = get_trading_days(all_prices, start_date, n_days)
print("Selected trading days:", trading_days)
