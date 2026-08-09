"""FinMind MCP server entrypoint."""

from __future__ import annotations

import os

from fastmcp import FastMCP
from starlette.responses import JSONResponse

from finmind_mcp.client import FinMindClient
from finmind_mcp.tools import register_tools

mcp = FastMCP("FinMind Taiwan Market Data")
client = FinMindClient()
register_tools(mcp, client)


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    """Render-friendly health check that does not open an MCP stream."""
    return JSONResponse({"status": "healthy", "service": "finmind-mcp"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    if os.getenv("MCP_STDIO", "").lower() in {"1", "true", "yes"}:
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="http", host="0.0.0.0", port=port, path="/mcp")
