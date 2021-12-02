import random
practice = input("Do you want to practise the multiplication table? Please enter Y or N: ")

while practice == "Y":
    number1 = random.randint(1,9)
    number2 = random.randint(1,9)
    result = int(input(f"What's the result of {number1} times {number2}? "))
    while result != (number1 * number2):
        result = int(input("Wrong answer! Please try again: "))
    print("You are right!")
    print(" ")
    practice = input("Do you want to continue your practice? Please enter Y or N: ")

print("Good-bye!")

