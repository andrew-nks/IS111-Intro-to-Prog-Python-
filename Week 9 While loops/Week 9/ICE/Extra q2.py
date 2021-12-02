from string import digits
password = input("Enter a passwrod: ")

def check_valid(password):
    import string
    req = 0
    if len(password) < 6:
        return False
    if len(password) > 10:
        return False

    for ch in password:
        if ch in string.whitespace:
            return False
        if ch in string.ascii_lowercase:
            req += 1
        if ch in string.ascii_uppercase:
            req += 1
        if ch in string.digits:
            req += 1
        if ch in "!@#$%^&*()-_=+*/'?.,><;:[]""\|~`'":
            req += 1
    
    if req != 0:
        return False

while check_valid(password) == False:
    print("The password entered is not valid!")
    password = input("Enter a password: ")

print("Thank you!")

