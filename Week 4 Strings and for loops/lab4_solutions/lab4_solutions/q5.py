## Q5
# solution
def pad_message(msg, width):
    
    length = len(msg)
    if (length > width):
        return msg[0:width]
    
    result = ''
    length_of_padding = width - length
    for n in range(length_of_padding):
        result += ' '
    result += msg
    return result

print(pad_message("IS111 Lab 5", 20))
print(pad_message("IS111 Lab 5", 8))
print(pad_message("hello", 20))
print(pad_message("python programming", 20))
print(pad_message("Hello World! I enjoy programming in Python.",20))

