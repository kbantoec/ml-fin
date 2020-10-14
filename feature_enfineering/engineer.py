import pandas as pd
import talib as ta
from typing import List


class FeatureEngineer:
    def __init__(self, df):
        assert isinstance(df, pd.DataFrame), f"Pass an 'pandas.DataFrame', not {type(df).__name__!r}."
        self.df = df
        self.__metrics: dict = {'SMA': ta.SMA, 'RSI': ta.RSI}

    def create_moving_averages(self, ma_periods: List[int], colnames: List[str]) -> None:
        """Creates Moving Averages from columns of a pandas DataFrame.

        Parameters
        ----------
        ma_periods : List[int]
            List of time periods (int) to build moving averages upon.
            For example: [14, 30, 50]

        colnames : List[str]
            List of column names from which we want to create moving averages.
        """
        for t in ma_periods:
            for colname in colnames:
                self.df[f"ma_{t}"] = ta.SMA(self.df[colname].to_numpy(), timeperiod=t) / self.df[colname]

    def create_rsi(self, rsi_periods: List[int], colnames: List[str]) -> None:
        """Creates RSI signals from columns of a pandas DataFrame.

        Parameters
        ----------
        rsi_periods : List[int]
            List of time periods (int) to build RSI signals upon.
            For example: [14, 30, 50]

        colnames : List[str]
            List of column names from which we want to create moving averages.
        """
        self.__assert_type(rsi_periods, list)
        self.__assert_type(colnames, list)

        for t in rsi_periods:
            for colname in colnames:
                self.df[f"rsi_{t}"] = ta.RSI(self.df[colname].to_numpy(), timeperiod=t)

    @staticmethod
    def __assert_type(inp, type):
        assert isinstance(inp, type), f"Pass a input of type {type.__name__!r}, not {type(inp).__name__}."


if __name__ == '__main__':
    aapl = pd.read_csv('../data/AAPL.csv')
    fe = FeatureEngineer(aapl)
    fe.create_moving_averages([14, 20], colnames=['Close'])