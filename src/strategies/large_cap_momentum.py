from .base import BaseStrategy, Signal, SignalType

class LargeCapMomentumStrategy(BaseStrategy):
    """Simple EMA crossover momentum strategy suitable for BTC/ETH."""
    name = "large_cap_momentum"
    asset_class = "large_cap"

    def generate_signal(self, market_data: dict) -> Signal:
        # Placeholder logic — replace with real indicator calculation
        price = market_data.get("close", 0)
        ema_fast = market_data.get("ema_12", price)
        ema_slow = market_data.get("ema_26", price)

        if ema_fast > ema_slow * 1.002:
            return Signal(
                asset=market_data.get("symbol", "BTC/USDT"),
                signal=SignalType.BUY,
                size_pct=0.01,
                rationale="Fast EMA crossed above slow EMA",
                confidence=0.65,
                asset_class=self.asset_class
            )
        elif ema_fast < ema_slow * 0.998:
            return Signal(
                asset=market_data.get("symbol", "BTC/USDT"),
                signal=SignalType.SELL,
                size_pct=0.01,
                rationale="Fast EMA crossed below slow EMA",
                confidence=0.60,
                asset_class=self.asset_class
            )
        return Signal(
            asset=market_data.get("symbol", "BTC/USDT"),
            signal=SignalType.HOLD,
            size_pct=0.0,
            rationale="No clear momentum signal",
            confidence=0.5,
            asset_class=self.asset_class
        )
