import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import scipy.stats as stats
import openpyxl
import os
from pathlib import Path

SP500_daily_prices = '/Users/nuno/FinEdu/finEdu/files_excel/S_P 500 Index 2023-10-30 20_00_03.xlsx'
DJI_daily_prices = '/Users/nuno/FinEdu/finEdu/files_excel/Dow Jones Industrial Average (DJIA) 2023-10-30 20_05_10.xlsx'
NDQ_Comp_daily_prices = '/Users/nuno/FinEdu/finEdu/files_excel/Nasdaq Composite Index 2023-10-30 20_06_38.xlsx'
RUSSELL_2000_dialy_prices = '/Users/nuno/FinEdu/finEdu/files_excel/Russell 2000 Index 2023-10-31 20_13_04.xlsx'


def excel_to_csv(file, name: str):
    read_file = pd.read_excel(file)
    file_name = name + '.csv'

    read_file.to_csv(file_name, index=None, header=True)

    df = pd.DataFrame(pd.read_csv(file_name))

    return df

# excel_to_csv(RUSSELL_2000_dialy_prices, 'Russell2000 Daily Prices')

sp500_csv = '/Users/nuno/FinEdu/finEdu/files_csv/indexes/SP500 Daily Prices.csv'
dji_csv = '/Users/nuno/FinEdu/finEdu/files_csv/indexes/DJI Daily Prices.csv'
ndq_comp_csv = '/Users/nuno/FinEdu/finEdu/files_csv/indexes/NDQ Composite Daily Prices.csv'
russell_csv = '/Users/nuno/FinEdu/finEdu/files_csv/indexes/Russell2000 Daily Prices.csv'


def get_prices(file):
    prices = pd.read_csv(file, index_col=[0], parse_dates=[0])
    return prices['Value']

sp500_prices = get_prices(sp500_csv)
dji_prices = get_prices(dji_csv)
ndq_prices = get_prices(ndq_comp_csv)
russell_prices = get_prices(russell_csv)


# Normalized Returns (Price Based)
sp500_prices_norm = sp500_prices.div(sp500_prices.iloc[-1]).mul(100)
dji_prices_norm = dji_prices.div(dji_prices.iloc[-1]).mul(100)
ndq_prices_norm = ndq_prices.div(ndq_prices.iloc[-1]).mul(100)
russell_prices_norm = russell_prices.div(russell_prices.iloc[-1]).mul(100)

def export_normalized_data(data, name: str) -> None:
    filepath = Path(f'normalized_data_csv/{name}.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(filepath)
    

# export_normalized_data(sp500_prices_norm, 'sp500_prices_norm')
# export_normalized_data(dji_prices_norm, 'dji_prices_norm')
# export_normalized_data(ndq_prices_norm, 'ndq_prices_norm')
# export_normalized_data(russell_prices_norm, 'russell_prices_norm')

# Normalized Returns (CSVs)
sp500 = '/Users/nuno/FinEdu/normalized_data_csv/sp500_prices_norm.csv'
dji = '/Users/nuno/FinEdu/normalized_data_csv/dji_prices_norm.csv'
ndq = '/Users/nuno/FinEdu/normalized_data_csv/ndq_prices_norm.csv'
russell = '/Users/nuno/FinEdu/normalized_data_csv/russell_prices_norm.csv'
