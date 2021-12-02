# Q1
# output = ["IS111", "Pytho", "Progr", "List"]
# def modify_list(my_list):
#     for index in range(len(my_list)):
#         x = my_list[index]
#         if len(x) > 5:
#             my_list[index] = x[0:5]

# str_list = ["IS111", "Python", "Programming", "List"]

# modify_list(str_list)
# print(str_list)

# part 2
# output = ["IS111", "Pytho", "Progr", "List"]
# def modify_list(my_list):
#     for element in my_list:
#         if len(element) > 5:
#             element = element[0:5]

# str_list = ["IS111", "Python", "Programming", "List"]

# modify_list(str_list)
# print(str_list)

# Q2


# def extract_email_id(email):
#     output = " "
#     for i in range(len(email)):
#         ch = email[i]
#         if  ch != '@':
#             output = " "
#         else:
#             output += email[0:i]
#             break
    
#     return output
    
# print(extract_email_id("jerry.lee@sis.smu.edu.sg"))
# print(extract_email_id("alan_wong.com"))
# print(extract_email_id(""))
# print(extract_email_id("alan_wong@gmail.com"))



# # my_str = 'test'
# # print(my_str[1::2])
# # print("Andrew" * 1000)

# # Part 2
# def extract_multiple_email_ids(email):
#     extracted_text = email.split(";")
#     for i, address in enumerate(extracted_text):
#         print(extract_email_id(address))
        
#         # for index, letter in enumerate(address):
#         #         if letter == "@":
#         #             print(address[0:index])
                

# extract_multiple_email_ids("jerry.lee@sis.smu.edu.sg;alan_wong@gmail.com;george_tan@yahoo.com")
# extract_multiple_email_ids("")
# extract_multiple_email_ids("jerry.lee@sis.smu.edu.sg")


# Q3
# import string

# def is_valid_username(username):
#     if len(username) >= 8:
#         return False
#     if username == "" or username == " ":
#         return False
#     valid_ch = string.ascii_lowercase + string.digits + "_.!#$%?"
#     for ch in username:
#         if ch not in valid_ch:
#             return False
#     return True
    
# username_list = ['abcdefgh','abcdefghi','ab$cd','ab_cd','ab-cd','ab:cd','','ab cd','abcDef','abc8ef']
# for username in username_list:
#     print("The username '" + username +"' is valid : " + str(is_valid_username(username)))


# Q4a
# def get_avg_len(data_list):
#     length = 0
#     no_of_words = 0
#     for word in data_list:
#         length += len(word)
#         no_of_words += 1
#     if no_of_words == 0:
#         return 0
#     else:
#         return length / no_of_words

# print(get_avg_len(["C", "Java", "Python", "PHP"]))
# print(get_avg_len([]))

# Q4b
# def get_longest_str(data_list):
#     longest_str_len = 0
#     longest_str = " "
#     for word in data_list:
#         length = len(word)
#         if length > longest_str_len:
#             longest_str_len = length
#             longest_str = word

#     return longest_str

# print(get_longest_str(["C", "Java", "Python", "PHP"]))
# print(get_longest_str([]))
# print(get_longest_str(["C", "Java", "HTML", "PHP"])) 

# Q4c

def concatenate_emails(a_list):
    for word in a_list:
        for ch in word:
            if ch.count('@') == 1:
                print(word)

my_list1 = ["tommy.goh@sis.smu.edu.sg","alan_wong@gmail.com"]
print(concatenate_emails(my_list1))

