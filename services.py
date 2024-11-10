
TAX_BRACKETS = [
    (10000, 0.1),     # 10% for income up to 10,000
    (30000, 0.2),     # 20% for income between 10,001 and 40,000
    (40000, 0.3),     # 30% for income between 40,001 and 80,000
    (float('inf'), 0.4)  # 40% for income above 80,000
]

STANDARD_DEDUCTION = 12500  # Standard deduction amount

def calculate_tax(income, deductions):
    """
    Calculates the income tax and returns the result
    Params: income -> (int) & dedcutions -> (int)
    Return: tax -> (float) 
    """
    # Apply standard deduction if no deductions provided
    taxable_income = max(0, income - (deductions or STANDARD_DEDUCTION))
    tax = 0

    # Calculate tax based on progressive tax brackets
    for limit, rate in TAX_BRACKETS:
        if taxable_income > limit:
            tax += limit * rate
            taxable_income -= limit
        else:
            tax += taxable_income * rate
            break
    return tax
def calculate_GST(price, percentage):
    """
    Calculates the GST based on the category of the product and resturns the result
    Params: price -> (int) & percentage -> (float)
    Return: tax -> (float) 
    """
    tax = (price * percentage)/100
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