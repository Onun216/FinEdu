import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import matplotlib
import jinja2

from finEdu import app
from flask import render_template, request, redirect, url_for, flash

from finEdu.banking.forms import MortgageForm, MortgageDataForm

from finEdu.banking.banking_formulas import loan_terms, amort_interest
from finEdu.banking.banking_formulas import pmt, group_by_period, amort_interest
from finEdu.banking.banking_formulas import sum_by_group, yearly_cost_increases
from finEdu.banking.banking_formulas import annual_payments, sum_loan_values

from finEdu.banking.banking_graphs import mortgage_example

# Para evitar o erro "UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail."
matplotlib.use('agg')

@app.route('/banking', methods=['GET', 'POST'])
def banking():
    form = MortgageForm(request.form)
    if request.method == 'GET':
        return render_template('banking/banking.html', form=form)

    else:
        purchase_price = form.purchase_price.data
        max_loan = form.max_loan.data
        interest_rate = form.interest_rate.data
        period = form.period.data
        dscr = form.dscr.data
        available_income = form.available_income.data
        outstanding_loan = form.outstanding_loan.data

        l_terms = loan_terms(rate=interest_rate, available_income=available_income, 
                             dscr=dscr, period=period,
                             fv=outstanding_loan, pp=purchase_price, max_loan=max_loan)
            
        detail = amort_interest(interest_rate, l_terms[3], l_terms[1], period)

        amortization_payments, interest_payments = detail

        example = mortgage_example(period, amortization_payments, interest_payments)

        # Utilizamos numpy para converter todos os valores do array para valores positivos
        # Utilizamos numpy array para arredondar todos os valores para 2 casas decimais
        a_pmts = abs(np.round(amortization_payments, decimals=2)).tolist()
        i_pmts = abs(np.round(interest_payments, decimals=2)).tolist()

        # Número de meses no contrato
        months = range(0, (period*12)+1)

        table = [months, a_pmts, i_pmts]

        plot_url = example
 
        return render_template('banking/banking.html', form=form, l_terms=l_terms,
                           max_loan=max_loan, table=zip(*table), plot_url=plot_url,
                           amortization_payments=amortization_payments, 
                           interest_payments=interest_payments)


@app.route('/buy-vs-rent', methods=['GET', 'POST'])
def buy_vs_rent():
    form = MortgageDataForm(request.form)  
    if request.method == 'GET':  
     
        return render_template('banking/buy_vs_rent.html', form=form)
    
    else:
        value = form.value.data
        period = form.period.data
        euribor = form.euribor.data
        spread = form.spread.data

        taeg = form.taeg.data
        early_amort = form.early_amort.data

        eval_comission = form.eval_comission.data
        dossier_comission = form.dossier_comission.data
        form_comission = form.form_comssion.data
        other_costs = form.other_costs.data
        mortgage_costs = form.mortage_costs.data
        financing_tax = form.financing_tax.data

        # Variáveis iniciadas         
        tan = float(euribor) + float(spread)
        insurance_costs = 0
        total_initial_costs = 0

        # Prestação mensal
        # Consideramos FV=0
        # Permitir a opção de ter um FV !=0 (em construção)
        monthly_pmt = pmt(tan, period*12, value, 0)

        # Consideramos FV=0
        # Permitir a opção de ter um FV !=0 (em construção)
        amort_interest_data = amort_interest(rate=tan, loan=value,
                                    cf=monthly_pmt, period=period, fv=0)

        # Custo inicial associado com seguros e manutenção do imóvel
        # Valor padrão estipulou-se em 0,00477% do valor do empréstimo
        initial_yearly_cost = value * 0.00477
 
        # A cada ano, estima-se que o valor acima referido aumente 
        # Aplica-se um aumento baseado em períodos de 10 anos:
        # 1º Período -> Aumento de 50 anuais nos custos 
        # 2º Período -> Aumento de 75 anuais nos custos
        # 3º Período -> Aumento de 150 anuais nos custos
        # 4º Período -> Aumento de 300 anuais nos custos 
        costs = yearly_cost_increases(initial_yearly_cost, period)

        amortization_payments, interest_payments = amort_interest_data

        a_pmts = abs(np.round(amortization_payments, decimals=2)).tolist()
        i_pmts = abs(np.round(interest_payments, decimals=2)).tolist()

        # Agrupa em conjuntos de 12 elementos
        # Cada conjunto corresponde a um ano
        amort = group_by_period(a_pmts, 12)
        interest = group_by_period(i_pmts, 12)

        # Soma os elementos de cada grupo
        sum_amort_per_year = sum_by_group(amort)
        sum_interest_per_year = sum_by_group(interest)

        # Número de anos
        years = range(1, period + 1)

        annual_pmts = annual_payments(sum_amort_per_year, sum_interest_per_year, costs)

        total_pmts = sum(annual_pmts)

        loan_value_per_period = group_by_period(sum_amort_per_year, 5)
        total_loan_values = sum_by_group(loan_value_per_period)
        total_loan_values_sum = sum_loan_values(total_loan_values)

        # Cálculo da prestação mensal para cada ano
        monthly_pmts = [pmt / 12 for pmt in annual_pmts]

        # Dados para a tabela HTML
        table = [years, annual_pmts, sum_amort_per_year, sum_interest_per_year, costs, monthly_pmts]

        return render_template('banking/buy_vs_rent.html', form=form,euribor=euribor, 
                            spread=spread, taeg=taeg,value=value,
                            insurance_costs=insurance_costs,
                            total_initial_costs=total_initial_costs,
                            eval_comission=eval_comission, period=period,
                            dossier_comission=dossier_comission,
                            form_comission=form_comission,other_costs=other_costs,
                            mortgage_costs=mortgage_costs,financing_tax=financing_tax,
                            costs=costs, table=zip(*table),
                            total_loan_values_sum=total_loan_values_sum, 
                            total_pmts=total_pmts)