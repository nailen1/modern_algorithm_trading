

MAPPING_TICKERS_CRYPTO = {
    'BTC': 'bitcoin',
    'ETH': 'ethereum',
    'SUI': 'sui',
    'USDT': 'tether',
    'BNB': 'binancecoin',
    'SOL': 'solana',
    'XRP': 'ripple',
    'ADA': 'cardano',
}

MAPPING_TICKERS_FIAT = {
    'USD': 'usd',
    'KRW': 'krw',
    'EUR': 'eur',
    'JPY': 'jpy',
    'CNY': 'cny',
    'GBP': 'gbp',
    'BTC': 'btc',
    'ETH': 'eth',
    'SUI': 'sui',
    'USDT': 'usdt',
    'BNB': 'bnb',
    'SOL': 'sol',
    'XRP': 'xrp',
    'ADA': 'ada',
}

INVERSE_MAPPING_TICKERS_CRYPTO = {v: k for k, v in MAPPING_TICKERS_CRYPTO.items()}
INVERSE_MAPPING_TICKERS_FIAT = {v: k for k, v in MAPPING_TICKERS_FIAT.items()}
