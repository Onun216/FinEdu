from wtforms import IntegerField, StringField, BooleanField, TextAreaField,FloatField, Form, validators

# FloatField personalizado para aceitar ',' e '.'
class MyFloatField(FloatField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = float(valuelist[0].replace(',', '.'))
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid float value'))
class MortgageForm(Form):
    purchase_price = IntegerField('Preço do imóvel', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})
    max_loan = IntegerField('Montante Inicial %', [validators.NumberRange(min=0, max=100, message='Insira um valor entre 0 e 100')])
    interest_rate = IntegerField('Taxa de Juro %', [validators.NumberRange(min=0, max=100, message='Insira um valor entre 0 e 100')])
    period = IntegerField('Número de anos ', [validators.NumberRange(min=0)])
    dscr = IntegerField('Taxa de esforço', [validators.NumberRange(min=0)], default=3)
    available_income = IntegerField('Rendimento disponível', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})
    outstanding_loan = IntegerField('Montante em falta no fim do contrato ', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})

class MortgageDataForm(Form):
    value = MyFloatField('Valor a financiar', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})
    period = IntegerField('Prazo do financiamento', [validators.NumberRange(min=0, max=40)], render_kw={"placeholder": "€"})
    euribor = MyFloatField('Euribor', [validators.NumberRange(min=0)], render_kw={"placeholder": "%"})
    spread = MyFloatField('Spread', [validators.NumberRange(min=0)], render_kw={"placeholder": "%"})
    taeg = MyFloatField('TAEG', [validators.NumberRange(min=0)], render_kw={"placeholder": "%"})
    early_amort = MyFloatField('Custo da amortização antecipada', [validators.NumberRange(min=0)], render_kw={"placeholder": "%"})    
    
    eval_comission = MyFloatField('Comissão de avaliação', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})
    dossier_comission = MyFloatField('Comissão de dossier', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})
    form_comssion = MyFloatField('Comissão de formalização', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})
    other_costs = MyFloatField('Outros custos diversos', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})
    mortage_costs = MyFloatField('Emolumentos pelo registo da hipoteca', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})
    financing_tax = MyFloatField('Imposto de selo do contracto de financiamento', [validators.NumberRange(min=0)], render_kw={"placeholder": "€"})

    


