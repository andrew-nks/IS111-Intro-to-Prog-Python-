amount = float(input("How much money do you want to spend? "))

if amount < 98.50:
    unit_price = 58.50
else:
    unit_price = 98.50

import retail_utility
qty = retail_utility.calculate_max_quantity_and_change(unit_price, amount)

max_qty = 0
change = 0 

if unit_price == 98.50:
    if qty[1] >= 58.50:
        max_qty += int(qty[0] * 1000) + (qty[1] // 58.50) * 500
        change += (qty[1] - 58.50)
    else: 
        max_qty += int(qty[0] * 1000)
        change += qty[1]
else:
    max_qty += int(qty[0] * 500)
    change += qty[1]

print(f"You can buy {max_qty} grams of honey. You have ${change} as your change.")