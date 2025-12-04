import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("TIINGO_API_KEY")
BASE_URL = "https://api.tiingo.com/tiingo/daily"

if not API_KEY:
    raise RuntimeError("TIINGO_API_KEY not found in environment; add it to your .env")

def get_daily_prices(ticker):   # Prices for only Today
    url = f"{BASE_URL}/{ticker}/prices"
    params = {"token": API_KEY}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return pd.DataFrame(resp.json())


def get_historical_prices(ticker, start_date = "1900-01-01"):  # Later Add Start Data
    """Returns ALL Historical data of Ticker ticker as pd.DataFrame
    start_date: str in format 'YYYY-MM-DD' or None
    """
    url = f"{BASE_URL}/{ticker}/prices?startDate={start_date}&token={API_KEY}"     #### Prices Starting start_date to today for now
    requestResponse = requests.get(url)
    requestResponse.raise_for_status()
    return pd.DataFrame(requestResponse.json())

def get_metadata(ticker):
    url = f"{BASE_URL}/{ticker}?token={API_KEY}"
    requestResponse = requests.get(url)
    requestResponse.raise_for_status()
    return requestResponse.json()



historical_data_df = get_historical_prices(ticker="AAPL", start_date="2000-01-01")
meta_data_df = get_metadata("AAPL")
print(historical_data_df)

historical_data_df.to_csv("Apple Historical Market Data.csv", index=False)


