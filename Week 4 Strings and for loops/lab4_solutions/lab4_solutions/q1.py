## Q1.py
# Solution 1
month=int(input("Enter month: "))
days=(31, 28, 31, 30 , 31, 30, 31, 31, 30, 31, 30, 31)

if month < 1 or month > 12:
    print("Enter a number between 1 and 12 only!")
else:
    # month numbers start from 1 to 12 and days tuple indices start from 0 to 11
    num_days=days[month-1]
    print(f"There are {num_days} days in this month.")

# Solution 2
# Solution:
def get_num_days(month):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        num_days_in_month = 31
    elif month==4 or month==6 or month==9 or month==11:
        num_days_in_month = 30
    else:
        num_days_in_month = 28
    return num_days_in_month
    
month = int(input('Enter month: '))   
if month > 12 or month < 1:
    print('Enter a number between 1 and 12 only!')
else:
    num_days = get_num_days(month)
    print('There are', num_days, 'in this month.')
# ################################################################################