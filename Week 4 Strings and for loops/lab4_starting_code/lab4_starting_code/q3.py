print(f"Please tell us your monthly usage requirements.")

min_calls = int(input("What's the minimum outgoing calls (in mins) you need? "))
min_sms = int(input("What's the minimum number of SMS/MMS you need? "))
min_data = float(input("What's the minimum amount of data (in GB) you need? "))

if min_calls <= 80 and min_sms <= 500 and min_data <= 0.1:
    print(f"We recommend Combo 1")
elif min_calls <= 200 and min_sms <= 500 and min_data <= 2:
    print(f"We recommend Combo 2")
elif min_calls <= 300 and min_sms <= 1000 and min_data <= 3:
    print(f"We recommend Combo 3")
elif min_calls <= 400 and min_sms <= 1500 and min_data <= 4:
    print(f"We recommend Combo 4")
elif min_calls <= 800 and min_sms <= 2000 and min_data <= 10:
    print(f"We recommend Combo 5")
else:
    print(f"Sorry! We don't have any plan that satisfies your requirements.")