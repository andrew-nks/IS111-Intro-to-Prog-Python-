items = input("Do you have any item left in your shopping cart? Please enter Y or N: ")
total = 0

while items == "Y":
    name = input("Please enter the name of the item: ")
    price = float(input("PLease enter the price of the item: $ "))
    qty = int(input("Please enter the quantity of the item: "))
    total += (price * qty)
    print(" ")
    items = input("Do you have any item left in your shopping cart? Please enter Y or N: ")

print(" ")
print(f"Total price: ${total}")