my_dict = {}
letter_list = []
nested_list = []

with open("friends.txt") as file:
    for line in file:
        row = line.rstrip("\n").split("\t")
        if row[0] not in letter_list:
            letter_list.append(row[0])
        if row[1] not in letter_list:
            letter_list.append(row[1])
        nested_list.append(row)

    for letter in letter_list:
        nested_list_by_letter = []
        for data in nested_list:
            if data[0] == letter:
                nested_list_by_letter.append(data[1])
            if data[1] == letter:
                nested_list_by_letter.append(data[0])

        my_dict[letter] = nested_list_by_letter

# print(my_dict)

enter_letter = input("Enter friend: ")
enter_number = int(input("Enter degrees of separation: "))

result = ""
for key in my_dict:
    if enter_letter == key:
        if enter_number == 1:
            result = [letter for letter in my_dict[enter_letter]]
        if enter_number == 2:
            result = [letter for letter in my_dict[enter_letter]]
            for data in my_dict[enter_letter]:
                for letter in my_dict[data]:
                    if letter not in result:
                        result.append(letter)
        if enter_number == 3:
            result = [letter for letter in my_dict[enter_letter]]
            for data in my_dict[enter_letter]:
                for letter in my_dict[data]:
                    if letter not in result:
                        result.append(letter)
                    for ch in my_dict[letter]:
                        if ch not in result:
                            result.append(ch)

if enter_letter in result:
    result.remove(enter_letter)
print(result)
# print(my_dict)

    