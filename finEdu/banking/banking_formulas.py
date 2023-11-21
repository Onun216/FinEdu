import numpy as np
import numpy_financial as npf


def loan_terms(rate, available_income, dscr, period, fv, pp, max_loan):
    # Número de meses num ano
    m = 12

    rate = rate/100

    # Taxa Efectiva de juros
    er = (1 + rate/m) ** m - 1

    # Rendimento disponível ajustado à taxa de esforço (Debt Service Coverage Ratio)
    cf = -available_income / dscr

    # Valor máximo teórico do empréstimo
    present_value = npf.pv(rate=rate/m, nper=period*m, pmt=cf, fv=-fv)

    # Selecionamos o valor mais baixo entre o present_value e o LTV (Loan to Value)
    initial_loan_amount = min(present_value, pp*(max_loan / 100))

    terms = [er, cf, present_value, initial_loan_amount]
    
    return terms

def pmt(rate, loan, period, fv):
    m = 12
    rate = rate/100
    # Mostra o valor da prestação mensal
    pmt = npf.pmt(rate=rate/m, nper=period * m, pv=loan, fv=0) 
    return pmt

def amort_interest(rate, loan, cf, period, fv):
    m = 12
    rate = rate/100

    # Mostra o valor da dívida no fim de cada período mensal de pagamento 
    remaining_loan = npf.fv(rate=rate/m, nper=range(period*m +1), pmt=cf, pv=loan)

    # final_balance = npf.fv(rate=rate/m, nper=period*m, pmt=cf, pv=loan)

    # Mostra o valor da amortização em cada um dos meses
    amort = npf.ppmt(rate=rate/m, per=range(1, period*m +1), nper=period*m, pv=loan, fv=fv)

    # Mostra o valor do juro em cada um dos meses
    interest = npf.ipmt(rate=rate/m, per=range(1, period*m +1), nper=period*m, pv=loan, fv=fv)

    result = [amort, interest]

    return result

# Função que calcula o aumento progressivo dos custos anuais com seguros e afins
def yearly_cost_increases(initial_cost, period):
    years = range(0, period)
    list_of_rates = [50, 75, 150, 300]
    costs = []
    costs.append(initial_cost)
    i = 0
    for cost in costs:
        if len(costs) < 10:
           new_cost =  costs[i] + list_of_rates[0]
           costs.append(new_cost)
           i += 1
        if 10 <= len(costs) < 20:
            new_cost = costs[i] + list_of_rates[1]
            costs.append(new_cost)
            i += 1
        if 20 <= len(costs) < 30:
            new_cost = costs[i] + list_of_rates[2]
            costs.append(new_cost)
            i += 1
        if 30 <= len(costs) < 40:
            new_cost = costs[i] + list_of_rates[3]
            costs.append(new_cost)
            i += 1
    return costs


def group_by_period(list, nr_elements_per_group):
    nr_groups = len(list) / nr_elements_per_group
    groups = []
    temp_group = []
    for element in list:
        temp_group.append(element)
        if len(temp_group) == nr_elements_per_group:
            groups.append(temp_group)
            temp_group = []
    return groups

def sum_by_group(groups):
    sums = []
    for group in groups:
        sums.append(sum(group))
    return sums

# Função que soma os elementos de índice igual em 3 listas
def annual_payments(list1, list2, list3):
    annual_payments = []
    for i in range(len(list1)):
        total_pmts = list1[i] + list2[i] + list3[i]
        annual_payments.append(total_pmts)
    return annual_payments

# Função que soma o primeiro elemento da lista ao segundo
# Acumula os valores das somas numa lista nova
def sum_loan_values(list):
    value_sums = []
    for n in range(1, len(list) +1):
        value_sums.append(sum(list[:n]))
    return value_sums




