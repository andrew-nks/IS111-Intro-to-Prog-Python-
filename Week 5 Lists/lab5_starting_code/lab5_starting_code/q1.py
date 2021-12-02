## Q1 Initials
# Write your code below:
##############################

number = int(input("How many people will attend te meeting? "))

name_list = []

for i in range(1, number + 1):
    name = str(input(f"Participant {i}: "))
    split_name = name.split()
    initials = " "
    for n in split_name:
        initials += n[0]
    name_list.append(initials)
    


# print(f"The initials of the participants are as follows: ")
for i in name_list:
    print(i)






