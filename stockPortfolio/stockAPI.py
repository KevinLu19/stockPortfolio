# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 10/4/2019
# File: stockAPI.py
# Purpose: Handles the requests from Alpha Vantage API. 
# Modification: - Added function to return today's stock.
# ----------------------------------------------------------------------------------------

from alpha_vantage.timeseries import TimeSeries
from datetime import date

# Your key here
key = 'MQS69ABIP9YWEATW'
ts = TimeSeries(key)

todaysDate = date.today()

# aapl, meta = ts.get_daily(symbol='AAPL')
# print(aapl['2019-09-12'])


def retrieveDailyStock(ticker):
    ticker, meta = ts.get_daily(symbol=ticker)

    return (ticker[todaysDate])