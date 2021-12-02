# Name: Ng Kai Shen Andrew
# Email ID: andrew.ng.2021@scis.smu.edu.sg

def get_all_third_digits(str_list):
    # Replace the code below with your implementation.
    import string
    third_digits = []
    for i, string in enumerate(str_list):
        all_digits = []
        for index, ch in enumerate(string):
            if ch in ("0","1","2","3","4","5","6","7","8","9"):
                all_digits.append(ch)
        if len(all_digits) >= 3:
            third_digits.append(int(all_digits[2]))

    return third_digits

