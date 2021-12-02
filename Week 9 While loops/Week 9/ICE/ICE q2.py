integer = int(input("Enter an integer: "))
odd_int = ""
if integer % 2 != 0:
    odd_int += str(integer) + "," + " "

while integer >= 0:
    integer = int(input("Enter an integer: "))
    if integer > 0 and integer % 2 != 0:
        odd_int += str(integer) + "," + " "

print(" ")
print(f"Thanks!")
print(f"The odd positive integers you have entered are the following: {odd_int[:-2]}")
