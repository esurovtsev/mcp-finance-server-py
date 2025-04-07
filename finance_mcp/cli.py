#!/usr/bin/env python3

"""
Command-line interface for the Finance MCP server.
"""

import argparse
import sys
from finance_mcp.server import run_server


def main():
    """
    Main entry point for the Finance MCP server CLI.
    """
    parser = argparse.ArgumentParser(description="Finance MCP Server")
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show version information and exit"
    )
    
    # Add more command-line arguments here as needed
    # For example, you might want to add options for API keys or other configuration
    
    args = parser.parse_args()
    
    if args.version:
        from finance_mcp import __version__
        print(f"Finance MCP Server version {__version__}")
        sys.exit(0)
    
    # Run the server
    run_server()


if __name__ == "__main__":
    main()
