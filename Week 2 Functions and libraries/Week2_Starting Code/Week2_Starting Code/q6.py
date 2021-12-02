from week2_utility import *

age = int(input("Enter your age: "))
gender = str(input("Enter your gender: "))
premium = get_insurance_premium(age, gender)

# print(premium)

print(f"The insurance premium you have to pay is: ${premium}")