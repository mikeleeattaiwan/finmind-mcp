"""FinMind MCP server entrypoint."""

from __future__ import annotations

import os

import uvicorn
from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

from finmind_mcp.client import FinMindClient
from finmind_mcp.tools import register_tools

mcp = FastMCP("FinMind Taiwan Market Data")
client = FinMindClient()
register_tools(mcp, client)

mcp_app = mcp.http_app(path="/mcp")


async def health_check(request):
    """Render-friendly health check that does not open an MCP stream."""
    return JSONResponse({"status": "healthy", "service": "finmind-mcp"})


app = Starlette(
    routes=[
        Route("/health", health_check, methods=["GET"]),
        Mount("/", app=mcp_app),
    ],
    lifespan=mcp_app.lifespan,
)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    if os.getenv("MCP_STDIO", "").lower() in {"1", "true", "yes"}:
        mcp.run(transport="stdio")
    else:
        uvicorn.run(app, host="0.0.0.0", port=port)
