"""MCP tool registration for FinMind datasets."""

from __future__ import annotations

import json
from typing import Any

from fastmcp import FastMCP

from .client import FinMindClient


def _compact_response(dataset: str, payload: dict[str, Any]) -> str:
    """Return compact, predictable JSON text for MCP clients."""
    data = payload.get("data", [])
    response = {
        "dataset": dataset,
        "status": payload.get("status"),
        "msg": payload.get("msg"),
        "count": len(data) if isinstance(data, list) else None,
        "data": data,
    }
    return json.dumps(response, ensure_ascii=False, separators=(",", ":"))


def register_tools(mcp: FastMCP, client: FinMindClient | None = None) -> None:
    """Register all FinMind MCP tools."""
    finmind = client or FinMindClient()

    @mcp.tool
    def get_taiwan_stock_price(data_id: str, start_date: str, end_date: str = "") -> str:
        """查詢台股個股日成交資訊（日 K / OHLCV）。

        Args:
            data_id: 股票代號，例如 "2330"、"5274"
            start_date: 起始日期，格式 YYYY-MM-DD
            end_date: 結束日期，格式 YYYY-MM-DD；空白則由 FinMind 使用預設
        """
        dataset = "TaiwanStockPrice"
        payload = finmind.data(dataset, data_id=data_id, start_date=start_date, end_date=end_date)
        return _compact_response(dataset, payload)

    @mcp.tool
    def get_taiwan_stock_month_revenue(data_id: str, start_date: str, end_date: str = "") -> str:
        """查詢台股月營收。

        Args:
            data_id: 股票代號，例如 "2330"
            start_date: 起始日期，格式 YYYY-MM-DD
            end_date: 結束日期，格式 YYYY-MM-DD；空白則由 FinMind 使用預設
        """
        dataset = "TaiwanStockMonthRevenue"
        payload = finmind.data(dataset, data_id=data_id, start_date=start_date, end_date=end_date)
        return _compact_response(dataset, payload)

    @mcp.tool
    def get_taiwan_stock_institutional_investors(
        data_id: str,
        start_date: str,
        end_date: str = "",
    ) -> str:
        """查詢台股三大法人買賣超。

        Args:
            data_id: 股票代號，例如 "2330"
            start_date: 起始日期，格式 YYYY-MM-DD
            end_date: 結束日期，格式 YYYY-MM-DD；空白則由 FinMind 使用預設
        """
        dataset = "TaiwanStockInstitutionalInvestorsBuySell"
        payload = finmind.data(dataset, data_id=data_id, start_date=start_date, end_date=end_date)
        return _compact_response(dataset, payload)

    @mcp.tool
    def get_taiwan_stock_margin_purchase_short_sale(
        data_id: str,
        start_date: str,
        end_date: str = "",
    ) -> str:
        """查詢台股融資融券餘額。

        Args:
            data_id: 股票代號，例如 "2330"
            start_date: 起始日期，格式 YYYY-MM-DD
            end_date: 結束日期，格式 YYYY-MM-DD；空白則由 FinMind 使用預設
        """
        dataset = "TaiwanStockMarginPurchaseShortSale"
        payload = finmind.data(dataset, data_id=data_id, start_date=start_date, end_date=end_date)
        return _compact_response(dataset, payload)

    @mcp.tool
    def get_taiwan_stock_dividend(data_id: str, start_date: str = "", end_date: str = "") -> str:
        """查詢台股股利資料。

        Args:
            data_id: 股票代號，例如 "2330"
            start_date: 起始日期，格式 YYYY-MM-DD；可空白
            end_date: 結束日期，格式 YYYY-MM-DD；可空白
        """
        dataset = "TaiwanStockDividend"
        payload = finmind.data(dataset, data_id=data_id, start_date=start_date, end_date=end_date)
        return _compact_response(dataset, payload)

    @mcp.tool
    def get_taiwan_stock_financial_statement(
        data_id: str,
        start_date: str,
        end_date: str = "",
    ) -> str:
        """查詢台股財報資料。

        Args:
            data_id: 股票代號，例如 "2330"
            start_date: 起始日期，格式 YYYY-MM-DD
            end_date: 結束日期，格式 YYYY-MM-DD；空白則由 FinMind 使用預設
        """
        dataset = "TaiwanStockFinancialStatements"
        payload = finmind.data(dataset, data_id=data_id, start_date=start_date, end_date=end_date)
        return _compact_response(dataset, payload)

    @mcp.tool
    def get_finmind_dataset(
        dataset: str,
        data_id: str = "",
        start_date: str = "",
        end_date: str = "",
    ) -> str:
        """查詢任意 FinMind dataset。

        Args:
            dataset: FinMind dataset 名稱，例如 "TaiwanStockPrice"
            data_id: 資料代號，例如股票代號；可空白
            start_date: 起始日期，格式 YYYY-MM-DD；可空白
            end_date: 結束日期，格式 YYYY-MM-DD；可空白
        """
        payload = finmind.data(dataset, data_id=data_id, start_date=start_date, end_date=end_date)
        return _compact_response(dataset, payload)

    @mcp.tool
    def get_finmind_datalist(dataset: str, data_id: str = "") -> str:
        """查詢 FinMind dataset 可用參數清單。

        Args:
            dataset: FinMind dataset 名稱
            data_id: 資料代號；可空白
        """
        payload = finmind.datalist(dataset, data_id=data_id)
        return _compact_response(dataset, payload)
