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

## Video Walkthrough

[![Build Your Own MCP Server: Practical Guide with Python SDK and Cursor IDE](https://img.youtube.com/vi/YNe5aYutEPU/0.jpg)](https://www.youtube.com/watch?v=YNe5aYutEPU)

**[Watch: Build Your Own MCP Server: Practical Guide with Python SDK and Cursor IDE](https://www.youtube.com/watch?v=YNe5aYutEPU)**

This video provides context and explanations that complement the code in this repository:

- See the MCP server in action with a practical demonstration in Cursor IDE
- Understand the design decisions behind the implementation
- Learn how the different components work together
- Get insights into how AI models discover and interact with custom tools

If you're looking to understand not just the "what" but the "why" behind this MCP implementation, the video offers a guided tour through the development process and explains the reasoning behind key architectural choices.

