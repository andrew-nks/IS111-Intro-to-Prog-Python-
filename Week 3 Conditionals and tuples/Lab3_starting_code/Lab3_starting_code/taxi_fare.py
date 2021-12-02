# Q6
import math

flag_down_fare = float(input("What's the flag-down fare: $ "))
rate_400 = float(input("What's the rate per 400 meters within 9.8km? $ "))
rate_350 = float(input("What's the rate per 350 meters beyond 9.8km? $ "))
distance = int(input("What's the distance traveled (in meters)? "))
is_peak_period = input("Is the ride during a peak period? [yes/no] ") 
if is_peak_period == 'no':
    is_grave_period = input("Is the ride between midnight and 6am? [yes/no] ")
is_location_charge = input("Is there any location surcharge? [yes/no] ")
if is_location_charge == 'yes':
    location_surcharge = float(input("What's the amount of location surcharge? "))
else:
    location_surcharge = 0

if distance <= 1000:
    distance_fare = 0
else:
    if distance <= 9800:
            distance_fare = math.ceil((distance - 1000) / 400) * rate_400
        
    else:
        distance_fare = (8800/400 * rate_400) + math.ceil(((distance - 9800) / 350)) * rate_350

meter_fare = flag_down_fare + distance_fare

if is_peak_period == 'yes':
    time_surcharge = meter_fare * 0.25
else:
    if is_grave_period == 'yes':
        time_surcharge = meter_fare * 0.5

total_fare = meter_fare + time_surcharge + location_surcharge

print(f"The total fare is ${total_fare:.2f}")


    
    