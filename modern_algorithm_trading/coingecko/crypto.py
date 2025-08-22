import pandas as pd
from functools import cached_property
from universal_timeseries_transformer import TimeseriesMatrix
from .coin_timeseries import get_prices


class Crypto:
    def __init__(self, tickers_crypto: list[str], ticker_fiat: str, days: str):
        self.tickers_crypto = tickers_crypto
        self.ticker_fiat = ticker_fiat
        self.days = days

    @cached_property
    def df(self) -> pd.DataFrame:
        prices = get_prices(tickers_crypto=self.tickers_crypto, ticker_fiat=self.ticker_fiat, days=self.days)
        prices = prices.ffill().dropna()
        mapping_rename = {col: col.split(': prices')[0] for col in prices.columns}
        prices = prices.rename(columns=mapping_rename)
        return prices

    @cached_property
    def tm(self) -> TimeseriesMatrix:
        return TimeseriesMatrix(df=self.df)
    
    @cached_property
    def prices(self) -> pd.DataFrame:
        return self.tm.df

    @cached_property
    def returns(self) -> pd.DataFrame:
        return self.tm.returns

    @cached_property
    def cumreturns(self) -> pd.DataFrame:
        return self.tm.cumreturns
    
