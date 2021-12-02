## Q8
# ################################################################################
# The function below is for you to implement! 
def display_fibonacci(n):
    """
    This function takes in an integer n (greater or equal to 3). It prints out the 
    first n Fibonacci numbers, starting from 1. The function doesn’t return anything.
    """
    # Modify the code below to print the first n Fibonacci numbers
    list = [1, 1]
    for i in range(2, n):
       if n >= 3:
           list.append(list[-1] + list[-2])

    print(list)


display_fibonacci(10)
