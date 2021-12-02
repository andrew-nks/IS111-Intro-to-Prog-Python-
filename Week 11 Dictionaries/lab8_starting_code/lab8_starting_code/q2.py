## Q2 Prime Numbers
# write your code below
def create_prime_dict(my_list):
    my_dict = {}
    for data in my_list:
        for i in range(2,data):
            if data == 2:
                my_dict[data] = True
            elif data % i == 0:
                my_dict[data] = False
            else:
                my_dict[data] = True
    
    return my_dict



