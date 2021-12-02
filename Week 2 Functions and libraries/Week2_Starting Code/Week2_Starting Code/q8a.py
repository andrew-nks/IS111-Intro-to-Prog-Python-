# ################################################################################
# This function is for you to implement!
def calculate_tax_1(income):
    """
    This function assumes that the income is between $20,000 and $30,000.
    """
    
    # Modify the code below to return the right amount of tax.
    remainder = float(income - 20000)
    total_tax = remainder * 0.02 
    return total_tax
    
        
# ################################################################################

# Call the function above to test whether it works.
print(calculate_tax_1(25000.0))
