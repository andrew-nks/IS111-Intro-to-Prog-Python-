schedule_dict ={'Monday': 'swimming', 'Tuesday': 'basketball', 'Wednesday': 'tennis', 'Thursday': 'yoga', 'Friday': 'gymnastics'}

def reverse_dict(new_dict):
    swapped_dict = {}
    for x, y in new_dict.items():
        swapped_dict[y] = x
    
    return swapped_dict

print(reverse_dict(schedule_dict))

