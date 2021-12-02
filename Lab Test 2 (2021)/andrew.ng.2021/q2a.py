# Name: NG KAI SHEN ANDREW
# Email ID: andrew.ng.2021
def extract_names_1(str_name):
    
    pass
    # Write your code here.
    my_list = []
    new_list = str_name.split("#")
    for data in new_list:
        if data != "":
            my_list.append(data)
    return my_list
    
# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, str_name, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: extract_names_1("{str_name}")')
        print()
        print(f'Expected: {expected_output}')
        result = extract_names_1(str_name)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
    
    run_test_case(1, 'Alex Tan##xy1 z####abc$#S', ['Alex Tan', 'xy1 z', 'abc$', 'S'], "<class 'list'>")
    run_test_case(2, '#ab c##def#', ['ab c', 'def'], "<class 'list'>")