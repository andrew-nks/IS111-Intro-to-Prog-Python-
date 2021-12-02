### Q6 More on Lists
## c)
# Write your code below:
##############################################################
def get_non_common_strings(str_list1, str_list2):
    unique_str = []
    for letter in str_list1:
        if letter not in str_list2:
            unique_str.append(letter)

    for letter in str_list2:
        if letter not in str_list1:
            unique_str.append(letter)
            
    return unique_str







##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_non_common_strings(["a", "b", "c", "d"], ["b", "d", "e", "f"])
print("Expected: ['a', 'c', 'e', 'f']")
print("Actual  : " + str(r_list))
print()