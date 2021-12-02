# Q1
# a) "a >= b"
# "a <= b"
# b) "a >= b"

# c) False
# True

# a = 20
# b = 20
# if a >= b:
#     print("a >= b")
# if a <= b:
#     print("a <= b")

# a = 30
# b = 30
# if a >= b:
#     print("a >= b")
# elif a <= b:
#     print("a <= b")

# c = "IS111"
# d = "is111"
# e = "IS" + "111"

# print(c == d)
# print(c == e)

######################################################################################
# Q4
# def calculate_income_tax(annual_income):
#     if annual_income <= 20000:
#         return 0
#     else:
#         if annual_income <= 30000:
#             return (annual_income - 20000) * 0.02
#         else:
#             if annual_income <= 40000:
#                 return (annual_income - 30000) * 0.035 + 200
#             else:
#                 if annual_income <= 80000:
#                     return (annual_income - 40000) * 0.07 + 550
#                 else:
#                     if annual_income <= 120000:
#                         return (annual_income - 80000) * 0.115 + 3350
#                     else:
#                         if annual_income <= 160000:
#                             return (annual_income - 120000) * 0.15 + 7950
#                         else:
#                             if annual_income <= 200000:
#                                 return (annual_income - 160000) * 0.18 + 13950
#                             else:
#                                 if annual_income <= 240000:
#                                     return (annual_income - 200000) * 0.19 + 21150
#                                 else:
#                                     if annual_income <= 280000:
#                                         return (annual_income - 240000) * 0.195 + 28750
#                                     else:
#                                         if annual_income <= 320000:
#                                             return (annual_income - 280000) * 0.2 + 36550
#                                         else:
#                                             return (annual_income * 0.22) + 44550

# annual_income = int(input("Enter your annual taxable income: "))
# print(f"Your total tax is ${calculate_income_tax(annual_income)}")

#################################################################################
# Q7
# def get_discount_rate(num_boxes):
#     if num_boxes >= 5:
#         return 0.2
#     else:
#         if 2 <= num_boxes <= 4:
#             return 0.1
#         else:
#             return 0.0

# def calculate_total_amount(brand, num_boxes):
#     if brand == 'Tung Lok':
#         return (55.4 * num_boxes) * (1 - get_discount_rate(num_boxes))
#     else:
#         if brand == 'Man Fu Yuan':
#             return (59.6 * num_boxes) * (1 - get_discount_rate(num_boxes))
#         else:
#             return 'Invalid brand'

# brand = str(input("Which brand do you want to buy? "))
# num_boxes = int(input("How many boxes do your want to buy? "))

# print(f"You need to pay ${calculate_total_amount(brand, num_boxes)}")

# ##############################################################################################

# Q9
amount = float(input("What is the change? $"))

notes10 = int(amount // 10)
notes5 = int((amount % 10) // 5)
notes2 = int(((amount % 10) % 5) // 2)
cents100 = int((((amount % 10) % 5) % 2) / 1)
cents10 = int(((((amount % 10) % 5) % 2) % 1) // 0.1)
cents5 = int((((((amount % 10) % 5) % 2) % 1) % 0.1) // 0.05)
cents1 = int(((((((amount % 10) % 5) % 2) % 1) % 0.1) % 0.05) // 0.01)

if notes10 != 0:
    print(f"$10 note: {notes10}")
if notes5 != 0:
    print(f"$5 note: {notes5}")
if notes2 != 0:
    print(f"$2 note: {notes2}")
if cents100 != 0:
    print(f"$1 coin: {cents100}")
if cents10 != 0:
    print(f"10 cents coin: {cents10}")
if cents5 != 0:
    print(f"5 cents coin: {cents5}")
if cents1 != 0:
    print(f"1 cent coin: {cents1}")


