## Q1a Substitution Cipher
# write your code below
def encrypt(my_dict, msg):
    new_str = " "
    for ch in msg:
        if ch in my_dict:
            new_str += my_dict[ch]
        else:
            new_str += ch
    
        

    return new_str

# substitutions
