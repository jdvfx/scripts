import json
import urllib3

# free API key for 25 queries per day
api_key = "LRITJO07DMGCXMR6"

tickers = ["MSFT","AAPL","NVDA","AMZN"]

with open("share_prices.txt","w") as file:

    for ticker in tickers:
        u=f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}"
        resp = urllib3.request("GET", u)
        d = resp.data
        data = json.loads(d)
        try:
            current_price = data["Global Quote"]["05. price"]
            file.write(f"{ticker}:{current_price}\n")
            print(f"{ticker}:{current_price}")
        except Exception as e:
            print(f"ERR {ticker}: {e}")

