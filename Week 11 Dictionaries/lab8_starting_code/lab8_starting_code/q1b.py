## Q1b Substitution Cipher
# write your code below
def decrypt(my_dict,msg):
    new_str = ""
    for ch in msg:
        if ch in my_dict:
            new_str += my_dict[ch]
        else:
            new_str += " "
    
    return new_str


