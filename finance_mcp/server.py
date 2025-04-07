#!/usr/bin/env python3

"""
A minimal MCP server built with Python for financial data tools.
"""

import logging
from mcp.server.fastmcp import FastMCP
from finance_mcp import tools

# Configure logging to write to a file instead of stdout/stderr
# This avoids interference with the MCP communication channel
logging.basicConfig(
    filename='finance_mcp.log',  # Log to a file instead of stdout/stderr
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create an MCP server
mcp = FastMCP("Finance Tools")

# Register tools

@mcp.tool()
def lookup_stock_symbol(company_name):
    """
    Converts a company name to its stock symbol using a financial API.

    Args:
        company_name: The full company name (e.g., 'Tesla').

    Returns:
        The stock symbol (e.g., 'TSLA') or an error message.
    """
    logger.info(f"Looking up stock symbol for {company_name}")
    result = tools.lookup_stock_symbol(company_name)
    logger.info(f"Found symbol: {result}")
    return result

@mcp.tool()
def fetch_stock_data(stock_symbol, period="1mo"):
    """
    Fetches comprehensive stock data for a given symbol.

    Args:
        stock_symbol: The stock ticker symbol (e.g., 'TSLA').
        period: The period to analyze (e.g., '1mo', '3mo', '1y').

    Returns:
        A dictionary combining general stock info and historical market data.
    """
    logger.info(f"Fetching stock data for {stock_symbol} over period {period}")
    result = tools.fetch_stock_data(stock_symbol, period)
    logger.info(f"Successfully retrieved data for {stock_symbol}")
    return result

def run_server():
    """Run the MCP server."""
    logger.info("Starting Finance MCP server...")
    try:
        # Use stdio transport for better integration with Cascade
        mcp.run(transport="stdio")
    except Exception as e:
        logger.error(f"Error running server: {e}")
    finally:
        logger.info("Server shutdown complete")

if __name__ == "__main__":
    run_server()
