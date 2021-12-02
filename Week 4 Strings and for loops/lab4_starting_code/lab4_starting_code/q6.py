## Q6
######################################################################################
# This code is provided to you. DO NOT MODIFY THE CODE!
# def calculate_price_after_discount(unit_price, quantity, discount_rate):
#     """
#     This function takes in the unit price, quantity and discount rate of an item.
#     It returns the total price after discount for the item.
#     Parameters:
#         - unit_price (float): The unit price of the item.
#         - quantity (int): The quantity of the item being purchased.
#         - discount_rate (float): The percentage of discount. E.g., if there's a 
#           10% discount, then discount_rate is set to 10.
#     Return:
#         - The total price of the item with the specified quantity after discount.
#     """
#     return (unit_price * quantity * (1 - discount_rate/100))

# ######################################################################################
# # Write your solution below for Part A:
item_no = int(input("How many items do you want to check out? "))

payment = 0

for data in range(1, item_no + 1):
    print(f"Enter the details of Item {data}:")
    item = input("        What's this item? ")
    unit_price = float(input("        What's the unit price of this item? $"))
    quantity = int(input("        What's the quantity of this item? "))
    got_discount = input("        Does this item have any discount? [yes][no] ")
    if got_discount == 'yes':
        discount_rate = float(input("        What's the percentage of discount (%)? "))
    else:
        discount_rate = 0
    if unit_price != 0 and quantity != 0:
        payment += calculate_price_after_discount(unit_price, quantity, discount_rate)

print(f"{payment:.2f}")






######################################################################################
# Write your solution below for Part B:



# def calculate_price_after_discount2(unit_price, quantity, discount_rate):
#     return [((unit_price * quantity)- (unit_price * quantity * (1 - discount_rate/100))), (unit_price * quantity * (1 - discount_rate/100))]

# ######################################################################################
# # Write your solution below for Part A:
# item_no = int(input("How many items do you want to check out? "))

# total_amt = 0
# savings = 0

# for data in range(1, item_no + 1):
#     print(f"Enter the details of Item {data}:")
#     item = input("        What's this item? ")
#     unit_price = float(input("        What's the unit price of this item? $"))
#     quantity = int(input("        What's the quantity of this item? "))
#     got_discount = input("        Does this item have any discount? [yes][no] ")
#     if got_discount == 'yes':
#         discount_rate = float(input("        What's the percentage of discount (%)? "))
#     else:
#         discount_rate = 0
#     payment = calculate_price_after_discount2(unit_price, quantity, discount_rate)
#     if unit_price != 0 and quantity != 0:
#         total_amt += payment[1]
#         savings += payment[0]

# print(f"The total amount you have to pay is ${total_amt:.2f}")
# print(f"You have saved ${savings:.2f}")





