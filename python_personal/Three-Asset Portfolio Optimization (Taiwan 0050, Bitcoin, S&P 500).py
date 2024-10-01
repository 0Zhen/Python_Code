import pandas as pd
import numpy as np
import yfinance as yf
from scipy import stats
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Download data
start_date = '2018-01-01'
end_date = '2024-09-30'

# Set Taiwan timezone
taiwan_tz = pytz.timezone('Asia/Taipei')

# Download Taiwan 0050, Bitcoin, and S&P 500 data
tw0050 = yf.download('0050.TW', start=start_date, end=end_date, interval='1d')['Adj Close']
btc = yf.download('BTC-USD', start=start_date, end=end_date)['Adj Close']
sp500 = yf.download('^GSPC', start=start_date, end=end_date)['Adj Close']

# Calculate daily returns
tw0050_returns = tw0050.pct_change().dropna()
btc_returns = btc.pct_change().dropna()
sp500_returns = sp500.pct_change().dropna()

# Ensure the returns are aligned
aligned_returns = pd.concat([tw0050_returns, btc_returns, sp500_returns], axis=1).dropna()
aligned_returns.columns = ['Taiwan 0050', 'Bitcoin', 'S&P 500']

def calculate_risk_metrics(returns):
    """Calculate various risk metrics"""
    annualized_return = returns.mean() * 252
    annualized_volatility = returns.std() * np.sqrt(252)
    sharpe_ratio = annualized_return / annualized_volatility
    var_95 = np.percentile(returns, 5)
    cvar_95 = returns[returns <= var_95].mean()
    max_drawdown = (returns.cumsum() - returns.cumsum().cummax()).min()

    return {
        "Annualized Return": annualized_return,
        "Annualized Volatility": annualized_volatility,
        "Sharpe Ratio": sharpe_ratio,
        "VaR (95%)": var_95,
        "CVaR (95%)": cvar_95,
        "Max Drawdown": max_drawdown
    }

# Calculate risk metrics for all assets
risk_metrics = {asset: calculate_risk_metrics(aligned_returns[asset]) for asset in aligned_returns.columns}

# Create comparison table
comparison_df = pd.DataFrame(risk_metrics)
print(comparison_df)

# Calculate correlation matrix
correlation_matrix = aligned_returns.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Asset data
assets = ['Taiwan 0050', 'Bitcoin', 'S&P 500']
returns = np.array([risk_metrics[asset]['Annualized Return'] for asset in assets])
volatilities = np.array([risk_metrics[asset]['Annualized Volatility'] for asset in assets])

# Calculate covariance matrix
covariance_matrix = aligned_returns.cov() * 252

def portfolio_performance(weights):
    """Calculate portfolio return and volatility"""
    weights = np.array(weights)
    portfolio_return = np.sum(returns * weights)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))
    return portfolio_return, portfolio_volatility

def neg_sharpe_ratio(weights):
    """Calculate negative Sharpe ratio (for maximization)"""
    p_return, p_volatility = portfolio_performance(weights)
    return -(p_return - 0.02) / p_volatility  # Assuming risk-free rate of 2%

# Find the optimal Sharpe ratio portfolio
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for asset in range(len(assets)))
init_guess = [1/len(assets) for asset in range(len(assets))]
optimal_sharpe = minimize(neg_sharpe_ratio, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)

optimal_return, optimal_volatility = portfolio_performance(optimal_sharpe.x)

# Print detailed results
print("\nModel Calculation Results:")
print("\n1. Optimal Sharpe Ratio Portfolio:")
for i, asset in enumerate(assets):
    print(f"   {asset} weight: {optimal_sharpe.x[i]:.4f} ({optimal_sharpe.x[i]:.2%})")
print(f"   Expected annual return: {optimal_return:.4f} ({optimal_return:.2%})")
print(f"   Expected annual volatility: {optimal_volatility:.4f} ({optimal_volatility:.2%})")
print(f"   Sharpe ratio: {(optimal_return - 0.02) / optimal_volatility:.4f}")

# Calculate and print results for different portfolio allocations
allocations = [
    (1, 0, 0),  # 100% Taiwan 0050
    (0, 1, 0),  # 100% Bitcoin
    (0, 0, 1),  # 100% S&P 500
    (1/3, 1/3, 1/3),  # Equal weight
    tuple(optimal_sharpe.x)  # Optimal portfolio
]

print("\n2. Comparison of Different Portfolio Allocations:")
for i, allocation in enumerate(allocations):
    return_, volatility_ = portfolio_performance(allocation)
    sharpe = (return_ - 0.02) / volatility_
    print(f"\nAllocation {i+1}:")
    for j, asset in enumerate(assets):
        print(f"   {asset}: {allocation[j]:.2%}")
    print(f"   Expected annual return: {return_:.4f} ({return_:.2%})")
    print(f"   Expected annual volatility: {volatility_:.4f} ({volatility_:.2%})")
    print(f"   Sharpe ratio: {sharpe:.4f}")

# Generate efficient frontier data
num_portfolios = 100000
results = np.zeros((3, num_portfolios))
for i in range(num_portfolios):
    weights = np.random.random(3)
    weights /= np.sum(weights)
    portfolio_return, portfolio_volatility = portfolio_performance(weights)
    results[0,i] = portfolio_return
    results[1,i] = portfolio_volatility
    results[2,i] = (portfolio_return - 0.02) / portfolio_volatility

# Plot efficient frontier
plt.figure(figsize=(12, 8))
scatter = plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Sharpe Ratio')
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier: Taiwan 0050 vs Bitcoin vs S&P 500')
for i, asset in enumerate(assets):
    plt.plot(volatilities[i], returns[i], '*', markersize=15.0, label=asset)
plt.plot(optimal_volatility, optimal_return, 'g*', markersize=15.0, label='Optimal Portfolio')
plt.legend()

# Add text annotations for key points
for i, allocation in enumerate(allocations):
    return_, volatility_ = portfolio_performance(allocation)
    plt.annotate(f'Portfolio {i+1}\nReturn: {return_:.2%}\nVolatility: {volatility_:.2%}',
                 xy=(volatility_, return_), xytext=(5, 5), textcoords='offset points')

plt.tight_layout()
plt.show()