# This line of code prompts the user for a system time.
input_str = input('Please enter the system time (in seconds): ')

################################################################################
# Complete the code below to get the correct numbers of days, hours, minutes and seconds.
x = int(input_str)
day_in_secs = 60 * 60 * 24
hour_in_secs = 60 * 60
min_in_secs = 60

num_days = x // day_in_secs
num_sec_left = x % day_in_secs

num_hours = num_sec_left // hour_in_secs
num_sec_left %= hour_in_secs

num_minutes = num_sec_left // min_in_secs
num_sec_left %= min_in_secs

num_seconds = num_sec_left
# Put your code below
# print(num_days)
# print(num_hours)
# print(num_minutes)
# print(num_seconds)




################################################################################
# DO NOT MODIFY THE CODE BELOW!!!

# This line of code displays the results.
print('Based on this system time,' + str(num_days) + ' days, ' + str(num_hours) + ' hours, ' + str(num_minutes) + ' minutes and ' + str(num_seconds) + ' seconds have passed since 1 January 1970 00:00:00 UT.')