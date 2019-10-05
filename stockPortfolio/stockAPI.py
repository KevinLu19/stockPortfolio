# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 10/4/2019
# File: stockAPI.py
# Purpose: Handles the requests from Alpha Vantage API. 
# Modification: - Added function to return today's stock.
# ----------------------------------------------------------------------------------------

from datetime import date
import requests, json, alpha_vantage

API_KEY = 'MQS69ABIP9YWEATW'

# Modulate the request website.
apiFunction = "GLOBAL_QUOTE"
symbol = "GOOGL"
# r = requests.get('https://www.alphavantage.co/query?function={}&symbol={}&apikey={}'.format(apiFunction , symbol, API_KEY))

# if (r.status_code == 200):
#     # print (r.json())
#     result = r.json()
#     print (result)