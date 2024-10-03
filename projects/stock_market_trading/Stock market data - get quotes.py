# We download historical data from Yahoo Finance using the yfinance package
import pandas as pd
import numpy as np
import yfinance as yf
import datetime

sp500comp = pd.read_csv('sp500_companies.csv')

# List of tickers for S&P 500
tickers = list(sp500comp['Symbol'].unique())
tickers[62] = "BRK-B"
tickers[77] = "BF-B"

# Define the range of years you want to download data for
# 2018 has already been downloaded
years = [2018, 2019, 2020, 2021, 2022, 2023]

# Open a file to log errors
error_log = open("failed_downloads.txt", "w")

for year in years:
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    print(f"Downloading data for year {year}...")

    try:
        # Download historical data for all tickers for the current year
        data = yf.download(tickers, start=start_date, end=end_date)
        data.to_csv(f'sp500_data_{year}.csv')  # Save data for each year
    except Exception as e:
        print(f"An error occurred for year {year}: {e}")
        error_log.write(f"Error for year {year}: {e}\n")

# Close the error log file
error_log.close()

print("Download completed. Check 'failed_downloads.txt' for any errors.")

# There are a number of stocks, which were not yet listed in 2018 etc.
# We will do the calculations of average growth etc. and correlations based on existing data.

# 2024 until September 15
data = yf.download(tickers, start='2024-01-01', end='2024-09-15')
data.to_csv(f'sp500_data_2024.csv')
