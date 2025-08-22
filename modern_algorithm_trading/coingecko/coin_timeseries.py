from functools import partial, reduce
import requests
import pandas as pd
from urllib.parse import quote
from universal_timeseries_transformer import transform_timeseries
from .consts import COINGECKO_APIBASE_URL
from .basis import fetch_coingecko_response, map_response_to_data

def build_coingecko_url(coin_id: str, resource: str) -> str:
    return f"{COINGECKO_APIBASE_URL}/{quote(coin_id)}/{quote(resource)}"

def build_api_params(vs_currency: str, days: int | str, interval: str | None = None) -> dict:
    params = {"vs_currency": vs_currency, "days": days}
    if interval:
        params["interval"] = interval
    return params

def fetch_data_market_chart(coin_id: str, vs_currency: str, days: int | str) -> requests.Response:
    url = build_coingecko_url(coin_id, "market_chart")
    params = build_api_params(vs_currency, days)
    response = fetch_coingecko_response(url, params)
    return map_response_to_data(response)

def fetch_data_market_chart_range(coin_id: str, vs_currency: str, days: int | str, interval: str | None = None) -> requests.Response:
    url = build_coingecko_url(coin_id, "market_chart/range")
    params = build_api_params(vs_currency, days, interval)
    response = fetch_coingecko_response(url, params)
    return map_response_to_data(response)

def map_data_and_field_to_transformed_timeseries(data: dict, field: str) -> pd.DataFrame:
    df = pd.DataFrame(data[field]).rename(columns={0: 'timestamp', 1: field}).set_index('timestamp')
    return transform_timeseries(df, option_type='datetime')

def map_id_to_transformed_timeseries(coin_id: str, vs_currency: str, days: int | str) -> pd.DataFrame:
    data = fetch_data_market_chart(coin_id, vs_currency, days)
    prices = map_data_and_field_to_transformed_timeseries(data, 'prices')
    caps = map_data_and_field_to_transformed_timeseries(data, 'market_caps')
    volumes = map_data_and_field_to_transformed_timeseries(data, 'total_volumes')
    return reduce(lambda x, y: x.join(y, how='outer'), [prices, caps, volumes])

def map_id_and_field_to_transformed_timeseries(coin_id: str, field: str, vs_currency: str, days: int | str) -> pd.DataFrame:
    data = fetch_data_market_chart(coin_id, vs_currency, days)
    return map_data_and_field_to_transformed_timeseries(data, field)

def map_id_and_field_and_interval_to_transformed_timeseries(coin_id: str, field: str, vs_currency: str, interval: str, days: int | str) -> pd.DataFrame:
    data = fetch_data_market_chart_range(coin_id, vs_currency, days, interval)
    return map_data_and_field_to_transformed_timeseries(data, field)

get_timeseries_coin = map_id_and_field_to_transformed_timeseries
get_timeseries_crypto = get_timeseries_coin

get_timeserieses_coin = map_id_to_transformed_timeseries
get_timeserieses_crypto = get_timeserieses_coin


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

get_canonical_column_name = lambda ticker_fiat, ticker_crypto, field: f'{ticker_fiat}_{ticker_crypto}: {field}'

def get_triple(ticker_crypto: str, ticker_fiat: str, days: str) -> pd.DataFrame:
    df = map_id_to_transformed_timeseries(coin_id=MAPPING_TICKERS_CRYPTO[ticker_crypto], vs_currency=MAPPING_TICKERS_FIAT[ticker_fiat], days=days)
    mapping_rename = {col: get_canonical_column_name(ticker_fiat=ticker_fiat, ticker_crypto=ticker_crypto, field=col) for col in df.columns}
    return df.rename(columns=mapping_rename)

def get_single(ticker_crypto: str, ticker_fiat: str, field: str, days: str) -> pd.DataFrame:
    df = map_id_and_field_to_transformed_timeseries(coin_id=MAPPING_TICKERS_CRYPTO[ticker_crypto], field=field, vs_currency=MAPPING_TICKERS_FIAT[ticker_fiat], days=days)
    mapping_rename = {col: get_canonical_column_name(ticker_fiat=ticker_fiat, ticker_crypto=ticker_crypto, field=col) for col in df.columns}
    return df.rename(columns=mapping_rename)

get_price = partial(get_single, field='prices')
get_cap = partial(get_single, field='market_caps')
get_volume = partial(get_single, field='total_volumes')

def get_singles(tickers_crypto: list[str], ticker_fiat: str, field: str, days: str) -> pd.DataFrame:
    return reduce(lambda x, y: x.join(y, how='outer'), [get_single(ticker_crypto=ticker_crypto, ticker_fiat=ticker_fiat, field=field, days=days) for ticker_crypto in tickers_crypto])

get_prices = partial(get_singles, field='prices')
get_caps = partial(get_singles, field='market_caps')
get_volumes = partial(get_singles, field='total_volumes')