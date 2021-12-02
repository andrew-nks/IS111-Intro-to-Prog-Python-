# with open("students.txt") as students:
#     student_dict = {}
#     for line in students:
#         line = line.rstrip("\n")
#         row = line.split("\t")
#         email = row[1]
#         birthdate = row[2]
#         if email not in student_dict:
#             student_dict[email] = birthdate

# enter_email = input("Please enter an email ID: ")
# if enter_email in student_dict:
#     print(f"The birthdate of this student is {student_dict[enter_email]}")
# else:
#     print(f"This is not a valid email ID.")
# print("\n")
# next_check = input("Do you want to continue? [Y|N] : ")
# while next_check == "Y":
#     enter_email = input("Please enter an email ID: ")
#     if enter_email in student_dict:
#         print(f"The birthdate of this student is {student_dict[enter_email]}")
#     else:
#         print(f"This is not a valid email ID.")
#     print("\n")
#     next_check = input("Do you want to continue? [Y|N] : ")

# print("Good-bye!")

#####################################################################
# 4b)
with open("students.txt") as file:
    student_dict_two = {}
    for line in file:
        row = line.rstrip("\n").split("\t")
        name = row[0]
        email = row[1]
        birthdate = row[2]
        gender = row[3]
        if email not in student_dict_two:
            student_dict_two[email] = [name, gender, birthdate]

for key, value in student_dict_two.items():
    gender = value[1]
    if gender == "M":
        value[1] = "male"
    else:
        value[1] = "female"

enter_email = input("Please enter an email ID: ")
if enter_email in student_dict_two:
    print(f"This student is {student_dict_two[enter_email][0]}, {student_dict_two[enter_email][1]}, born on {student_dict_two[enter_email][2]}")
else:
    print(f"This is not a valid email ID.")
print("\n")
next_check = input("Do you want to continue? [Y|N] : ")
while next_check == "Y":
    enter_email = input("Please enter an email ID: ")
    if enter_email in student_dict_two:
        print(f"This student is {student_dict_two[enter_email][0]}, {student_dict_two[enter_email][1]}, born on {student_dict_two[enter_email][2]}")
    else:
        print(f"This is not a valid email ID.")
    print("\n")
    next_check = input("Do you want to continue? [Y|N] : ")

print("Good-bye!")