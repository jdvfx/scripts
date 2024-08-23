# Python 3.11

import requests
import urllib3
import string
import time
import json
from bs4 import BeautifulSoup

"""
get stock prices from YahooFinance or AlphaVantage
write to a txt file
"""

# dummy tickers
tickers = ["QQQ","AAPL","REI-UN.TO","VFV.TO","NVDA","TRP.TO"]

# AlphaVantage free API key for 25 queries per day 
api_key = "LRITJO07DMGCXMR6"

def get_yahoo_price(ticker:str) -> float|None:

    url = f"https://finance.yahoo.com/quote/{ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    liveprice = soup.find("fin-streamer", {"class": "livePrice yf-mgkamr"})
    try:
        return float(liveprice.get("data-value"))
    except Exception:
        return None

def get_alpha_price(ticker:str) -> float|None:

    u=f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}"
    resp = urllib3.request("GET", u)
    d = resp.data
    data = json.loads(d)
    try:
        return float(data["Global Quote"]["05. price"])
    except Exception:
        return None

with open("share_prices.txt","w") as file:

    for ticker in tickers:
        current_price = get_yahoo_price(ticker)
        if current_price:
            print(f"yahoo {ticker} {current_price}")
            file.write(f"{ticker}:{current_price}\n")
        else:
            current_price = get_alpha_price(ticker)
            if current_price:
                print(f"alpha {ticker} {current_price}")
                file.write(f"{ticker}:{current_price}\n")
            else:
                print(f">>> couldn't get {ticker}")
