# QTS - Quantitative Trading System

## What This is
An AI-powered algorithmic tranding system build from scratch for US equities.
Methodologies: Quantitative / systematic / algorithmic. Built on Physics and Data science principals -
where every strategies must be hypothesised, backtested, statistically validated, and monitored before real
capital can be allocated

## Status
| Phase | Description | Status |
|---|---|---|
| Phase 1 | Core backtesting engine | In progress |
| Phase 2 | ML signal generation (Layer 1) | Not started |
| Phase 3 | LLM research agent (Layer 2) | Not started |
| Phase 4 | AI strategy generator (Layer 3) | Not started |
| Phase 5 | Multi-agent system (Layer 4) | Not started |
| Phase 6 | Autonomous pipeline (Layer 5) | Not started |

## Key Decisions
- Historical data: yfinance (free, end-of-day OHLCV)
- Paper + live trading: Alpaca API
- Database: SQLite via pandas
- Interval: daily (1d) to start
- Primary market: US equities
- LLM: Claude (Anthropic) or OpenAI for Layers 2–5

## Scaffold
```
QTS/
├── config/
│   ├── __init__.py
│   └── settings.py          # Central config — tickers, dates, paths, params
├── data/
│   ├── raw/                 # Downloaded OHLCV CSVs from yfinance
│   └── processed/           # Cleaned, validated data ready for engine
├── engine/
│   ├── data.py              # Fetch, clean, store market data
│   ├── signal.py            # Buy/sell/hold signal generation
│   ├── portfolio.py         # Capital allocation and position sizing
│   ├── execution.py         # Order simulation, slippage, commissions
│   └── analytics.py         # Performance metrics and reporting
├── layers/
│   ├── layer1_ml/           # ML signal models (XGBoost/LightGBM)
│   ├── layer2_llm/          # LLM research agent (news, filings, sentiment)
│   ├── layer3_agent/        # AI strategy generator loop
│   ├── layer4_multi/        # Multi-agent orchestration system
│   └── layer5_auto/         # Autonomous monitoring and self-improvement
├── logs/                    # Runtime logs
├── notebooks/               # Jupyter exploration only — no production logic
├── outputs/                 # Plots, reports, summaries
├── tests/                   # One test file per engine module
├── main.py                  # Entry point
└── .env                     # API keys — never committed to GitHub
```

## Golden Rules
1. No real capital until walk-forward analysis shows consistent positive Sharpe across all windows
2. Paper trade minimum 30 days before any live deployment
3. First live deployment uses maximum 10% of intended allocation
4. Every strategy needs 100+ backtest trades — smaller samples are statistically meaningless
5. Max drawdown above 20% = automatic rejection
6. Lookahead bias is the most dangerous mistake — all signals delayed by one bar