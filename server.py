"""FinMind MCP server entrypoint."""

from __future__ import annotations

import os

from fastmcp import FastMCP

from finmind_mcp.client import FinMindClient
from finmind_mcp.tools import register_tools

mcp = FastMCP("FinMind Taiwan Market Data")
client = FinMindClient()
register_tools(mcp, client)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    if os.getenv("MCP_STDIO", "").lower() in {"1", "true", "yes"}:
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="http", host="0.0.0.0", port=port)
