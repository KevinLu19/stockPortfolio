# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 10/4/2019
# File: stockAPI.py
# Purpose: Handles the requests from Alpha Vantage API. 
# Modification: - Added function to return today's stock.
# ----------------------------------------------------------------------------------------

from datetime import date
import requests, json, alpha_vantage

# Key needed to use API. 
API_KEY = 'MQS69ABIP9YWEATW'

# Modulate the request website.
apiFunction = "GLOBAL_QUOTE"
symbol = "GOOGL"

def apiRequestData():
    r = requests.get('https://www.alphavantage.co/query?function={}&symbol={}&apikey={}'.format(apiFunction , symbol, API_KEY))

    if (r.status_code == 200):
        # Result fetches back a nested dictionary. Need to parse in order to get necessary data.
        result = r.json()

        #print (result)
        
        # Looping through nested dictionary to parse out necessary data.
        for data in result:
            for inner in result[data]:
                if (inner == "05. price"):
                    price = inner
                    print (price)
                

apiRequestData()