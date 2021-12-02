amount = float(input("Please pick a book. How much is it (in $)? "))
voucher = 100
total = amount

while amount < voucher:
    voucher -= amount
    remainder = voucher
    if remainder > 0:
        print(f"You still have ${remainder} left.")
        amount = float(input("Please pick another book. How much is it (in $)? "))
        total += amount

print(" ")
print("You are done!")
print(f"The total price is ${total}")