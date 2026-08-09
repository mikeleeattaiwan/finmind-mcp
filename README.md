# FinMind MCP

FinMind MCP server for Taiwan market data.

This project wraps the FinMind v4 data API as MCP tools so ChatGPT, Codex, or other MCP clients can query Taiwan stock datasets through a consistent interface.

## Features

Initial tools:

- `get_taiwan_stock_price` — Taiwan stock daily OHLCV
- `get_taiwan_stock_month_revenue` — monthly revenue
- `get_taiwan_stock_institutional_investors` — institutional investors buy/sell
- `get_taiwan_stock_margin_purchase_short_sale` — margin purchase and short sale
- `get_taiwan_stock_dividend` — dividend data
- `get_taiwan_stock_financial_statement` — financial statement data
- `get_finmind_dataset` — generic FinMind dataset query
- `get_finmind_datalist` — generic FinMind datalist query

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
```

Set your FinMind token:

```bash
export FINMIND_TOKEN="your-token"
```

FinMind can be called without a token, but using a token increases the official request quota.

## Run

HTTP transport:

```bash
python server.py
```

Default port is `8000`. Override with:

```bash
PORT=8787 python server.py
```

Stdio transport:

```bash
MCP_STDIO=1 python server.py
```

## Example tool arguments

```json
{
  "data_id": "2330",
  "start_date": "2026-01-01",
  "end_date": "2026-01-31"
}
```

## Docker

```bash
docker build -t finmind-mcp .
docker run --rm -p 8000:8000 -e FINMIND_TOKEN="$FINMIND_TOKEN" finmind-mcp
```

## Notes

- The server uses FinMind API v4 endpoints.
- `FINMIND_TOKEN` is read from the environment and is never committed.
- Tool responses are compact JSON strings with `dataset`, `count`, and `data` fields.
