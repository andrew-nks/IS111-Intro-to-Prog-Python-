from q5a import *

spam_dict = count_words_in_file("spam_sms.txt")
top_ten_list = []
values = []
for value in spam_dict.values():
    values.append(value)

while len(top_ten_list) < 10:
    for number in values:
        if number == max(values):
            top_ten_list.append(number)
            values.remove(number)

top_tuple_list = []
for i in range(0, len(top_ten_list)):
    number = top_ten_list[i]
    for key in spam_dict:
        if spam_dict[key] == number and len(top_tuple_list) < 10:
            top_tuple_list.append((key, spam_dict[key]))

print(top_tuple_list)
