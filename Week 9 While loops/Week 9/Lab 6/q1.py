gender = input("What's your gender? Please enter M or F: ")

while gender != "M" and gender != "F":
    print(f"Wrong input!")
    gender = input("What's your gender? Please enter M or F: ")

if gender == "M":
    print(f"Thanks! Your gender is male.")
else:
    print(f"Thanks! Your gender is female.")