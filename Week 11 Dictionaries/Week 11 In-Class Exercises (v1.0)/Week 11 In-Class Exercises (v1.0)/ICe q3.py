tuple_list = [(1, 'apple'), (2, 'banana'), (4, 'durian'), (8, 'orange'), (3, 'peach')]

def convert_to_dict(list):
    data_dict = {}
    for data in list:
        key = data[0]
        value = data[1]
        if key not in data_dict:
            data_dict[key] = value
    
    return data_dict

print(convert_to_dict(tuple_list))