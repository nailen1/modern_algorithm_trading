"""
Modern Algorithm Trading Module

A comprehensive module for algorithmic trading strategies and market data analysis.
Supports cryptocurrency and equity markets with various trading algorithms and data connectors.
"""

__version__ = "0.1.0"
__author__ = "Juneyoung Park"
__description__ = "Modern Algorithm Trading Module for Cryptocurrency and Equity Markets"

# Import main modules
from . import coingecko
from . import hantoo

# Version info
__all__ = [
    "coingecko",
    "hantoo",
    "__version__",
    "__author__",
    "__description__"
]
