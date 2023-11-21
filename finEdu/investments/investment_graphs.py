from finEdu.finData.index_info import sp500_prices, dji_prices, ndq_prices, russell_prices
from finEdu.finData.index_info import sp500, dji, ndq, russell
import numpy as np
import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib
import json
import plotly
import plotly.graph_objects as go
import seaborn as sb

sb.set_style('darkgrid')


def sp500_prices_graph():
    plt.clf()
    sp500_prices.plot(figsize=(15, 8), fontsize=13)
    plt.title('SP500', fontsize=15)
    plt.xlabel("Anos", fontsize=12)
    plt.ylabel("Preço (em USD)", fontsize=12)
    plt.savefig('/Users/nuno/FinEdu/finEdu/static/img/sp500_daily_prices.png')


def dji_prices_graph():
    plt.clf()
    dji_prices.plot(figsize=(15, 8), fontsize=13)
    plt.title('DowJones Industrial', fontsize=15)
    plt.xlabel("Anos", fontsize=12)
    plt.ylabel("Preço (em USD)", fontsize=12)
    plt.savefig('/Users/nuno/FinEdu/finEdu/static/img/dji_daily_prices.png')


def ndq_comp_prices_graph():
    plt.clf()
    ndq_prices.plot(figsize=(15, 8), fontsize=13)
    plt.title('Nasdaq Composite', fontsize=15)
    plt.xlabel("Anos", fontsize=12)
    plt.ylabel("Preço (em USD)", fontsize=12)
    plt.savefig('/Users/nuno/FinEdu/finEdu/static/img/ndq_comp_daily_prices.png')


def russell_prices_graph():
    plt.clf()
    russell_prices.plot(figsize=(15, 8), fontsize=13)
    plt.title('Russell 2000', fontsize=15)
    plt.xlabel("Anos", fontsize=12)
    plt.ylabel("Preço (em USD)", fontsize=12)
    plt.savefig(
        '/Users/nuno/FinEdu/finEdu/static/img/russell_2000_daily_prices.png')

def sp500_norm():
    df = pd.read_csv('/Users/nuno/FinEdu/normalized_data_csv/sp500_prices_norm.csv')
    fig = go.Figure([go.Scatter(x=df['Date'], y=df['Value'])])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def sp500_norm_comp():
    csv_file_paths = [sp500, dji, ndq, russell]
    dataframes = []
    for csv_file_path in csv_file_paths:
        dataframes.append(pd.read_csv(csv_file_path))
    
    traces = []
    legend_labels = ['sp500', 'DowJones', 'Nasdaq', 'Russell2000']
    i = 0
    for dataframe in dataframes:
        trace = go.Scatter(
            x=dataframe['Date'],
            y=dataframe['Value'],
            name=legend_labels[i],
        )
        traces.append(trace)
        i += 1
    
    fig = go.Figure()
    for trace in traces:
        fig.add_trace(trace)
    
    fig.update_layout(
        title='',
        xaxis_title='Data',
        yaxis_title='Retorno %',
        legend_title=''
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
