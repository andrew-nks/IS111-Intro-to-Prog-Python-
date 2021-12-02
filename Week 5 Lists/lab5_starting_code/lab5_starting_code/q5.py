## Q5 Tax Calculation

TAX_INFO = [
    (20000, 0, 0.02),
    (30000, 200, 0.035),
    (40000, 550, 0.07),
    (80000, 3350, 0.115),
    (120000, 7950, 0.15),
    (160000, 13950, 0.18),
    (200000, 21150, 0.19),
    (240000, 28750, 0.195),
    (280000, 36550, 0.2),
    (320000, 44550, 0.22)
]


# Write your code below:
##############################################################
def calculate_tax(income):
    tax_payable = 0
    for i, rate in enumerate(TAX_INFO):
        threshold = rate[0]
        tax_exact = rate[1]
        tax = TAX_INFO[i-1][1]
        tax_rate = TAX_INFO[i-1][2]
        if income <= 20000:
            tax_payable = 0.0
            break
        elif income == threshold:
            tax_payable = float(tax_exact)
            break
        elif income < threshold:
            tax_payable = float((threshold - income) * tax_rate + tax)
            break
        else:
            tax_payable = float((income - 320000) * rate[2] + rate[1])
            

    return tax_payable
        







##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

tax = calculate_tax(15000)
print("Expected: 0.0")
print("Actual  : " + str(tax))
print()
    
tax = calculate_tax(35000)
print("Expected: 375.0")
print("Actual  : " + str(tax))
print()
    
tax = calculate_tax(100000)
print("Expected: 5650.0")
print("Actual  : " + str(tax))
print()

tax = calculate_tax(350000)
print("Expected: 51150.0")
print("Actual  : " + str(tax))
print()

