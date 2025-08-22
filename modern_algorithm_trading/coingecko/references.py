COIN_IDS = [
    "bitcoin", "ethereum", "tether", "binancecoin", "solana",
    "ripple", "dogecoin", "tron", "cardano", "polkadot",
]

COINGECKO_RESOURCES = {
    "MARKET_CHART": "market_chart",
    "MARKET_CHART_RANGE": "market_chart/range",
    "OHLC": "ohlc",
    "TICKERS": "tickers",
    "HISTORY": "history",
}

# 지원되는 법정화폐 (일부 발췌, 실제는 더 많음)
COINGECKO_VS_CURRENCIES = [
    "usd", "eur", "krw", "jpy", "cny", "gbp",
    "btc", "eth", "usdt", "bnb"
]

COINGECKO_FILEDS = {
    "PRICES": "prices",
    "MARKET_CAP": "market_caps",
    "TOTAL_VOLUME": "total_volumes",
}

# days 파라미터 (market_chart에서 지원하는 기간)
# → 1 이하 = 5분봉, 90 이하 = 1시간봉, 그 이상 = 일봉
COINGECKO_DAYS_OPTIONS = {
    "1D": 1,
    "7D": 7,
    "14D": 14,
    "30D": 30,
    "90D": 90,
    "180D": 180,
    "1Y": 365,
    "MAX": "max"
}

# interval (market_chart/range에서 사용 가능)
COINGECKO_INTERVALS = [
    "5m",
    "hourly",
    "daily"
]