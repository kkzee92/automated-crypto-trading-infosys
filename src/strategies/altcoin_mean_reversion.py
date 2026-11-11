from .base import BaseStrategy, Signal, SignalType

class AltcoinMeanReversionStrategy(BaseStrategy):
    """RSI-based mean reversion for higher-volatility altcoins."""
    name = "altcoin_mean_reversion"
    asset_class = "altcoin"

    def generate_signal(self, market_data: dict) -> Signal:
        rsi = market_data.get("rsi_14", 50)
        symbol = market_data.get("symbol", "ETH/USDT")

        if rsi < 30:
            return Signal(
                asset=symbol,
                signal=SignalType.BUY,
                size_pct=0.005,  # smaller size for higher risk
                rationale=f"RSI oversold at {rsi}",
                confidence=0.55,
                asset_class=self.asset_class
            )
        elif rsi > 70:
            return Signal(
                asset=symbol,
                signal=SignalType.SELL,
                size_pct=0.005,
                rationale=f"RSI overbought at {rsi}",
                confidence=0.55,
                asset_class=self.asset_class
            )
        return Signal(
            asset=symbol,
            signal=SignalType.HOLD,
            size_pct=0.0,
            rationale="RSI neutral",
            confidence=0.4,
            asset_class=self.asset_class
        )
