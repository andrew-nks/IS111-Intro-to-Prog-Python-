#Lab2_Q4
# #####################################
# Write your code below to first define 
# the function calculate_interest()
def interest_earned(principal, years):
    x = principal * (1 + (ANNUAL_INTEREST_RATE / FREQUENCY_OF_COMPOUNDING)) ** (FREQUENCY_OF_COMPOUNDING * years) - principal
    return x




# ################################################################
# The default annual interest rate of 0.5%, compounded 
# monthly, has been provided for you.

# Annual interest rate (which is fixed)
ANNUAL_INTEREST_RATE = 0.005
# Number of times the interest is compounded per year
FREQUENCY_OF_COMPOUNDING = 12

# ################################################################
# Write your code below to prompt the user and display the 
# interest earned.
principal = float(input("What's the amount of your principal? "))
years = float(input("How many years do you want to deposit the money? "))

# print(f"The interest you will earn is ${interest_earned(principal, years):.2f}")
print(f"The interest you will earn is ${round(interest_earned(principal, years), 2)}")


