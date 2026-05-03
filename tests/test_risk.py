"""Tests for risk module."""
import pytest
from analytics.risk import value_at_risk


def test_var_empty_list():
    """value_at_risk should handle an empty list gracefully."""
    result = value_at_risk([])
    assert result is None


def test_max_drawdown_single_price_returns_zero():
    """max_drawdown should be zero when there is not enough data."""
    from analytics.risk import max_drawdown

    assert max_drawdown([100.0]) == 0.0
