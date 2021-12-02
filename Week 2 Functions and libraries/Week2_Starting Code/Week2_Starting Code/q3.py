# ################################################################################
# The following code is given to you.
def print_a_customized_line(symbol, n):
    """
    This function prints the specified symbol n times in the same row.
    For example, if symbol is '*' and n is 5, the function prints '*****'.
    
    Parameters:
        - symbol: The symbol to be repeated.
        - n: The number of times the symbol is to be repeated.
    """
    for i in range(n):
        print(symbol, end='')
    print()
# ################################################################################
def print_a_message(msg, symbol):
    """
    This function displays a given text message enclosed in a pair of the specified symbols.
    For example, if msg is "Welcome" and symbol is "#", then the function displays "# Welcome #".
    
    Parameters:
      - msg: A string that represents the text message to be displayed.
      - symbol: A single character that is used to enclose the text message.
    """
    print(symbol + " " + msg + " " + symbol)
    
# ################################################################################
# This function is for you to implement!
def print_signage(msg, symbol):
    pass
    # Write your code below to print out the correct output.
    n = len(msg) + len(symbol) + 3
    print_a_customized_line(symbol, n)
    print_a_message(msg, symbol)
    print_a_customized_line(symbol, n)
   


# ################################################################################
# The code below is to test your implementation above.
# DO NOT MODIFY THE CODE BELOW!

print_signage("Hello!", "*")
print()
print_signage("Welcome to SMU", "#")
# ################################################################################
print('hello')