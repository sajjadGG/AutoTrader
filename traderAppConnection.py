from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import MetaTrader5 as mt5

if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()


authorized=mt5.login(1818932 , password="ZZub4iw" ,server = "Alpari-nano")  # the terminal database password is applied if connection data is set to be remembered
if authorized:
    print("connected to account")
        # display trading account data 'as is'
    print(mt5.account_info())
    # display trading account data in the form of a list
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
