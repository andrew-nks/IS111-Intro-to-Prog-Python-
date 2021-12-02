def get_larger_values(list_val):
    new_list = []
    average = sum(list_val) / len(list_val)
    for n in list_val:
        if n > average:
            new_list.append(n)
    
    return new_list


print(get_larger_values([2.5, 3.5, 5.5, 1.0])) 