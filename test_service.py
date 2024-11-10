from services import *
#Test the income tax function
def testIncomeTax():
    #Test case 1: Single person with no dependents and income of 250000 rs
    result = calculate_tax(250000,0)
    assert result == 0
    
    #Test case 2: Single person with no dependents and income of 500000 rs
    result = calculate_tax(500000,0)
    assert result == 25000

def testGST():
    #Test case 1: Spends  250000 rs for gold 
    result = calculate_GST(250000,0.03)
    assert result == 7500