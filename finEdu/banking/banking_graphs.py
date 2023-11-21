import matplotlib.pyplot as plt

def mortgage_example(period, amortization_pmt, interest_pmt):
        plt.figure(figsize=(12,8))
        plt.bar(range(1, period*12 + 1), -amortization_pmt, 
                label="Amortização")
        plt.bar(range(1, period*12 + 1), -interest_pmt, 
                bottom = -amortization_pmt, label = "Juro")
        plt.legend(fontsize=20)
        plt.title("Pagamentos mensais", fontsize=15)
        plt.xlabel("Meses", fontsize=12)
        plt.ylabel("Montante a pagar (em EUR)", fontsize=12)
        plt.savefig('/Users/nuno/FinEdu/finEdu/static/img/mortgage_graph.png')
        