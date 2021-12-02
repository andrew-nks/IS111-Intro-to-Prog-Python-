# Q4 a)

# new_pin = input("Enter your new PIN: ")
# confirm_pin = input("Confirm your new PIN: ")

# def check_valid(new_pin, confirm_pin):
#     import string
#     if new_pin != confirm_pin:
#         return False

#     if len(new_pin) != 6:
#         return False
    
#     for i, e in enumerate(new_pin):
#         if e not in string.digits:
#             return False
    

# while check_valid(new_pin, confirm_pin) == False:
#     print("Sorry! There is an error!")
#     new_pin = input("Enter your new PIN: ")
#     confirm_pin = input("Confirm your new PIN: ")

# print(" ")
# print("Thanks! Your new PIN has been set!")

# b)

new_pin = input("Enter your new PIN: ")
confirm_pin = input("Confirm your new PIN: ")

def check_valid(new_pin, confirm_pin):
    import string
    errors = []
    if new_pin != confirm_pin:
        errors.append("match")

    if len(new_pin) > 6:
        errors.append("too long")

    if len(new_pin) < 6:
        errors.append("too short")
    
    for i, e in enumerate(new_pin):
        if e not in string.digits:
            errors.append("non digit")

    return errors
    

while check_valid(new_pin, confirm_pin) != []:
    print("Sorry! There is an error!")

    for i, e in enumerate(check_valid(new_pin, confirm_pin)):
        if e == "too long":
            print("    - The PIN number is too long.")
        if e == "too short":
            print("    - The PIN number is too short.")
        if e == "non digit":
            print("    - The PIN number contains a non-digit character.")
        if e == "match":
            print("    - The second PIN doesn't match the first PIN.")

    new_pin = input("Enter your new PIN: ")
    confirm_pin = input("Confirm your new PIN: ")

print(" ")
print("Thanks! Your new PIN has been set!")