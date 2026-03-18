"""Output formatting utilities."""
from __future__ import annotations


def format_pct(value: float, decimals: int = 2) -> str:
    """Format a decimal as a percentage string.

    Bug: the function receives values already in percent form (e.g. 5.3 meaning 5.3%)
    but multiplies by 100 again, producing wrong output like "530.00%".
    """
    return f"{value * 100:.{decimals}f}%"   # BUG: value is already in percent form


def format_currency(amount: float, symbol: str = "$") -> str:
    """Format a number as currency."""
    return f"{symbol}{amount:,.2f}"


def format_ratio(value: float, decimals: int = 3) -> str:
    return f"{value:.{decimals}f}x"
