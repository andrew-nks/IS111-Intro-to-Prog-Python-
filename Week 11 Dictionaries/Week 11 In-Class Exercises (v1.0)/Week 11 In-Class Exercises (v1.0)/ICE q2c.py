from q2a import *

print(f"Current GPA information:\n")
display_all_gpas(gpa_dict)

print('\n')
name_add_gpa = input("Whose GPA do you want to add? ")

while name_add_gpa in gpa_dict:
    print(f"Sorry! This student already exists.")
    name_add_gpa = input("Whose GPA do you want to add? \n")

new_gpa = float(input(f"What's the GPA of {name_add_gpa}? "))
print("Thanks! GPA has been added.")
gpa_dict[name_add_gpa] = new_gpa

print('\n')
print(f"the new GPA information: \n")
display_all_gpas(gpa_dict)