from string import digits


def retrieve_numbers(string1):
    str_list = ""
    import string 
    
    for i in string1:
        if i in string.digits:
            str_list += i
        if i not in string.digits:
            str_list += " "
    
    new_str_list = str_list.split()
    
    return  " ".join(new_str_list)

print(retrieve_numbers("12abc600$##0900AB 100X") )