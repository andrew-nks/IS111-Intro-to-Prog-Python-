# Q1
def get_strings(str_list, t):
    new_list = []
    length = 0

    for data in str_list:
        if length <= t:
            length += len(data)
            new_list.append(data)

    
    return new_list

print(get_strings(['a', 'bc', 'defgh', 'ij', 'k', 'lmn'], 9))