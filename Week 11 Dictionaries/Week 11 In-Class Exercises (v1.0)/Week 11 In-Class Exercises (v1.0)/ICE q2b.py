from q2a import *
print(f"Current GPA information:\n")
display_all_gpas(gpa_dict)

print('\n')
name_change_gpa = input("Whose GPA do you want to change? ")

while name_change_gpa not in gpa_dict:
    print(f"Sorry! this student doesn't exist.")
    name_change_gpa = input("Whose GPA do you want to change? \n")

new_gpa = input("What's the new GPA? ")
print("Thanks! GPA has changed.")
gpa_dict[name_change_gpa] = new_gpa

print('\n')
print(f"the new GPA information: \n")
display_all_gpas(gpa_dict)