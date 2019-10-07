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
# symbol = "GOOGL"

# Storing keys so we can access them.
stockOpen = "02. open"
stockHigh = "03. high"
stockLow = "04. low"
stockPrice = "05. price"

def apiRequestData(symbol, sharesQty):
    r = requests.get('https://www.alphavantage.co/query?function={}&symbol={}&apikey={}'.format(apiFunction , symbol, API_KEY))

    if (r.status_code == 200):
        # Result fetches back a nested dictionary. Need to parse in order to get necessary data.
        result = r.json()

        #print (result)

        # Looping through nested dictionary to parse out necessary data.
        for data in result:
            for inner in result[data]:
                if (inner == stockPrice):
                    price = inner
                    sharesPrice = result[data][price]
                    totalSharesCost = float(sharesQty) * float(sharesPrice)

                    return totalSharesCost

#apiRequestData("GOOGL", 2)