"""Tests for portfolio analytics."""
import pytest
from analytics.portfolio import calculate_returns, sharpe_ratio, top_holdings


def test_calculate_returns_basic():
    prices = [100.0, 105.0, 110.25]
    returns = calculate_returns(prices)
    assert len(returns) == 2
    # 5% gain then 5% gain
    assert abs(returns[0] - 5.0) < 0.01, f"Expected ~5.0, got {returns[0]}"
    assert abs(returns[1] - 5.0) < 0.01, f"Expected ~5.0, got {returns[1]}"


def test_sharpe_ratio_zero_std():
    """Should return None (or some sensible value) when all returns are equal."""
    returns = [0.5, 0.5, 0.5, 0.5]
    result = sharpe_ratio(returns)
    # Should not raise ZeroDivisionError
    assert result is None or isinstance(result, float)


def test_top_holdings_returns_descending():
    portfolio = {"AAPL": 0.30, "MSFT": 0.25, "TSLA": 0.15, "NVDA": 0.20, "AMZN": 0.10}
    top = top_holdings(portfolio, n=3)
    values = [v for _, v in top]
    assert values == sorted(values, reverse=True), "Holdings should be in descending order"


def test_top_holdings_returns_correct_top_n():
    portfolio = {"AAPL": 0.30, "MSFT": 0.25, "TSLA": 0.15}
    top = top_holdings(portfolio, n=2)
    assert top == [("AAPL", 0.30), ("MSFT", 0.25)]
