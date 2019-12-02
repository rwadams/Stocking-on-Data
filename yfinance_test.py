#!/usr/bin/env python3

import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
#print(msft.info)

# get historical market data
hist = msft.history(period="max")
print(type(hist))
export_csv = hist.to_csv(r'C:\Users\rwadams\Documents\Fall 2019\CS 437 Project\y_finance_test_output.csv')

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show balance heet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show options expirations
msft.options

# get option chain for specific expiration
#opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
