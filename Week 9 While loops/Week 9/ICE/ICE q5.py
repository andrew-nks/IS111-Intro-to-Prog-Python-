import string
def get_strings_with_digits(str_list, t):
    import string
    digit_count = 0
    new_list = []
    unique_list = []
    
    for data in str_list:
        for ch in data:
            if ch in string.digits:
                if digit_count <= t:            
                    digit_count += 1
                    new_list.append(data)

    for data in new_list:
        if data not in unique_list:
            unique_list.append(data)
       
    return unique_list

print(get_strings_with_digits(['ab12', 'IS111', '9', 'X7z', 'k', 'lmn'], 5))
            