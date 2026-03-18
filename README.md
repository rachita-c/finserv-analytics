# FinServ Analytics

Internal portfolio analytics library used by the FinServ Co dashboard.

## Setup

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest tests/
```

## Modules

| Module | Description |
|--------|-------------|
| `analytics/portfolio.py` | Returns, Sharpe ratio, top holdings |
| `analytics/risk.py` | VaR, max drawdown |
| `analytics/formatters.py` | Percentage and currency formatting |
