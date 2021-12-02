### Q3 Shopping Cart
## a)
# Write your code below:
##############################################################
def calculate_total_price(item_list):
    total = 0
    for i, item in enumerate(item_list):
        unit_price = item[1]
        qty = item[2]
        product = unit_price * qty
        total += product

    return total





##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
item_list = [("milk", 5.45, 2), ("eggs", 2.45, 1), ("shampoo", 8.90, 2)]
print('Expected: 31.15')
print('Actual:   ' + str(round(calculate_total_price(item_list),2)))