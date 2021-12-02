import random
number = random.randint(1, 100)
print(f"random number is {number}")
guess = int(input("Enter your guess (between 1 and 100) : "))

def higher_lower(guess, number):
    if guess < number:
        return "lower"
    if guess > number:
        return "higher"
    else:
        return True

while higher_lower(guess, number) != True:
    if higher_lower(guess, number) == "lower":
        print("Your guess is too low!")
    if higher_lower(guess, number) == "higher":
        print("Your guess is too high!")
    print(" ")
    guess = int(input("Enter your guess (between 1 and 100) : "))

print("Bingo!")
