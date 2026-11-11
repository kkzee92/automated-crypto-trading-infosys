#!/usr/bin/env python3
"""
Orchestrator for the Automated Crypto Trading Information System.
Default mode: paper trading only.
"""

import os
import argparse
from dotenv import load_dotenv
import structlog

load_dotenv()

logger = structlog.get_logger()

def main():
    parser = argparse.ArgumentParser(description="Crypto Trading Information System")
    parser.add_argument("--mode", choices=["paper", "backtest", "live"], default="paper")
    args = parser.parse_args()

    live_enabled = os.getenv("LIVE_TRADING", "false").lower() == "true"

    if args.mode == "live" and not live_enabled:
        logger.error("Live trading is disabled. Set LIVE_TRADING=true and implement additional safeguards.")
        return

    logger.info("Starting system", mode=args.mode, live_enabled=live_enabled)
    # TODO: Wire up data ingestion, strategy selection by asset class, risk checks, and paper execution
    print("System skeleton ready. Implement strategy modules and data feeds next.")
    print("See strategies/ and docs/ for guidance.")

if __name__ == "__main__":
    main()
