### Q2 List of Numbers
## a) 
# Write your code below:
##############################################################
def get_leap_years(year_list):
    leap_list = []
    for year in year_list:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_list.append(year)
        elif year % 4 == 0:
            leap_list.append(year)
    return leap_list







##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: [2000, 2020]')
print('Actual:   ' + str(get_leap_years([2018, 2000, 1800, 1900, 2011, 2020])))

print('\nTest Case 2')
print('-' * 11)
print('Expected: []')
print('Actual:   ' + str(get_leap_years([2018, 2001, 1800, 1900, 2011, 2100])))
