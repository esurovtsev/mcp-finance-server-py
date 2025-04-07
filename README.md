# Finance MCP Server

A minimal MCP server built with Python that exposes two example tools: one to convert a company name into a stock symbol, and another to fetch financial data from Yahoo Finance. The project focuses on learning how to build and run an MCP server—using a simple financial scenario purely as a demo use case.

## Installation

### Development Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mcp-finance-server-py.git
cd mcp-finance-server-py

# Install in development mode
uv pip install -e .
```

### Production Installation

```bash
uv pip install finance-mcp
```

## Usage

### Running the Server Directly

```bash
finance-mcp
```

### Configuration with Claude Desktop or other MCP clients

Add this to your MCP configuration file (e.g., `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "finance-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/mcp-finance-server-py", // Update this path
        "run",
        "finance-mcp"
      ]
    }
  }
}
```

