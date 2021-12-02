import os

items = input("Do you have any item left in your shopping cart? Please enter Y or N: ")
total = 0
total_items = ""

while items == "Y":
    name = input("Please enter the name of the item: ")
    price = float(input("PLease enter the price of the item: $"))
    qty = int(input("Please enter the quantity of the item: "))
    total += (price * qty)
    total_items += str(name) + "   " + "$" + str(price) + "    " + str(qty) + os.linesep
    print(" ")
    items = input("Do you have any item left in your shopping cart? Please enter Y or N: ")

print(" ")
print("You've entered the following items: ")
print(total_items)


print(" ")
print(f"Total price: ${total}")