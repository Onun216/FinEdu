import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import scipy.stats as stats

Brent_daily_prices = '/Users/nuno/FinEdu/finEdu/files_excel/Brent Crude Oil 2023-10-30 20_08_52.xlsx'



def excel_to_csv(file, name: str):
    read_file = pd.read_excel(file)
    file_name = name + '.csv'

    read_file.to_csv(file_name, index=None, header=True)

    df = pd.DataFrame(pd.read_csv(file_name))

    return df


def get_prices(file):
    prices = pd.read_csv(file, index_col=[0], parse_dates=[0])
    return prices['Value']

brent_prices = get_prices(brent_csv)

brent_prices_norm = brent_prices.div(brent_prices.iloc[-1]).mul(100)