"""Tests for risk module."""
import pytest
from analytics.risk import value_at_risk


def test_var_empty_list():
    """value_at_risk should handle an empty list gracefully."""
    result = value_at_risk([])
    assert result is None


def test_var_normal_returns():
    """value_at_risk should return the correct VaR for a non-empty list."""
    returns = [-0.05, -0.03, -0.01, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14]
    result = value_at_risk(returns, confidence=0.95)
    assert result is not None
    assert result == -0.05
