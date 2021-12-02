with open("phone_numbers.txt") as numbers:
    phone_dict = {}
    for line in numbers:
        row = line.rstrip("\n").split("|")
        name = row[0]
        phone = row[1]
        if name in phone_dict:
            phone_dict[name].append(phone)
        if name not in phone_dict:
            phone_dict[name] = [phone]
        

enter_name = input("Enter a person's name: ")
count = 0
if enter_name in phone_dict:
    count = len(phone_dict[enter_name])
    print(f"{enter_name} has {count} number(s): ")
    for value in phone_dict[enter_name]:
        print(value)
else:
    print(f"{enter_name} cannto e found in our database.")