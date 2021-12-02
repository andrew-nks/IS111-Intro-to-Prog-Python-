# Name: NG KAI SHEN ANDREW
# Email ID: andrew.ng.2021
def extract_names_2(name_list):
    
    pass
    # Write your code here.
    import string
    if name_list == []:
        return []
    new_list = []

    for data in name_list:
        new_str = ""
        for ch in data:
            if ch.isalpha() or ch == " ":
                new_str += ch
        new_list.append(new_str)

    for data in new_list:
        check = 0
        for ch in data:
            if ch.isalpha():
                check += 1
        if check == 0:     
            new_list.remove(data)
            
    return new_list


# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, name_list, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: extract_names_2({name_list})')
        print()
        print(f'Expected: {expected_output}')
        result = extract_names_2(name_list)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
    
    run_test_case(1, ['Alex T5an', '^Harry Potter$', 'Squid$$ Game', 'abc','5 -6- 7-8'], ['Alex Tan', 'Harry Potter', 'Squid Game', 'abc'], "<class 'list'>")
    run_test_case(2, ['Alina Star**kov', 'Jessie Mei   Li'], ['Alina Starkov', 'Jessie Mei   Li'], "<class 'list'>")
    run_test_case(3, ['@@ 12'], [], "<class 'list'>")
    run_test_case(4, [], [], "<class 'list'>")
