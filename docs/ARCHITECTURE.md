# System Architecture

## Data Layer
- Uses CCXT for unified exchange access (spot markets).
- Normalized OHLCV, order book snapshots, and ticker data.
- Optional on-chain metrics via public APIs (placeholder).

## Strategy Layer
Strategies are organized by asset class:

| Asset Class       | Example Strategies                  | Risk Profile |
|-------------------|-------------------------------------|--------------|
| Large-cap (BTC/ETH) | Momentum, EMA crossover, breakout | Moderate    |
| Altcoins          | Mean-reversion, RSI extremes       | Higher      |
| Memecoins         | Strict volume/liquidity filters    | Very high   |
| Stablecoins       | Cross-exchange spread monitoring   | Low         |

Each strategy implements a common interface returning a Signal (BUY/SELL/HOLD + size + rationale).

## Risk Layer
- Position sizing via fixed fractional or volatility targeting.
- Hard stops on daily loss and max exposure.
- Correlation checks across assets.

## Security Layer
- See SECURITY.md.

## Execution Layer
- Paper trading by default: simulates fills against current mid-price with configurable slippage.
- Live execution path exists but is gated and requires explicit configuration + additional checks.
