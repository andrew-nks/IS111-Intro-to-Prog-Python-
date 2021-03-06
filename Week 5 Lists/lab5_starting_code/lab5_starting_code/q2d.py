### Q2 List of Numbers
## d)
# Write your code below:
##############################################################
def get_prime_numbers(num_list, sep):
    string = " "
    for n in num_list:
        if n > 1:
            if all(n % i != 0 for i in range(2,n)):
                string += str(n) + sep
    
    return string[:-1]




##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: 2-7-11-19')
print('Actual:   ' + str(get_prime_numbers([2, 4, 7, 9, 11, 16, 19, 21], '-')))

print('\nTest Case 2')
print('-' * 11)
print('Expected: 3')
print('Actual:   ' + str(get_prime_numbers([3, 4, 8, 9, 12, 16], '*')))
