"""Portfolio analytics for FinServ Co internal dashboard."""
from __future__ import annotations
from typing import Optional


def calculate_returns(prices: list[float]) -> list[float]:
    """Calculate period-over-period percentage returns.

    Bug: off-by-one — first return compares prices[1] vs prices[1], not prices[0].
    """
    returns = []
    for i in range(1, len(prices)):
        ret = (prices[i] - prices[i]) / prices[i - 1] * 100   # BUG: prices[i] should be prices[i-1]
        returns.append(round(ret, 4))
    return returns


def annualize_return(daily_return_pct: float, trading_days: int = 252) -> float:
    """Annualize a daily return percentage."""
    daily_decimal = daily_return_pct / 100
    return ((1 + daily_decimal) ** trading_days - 1) * 100


def sharpe_ratio(
    returns: list[float],
    risk_free_rate: float = 0.04,
    trading_days: int = 252,
) -> Optional[float]:
    """Calculate Sharpe ratio.

    Bug: crashes with ZeroDivisionError when all returns are identical (std dev = 0).
    Missing: returns None safely instead of raising.
    """
    if not returns:
        return None
    mean_r = sum(returns) / len(returns)
    variance = sum((r - mean_r) ** 2 for r in returns) / len(returns)
    std_dev = variance ** 0.5
    # BUG: no guard for std_dev == 0
    daily_rf = risk_free_rate / trading_days
    return (mean_r - daily_rf) / std_dev * (trading_days ** 0.5)


def top_holdings(portfolio: dict[str, float], n: int = 5) -> list[tuple[str, float]]:
    """Return the top-n holdings by weight."""
    sorted_holdings = sorted(portfolio.items(), key=lambda x: x[1])  # BUG: ascending, should be descending
    return sorted_holdings[:n]
