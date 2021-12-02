def pad_message(msg, width):
    for i in range(len(msg)):
        if len(msg) < width:
            return (((width - len(msg)) * " ") + msg)
        elif len(msg) > width:
            return msg[0:((len(msg) - (len(msg) - width)))]


print(pad_message("IS111 Lab 5", 20))
print(pad_message("IS111 Lab 5", 8))
print(pad_message("hello", 20))
print(pad_message("python programming", 20)) 
print(pad_message("Hello World! I enjoy programming in Python.",20))
