# In this part we combine the data into a stacked form and calculate the day to day growth for each stock. #

import pandas as pd
import numpy as np
import yfinance as yf
import datetime

sp500_data = {}  # Dictionary to store DataFrames with year as key

for i in range(2018, 2025):
    file_name = f'sp500_data_{i}.csv'
    sp500_data[i] = pd.read_csv(file_name)

# Clean up the column names and indexes

sp500_2018 = sp500_data[2018]
sp500_2018_adj_close = sp500_2018.iloc[2:252, 0:504]
adj_columns = list(sp500_2018.columns[0:504])
adj_columns[0] = "Date"
symbols = list(sp500_2018.iloc[0, 0:504])
symbols = symbols[1:]
adj_columns = [adj_columns[0]] + symbols
sp500_2018_adj_close.columns = adj_columns

sp500_2018_close = sp500_2018.iloc[2:252, [0] + list(range(504, 1007))]
sp500_2018_close.columns = adj_columns

sp500_2018_high = sp500_2018.iloc[2:252, [0] + list(range(1007, 1510))]
sp500_2018_high.columns = adj_columns

sp500_2018_low = sp500_2018.iloc[2:252, [0] + list(range(1510, 2013))]
sp500_2018_low.columns = adj_columns

sp500_2018_open = sp500_2018.iloc[2:252, [0] + list(range(2013, 2516))]
sp500_2018_open.columns = adj_columns

sp500_2018_volume = sp500_2018.iloc[2:252, [0] + list(range(2516, 3019))]
sp500_2018_volume.columns = adj_columns

sp500_2019 = sp500_data[2019]
sp500_2019_adj_close = sp500_2019.iloc[2:253, 0:504]
adj_columns = list(sp500_2019.columns[0:504])
adj_columns[0] = "Date"
symbols = list(sp500_2019.iloc[0, 0:504])
symbols = symbols[1:]
adj_columns = [adj_columns[0]] + symbols
sp500_2019_adj_close.columns = adj_columns

sp500_2019_close = sp500_2019.iloc[2:253, [0] + list(range(504, 1007))]
sp500_2019_close.columns = adj_columns

sp500_2019_high = sp500_2019.iloc[2:253, [0] + list(range(1007, 1510))]
sp500_2019_high.columns = adj_columns

sp500_2019_low = sp500_2019.iloc[2:253, [0] + list(range(1510, 2013))]
sp500_2019_low.columns = adj_columns

sp500_2019_open = sp500_2019.iloc[2:253, [0] + list(range(2013, 2516))]
sp500_2019_open.columns = adj_columns

sp500_2019_volume = sp500_2019.iloc[2:253, [0] + list(range(2516, 3019))]
sp500_2019_volume.columns = adj_columns

sp500_2020 = sp500_data[2020]
sp500_2020_adj_close = sp500_2020.iloc[2:254, 0:504]
adj_columns = list(sp500_2020.columns[0:504])
adj_columns[0] = "Date"
symbols = list(sp500_2020.iloc[0, 0:504])
symbols = symbols[1:]
adj_columns = [adj_columns[0]] + symbols
sp500_2020_adj_close.columns = adj_columns

sp500_2020_close = sp500_2020.iloc[2:254, [0] + list(range(504, 1007))]
sp500_2020_close.columns = adj_columns

sp500_2020_high = sp500_2020.iloc[2:254, [0] + list(range(1007, 1510))]
sp500_2020_high.columns = adj_columns

sp500_2020_low = sp500_2020.iloc[2:254, [0] + list(range(1510, 2013))]
sp500_2020_low.columns = adj_columns

sp500_2020_open = sp500_2020.iloc[2:254, [0] + list(range(2013, 2516))]
sp500_2020_open.columns = adj_columns

sp500_2020_volume = sp500_2020.iloc[2:254, [0] + list(range(2516, 3019))]
sp500_2020_volume.columns = adj_columns

sp500_2021 = sp500_data[2021]
sp500_2021_adj_close = sp500_2021.iloc[2:253, 0:504]
adj_columns = list(sp500_2021.columns[0:504])
adj_columns[0] = "Date"
symbols = list(sp500_2021.iloc[0, 0:504])
symbols = symbols[1:]
adj_columns = [adj_columns[0]] + symbols
sp500_2021_adj_close.columns = adj_columns

sp500_2021_close = sp500_2021.iloc[2:253, [0] + list(range(504, 1007))]
sp500_2021_close.columns = adj_columns

sp500_2021_high = sp500_2021.iloc[2:253, [0] + list(range(1007, 1510))]
sp500_2021_high.columns = adj_columns

sp500_2021_low = sp500_2021.iloc[2:253, [0] + list(range(1510, 2013))]
sp500_2021_low.columns = adj_columns

sp500_2021_open = sp500_2021.iloc[2:253, [0] + list(range(2013, 2516))]
sp500_2021_open.columns = adj_columns

sp500_2021_volume = sp500_2021.iloc[2:253, [0] + list(range(2516, 3019))]
sp500_2021_volume.columns = adj_columns


sp500_2022 = sp500_data[2022]
sp500_2022_adj_close = sp500_2022.iloc[2:253, 0:504]
adj_columns = list(sp500_2022.columns[0:504])
adj_columns[0] = "Date"
symbols = list(sp500_2022.iloc[0, 0:504])
symbols = symbols[1:]
adj_columns = [adj_columns[0]] + symbols
sp500_2022_adj_close.columns = adj_columns

sp500_2022_close = sp500_2022.iloc[2:253, [0] + list(range(504, 1007))]
sp500_2022_close.columns = adj_columns

sp500_2022_high = sp500_2022.iloc[2:253, [0] + list(range(1007, 1510))]
sp500_2022_high.columns = adj_columns

sp500_2022_low = sp500_2022.iloc[2:253, [0] + list(range(1510, 2013))]
sp500_2022_low.columns = adj_columns

sp500_2022_open = sp500_2022.iloc[2:253, [0] + list(range(2013, 2516))]
sp500_2022_open.columns = adj_columns

sp500_2022_volume = sp500_2022.iloc[2:253, [0] + list(range(2516, 3019))]
sp500_2022_volume.columns = adj_columns

sp500_2023 = sp500_data[2023]
sp500_2023_adj_close = sp500_2023.iloc[2:252, 0:504]
adj_columns = list(sp500_2023.columns[0:504])
adj_columns[0] = "Date"
symbols = list(sp500_2023.iloc[0, 0:504])
symbols = symbols[1:]
adj_columns = [adj_columns[0]] + symbols
sp500_2023_adj_close.columns = adj_columns

sp500_2023_close = sp500_2023.iloc[2:252, [0] + list(range(504, 1007))]
sp500_2023_close.columns = adj_columns

sp500_2023_high = sp500_2023.iloc[2:252, [0] + list(range(1007, 1510))]
sp500_2023_high.columns = adj_columns

sp500_2023_low = sp500_2023.iloc[2:252, [0] + list(range(1510, 2013))]
sp500_2023_low.columns = adj_columns

sp500_2023_open = sp500_2023.iloc[2:252, [0] + list(range(2013, 2516))]
sp500_2023_open.columns = adj_columns

sp500_2023_volume = sp500_2023.iloc[2:252, [0] + list(range(2516, 3019))]
sp500_2023_volume.columns = adj_columns

sp500_2024 = sp500_data[2024]
sp500_2024_adj_close = sp500_2024.iloc[2:179, 0:504]
adj_columns = list(sp500_2024.columns[0:504])
adj_columns[0] = "Date"
symbols = list(sp500_2024.iloc[0, 0:504])
symbols = symbols[1:]
adj_columns = [adj_columns[0]] + symbols
sp500_2024_adj_close.columns = adj_columns

sp500_2024_close = sp500_2024.iloc[2:179, [0] + list(range(504, 1007))]
sp500_2024_close.columns = adj_columns

sp500_2024_high = sp500_2024.iloc[2:179, [0] + list(range(1007, 1510))]
sp500_2024_high.columns = adj_columns

sp500_2024_low = sp500_2024.iloc[2:179, [0] + list(range(1510, 2013))]
sp500_2024_low.columns = adj_columns

sp500_2024_open = sp500_2024.iloc[2:179, [0] + list(range(2013, 2516))]
sp500_2024_open.columns = adj_columns

sp500_2024_volume = sp500_2024.iloc[2:179, [0] + list(range(2516, 3019))]
sp500_2024_volume.columns = adj_columns

# Merge using adj_close: This led to huge errors for one stock
#merged_2018 = pd.merge(left=sp500_2018_open, right=sp500_2018_adj_close, on='Date')
#merged_2019 = pd.merge(left=sp500_2019_open, right=sp500_2019_adj_close, on='Date')
#merged_2020 = pd.merge(left=sp500_2020_open, right=sp500_2020_adj_close, on='Date')
#merged_2021 = pd.merge(left=sp500_2021_open, right=sp500_2021_adj_close, on='Date')
#merged_2022 = pd.merge(left=sp500_2022_open, right=sp500_2022_adj_close, on='Date')
#merged_2023 = pd.merge(left=sp500_2023_open, right=sp500_2023_adj_close, on='Date')
#merged_2024 = pd.merge(left=sp500_2024_open, right=sp500_2024_adj_close, on='Date')

# Merge using close
merged_2018 = pd.merge(left=sp500_2018_open, right=sp500_2018_close, on='Date')
merged_2019 = pd.merge(left=sp500_2019_open, right=sp500_2019_close, on='Date')
merged_2020 = pd.merge(left=sp500_2020_open, right=sp500_2020_close, on='Date')
merged_2021 = pd.merge(left=sp500_2021_open, right=sp500_2021_close, on='Date')
merged_2022 = pd.merge(left=sp500_2022_open, right=sp500_2022_close, on='Date')
merged_2023 = pd.merge(left=sp500_2023_open, right=sp500_2023_close, on='Date')
merged_2024 = pd.merge(left=sp500_2024_open, right=sp500_2024_close, on='Date')

# Concatenate below
merged_all = pd.concat([merged_2018, merged_2019, merged_2020, merged_2021, merged_2022, merged_2023, merged_2024])
merged_all = merged_all.sort_values(by=['Date'])
merged_all.to_csv('merged_all.csv', index=False)

# Calculate daily growth (adj_close - open) / open
daily_growth = merged_all[['Date']].copy()

for symbol in symbols:
        merged_all[f'{symbol}_x'] = pd.to_numeric(merged_all[f'{symbol}_x'], errors='coerce')
        merged_all[f'{symbol}_y'] = pd.to_numeric(merged_all[f'{symbol}_y'], errors='coerce')

for symbol in symbols:
 daily_growth[f'{symbol}_growth'] = (merged_all[f'{symbol}_y'] - merged_all[f'{symbol}_x']) / merged_all[f'{symbol}_x']

# Save as csv
daily_growth.to_csv('daily_growth.csv', index=False)



