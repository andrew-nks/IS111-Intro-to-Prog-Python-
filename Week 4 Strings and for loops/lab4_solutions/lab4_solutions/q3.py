## Q3
# Solution:

print("Please tell us your monthly usage requirements.")
print()

calls = int(input("What's the minimum outgoing calls (in mins) you need? "))
sms = int(input("What's the minimum number of SMS/MMS you need? "))
data = float(input("What's the minimum amount of data (in GB) you need? "))

plan = ''
if (calls <= 80 and sms <= 300 and data <= 0.1):
    plan = 'Combo 1'
elif (calls <= 200 and sms <= 500 and data <= 2.0):
    plan = 'Combo 2'
elif (calls <= 300 and sms <= 1000 and data <= 3.0):
    plan = 'Combo 3'
elif (calls <= 400 and sms <= 1500 and data <= 4.0):
    plan = 'Combo 4'
elif (calls <= 800 and sms <= 2000 and data <= 10.0):
    plan = 'Combo 5'

if (plan == ''):
    print("Sorry! We don't have any plan that satisfies your requirements.")
else:
    print("We recommend " + plan)