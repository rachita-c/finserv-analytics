"""Tests for risk module."""
import pytest
from analytics.risk import value_at_risk


def test_var_empty_list():
    """value_at_risk should handle an empty list gracefully."""
    result = value_at_risk([])
    assert result is None
