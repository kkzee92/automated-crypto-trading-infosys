from enum import Enum
from dataclasses import dataclass
from typing import Optional

class SignalType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

@dataclass
class Signal:
    asset: str
    signal: SignalType
    size_pct: float  # fraction of available capital
    rationale: str
    confidence: float  # 0.0 - 1.0
    asset_class: str

class BaseStrategy:
    """Common interface for all asset-class strategies."""
    name: str = "base"
    asset_class: str = "generic"

    def generate_signal(self, market_data: dict) -> Optional[Signal]:
        raise NotImplementedError
