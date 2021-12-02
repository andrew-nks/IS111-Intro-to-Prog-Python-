# Name: Ng Kai Shen Andrew
# Email ID: andrew.ng.2021@scis.smu.edu.sg

def get_right_most_even_digit(number):
    # Replace the code below with your implementation.
    # for digit in str_digits:
    even_list = []
    for i, value in enumerate(str(number)):
        if value in ("2", "4", "6", "8", "0"):
            even_list.append(value)
        
    if even_list == []:
        return None
    else:
        return even_list[-1]




    