# # Q1
# message = input("Enter a message : ")
# for n in message:
#     print(n, end=" ")

# # part 2
# message = input("Enter a message : ")
# for i, n in enumerate(message):
#     if i == len(message) - 1:
#         print(n)
#         break 
#     print(n, end="-")   

# part 3
# message = input("Enter a message : ")
# sep = input("Enter a separator : ")

# def print_message_with_separators(message, sep):
#     for i, ch in enumerate(message):
#         if i == len(message) - 1:
#             print(ch)
#             break
#         print(ch, end= sep)

# print_message_with_separators(message, sep)

##################################################################3
# Q2
# def display_numbers(m , n):
#     for number in range(m, n+1):
#         if number % 3 == 0 and number % 5 != 0:
#             print("-", end=" ")
#         elif number % 3 != 0 and number % 5 == 0:
#             print("*", end=" ")
#         elif number % 3 == 0 and number % 5 == 0:
#             print("#", end=" ")
#         else:
#             print(number, end=" ")

# display_numbers(1,16)
##########################################################################

# Q4

# word = input("Enter a word: ")

# def check_palindrome(word):
#     l = len(word) 
#     if l % 2 == 0:
#         if word[l // 2] == word[l // 2 + 1] and word[0] == word[l - 1] and word[1] == word[l - 2]:
#             print(f"{word} is a palindrome")
#         else:
#             print(f"{word} is NOT a palindrome")
#     else:
#         if word[l // 2 - 1] == word[l // 2 + 1] and word[0] == word[l - 1]:
#             print(f"{word} is a palindrome")
#         else:
#             print(f"{word} is NOT a palidrome")

# check_palindrome(word)

# def check_palindrome(word):
#     if word[::-1] == word:
#         print(f"{word} is a palindrome")
#     else:
#         print(f"{word} is NOT a palindrome")

# check_palindrome(word)

# Q5
