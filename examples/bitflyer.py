#!/usr/bin/env python3
from cryptofeed import FeedHandler
from cryptofeed.defines import TRADES

from asyncio_quant_tick.exchanges import Bitflyer
from asyncio_quant_tick.trades import (
    CandleCallback,
    NonSequentialIntegerTradeCallback,
    SignificantTradeCallback,
)


async def candles(candle: dict, timestamp: float) -> None:
    """Candles."""
    print(candle)


if __name__ == "__main__":
    fh = FeedHandler()
    fh.add_feed(
        Bitflyer(
            symbols=["BTC/JPY"],
            channels=[TRADES],
            callbacks={
                TRADES: NonSequentialIntegerTradeCallback(
                    SignificantTradeCallback(
                        CandleCallback(candles, window_seconds=60),
                        significant_trade_filter=100_000,
                        window_seconds=60,
                    )
                )
            },
        )
    )
    fh.run()
