## Q8
# ################################################################################
# The functions below are for you to implement! 
# solution
def display_fibonacci(n):
    """
    This function takes in an integer n (greater or equal to 3). It prints out the 
    first n Fibonacci numbers, starting from 1. The function doesn’t return anything.
    """
    # Modify the code below to print the first n Fibonacci numbers
    prev_prev_number = 1 
    prev_number = 1
    print("1 1 ", end='')
    
    # We assume that n >= 3.
    for i in range(2, n):
        # Calculate the current Fibonacci number
        # based on the previous two numbers.
        curr_number = prev_prev_number + prev_number
        print( str(curr_number) + ' ', end='')
        
        # Update prev_prev_number and prev_number
        # for the next iteration.
        prev_prev_number = prev_number
        prev_number = curr_number
        
    # This is to end the entire line and move
    # the cursor to the next line.
    print()



