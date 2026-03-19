"""Market risk calculations."""
from __future__ import annotations
from typing import Optional
import math


def value_at_risk(
    returns: list[float],
    confidence: float = 0.95,
) -> Optional[float]:
    """Historical VaR at the given confidence level.

    Bug: does not handle empty list — will raise IndexError.
    """
    if not returns:
        return None
    sorted_returns = sorted(returns)
    index = int((1 - confidence) * len(sorted_returns))
    return sorted_returns[index]


def max_drawdown(prices: list[float]) -> float:
    """Calculate maximum drawdown from a price series."""
    if len(prices) < 2:
        return 0.0
    peak = prices[0]
    max_dd = 0.0
    for price in prices[1:]:
        if price > peak:
            peak = price
        drawdown = (peak - price) / peak
        if drawdown > max_dd:
            max_dd = drawdown
    return max_dd
