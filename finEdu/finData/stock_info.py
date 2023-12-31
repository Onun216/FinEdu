import yfinance as yf
import pandas as pd
import numpy as np


# msft = yf.Ticker("MSFT")

# get all stock info
# msft.info

# get historical market data
# validRanges': ['1mo', '3mo', '6mo', 'ytd', '1y', '2y', '5y', '10y', 'max']
# hist = msft.history(period="max")
# print(hist)
# hist.to_csv('filename.csv')

# show meta information about the history (requires history() to be called first)
# msft.history_metadata

# show actions (dividends, splits, capital gains)
# msft.actions
# msft.dividends
# msft.splits
# msft.capital_gains  # only for mutual funds & etfs

# show share count
# msft.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement
# msft.income_stmt
# msft.quarterly_income_stmt
# - balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet
# - cash flow statement
# msft.cashflow
# msft.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
# msft.major_holders
# msft.institutional_holders
# msft.mutualfund_holders

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
# msft.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
# msft.isin

# show options expirations
# msft.options

# show news
# msft.news

# get option chain for specific expiration
# opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts

# If you want to use a proxy server for downloading data
# msft.history(..., proxy="PROXY_SERVER")
# msft.get_actions(proxy="PROXY_SERVER")
# msft.get_dividends(proxy="PROXY_SERVER")
# msft.get_splits(proxy="PROXY_SERVER")
# msft.get_capital_gains(proxy="PROXY_SERVER")
# msft.get_balance_sheet(proxy="PROXY_SERVER")
# msft.get_cashflow(proxy="PROXY_SERVER")
# msft.option_chain(..., proxy="PROXY_SERVER")

# Multiple tickers
# tickers = yf.Tickers('msft aapl goog')

# access each ticker using (example)
# tickers.tickers['MSFT'].info
# tickers.tickers['AAPL'].history(period="1mo")
# tickers.tickers['GOOG'].actions
