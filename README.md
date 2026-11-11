# Automated Cryptocurrency Trading Information System

**Educational & Research Framework** — Not financial advice. Use at your own risk. Cryptocurrency trading involves substantial risk of loss.

This repository provides a modular, security-first architecture for automated cryptocurrency trading information systems. It includes data ingestion pipelines, asset-class specific strategy modules, risk management, and cyber/data security controls.

## Key Features

- **Multi-source market data** (via CCXT and public APIs)
- **Asset-class tailored strategies**:
  - Large-cap (BTC/ETH): Momentum, trend-following
  - Mid/Alt-coins: Mean-reversion, volatility breakout
  - Memecoins / High-vol: Strict risk gates, sentiment overlays
  - Stablecoins: Arbitrage / yield monitoring (informational)
- **Security architecture**: Secure key handling, encryption helpers, audit logging, input validation, rate limiting patterns
- **Risk controls**: Position sizing, max drawdown stops, paper-trading mode by default
- **Backtesting hooks** and paper trading simulator

## Architecture Overview

```
├── data/          # Ingestion, normalization, caching
├── strategies/    # Per-asset-class strategy implementations
├── risk/          # Position sizing, circuit breakers
├── security/      # Key management, encryption, audit
├── execution/     # Paper trading / order simulation (live disabled by default)
└── main.py        # Orchestrator
```

See `docs/SECURITY.md` and `docs/ARCHITECTURE.md` for full details.

## Quick Start (Paper Trading Only)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp config/example.env .env
# Edit .env with read-only API keys if desired (never commit)
python src/main.py --mode paper
```

## Security Principles

- API keys stored only in environment variables or a secrets manager
- No hard-coded secrets
- All external inputs validated and sanitized
- Audit logs for all strategy decisions and order simulations
- Default to paper trading; live execution requires explicit enablement and additional safeguards
- Principle of least privilege for any connected accounts

## Disclaimer

This software is provided for educational and research purposes only. It does not constitute financial, investment, or trading advice. Past performance of any strategy is not indicative of future results. Cryptocurrency markets are highly volatile and can result in total loss of capital. Always conduct your own research and consult licensed professionals.

## License

MIT License
