import numpy as np
import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib
import json
import plotly
import plotly.graph_objects as go


from finEdu import app
from flask import render_template, request, redirect, url_for, flash, jsonify
from finEdu.investments.investment_graphs import sp500_prices_graph, dji_prices_graph,  ndq_comp_prices_graph, russell_prices_graph
from finEdu.investments.investment_graphs import sp500_norm, sp500_norm_comp


matplotlib.use('agg')


@app.route('/investments', methods=['GET', 'POST'])
def investments():

    return render_template('investments/investments.html')


@app.route('/stocks', methods=['GET', 'POST'])
def stocks():

    return render_template('investments/stocks.html')


@app.route('/index-performance', methods=['GET', 'POST'])
def index_performance():

    if request.method == 'GET':
        np.set_printoptions(precision=4, suppress=True)
        plot_sp500_prices = sp500_prices_graph()
        plot_dji_prices = dji_prices_graph()
        plot_ndq_prices = ndq_comp_prices_graph()
        plot_russell_prices = russell_prices_graph()

        plot_urls = [plot_sp500_prices, plot_dji_prices,
                     plot_ndq_prices, plot_russell_prices]

    return render_template('investments/index-stats.html', plot_urls=plot_urls)


@app.route('/sp500', methods=['GET', 'POST'])
def sp500():
    if request.method == 'GET':
        norm_graph = sp500_norm()
        comp_norm_graph = sp500_norm_comp()
       
    return render_template('investments/sp500.html', norm_graph=norm_graph, 
                        comp_norm_graph=comp_norm_graph)
