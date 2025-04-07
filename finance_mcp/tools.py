"""Finance MCP Server tools.

This module contains the tools exposed by the Finance MCP server.
"""

import requests
import yfinance as yf
from pprint import pformat

def lookup_stock_symbol(company_name):
    """
    Converts a company name to its stock symbol using a financial API.

    Args:
        company_name: The full company name (e.g., 'Tesla').

    Returns:
        The stock symbol (e.g., 'TSLA') or an error message.
    """
    api_url = "https://www.alphavantage.co/query"
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": company_name,
        "apikey": "your_alphavantage_api_key"  # Replace with actual API key in production
    }
    
    response = requests.get(api_url, params=params)
    data = response.json()
    
    if "bestMatches" in data and data["bestMatches"]:
        return data["bestMatches"][0]["1. symbol"]
    else:
        return f"Symbol not found for {company_name}."

def fetch_stock_data(stock_symbol, period="1mo"):
    """
    Fetches comprehensive stock data for a given symbol.

    Args:
        stock_symbol: The stock ticker symbol (e.g., 'TSLA').
        period: The period to analyze (e.g., '1mo', '3mo', '1y').

    Returns:
        A dictionary combining general stock info and historical market data.
    """
    try:
        stock = yf.Ticker(stock_symbol)

        # Retrieve general stock info and historical market data
        stock_info = stock.info  # Basic company and stock data
        stock_history = stock.history(period=period).to_dict()  # Historical OHLCV data

        # Combine both into a single dictionary
        combined_data = {
            "stock_symbol": stock_symbol,
            "info": stock_info,
            "history": stock_history
        }

        return pformat(combined_data)

    except Exception as e:
        return {"error": f"Error fetching stock data for {stock_symbol}: {str(e)}"}

