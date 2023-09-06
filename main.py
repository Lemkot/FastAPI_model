from fastapi import FastAPI
import yfinance as yf
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

app = FastAPI()

@app.post('/')
async def price():
    try:
        # Define the ticker symbol of the stock you want to fetch data for
        ticker_symbol = 'AAPL'

        # Create a Yahoo Finance ticker object
        stock = yf.Ticker(ticker_symbol)

        # Fetch historical data for the stock
        historical_data = stock.history(period='1y')  # Adjust the period as needed

        if historical_data.empty:
            return {"error": "No historical data available for the given ticker symbol."}

        # Extract the most recent closing price
        prices = historical_data['Close']
        
        # Fit an ARIMA model to the training data
        order = (5, 1, 0)  # Example order for ARIMA (p, d, q)
        model = ARIMA(prices, order=order)
        model_fit = model.fit()
        
        # Forecast the next day's price
        forecasted_value_next_day = model_fit.forecast(steps=1).iloc[0]
        
        return {"ticker": ticker_symbol, "forecasted_price": float(forecasted_value_next_day)}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
