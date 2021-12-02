original = list(input("What's the original message? "))

def encryption(original):
    for i in range(len(original)):
        letter = original[i]
        if letter == 'a':
            original[i] = 'e'
        elif letter == 'e':
            original[i] = 'i'
        elif letter == 'i':
           original[i] = 'o'
        elif letter == 'o':
            original[i] = 'u'
        elif letter == 'u':
            original[i] = 'a'
    return ''.join(original)

# print(f"The encrypted message is '{encryption(original)}")

reverse_encryption = encryption(original)[::-1]

print(f"The encrypted message is '{reverse_encryption}")