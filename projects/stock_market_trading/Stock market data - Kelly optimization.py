# This will take a list of stocks and suggest a Kelly-optimal investment allocation #

import numpy as np
import pandas as pd
from cvxopt import matrix, solvers
from typing import Dict
from typing import Tuple

"""Ledoit & Wolf constant correlation unequal variance shrinkage estimator."""
"""https://github.com/WLM1ke/LedoitWolf?tab=readme-ov-file"""
def shrinkage(returns: np.array) -> Tuple[np.array, float, float]:
    """Shrinks sample covariance matrix towards constant correlation unequal variance matrix.

    Ledoit & Wolf ("Honey, I shrunk the sample covariance matrix", Portfolio Management, 30(2004),
    110-119) optimal asymptotic shrinkage between 0 (sample covariance matrix) and 1 (constant
    sample average correlation unequal sample variance matrix).

    Paper:
    http://www.ledoit.net/honey.pdf

    Matlab code:
    https://www.econ.uzh.ch/dam/jcr:ffffffff-935a-b0d6-ffff-ffffde5e2d4e/covCor.m.zip

    Special thanks to Evgeny Pogrebnyak https://github.com/epogrebnyak

    :param returns:
        t, n - returns of t observations of n shares.
    :return:
        Covariance matrix, sample average correlation, shrinkage.
    """
    t, n = returns.shape
    mean_returns = np.mean(returns, axis=0, keepdims=True)
    returns -= mean_returns
    sample_cov = returns.transpose() @ returns / t

    # sample average correlation
    var = np.diag(sample_cov).reshape(-1, 1)
    sqrt_var = var ** 0.5
    unit_cor_var = sqrt_var * sqrt_var.transpose()
    average_cor = ((sample_cov / unit_cor_var).sum() - n) / n / (n - 1)
    prior = average_cor * unit_cor_var
    np.fill_diagonal(prior, var)

    # pi-hat
    y = returns ** 2
    phi_mat = (y.transpose() @ y) / t - sample_cov ** 2
    phi = phi_mat.sum()

    # rho-hat
    theta_mat = ((returns ** 3).transpose() @ returns) / t - var * sample_cov
    np.fill_diagonal(theta_mat, 0)
    rho = (
        np.diag(phi_mat).sum()
        + average_cor * (1 / sqrt_var @ sqrt_var.transpose() * theta_mat).sum()
    )

    # gamma-hat
    gamma = np.linalg.norm(sample_cov - prior, "fro") ** 2

    # shrinkage constant
    kappa = (phi - rho) / gamma
    shrink = max(0, min(1, kappa / t))

    # estimator
    sigma = shrink * prior + (1 - shrink) * sample_cov

    return sigma, average_cor, shrink

# takes in a numpy array
# returns = daily_growth.iloc[0:, 1: -1].to_numpy()
# ledoit = shrinkage(returns)

""" https://vegapit.com/article/numerically_solve_kelly_criterion_multiple_simultaneous_bets """
def clip(x: float) -> float:
    """Clip values to be between 0 and 1."""
    return max(0, min(1, x))

""" https://github.com/thk3421-models/KellyPortfolio/blob/main/kelly.py """
def kelly_optimization(daily_growth: pd.DataFrame, tickers: list, config: Dict) -> pd.DataFrame:
    # Step 1: Select the relevant columns
    selected_data = daily_growth[['Date'] + tickers].copy()
    selected_data.set_index('Date', inplace=True)

    # Step 2: Extract returns (assuming daily_growth already contains returns)
    returns = selected_data

    # Step 3: Use the provided shrinkage estimator to get the covariance matrix
    cov_matrix, avg_cor, shrink = shrinkage(returns.values)

    # Step 4: Calculate mean returns
    mean_returns = returns.mean().values * 252  # Annualize the mean returns

    # Step 5: Define the quadratic programming problem
    n = len(tickers)
    P = matrix(cov_matrix)
    q = matrix(-mean_returns)
    G = matrix(np.vstack((-np.eye(n), np.eye(n))))
    h = matrix(np.hstack((np.zeros(n), np.ones(n))))
    A = matrix(1.0, (1, n))
    b = matrix(1.0)

    # Step 6: Solve the quadratic programming problem
    sol = solvers.qp(P, q, G, h, A, b)
    kelly_weights = np.array(sol['x']).flatten()

    # Create a DataFrame for the weights
    weights_df = pd.DataFrame(kelly_weights, index=tickers, columns=['Weights'])

    # Calculate capital allocation
    weights_df['Capital_Allocation'] = weights_df['Weights'] * config['capital']

    # Display results
    print('Kelly Weights with No Shorting or Borrowing')
    print(weights_df.round(2))
    cash = config['capital'] - weights_df['Capital_Allocation'].sum()
    print('Cash:', np.round(cash))
    print('*' * 100)

    return weights_df

# Example usage:
# daily_growth = pd.read_csv('path_to_your_file.csv')
# tickers = ['A', 'AAL', 'AAPL']
# config = {
#     'capital': 1000000,
#     'annual_risk_free_rate': 0.02,
#     'kelly_fraction': 1.0
# }
# optimized_portfolio = kelly_optimization(daily_growth, tickers, config)
# print(optimized_portfolio)







tickers = ['NVDA', 'FTNT', 'MPWR', 'CRWD', 'FICO']
config = {
     'capital': 1000,
     'annual_risk_free_rate': 0.02,
     'kelly_fraction': 1.0
}

optimized_portfolio = kelly_optimization(daily_growth, tickers, config)
print(optimized_portfolio)

# Test on random draw of stocks

import random

def select_random_symbols(symbols, num_items):
    if num_items > len(symbols):
        raise ValueError("Number of items to be selected cannot be greater than the number of available symbols.")
    return random.sample(symbols, num_items)
symbols = list(daily_growth.columns)[1:-1]
tickers = select_random_symbols(symbols, 5)
print(tickers)

optimized_portfolio = kelly_optimization(daily_growth, tickers, config)
print(optimized_portfolio)
