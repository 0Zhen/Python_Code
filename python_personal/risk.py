import pandas as pd
import numpy as np
import yfinance as yf
from scipy import stats

# 下載數據
start_date = '2018-01-01'
end_date = '2023-12-31'

sp500 = yf.download('^GSPC', start=start_date, end=end_date)['Adj Close']
btc = yf.download('BTC-USD', start=start_date, end=end_date)['Adj Close']

# 計算每日收益率
sp500_returns = sp500.pct_change().dropna()
btc_returns = btc.pct_change().dropna()


def calculate_risk_metrics(returns):
    """計算各種風險指標"""
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


# 計算風險指標
sp500_metrics = calculate_risk_metrics(sp500_returns)
btc_metrics = calculate_risk_metrics(btc_returns)

# 創建比較表格
comparison_df = pd.DataFrame({
    "S&P 500": sp500_metrics,
    "Bitcoin": btc_metrics
})

print(comparison_df)

# 計算相關性
correlation = sp500_returns.corr(btc_returns)
print(f"\n相關係數: {correlation:.4f}")

# 進行T檢驗
t_stat, p_value = stats.ttest_ind(sp500_returns, btc_returns)
print(f"\nT檢驗結果:")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")