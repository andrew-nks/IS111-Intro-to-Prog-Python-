## Q6
######################################################################################
# This code is provided to you. DO NOT MODIFY THE CODE!
def calculate_price_after_discount(unit_price, quantity, discount_rate):
    """
    This function takes in the unit price, quantity and discount rate of an item.
    It returns the total price after discount for the item.
    Parameters:
        - unit_price (float): The unit price of the item.
        - quantity (int): The quantity of the item being purchased.
        - discount_rate (float): The percentage of discount. E.g., if there's a 
          10% discount, then discount_rate is set to 10.
    Return:
        - The total price of the item with the specified quantity after discount.
    """
    return (unit_price * quantity * (1 - discount_rate/100))

######################################################################################
# Write your solution below for Part A:
# Solution:

num_items = int(input("How many items do you want to check out? "))

total_price = 0.0

for n in range(1, num_items + 1):
    print("Enter the details of Item " + str(n) + ":")
    name = input("\tWhat's this item? ")
    price = float(input("\tWhat's the unit price of this item? $"))
    qty = int(input("\tWhat's the quantity of this item? "))
    has_discount = input("\tDoes this item have any discount? [yes|no] ")
    discount_rate = 0.0
    if (has_discount == 'yes'):
        discount_rate = float(input("\tWhat's the percentage of discount (%)? "))
    total_price += calculate_price_after_discount(price, qty, discount_rate)
    
print("The total amount you have to pay is $" + str(round(total_price, 2)))

######################################################################################
# Write your solution below for Part B:
# Solution:
def calculate_price_after_discount_2(unit_price, quantity, discount_rate):
    """
    This function takes in the unit price, quantity and discount rate of an item.
    It returns the total price after discount for the item.
    Parameters:
        - unit_price (float): The unit price of the item.
        - quantity (int): The quantity of the item being purchased.
        - discount_rate (float): The percentage of discount. E.g., if there's a 10% discount, 
                then discount_rate is set to 10.
    Return:
        - The total price of the item with the specified quantity after discount.
        - The savings.
    """
    original_total_price = unit_price * quantity
    savings = original_total_price * discount_rate/100
    return (original_total_price - savings, savings)

num_items = int(input("How many items do you want to check out? "))

total_price = 0.0
total_savings = 0.0

for n in range(1, num_items + 1):
    print("Enter the details of Item " + str(n) + ":")
    name = input("\tWhat's this item? ")
    price = float(input("\tWhat's the unit price of this item? $"))
    qty = int(input("\tWhat's the quantity of this item? "))
    has_discount = input("\tDoes this item have any discount? [yes|no] ")
    discount_rate = 0.0
    if (has_discount == 'yes'):
        discount_rate = float(input("\tWhat's the percentage of discount (%)? "))
    
    result_tuple = calculate_price_after_discount_2(price, qty, discount_rate)
    discounted_price = result_tuple[0] 
    savings = result_tuple[1]
    total_price += discounted_price
    total_savings += savings
    
print("The total amount you have to pay is $" + str(round(total_price, 2)))
print("You have saved $" + str(round(total_savings, 2)))



