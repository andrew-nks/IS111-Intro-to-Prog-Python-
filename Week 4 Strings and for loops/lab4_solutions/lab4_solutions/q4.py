## Q4
###########################################################################################
# PART 1
# Solution
def encrypt_msg1(orig_msg):
    
    encrypted_msg = ''
    for ch in orig_msg:
        if (ch == 'a'):
            encrypted_msg = encrypted_msg + 'e'
        elif (ch == 'e'):
            encrypted_msg = encrypted_msg + 'i'
        elif (ch == 'i'):
            encrypted_msg = encrypted_msg + 'o'
        elif (ch == 'o'):
            encrypted_msg = encrypted_msg + 'u'
        elif (ch == 'u'):
            encrypted_msg = encrypted_msg + 'a'
        else:
            encrypted_msg = encrypted_msg + ch
    return encrypted_msg

msg = input("What's the original message? ")
print(f"The encrypted message is '{encrypt_msg1(msg)}'")

##############################################################################################
# PART 2
# Solution 1: 

def encrypt_msg2(orig_msg):
    
    encrypted_msg = ''
    
    for i in range(len(orig_msg)-1, -1, -1):
        ch = orig_msg[i]
        if (ch == 'a'):
            encrypted_msg = encrypted_msg + 'e'
        elif (ch == 'e'):
            encrypted_msg = encrypted_msg + 'i'
        elif (ch == 'i'):
            encrypted_msg = encrypted_msg + 'o'
        elif (ch == 'o'):
            encrypted_msg = encrypted_msg + 'u'
        elif (ch == 'u'):
            encrypted_msg = encrypted_msg + 'a'
        else:
            encrypted_msg = encrypted_msg + ch
    return encrypted_msg

msg = input("What's the original message? ")
print("The encrypted message is '" + encrypt_msg2(msg) + "'")

# Solution 2: 

def encrypt_msg3(orig_msg):
    
    msg = orig_msg[::-1]
    return encrypt_msg1(msg)

msg = input("What's the original message? ")
print("The encrypted message is '" + encrypt_msg3(msg) + "'")