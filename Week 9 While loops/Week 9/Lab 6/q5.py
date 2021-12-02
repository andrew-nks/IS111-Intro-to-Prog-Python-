str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

def string_conditions(str_1, str_2):
    import string
    conditions = 0
    if len(str_1) >= len(str_2):
        conditions += 1
        
    for ch in str_1:
        if ch in string.whitespace:
            conditions += 1
            break
    for ch in str_2:
        if ch in string.whitespace:
            conditions += 1
    
    for ch in str_1:
        if ch not in str_2:
            conditions += 1
    
    return conditions

while string_conditions(str_1, str_2) != 0:
    print("Conditions not satisfied!")
    print(" ")
    str_1 = input("Enter the first string: ")
    str_2 = input("Enter the second string: ")

print("Bingo!")
