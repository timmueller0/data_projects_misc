# This script loads S&P 500 stock market data to create some benchmark measures
# We start by scraping a list of S & P 500 components from Wikipedia

import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException, HTTPError

# URL of the Wikipedia page with S&P 500 companies
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError if the status is 4xx, 5xx
except RequestException as e:
    print(f"There was an issue with your request: {e}")
except HTTPError as e:
    print(f"HTTP error occurred: {e}")

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first table on the page, which contains the S&P 500 companies
table = soup.find('table', {'id': 'constituents'})  # The table has an 'id' attribute of 'constituents'

# Extract the headers (table column names)
headers = [header.text.strip() for header in table.find_all('th')]

# Extract the rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip the first row with headers
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]  # Clean up the text
    rows.append(cols)

# Convert the data into a DataFrame for easier manipulation
df = pd.DataFrame(rows, columns=headers)

# Display the first few rows of the DataFrame
print(df.head())

# Save the data to a CSV file if needed
df.to_csv('sp500_companies.csv', index=False)



