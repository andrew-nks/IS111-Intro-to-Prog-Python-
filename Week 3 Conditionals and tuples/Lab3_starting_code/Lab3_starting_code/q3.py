## Q3 PART 1
# This function is for you to implement!
def calculate_salary(monthly_sales):
    
    # This variable is defined for you to use.
    BASE_SALARY = 2000.0
    
    # ################################################################################
    # Modify the code below to return the right amount of salary.
    if monthly_sales < 10000:
        return BASE_SALARY + monthly_sales * 0.05
    else:
        if monthly_sales < 15000:
            return BASE_SALARY + monthly_sales * 0.1
        else:
            if monthly_sales < 18000:
                return BASE_SALARY + monthly_sales * 0.15
            else:
                return BASE_SALARY + monthly_sales * 0.18
    
    
    # ################################################################################

## Q3 PART 2
# Write your code below
monthly_sales = int(input("Enter monthly sales amount($): "))

print(f"The monthly pay for the salesperson is ${calculate_salary(monthly_sales)}")


