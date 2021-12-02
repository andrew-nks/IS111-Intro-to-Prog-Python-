# age = int(input("Enter your age (between 0 and 100, both inclusive): "))

# while age < 0 or age > 100:
#     print(f"Please enter a valid age!")
#     age = int(input("Enter your age again: "))
# print(f"Thanks!")

# b)

# student = str(input("Are you a student? "))

# while student not in ("Yes", "YES", "yes", "NO", "no", "No"):
#     print(f"Please enter a valid answer (YES, Yes, yes, NO, No or no)." )
#     student = input("Are you a student? ")
# print(f"Got it!")

# c)

def name_valid(name):
    import string
    for i, e in enumerate(name):
        if not (e in string.ascii_lowercase or e in string.ascii_uppercase or e in string.whitespace):
            return False
        

name = input("Enter your name: ")

while name_valid(name) == False:
    print(f"Please enter a valid name! ")
    name = input("Enter your name: ")

print(f"Thank you!")
