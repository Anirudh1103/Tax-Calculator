#Income tax
def calculate_tax(income, deductions):
    """
    Calculates the income tax and returns the result
    Params: income -> (int) & dedcutions -> (int)
    Return: taxAmount -> (float) 
    """
    taxable_income = income - deductions
    percentage = 0
    if taxable_income >300000:
        percentage = 0.05
    elif taxable_income > 600000:
        percentage = 0.10
    elif taxable_income >900000:
        percentage = 0.15
    elif taxable_income > 1200000:
        percentage = 0.20
    elif taxable_income > 1500000:
        percentage = 0.30
    taxAmount = taxable_income * percentage
    return taxAmount
        
def calculate_GST(price, percentage):
    """
    Calculates the GST based on the category of the product and resturns the result
    Params: price -> (int) & percentage -> (float)
    Return: tax -> (float) 
    """
    tax = (price * percentage)
    return tax

def calculate_Corporate_Tax(Total_income,OverHeads):
    """
    Calculates the Corporate Tax based on the Total income, Overheads and Depreciation
    Params: Total_income -> (int) & Overheads -> (int)
    Return: tax -> (float) 
    """
    #Default Depreciation = 6%
    #Corporate Tax is 25% on profit
    Depreciation = Total_income * 0.06
    Profit = Total_income - (OverHeads  + Depreciation)
    tax = Profit * 0.25
    return tax

def calculate_perquisite_tax(value_of_perks, rate):
    """
    Calculates the perquisite tax.
    Params: value_of_perks -> (int), rate -> (float)
    Return: tax -> (float) 
    """
    tax = (value_of_perks * rate) / 100
    return tax

def calculate_capital_gain_tax(capital_gain, rate):
    """
    Calculates the capital gain tax.
    Params: capital_gain -> (int), rate -> (float)
    Return: tax -> (float) 
    """
    tax = (capital_gain * rate) / 100
    return tax

def calculate_securities_transaction_tax(transaction_value, rate):
    """
    Calculates the securities transaction tax.
    Params: transaction_value -> (int), rate -> (float)
    Return: tax -> (float) 
    """
    tax = (transaction_value * rate) / 100
    return tax

def calculate_sales_tax(price, rate):
    """
    Calculates the sales tax.
    Params: price -> (int), rate -> (float)
    Return: tax -> (float) 
    """
    tax = (price * rate) / 100
    return tax

def calculate_customs_duty(import_value, rate):
    """
    Calculates the customs duty.
    Params: import_value -> (int), rate -> (float)
    Return: tax -> (float) 
    """
    tax = (import_value * rate) / 100
    return tax

def calculate_entertainment_tax(ticket_price, rate):
    """
    Calculates the entertainment tax.
    Params: ticket_price -> (int), rate -> (float)
    Return: tax -> (float) 
    """
    tax = (ticket_price * rate) / 100
    return tax
