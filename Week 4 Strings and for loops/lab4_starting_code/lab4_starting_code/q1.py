number = int(input("Enter month: "))
if number > 12 or number < 1:
    print(f"Enter a nubmer between 1 and 12 only!")
else:
    if number == 1 or number == 3 or number == 5 or number == 7 or number == 8 or number == 10 or number == 12:
        print(f"There are 31 days in this month.")
    elif number == 2:
        print(f"There are 28 days in this month.")
    else:
        print(f"There are 30 days in this month.")

