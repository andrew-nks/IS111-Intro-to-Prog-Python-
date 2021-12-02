# q1 a
with open("seating_plan.txt") as file:
    row_list = []
    number_name = []
    my_dict = {}
    for line in file:
        row = line.rstrip("\n").split(",")
        row_letter = row[0]
        row_number = row[1]
        name = row[2]
        if row_letter not in row_list:
            row_list.append(row_letter)
        number_name.append(row)
    
    for letter in row_list:
        nested_list = []
        for data in number_name:
            if data[0] == letter:
                nested_list.append([data[1], data[2]])
        
        my_dict[letter] = nested_list

enter_letter = input("Enter a letter (from A to E) : ")
enter_number = input("Enter a seat number (from 1 to 25) :")

result = ""
left_result = ""
right_result = ""
left_number = str(int(enter_number) - 1)
right_number = str(int(enter_number) + 1)

for key in my_dict:
    if enter_letter == key:
        for data in my_dict[enter_letter]:
            if enter_number == data[0]:
                result = f"The person seated at the seat {enter_letter}{enter_number} is {data[1]}"
            if left_number == data[0]:
                left_result = f"The person sitting on the left side of that person is {data[1]}"
            if right_number == data[0]:
                right_result = f"The person sitting on the right side of that person is {data[1]}"


if result == "":
    print(f"Seat not taken")
else:            
    print(result)

if left_result == "":
    print(f"Seat not taken on the left side")
else:
    print(left_result)

if right_result == "":
    print(f"Seat not taken on the right side")
else:
    print(right_result)



