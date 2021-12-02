### Q6 More on Lists
## b)
# Write your code below:
##############################################################
def get_larger_numbers(num_list1, num_list2):
    new_list = []
    for i, value1 in enumerate(num_list1):
        if all(value1 > value2 for value2 in num_list2):
                new_list.append(value1)
    return new_list







##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_larger_numbers([4, 6, 10], [1, 3, 5])
print("Expected: [6, 10]")
print("Actual  : " + str(r_list))
print()
