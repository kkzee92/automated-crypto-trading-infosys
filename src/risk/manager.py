import os
from typing import List
from ..strategies.base import Signal

class RiskManager:
    def __init__(self):
        self.max_position_pct = float(os.getenv("MAX_POSITION_PCT", "0.02"))
        self.max_daily_loss_pct = float(os.getenv("MAX_DAILY_LOSS_PCT", "0.05"))

    def approve(self, signals: List[Signal], portfolio_value: float) -> List[Signal]:
        approved = []
        for sig in signals:
            if sig.size_pct > self.max_position_pct:
                sig.size_pct = self.max_position_pct
                sig.rationale += " [size capped by risk manager]"
            # Additional checks (drawdown, correlation, liquidity) would go here
            approved.append(sig)
        return approved
