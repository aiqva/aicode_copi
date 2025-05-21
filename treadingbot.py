"""
use alphavantage API to get stock data
and plot it using matplotlib
and use pandas to manipulate the data
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

ALPHA_API_KEY = "ZC5FHTWX4Z8P6UZH"
ALPHA_API_URL = "https://www.alphavantage.co/query"
ALPHA_API_FUNCTION = "TIME_SERIES_WEEKLY_ADJUSTED"
ALPHA_API_OUTPUT_SIZE = "full"

def get_weekly_stock_data(symbol, interval="5min"):
    """
    Get weekly stock data for a given symbol
    """
    params = {
        "function": ALPHA_API_FUNCTION,
        "symbol": symbol,
        "interval": interval,
        "apikey": ALPHA_API_KEY,
        "outputsize": "full"
    }
    response = requests.get(ALPHA_API_URL, params=params)
    data = response.json()
    return data

def main():
    """
    Main function to get stock data and plot it
    """
    symbol = input("Enter the stock symbol: ")
    data = get_weekly_stock_data(symbol)
    if "Error Message" in data:
        print("Error: Invalid stock symbol")
        return
    ## Process the data
    # Convert the data to a pandas DataFrame
    df= pd.DataFrame.from_dict(data["Weekly Adjusted Time Series"], orient="index")

    # Convert the index to datetime
    df.index = pd.to_datetime(df.index)

    # Convert the columns to numeric
    df = df.apply(pd.to_numeric, errors="coerce")

    # Sort the data by date
    df = df.sort_index()

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["5. adjusted close"], label="Adjusted Close")
    plt.title(f"{symbol} Weekly Adjusted Close Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.show()

    # Print the data
    print("Weekly Adjusted Time Series:")
    print("--------------------------------------------------")
    print(data)

if __name__ == "__main__":
    main()