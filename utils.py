import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from backtesting import Strategy, Backtest
from backtesting.lib import crossover

import tulipy as ti


def print_indicator_info(indicator):
    print("Type:", indicator.type)
    print("Full Name:", indicator.full_name)
    print("Inputs:", indicator.inputs)
    print("Options:", indicator.options)
    print("Outputs:", indicator.outputs)


def get_data(start_date, end_date, name="DEXJPUS", data_source="fred"):
    from pandas_datareader import data

    return data.DataReader(name, data_source, start_date, end_Date)


def string_mt5_timeframe(timeframe):
    """return mt5.TIMEFRAME object from timeframe

    Args:
        timeframe (str): it can be 'D1','H1','H12','H2','H3','H4','H6','H8','M1','M10','M12','M15','M2','M20','M3','M30','M4','M5','M6','MN1','W1'

    """
    import MetaTrader5 import mt5
    return getattr(mt5,'TIMEFRAME_'+timeframe)
    
    



def get_meta_trader_date(start_date=None, end_date=None, pair='EURUSD',timeframe='D1',timezone="Etc/UTC",
    renamedic = {
        'open' : 'Open' ,
        'high' : 'High' ,
        'low'  : 'Low' ,
        'close': 'Close'}):

    from MetaTrader5 import mt5
    from datetime import datetime,timedelta
    import pytz

    if not mt5.initialize():
        print("initialize failed")
        mt5.shutdown()

    timezone = pytz.timezone(timezone)
    if start_date is None:
        start_Date = datetime(2006, 1, 1, tzinfo=timezone)
    if end_date is None:
        end_date = datetime(2020, 9, 27, tzinfo=timezone)

    rates = mt5.copy_rates_range(pair,string_mt5_timeframe(timeframe),start_date,end_date)
    mt5.shutdown()
    rates_frame = pd.DataFrame(rates)
    rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
    print("received date from {} to {}".format(min(rates_frame['time']) , max(rates_frame['time'])))
    print("length is {}".format(len(rates_frame)))


    return rates_frame