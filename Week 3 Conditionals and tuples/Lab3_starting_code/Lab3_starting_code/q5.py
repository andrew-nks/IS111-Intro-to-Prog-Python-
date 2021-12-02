# # Q5
# # The following function is provided to you.
# # Do not modify the function definition!
def get_user_info():
    """
    This function prompts the user for his/her name, gender, age and whether
    or not he/she is a student.
    The function returns a tuple that contains all the information entered
    by the user.
    """
    name = input("What's your name? ")
    gender = input("What's your gender? [M|F] ")
    age = int(input("What's your age? "))
    is_student = input("Are you a student? [yes|no] ")
    return (name, gender, age, is_student == 'yes')

# # Write your code below:
user_info = get_user_info()
name = user_info[0]
gender = user_info[1]
age = user_info[2]
is_student = user_info[3]

if age <= 6:
   print(f"{name}, you can travel for free.")
else:
    if gender == 'M':
        print("Mr.", end='')
    if gender == 'F':
        print("Ms.", end='')
    if age >= 60:
        print(f" {name}, you can get concessionary fare for senior citizens.")
    else:
        if is_student == True:
            print(f" {name}, you can get concessionary pass for students.")
        else:
            print(f" {name}, you need to pay full price fare.")
