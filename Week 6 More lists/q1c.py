def check_numbers(int_list_1, int_list_2):
    for i in int_list_1:
        if all(i % value != 0 for value in int_list_2):
            return False
    return True
       
            



print(check_numbers([3, 8, 10, 15, 16], [9, 3, 2, 5]) )
print(check_numbers([3, 8, 10, 6, 2, 5], [9, 3, 7]) )