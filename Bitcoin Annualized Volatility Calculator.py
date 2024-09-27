import numpy as np
import pandas as pd
import yfinance as yf


def calculate_annualized_volatility(ticker, start_date, end_date):
    # Download historical data
    data = yf.download(ticker, start=start_date, end=end_date)

    # Calculate daily returns
    data['Returns'] = data['Close'].pct_change()

    # Calculate daily volatility
    daily_volatility = np.std(data['Returns'])

    # Annualize the volatility
    annualized_volatility = daily_volatility * np.sqrt(252)  # 252 trading days in a year

    return annualized_volatility


# Example usage
btc_volatility = calculate_annualized_volatility('BTC-USD', '2019-01-01', '2024-09-01')
print(f"Bitcoin's annualized volatility: {btc_volatility:.2%}")