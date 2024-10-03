# Creating and testing a daytrading strategy on the S&P 500 Index

This project is work in progress and still contains many errors.
But the goal is to use publicly available stockmarket data and devise a daytrading strategy based on some analyses and statistical regularities.
The index of interest is the [S&P 500](https://en.wikipedia.org/wiki/S%26P_500).

There are many steps to be taken, and if I have time, I will describe them in detail in a Jupyter Notebook.
For now, the separate files are available here, without much explanation.

This is what happens (or is supposed to happen) in each file:
- `Stock market data - scrape components.py` - In order to download the stockmarket data, we first need the full list of stocks included in the S&P 500. In this file we scrape the data from the English Wikipedia page to put that list together.
- `Stock market data - get quotes.py` - We download historical data from Yahoo Finance using the `yfinance` package. 
- `Stock market data - clean and stack.py` - In this part we combine the data into a stacked form and calculate the day to day growth for each stock.
- `Stock market data - calculate avg performance.py`- We now create some benchmarks about the performance of individual stocks.
- `Stock market data - Network neighbours.py` - This file will use the correlation matrix of the daily returns of each stock and create a network from it. We use each stock's network neighbours to draw (what we think) might be desirable candidates for our portfolio.
- `Stock market data - clustering.py` - It makes sense to differentiate different economic sectors when trading. In this file we use spectral clustering to determine stocks that belong to different economic sectors or market segments based on the daily return correlation matrix.
- `Stock market data - portfolio selection.py` - Here we use all of the above information (network neighbours, market segment, average performance) to pick a selection of promising stocks.

Some interlude: Let's say we found a way to identify stocks that are generally promising. The code so far identified these kind of stocks. But we still need to decide how we want to allocate our money to a promising portfolio. The approach taken here uses an implementation of the [Kelly criterion](https://en.wikipedia.org/wiki/Kelly_criterion) in order to allocate our funding in such a way that for a certain risk level, the expected long-term growth is maximised. For this to work, some linear optimisation is necessary. Luckily, other people have implemented this before, and provided their code. The Ledoit-Wolf-Estimator has been programmed by [WLM1ke](https://github.com/WLM1ke), the original code is [here](https://github.com/WLM1ke/LedoitWolf?tab=readme-ov-file).

- `Stock market data - Kelly optimization.py` - So here the Ledoit-Wolf-Estimator is used to implement the Kelly-Optimization. The latter uses Linear Programming to find an optimal allocation of funds to a portfolio. (A maximum of 5 stocks will be traded here.)
- `Stock market data - get trading days.py` - In order to simulate trading, we later need to define the number of trading days. This is a subroutine to pick valid trading days based on the existing data.
- `Stock market data - sell portfolio.py` - We also need some function to sell our portfolio and add up the proceeds from a given sale. This is needed to calculate the starting capital for the next trading day.
- `Stock market data - simulate trading functions.py` - This script contains all the necessary functions (from the previous steps) that need to be applied on a given trading day.
- `Stock market data - simulate trading 4.py` - Finally! This script implements the whole trading process for a specified trading window and also plots the development of the portfolio value.
- `Stock market data - benchmark.py` - Since we need to evaluate our trading strategy against some benchmark, this file creates the results for such a benchmark strategy. The strategy here is to select 5 random stocks at the beginning of the trading window and hold them until the end of the trading window. Thus we can compare how trading every day, based on our rules, compares to a buy-and-hold-strategy.

I will still add many improvements. But generally, this code works.
There are some known issues:
* The Kelly-Optimization sometimes cannot reach an optimal solution. In this case, just a random sample of 5 stocks ( in a given market segment) are picked. This seems to happen far too often. I will change the code so that the optimization is iterated until an optimal solution is found. A random selection will only be the last resort.
* The routine for the stockmarket data download could be updated to always download the latest data and update the calculations accordingly. This is on my list.
* The whole project is complex and needs to be more user friendly. Some kind of user interface or at least proper prompting of input values is needed.
* It despreately needs a better structure and version control.
* Buying and selling are assumed to be free. Obviously this is not true. There is a buy and sell spread, there are trading costs, etc. This still needs to be implemented.
* The benchmark function can probably be more easily integrated than running in a stand-alone file.
* If I get my hands on actual historical intraday data, I will devise a way to implement buying and selling decision within a day . Right now, stocks are being bought at the opening price and sold at the selling price.
